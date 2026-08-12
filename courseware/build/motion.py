#!/usr/bin/env python3
"""Slide transitions + entrance animations for the house deck.

python-pptx has no API for either, so both are written as raw DrawingML
appended to each slide's <p:sld> element.

Two public helpers:

  apply_transitions(prs, plan)   -- per-slide transition, chosen by slide role
  animate(slide, shapes, ...)    -- staged entrance animation for shapes

Design intent (why this is not one uniform fade):
  * Section/topic dividers get a directional PUSH  -> "we are moving on".
  * Activity + scenario slides get a WIPE           -> "new task starts".
  * Concept/content slides get a soft FADE          -> no distraction.
  * Cover / closing get a MORPH-adjacent ZOOM       -> a deliberate flourish.
Transitions are set to a fast speed so they read as polish, never as delay.
Every effect used here is a PowerPoint-native transition that also degrades
gracefully in Keynote/LibreOffice and in the exported PDF (which ignores them).
"""
from pptx.oxml.ns import qn
from lxml import etree

_NSMAP = {
    "p":   "http://schemas.openxmlformats.org/presentationml/2006/main",
    "a":   "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p14": "http://schemas.microsoft.com/office/powerpoint/2010/main",
    "mc":  "http://schemas.openxmlformats.org/markup-compatibility/2006",
}


def _q(tag):
    """'p14:ripple' -> '{http://...2010/main}ripple'"""
    pfx, local = tag.split(":", 1)
    return "{%s}%s" % (_NSMAP[pfx], local)


# --------------------------------------------------------------- transitions
# name -> (element tag, attributes). p14: effects need the mc:AlternateContent
# wrapper, so we keep to the core p: set which every renderer understands.
_TRANSITIONS = {
    "fade":        ("p:fade",  {}),
    "push_left":   ("p:push",  {"dir": "l"}),
    "push_up":     ("p:push",  {"dir": "u"}),
    "wipe_left":   ("p:wipe",  {"dir": "l"}),
    "wipe_right":  ("p:wipe",  {"dir": "r"}),
    "wipe_up":     ("p:wipe",  {"dir": "u"}),
    "zoom":        ("p:zoom",  {}),
    "cover_up":    ("p:cover", {"dir": "u"}),
    "split":       ("p:split", {"orient": "horz", "dir": "out"}),
    "cut":         ("p:cut",   {}),
}


def set_transition(slide, kind="fade", speed="fast", advance_click=True):
    """Attach a single <p:transition> to one slide, replacing any existing one."""
    tag, attrs = _TRANSITIONS.get(kind, _TRANSITIONS["fade"])
    sld = slide._element

    for old in sld.findall(qn("p:transition")):
        sld.remove(old)

    tr = sld.makeelement(qn("p:transition"), {"spd": speed})
    if advance_click:
        tr.set("advClick", "1")
    eff = sld.makeelement(qn(tag), {k: v for k, v in attrs.items()})
    tr.append(eff)

    # <p:transition> must sit after <p:cSld> and <p:clrMapOvr>; appending at the
    # end of <p:sld> satisfies the schema because timing comes last and we insert
    # transition before any existing <p:timing>.
    timing = sld.find(qn("p:timing"))
    if timing is not None:
        timing.addprevious(tr)
    else:
        sld.append(tr)
    return tr


def apply_transitions(prs, plan=None, default="fade", speed="fast"):
    """Apply a transition to every slide.

    `plan` maps a 0-based slide index -> transition name. Slides absent from the
    plan get `default`. Returns a {kind: count} tally for build logging.
    """
    plan = plan or {}
    tally = {}
    for i, sl in enumerate(prs.slides):
        kind = plan.get(i, default)
        set_transition(sl, kind, speed=speed)
        tally[kind] = tally.get(kind, 0) + 1
    return tally


# ---------------------------------------------------------------- animations
# A <p:timing> tree that plays a list of shapes as a click-triggered sequence:
# each shape fades+rises in, one after the other, on a single click.
#
# The structure PowerPoint expects is deep but rigid:
#   timing > tnLst > par > cTn > childTnLst > seq > cTn > childTnLst
#     > par(click) > cTn > childTnLst > par(group) > cTn > childTnLst
#       > par(effect) > ... > animEffect + anim(style)

