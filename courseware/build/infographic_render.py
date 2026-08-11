"""AntV Infographic renderer — ports the deterministic (non-AI) DSL-builder +
HTML-writer + Playwright screenshot pipeline from the reference project
(Reference/wsq-courseware-generator-claude-streamlit/courseware_agents/slides/
infographic_agent.py) into this course's synchronous build_slides.py.

Pipeline: structured items -> AntV JSON "options" -> self-contained HTML
(engine inlined from assets/infographic.min.js, no CDN) -> Playwright
screenshot -> PNG, cached on a content hash so re-running the build after an
unrelated edit doesn't re-render unchanged infographics.

Icons/illustrations are resolved by the browser at render time from
api.iconify.design / raw.githubusercontent.com (undraw SVGs) with a 3s
timeout and silent-null fallback baked into the HTML template — a slide
still renders correctly (just without icon art) if those are unreachable.
"""
import os, json, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ANTV_JS_PATH = os.path.join(HERE, "assets", "infographic.min.js")
CACHE_DIR = os.path.join(HERE, ".infographic_cache")

# ---------------------------------------------------------------------------
# AntV Infographic template mapping by visualization category
# (ported verbatim from courseware_agents/slides/infographic_agent.py:37-119)
# ---------------------------------------------------------------------------
TEMPLATE_MAP = {
    "overview": [
        "list-grid-badge-card", "list-grid-candy-card-lite", "list-grid-ribbon-card",
        "list-zigzag-down-compact-card", "list-zigzag-up-compact-card",
        "list-zigzag-down-simple", "list-zigzag-up-simple",
        "list-row-horizontal-icon-arrow", "list-row-simple-illus",
        "list-sector-plain-text", "list-column-done-list",
        "list-column-vertical-icon-arrow", "list-column-simple-vertical-arrow",
    ],
    "process": [
        "sequence-snake-steps-compact-card", "sequence-snake-steps-simple",
        "sequence-snake-steps-underline-text", "sequence-roadmap-vertical-simple",
        "sequence-roadmap-vertical-plain-text", "sequence-stairs-front-compact-card",
        "sequence-stairs-front-pill-badge", "sequence-ascending-steps",
        "sequence-ascending-stairs-3d-underline-text",
        "sequence-color-snake-steps-horizontal-icon-line",
        "sequence-horizontal-zigzag-underline-text", "sequence-horizontal-zigzag-simple-illus",
        "sequence-zigzag-steps-underline-text", "sequence-mountain-underline-text",
        "sequence-filter-mesh-simple",
    ],
    "comparison": [
        "compare-binary-horizontal-badge-card-arrow", "compare-binary-horizontal-simple-fold",
        "compare-binary-horizontal-underline-text-vs",
        "compare-hierarchy-left-right-circle-node-pill-badge", "compare-swot",
    ],
    "cycle": [
        "sequence-circular-simple", "sequence-pyramid-simple",
        "sequence-cylinders-3d-simple", "sequence-zigzag-pucks-3d-simple",
    ],
    "hierarchy": [
        "hierarchy-tree-curved-line-rounded-rect-node", "hierarchy-tree-tech-style-badge-card",
        "hierarchy-tree-tech-style-capsule-item", "hierarchy-structure",
    ],
    "statistics": [
        "chart-pie-compact-card", "chart-pie-plain-text", "chart-pie-donut-plain-text",
        "chart-pie-donut-pill-badge", "chart-bar-plain-text", "chart-column-simple",
        "chart-line-plain-text", "chart-wordcloud",
    ],
    "timeline": [
        "sequence-timeline-simple", "sequence-timeline-rounded-rect-node",
        "sequence-timeline-simple-illus", "sequence-roadmap-vertical-simple",
    ],
    "relationship": [
        "relation-circle-icon-badge", "relation-circle-circular-progress",
    ],
    "quadrant": [
        "quadrant-quarter-simple-card", "quadrant-quarter-circular", "quadrant-simple-illus",
    ],
}

# Fallback icons when an item has none / an unrecognized kind
DEFAULT_ICONS = [
    "mdi/lightbulb", "mdi/check-circle", "mdi/star", "mdi/shield-check",
    "mdi/cog", "mdi/chart-line", "mdi/book-open", "mdi/account-group",
]

