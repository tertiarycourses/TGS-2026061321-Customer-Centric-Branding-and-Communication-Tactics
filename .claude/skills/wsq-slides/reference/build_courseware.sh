#!/usr/bin/env bash
# Single-command aligned build of all WSQ courseware from the single source
# (course_data.py + data_domainN.py + the concept-enrichment module). Produces
# in courseware/: the PPT (+ slide_map.json for the LP page citations), LP and
# LG as DOCX + PDF, with page-numbered Tables of Contents in the LP/LG PDFs.
#
# Pipeline: run the python-pptx / python-docx generators, render to PDF with
# LibreOffice, inject a static page-numbered TOC (LibreOffice can't update the
# TOC field headless), then re-render the LP/LG PDFs.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$HERE/../.." && pwd)"
CW="$REPO/courseware"
SOFFICE="${SOFFICE:-soffice}"

SHORT="$(python3 -c "import sys;sys.path.insert(0,'$HERE');import course_data as C;print(C.SHORT_TITLE)")"

echo "==> Generate PPT / LP / LG from the single source"
python3 "$HERE/build_slides.py"          # also writes slide_map.json
python3 "$HERE/build_lesson_plan.py"     # cites deck pages via slide_map.json
python3 "$HERE/build_learner_guide.py"

PPT="$(ls -t "$CW"/*.pptx | head -1)"
LP="$CW/LP-$SHORT.docx"
LG="$CW/LG-$SHORT.docx"

echo "==> Render PDFs (pass 1)"
"$SOFFICE" --headless --convert-to pdf --outdir "$CW" "$PPT" >/dev/null 2>&1
"$SOFFICE" --headless --convert-to pdf --outdir "$CW" "$LP"  >/dev/null 2>&1
"$SOFFICE" --headless --convert-to pdf --outdir "$CW" "$LG"  >/dev/null 2>&1

echo "==> Inject page-numbered Table of Contents (LP + LG)"
python3 "$HERE/inject_toc.py" "$LP" "${LP%.docx}.pdf" 2
python3 "$HERE/inject_toc.py" "$LG" "${LG%.docx}.pdf" 2

echo "==> Render PDFs (pass 2 — with built TOC)"
"$SOFFICE" --headless --convert-to pdf --outdir "$CW" "$LP" >/dev/null 2>&1
"$SOFFICE" --headless --convert-to pdf --outdir "$CW" "$LG" >/dev/null 2>&1

echo "==> Done. Artifacts in courseware/:"
ls -1 "$CW"/*.pptx "$CW"/*.docx "$CW"/*.pdf