_EFFECT_XML = """
<p:par xmlns:p="{p}" xmlns:a="{a}">
  <p:cTn id="{cid}" presetID="{preset}" presetClass="entr" presetSubtype="{subtype}"
         fill="hold" grpId="0" nodeType="{node}">
    <p:stCondLst><p:cond delay="{delay}"/></p:stCondLst>
    <p:childTnLst>
      <p:set>
        <p:cBhvr>
          <p:cTn id="{cid2}" dur="1" fill="hold">
            <p:stCondLst><p:cond delay="0"/></p:stCondLst>
          </p:cTn>
          <p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl>
          <p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst>
        </p:cBhvr>
        <p:to><p:strVal val="visible"/></p:to>
      </p:set>
      <p:animEffect transition="in" filter="fade">
        <p:cBhvr>
          <p:cTn id="{cid3}" dur="{dur}"/>
          <p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl>
        </p:cBhvr>
      </p:animEffect>
      <p:anim calcmode="lin" valueType="num">
        <p:cBhvr additive="base">
          <p:cTn id="{cid4}" dur="{dur}" fill="hold"/>
          <p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl>
          <p:attrNameLst><p:attrName>ppt_y</p:attrName></p:attrNameLst>
        </p:cBhvr>
        <p:tavLst>
          <p:tav tm="0"><p:val><p:strVal val="#ppt_y+{rise}"/></p:val></p:tav>
          <p:tav tm="100000"><p:val><p:strVal val="#ppt_y"/></p:val></p:tav>
        </p:tavLst>
      </p:anim>
    </p:childTnLst>
  </p:cTn>
</p:par>
"""

_TIMING_SHELL = """
<p:timing xmlns:p="{p}" xmlns:a="{a}">
  <p:tnLst>
    <p:par>
      <p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot">
        <p:childTnLst>
          <p:seq concurrent="1" nextAc="seek">
            <p:cTn id="2" dur="indefinite" nodeType="mainSeq">
              <p:childTnLst/>
              <p:prevCondLst>
                <p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond>
              </p:prevCondLst>
              <p:nextCondLst>
                <p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond>
              </p:nextCondLst>
            </p:cTn>
          </p:seq>
        </p:childTnLst>
      </p:cTn>
    </p:par>
  </p:tnLst>
</p:timing>
"""

# preset 10 = "Fade"; combined with the ppt_y tween this reads as "fade up".
_PRESET_FADE = 10


def animate(slide, shapes, dur=400, stagger=True, rise=0.035):
    """Give `shapes` a staggered fade-up entrance on this slide.

    shapes  -- list of pptx shape objects, in the order they should appear
    dur     -- per-shape duration in ms
    stagger -- True: each shape waits for the previous (auto-chained after the
               first click). False: all appear together on one click.
    rise    -- how far the shape travels up, as a fraction of slide height.

    Safe to call with an empty list. Replaces any existing <p:timing>.
    """
    shapes = [s for s in shapes if s is not None]
    if not shapes:
        return

    sld = slide._element
    for old in sld.findall(qn("p:timing")):
        sld.remove(old)

    timing = etree.fromstring(
        _TIMING_SHELL.format(p=_NSMAP["p"], a=_NSMAP["a"]).encode()
    )
    # locate the mainSeq childTnLst we append click-groups into
    seq_children = timing.find(
        ".//{%s}seq/{%s}cTn/{%s}childTnLst" % (_NSMAP["p"], _NSMAP["p"], _NSMAP["p"])
    )

    cid = 10
    for i, shp in enumerate(shapes):
        # Every shape after the first plays automatically once the group starts,
        # so the whole build runs off a single click when stagger=True.
        node = "clickEffect" if (i == 0 or not stagger) else "afterEffect"
        delay = "0" if (i == 0 or not stagger) else "0"

        click_par = etree.fromstring(
            """<p:par xmlns:p="{p}"><p:cTn id="{a}" fill="hold">
                 <p:stCondLst><p:cond delay="{d}"/></p:stCondLst>
                 <p:childTnLst>
                   <p:par><p:cTn id="{b}" fill="hold">
                     <p:stCondLst><p:cond delay="0"/></p:stCondLst>
                     <p:childTnLst/>
                   </p:cTn></p:par>
                 </p:childTnLst>
               </p:cTn></p:par>""".format(
                p=_NSMAP["p"], a=cid, b=cid + 1, d="indefinite" if node == "clickEffect" else "0"
            ).encode()
        )
        inner = click_par.find(
            ".//{%s}par/{%s}cTn/{%s}childTnLst" % (_NSMAP["p"], _NSMAP["p"], _NSMAP["p"])
        )

        eff = etree.fromstring(
            _EFFECT_XML.format(
                p=_NSMAP["p"], a=_NSMAP["a"],
                cid=cid + 2, cid2=cid + 3, cid3=cid + 4, cid4=cid + 5,
                preset=_PRESET_FADE, subtype=0, node=node,
                delay=delay, dur=dur, spid=shp.shape_id,
                rise="%.4f" % rise,
            ).encode()
        )
        inner.append(eff)
        seq_children.append(click_par)
        cid += 10

    # <p:timing> is the last child of <p:sld>
    sld.append(timing)


def build_plan(roles):
    """Map slide roles to transition names.

    `roles` is a list, one entry per slide, of role strings emitted by the deck
    builder. Unknown roles fall through to a fade.
    """
    by_role = {
        "cover":     "zoom",
        "section":   "push_left",
        "subdivider": "push_up",
        "scenario":  "wipe_left",
        "roles":     "wipe_left",
        "discussion": "wipe_left",
        "reflection": "wipe_left",
        "big":       "zoom",
        "closing":   "zoom",
        "admin":     "fade",
        "content":   "fade",
    }
    return {i: by_role.get(r, "fade") for i, r in enumerate(roles)}