# This project's diagram helpers use short semantic "kind" strings
# (icon_badge / icon_cards_grad / what_is_items etc.) — map them to Iconify
# Material Design Icon names so the same content driving a native shape can
# also drive an AntV infographic without touching data_domain*.py.
ICON_KIND_MAP = {
    "chat": "mdi/chat", "gear": "mdi/cog", "flag": "mdi/flag",
    "search": "mdi/magnify", "chart": "mdi/chart-line", "refresh": "mdi/refresh",
    "shield": "mdi/shield-check", "people": "mdi/account-group",
    "clock": "mdi/clock-outline", "target": "mdi/target", "star": "mdi/star",
    "lightning": "mdi/lightning-bolt", "check": "mdi/check-circle",
    "idea": "mdi/lightbulb", "heart": "mdi/heart",
}


def _truncate(s, n):
    """Truncate at a word boundary (never mid-word) and strip a trailing
    dash/punctuation before the ellipsis so labels never end "...Mea…"."""
    s = str(s or "").strip()
    if len(s) <= n:
        return s
    cut = s[:n]
    if " " in cut:
        cut = cut[: cut.rfind(" ")]
    return cut.rstrip(" ,.;:—–-") + "…"


def _split_long_heading(heading, cap):
    """Headings written as "Primary — Secondary" (e.g. Keller model level
    names) overflow fixed-width template boxes and collide with the desc
    line below once they wrap to 2 lines. If the full heading exceeds cap,
    keep only the primary term as the label and fold the secondary term
    into the description instead of losing it."""
    heading = str(heading or "")
    if len(heading) <= cap:
        return heading, None
    for marker in (" — ", " – ", " - "):
        if marker in heading:
            primary, _, secondary = heading.partition(marker)
            return primary.strip(), secondary.strip()
    return heading, None


def _resolve_icon(kind, i):
    if kind and kind in ICON_KIND_MAP:
        return ICON_KIND_MAP[kind]
    if kind and isinstance(kind, str) and kind.startswith("mdi/"):
        return kind
    return DEFAULT_ICONS[i % len(DEFAULT_ICONS)]


def _normalize_item(it, i, label_cap=24):
    """Accept this project's existing tuple shapes and return an AntV item dict.

    Recognised shapes (matching what already flows into icon_cards_grad,
    ecosystem_map's what_is_items, process_items/takeaways_items, and
    donut_ring/stats_bar's (label, value) pairs):
      (kind, label)                 -> icon + label
      (kind, heading, body)         -> icon + label + desc
      (heading, caption)            -> label + desc (no icon kind supplied)
      (label, value:int/float)      -> label + numeric value (for chart-* templates)
    Also accepts a plain dict already shaped for AntV ({"label":..,"desc":..,
    "icon":..,"value":..}) and passes it through (with truncation applied).

    `label_cap` is tightened by build_antv_options() for templates with
    narrower per-item boxes (e.g. compare-*) — a label that still wraps to
    2 lines collides with the desc line under it (the AntV templates don't
    reflow desc position based on label height), so those need a shorter
    cap than the default even though it also worked fine elsewhere.
    """
    if isinstance(it, dict):
        entry = {"label": _truncate(it.get("label", f"Point {i+1}"), label_cap)}
        if it.get("desc"):
            entry["desc"] = _truncate(it["desc"], 55)
        entry["icon"] = _resolve_icon(it.get("icon") or it.get("kind"), i)
        if "value" in it:
            entry["value"] = it["value"]
        return entry

    if isinstance(it, (tuple, list)):
        if len(it) == 2 and isinstance(it[1], (int, float)) and not isinstance(it[1], bool):
            # (label, value)
            return {"label": _truncate(it[0], label_cap), "icon": DEFAULT_ICONS[i % len(DEFAULT_ICONS)],
                     "value": it[1]}
        if len(it) == 2:
            a, b = it
            if a in ICON_KIND_MAP or (isinstance(a, str) and a.startswith("mdi/")):
                # (kind, label)
                return {"label": _truncate(b, label_cap), "icon": _resolve_icon(a, i)}
            # (heading, caption)
            primary, secondary = _split_long_heading(a, label_cap)
            desc = f"{secondary} — {b}" if secondary else b
            return {"label": _truncate(primary, label_cap), "desc": _truncate(desc, 55),
                     "icon": DEFAULT_ICONS[i % len(DEFAULT_ICONS)]}
        if len(it) >= 3:
            kind, heading, body = it[0], it[1], it[2]
            primary, secondary = _split_long_heading(heading, label_cap)
            desc = f"{secondary} — {body}" if secondary else body
            return {"label": _truncate(primary, label_cap), "desc": _truncate(desc, 55),
                     "icon": _resolve_icon(kind, i)}

    return {"label": _truncate(str(it), label_cap), "icon": DEFAULT_ICONS[i % len(DEFAULT_ICONS)]}


def build_antv_options(title, items, template):
    """Build the AntV Infographic JSON `options` dict from this project's item
    tuples, following the same per-template item-count limits and compare-
    group-splitting rules as the reference project's build_antv_dsl()."""
    is_chart = template.startswith("chart-")
    is_sequence = template.startswith("sequence-") or template.startswith("list-zigzag")
    is_horizontal = ("horizontal" in template or "snake" in template
                      or "ascending" in template or "stairs" in template)
    is_compare = template.startswith("compare-")
    is_hierarchy = template.startswith("hierarchy-")

    if is_hierarchy:
        cap = 8  # 1 root + up to 7 children
    elif is_sequence and is_horizontal:
        cap = 3
    elif is_sequence:
        cap = 4
    elif is_chart:
        cap = 4
    elif is_compare:
        cap = 4
    else:
        cap = 6

    if len(items) > cap:
        print(f"WARNING [infographic_render]: '{title}' has {len(items)} items but "
              f"template '{template}' caps at {cap} — {len(items) - cap} item(s) silently "
              f"dropped: {[str(item) for item in items[cap:]]}")

    # compare-* templates have narrower per-item boxes than list/sequence
    # templates — a label that wraps to 2 lines collides with its desc line.
    label_cap = 16 if is_compare else 24
    norm = [_normalize_item(it, i, label_cap=label_cap) for i, it in enumerate(items[:cap])]

    if is_hierarchy and len(norm) >= 2:
        # First item is the hub/root; the rest hang off it as one flat level
        # of children (matches how ecosystem/what_is hub+spoke data reads).
        root = norm[0].copy()
        root["children"] = norm[1:]
        norm = [root]

    if is_chart:
        for i, entry in enumerate(norm):
            entry.pop("desc", None)
            if not isinstance(entry.get("value"), (int, float)):
                entry["value"] = (i + 1) * 20

    if is_compare and len(norm) >= 2:
        mid = max(1, len(norm) // 2)
        group_a, group_b = norm[:mid], norm[mid:]
        root_a = group_a[0].copy()
        if len(group_a) > 1:
            root_a["children"] = group_a[1:]
        root_b = group_b[0].copy()
        if len(group_b) > 1:
            root_b["children"] = group_b[1:]
        norm = [root_a, root_b]

    return {
        "template": template,
        "title": {"text": _truncate(title, 50) or "Infographic"},
        "data": {"items": norm},
    }


_ANTV_SCRIPT_CACHE = None


def _get_antv_script_content():
    global _ANTV_SCRIPT_CACHE
    if _ANTV_SCRIPT_CACHE is None:
        with open(ANTV_JS_PATH, "r", encoding="utf-8") as f:
            _ANTV_SCRIPT_CACHE = f.read()
    return _ANTV_SCRIPT_CACHE


def _write_antv_html(html_path, options, title):
    """Self-contained HTML: AntV engine inlined (no CDN, no file:// CORS
    issues), plus an Iconify/undraw resource loader with a 3s abort timeout
    and silent-null fallback. Ported from infographic_agent.py:1057-1141."""
    safe_title = str(title).replace("<", "&lt;").replace(">", "&gt;")
    options_json = json.dumps(options)
    script_tag = f"<script>{_get_antv_script_content()}</script>"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{safe_title} - Infographic</title>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ background: #FFFFFF; }}
    #container {{ width: 1792px; min-height: 1024px; }}
  </style>
</head>
<body>
  <div id="container"></div>
  {script_tag}
  <script>
    AntVInfographic.registerResourceLoader(async (config) => {{
      const {{ data, scene }} = config;
      try {{
        let url;
        if (scene === 'icon') url = `https://api.iconify.design/${{data}}.svg`;
        else if (scene === 'illus') url = `https://raw.githubusercontent.com/balazser/undraw-svg-collection/refs/heads/main/svgs/${{data}}.svg`;
        else return null;
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 3000);
        const r = await fetch(url, {{ referrerPolicy: 'no-referrer', signal: controller.signal }});
        clearTimeout(timeoutId);
        if (!r.ok) return null;
        const text = await r.text();
        if (!text || !text.trim().startsWith('<svg')) return null;
        return AntVInfographic.loadSVGResource(text);
      }} catch (e) {{ return null; }}
    }});
  </script>
  <script>
    window.__RENDERED__ = false;
    try {{
      const ig = new AntVInfographic.Infographic({{ container: '#container', width: 1792, height: 1024 }});
      const opts = {options_json};
      ig.setOptions(opts);
      ig.performRender();
      setTimeout(() => {{ try {{ ig.performRender(); }} catch(e) {{}} window.__RENDERED__ = true; }}, 2000);
      setTimeout(() => {{ try {{ ig.performRender(); }} catch(e) {{}} window.__RENDERED__ = true; }}, 4000);
    }} catch (e) {{
      console.error('AntV render error:', e);
      window.__RENDERED__ = true;
    }}
  </script>
</body>
</html>"""
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)


# Bump whenever the rendering/post-processing logic changes so previously
# cached PNGs (rendered under the old logic) don't get served stale.
RENDER_VERSION = "v2-autocrop"


def _content_hash(options):
    blob = json.dumps({"v": RENDER_VERSION, "opts": options}, sort_keys=True).encode("utf-8")
    return hashlib.sha1(blob).hexdigest()[:16]


def _autocrop_to_content(png_path, padding=36):
    """Some AntV templates (e.g. hierarchy-tree) lay out their content at
    natural size within the fixed 1792x1024 canvas instead of stretching to
    fill it, leaving a mostly-blank image that then renders tiny once fit
    into a slide. Crop every render to its actual content bounding box (vs
    the solid-white #FFFFFF background set in the HTML template) so every
    infographic fills its slide consistently regardless of the template's
    own layout habits."""
    from PIL import Image, ImageChops

    img = Image.open(png_path).convert("RGB")
    bg = Image.new("RGB", img.size, (255, 255, 255))
    bbox = ImageChops.difference(img, bg).getbbox()
    if bbox is None:
        return  # fully blank render — leave as-is, caller's size check will catch it
    left, top, right, bottom = bbox
    left = max(0, left - padding)
    top = max(0, top - padding)
    right = min(img.width, right + padding)
    bottom = min(img.height, bottom + padding)
    img.crop((left, top, right, bottom)).save(png_path)


def get_png_size(png_path):
    """Pixel (width, height) of a rendered infographic — since auto-crop
    means every image has its own aspect ratio now, callers need this to
    fit the picture into a slide's content area without distortion."""
    from PIL import Image
    with Image.open(png_path) as img:
        return img.size


def render_infographic_png(title, items, template, browser, work_dir=None, use_cache=True):
    """Render one infographic to PNG using an already-launched Playwright
    Chromium `browser` (share one browser across many calls — launching per
    call is what the reference project's docs warn is slow/flaky).

    Returns the PNG path. Cached under CACHE_DIR keyed on a content hash of
    the AntV options, so unrelated build re-runs skip re-rendering.
    """
    options = build_antv_options(title, items, template)
    key = _content_hash(options)

    os.makedirs(CACHE_DIR, exist_ok=True)
    png_path = os.path.join(CACHE_DIR, f"{key}.png")
    if use_cache and os.path.exists(png_path) and os.path.getsize(png_path) > 10000:
        return png_path

    work_dir = work_dir or CACHE_DIR
    os.makedirs(work_dir, exist_ok=True)
    html_path = os.path.join(work_dir, f"{key}.html")
    _write_antv_html(html_path, options, title)

    from pathlib import Path
    file_url = Path(html_path).as_uri()

    def _do_screenshot(wait_ms):
        page = browser.new_page(viewport={"width": 1792, "height": 1024})
        try:
            page.set_default_timeout(30000)
            page.goto(file_url, wait_until="domcontentloaded")
            try:
                page.wait_for_function("() => window.__RENDERED__ === true", timeout=wait_ms)
            except Exception:
                page.wait_for_timeout(wait_ms)
            page.wait_for_timeout(500)
            page.screenshot(path=png_path, full_page=True)
        finally:
            page.close()

    ok = False
    for wait_ms in (5000, 8000, 12000):
        try:
            _do_screenshot(wait_ms)
        except Exception:
            pass
        if os.path.exists(png_path) and os.path.getsize(png_path) > 10000:
            ok = True
            break

    if ok:
        _autocrop_to_content(png_path)

    if not ok:
        raise RuntimeError(f"Infographic render failed for '{title}' (template={template})")

    return png_path
