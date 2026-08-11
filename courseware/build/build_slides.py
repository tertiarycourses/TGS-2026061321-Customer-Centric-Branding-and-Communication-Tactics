#!/usr/bin/env python3
"""Generate the Customer-Centric Branding and Communication Tactics slide deck
(Tertiary WSQ house style, mostly white/light with a few sparing dark
"impact" accent slides — see tertiary-softskills-ppt-design).

Design helpers are the shared wsq-slides visual component library (cover,
section, content, two_col, cards3, tile_grid, flow_h, trainer_slide,
big_statement, brk) PLUS the expanded soft-skills diagram library
(pyramid_steps, icon_cards_grad, pros_cons_arrows, journey_loop, hex_model,
quadrant_2x2, quote_callout, playbook_numerals) and the case-study/role-play
activity pattern (scenario_slide, role_cards_slide, discussion_slide,
reflection_slide) that replaces step-by-step instructions for this course
family. Content is driven entirely by course_data.py + data_domain1..4.py so
the deck stays 100% aligned with the Lesson Plan and Learner Guide. Also
writes slide_map.json (topic/activity/admin-anchor -> page number) so the
Lesson Plan builder can cite the correct deck page for every teaching row.
"""
import os, sys, json, math
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
from lxml import etree
A_NS="http://schemas.openxmlformats.org/drawingml/2006/main"
def _qn(tag): return f"{{{A_NS}}}{tag}"
def add_shadow(shape,blur=90000,dist=28000,direction=5400000,color="1B2333",alpha=26000):
    """Soft outer drop-shadow via raw OOXML (python-pptx has no high-level API for
    this) — replaces any existing effectLst so repeated calls / shadow.inherit=False
    never produce two sibling <a:effectLst> elements (invalid OOXML)."""
    spPr=shape._element.spPr
    existing=spPr.find(_qn("effectLst"))
    if existing is not None: spPr.remove(existing)
    effectLst=etree.SubElement(spPr,_qn("effectLst"))
    shdw=etree.SubElement(effectLst,_qn("outerShdw"))
    shdw.set("blurRad",str(blur)); shdw.set("dist",str(dist))
    shdw.set("dir",str(direction)); shdw.set("rotWithShape","0")
    clr=etree.SubElement(shdw,_qn("srgbClr")); clr.set("val",color)
    al=etree.SubElement(clr,_qn("alpha")); al.set("val",str(alpha))
    return shape

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import infographic_render as IG
import course_data as C
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
from data_domain4 import DOMAIN4
ACTIVITIES = DOMAIN1 + DOMAIN2 + DOMAIN3 + DOMAIN4

REPO = os.path.dirname(os.path.dirname(HERE))
ASSETS = os.path.join(REPO, "courseware", "assets")

# ---------------- palette (house standard) ----------------
BLUE=RGBColor(0x1F,0x6F,0xEB); TEAL=RGBColor(0x10,0xB9,0x81); AMBER=RGBColor(0xF5,0x9E,0x0B)
INK=RGBColor(0x16,0x1B,0x26); GREY=RGBColor(0x5B,0x63,0x72); LIGHT=RGBColor(0xF5,0xF8,0xFC)
WHITE=RGBColor(0xFF,0xFF,0xFF); LINE=RGBColor(0xE2,0xE8,0xF0); VIOLET=RGBColor(0x7C,0x3A,0xED)

prs=Presentation(); prs.slide_width=Inches(13.333); prs.slide_height=Inches(7.5)
SW,SH=prs.slide_width,prs.slide_height
BLANK=prs.slide_layouts[6]

def slide(): return prs.slides.add_slide(BLANK)
def rect(s,x,y,w,h,color,line=None,shadow=False):
    sp=s.shapes.add_shape(1,x,y,w,h); sp.fill.solid(); sp.fill.fore_color.rgb=color
    if line is None: sp.line.fill.background()
    else: sp.line.color.rgb=line; sp.line.width=Pt(1)
    sp.shadow.inherit=False
    if shadow: add_shadow(sp)
    return sp
def oval(s,x,y,w,h,color,shadow=False):
    sp=s.shapes.add_shape(9,x,y,w,h); sp.fill.solid(); sp.fill.fore_color.rgb=color
    sp.line.fill.background(); sp.shadow.inherit=False
    if shadow: add_shadow(sp)
    return sp
def txt(s,x,y,w,h,runs,align=PP_ALIGN.LEFT,anchor=MSO_ANCHOR.TOP,space=4):
    tb=s.shapes.add_textbox(x,y,w,h); tf=tb.text_frame; tf.word_wrap=True; tf.vertical_anchor=anchor
    for i,line in enumerate(runs):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph()
        p.alignment=align; p.space_after=Pt(space)
        for t,sz,col,bold in line:
            r=p.add_run(); r.text=t; r.font.size=Pt(sz); r.font.bold=bold
            r.font.color.rgb=col; r.font.name="Arial"
    return tb
def bullets(s,x,y,w,h,items,size=18,color=INK,gap=10,mcolor=BLUE):
    tb=s.shapes.add_textbox(x,y,w,h); tf=tb.text_frame; tf.word_wrap=True
    for i,it in enumerate(items):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph(); p.space_after=Pt(gap)
        lvl=it[1] if isinstance(it,tuple) else 0
        text=it[0] if isinstance(it,tuple) else it
        r=p.add_run(); r.text=("•  " if lvl==0 else "–  ")+text
        r.font.size=Pt(size if lvl==0 else size-2); r.font.color.rgb=color if lvl==0 else GREY
        r.font.name="Arial"; r.font.bold=(lvl==0 and isinstance(it,tuple) and len(it)>2 and it[2])
    return tb

PAGE={"n":0}
def footer(s):
    PAGE["n"]+=1
    txt(s,Inches(0.4),Inches(7.05),Inches(7.5),Inches(0.35),
        [[(f"{C.SHORT_TITLE}  ·  {C.COURSE_CODE}",9,GREY,False)]])
    txt(s,Inches(5.0),Inches(7.05),Inches(3.3),Inches(0.35),
        [[("© 2026 Tertiary Infotech Academy Pte Ltd",9,GREY,False)]],align=PP_ALIGN.CENTER)
    txt(s,Inches(12.4),Inches(7.05),Inches(0.6),Inches(0.35),
        [[(str(PAGE["n"]),9,GREY,False)]],align=PP_ALIGN.RIGHT)
def head(s,title,kicker=None,kcolor=BLUE):
    rect(s,0,0,SW,SH,WHITE); rect(s,0,0,Inches(0.28),Inches(1.55),kcolor)
    if kicker: txt(s,Inches(0.85),Inches(0.5),Inches(11.6),Inches(0.4),[[(kicker,14,kcolor,True)]])
    size=29 if len(title)<=45 else (23 if len(title)<=75 else 19)
    txt(s,Inches(0.85),Inches(0.9),Inches(11.9),Inches(0.9),[[(title,size,INK,True)]])
    rect(s,Inches(0.85),Inches(1.7),Inches(11.63),Inches(0.02),LINE)
    return s
def _logo(name):
    p=os.path.join(ASSETS,name)
    return p if os.path.exists(p) else None

# ---------------- slide templates (shared wsq-slides component library) ----------------
def cover():
    s=slide(); rect(s,0,0,SW,SH,WHITE)
    rect(s,0,0,SW,Inches(0.22),BLUE); rect(s,0,Inches(7.28),SW,Inches(0.22),TEAL)
    org=_logo("tertiary-infotech-logo.png")
    if org: s.shapes.add_picture(org,Inches(0.85),Inches(0.7),height=Inches(1.05))
    rect(s,Inches(10.7),Inches(0.72),Inches(1.85),Inches(1.0),BLUE)
    txt(s,Inches(10.7),Inches(0.9),Inches(1.85),Inches(0.4),[[("WSQ",22,WHITE,True)]],align=PP_ALIGN.CENTER)
    txt(s,Inches(10.7),Inches(1.3),Inches(1.85),Inches(0.35),[[("COURSE",9,WHITE,True)]],align=PP_ALIGN.CENTER)
    txt(s,Inches(0.9),Inches(2.3),Inches(12),Inches(0.6),[[("COURSE SLIDES  ·  WSQ",16,BLUE,True)]])
    txt(s,Inches(0.9),Inches(2.85),Inches(12.0),Inches(1.9),[[(C.TITLE,38,INK,True)]])
    rect(s,Inches(0.92),Inches(4.75),Inches(2.4),Inches(0.06),TEAL)
    txt(s,Inches(0.9),Inches(5.05),Inches(12),Inches(1.4),
        [[(f"WSQ Course Code: {C.COURSE_CODE}",16,GREY,False)],
         [("Conducted by Tertiary Infotech Academy Pte Ltd  ·  UEN 201200696W",14,GREY,False)]],space=6)
    txt(s,Inches(0.9),Inches(6.5),Inches(12),Inches(0.4),[[(f"Version {C.VERSION}  ·  {C.VERSION_DATE}",12,GREY,False)]])
    txt(s,Inches(0.9),Inches(6.85),Inches(12),Inches(0.34),[[("© 2026 Tertiary Infotech Academy Pte Ltd. All rights reserved.  ·  www.tertiarycourses.com.sg",10,GREY,False)]])
    PAGE["n"]+=1  # cover has no visible footer, but still counts as page 1

def section(kicker,title,n,sub=""):
    s=slide(); rect(s,0,0,SW,SH,WHITE); rect(s,0,0,Inches(0.28),SH,BLUE)
    rect(s,Inches(0.85),Inches(2.5),Inches(0.14),Inches(2.0),TEAL)
    txt(s,Inches(1.25),Inches(2.55),Inches(11),Inches(0.6),[[(kicker,18,BLUE,True)]])
    txt(s,Inches(1.25),Inches(3.0),Inches(11.4),Inches(1.6),[[(title,40,INK,True)]])
    if sub: txt(s,Inches(1.27),Inches(4.55),Inches(11),Inches(0.8),[[(sub,16,GREY,False)]])
    txt(s,Inches(10.0),Inches(0.7),Inches(2.8),Inches(1.6),[[(n,72,RGBColor(0xE2,0xE8,0xF0),True)]],align=PP_ALIGN.RIGHT)
    footer(s)
def content(title,items,kicker=None,size=20):
    s=head(slide(),title,kicker); bullets(s,Inches(0.85),Inches(1.95),Inches(11.6),Inches(4.9),items,size=size); footer(s); return s
def two_col(title,left,right,kicker=None,lhead="",rhead="",source=None):
    s=head(slide(),title,kicker)
    rect(s,Inches(0.85),Inches(1.95),Inches(5.7),Inches(4.7),LIGHT,shadow=True); rect(s,Inches(6.95),Inches(1.95),Inches(5.55),Inches(4.7),LIGHT,shadow=True)
    if lhead: txt(s,Inches(1.1),Inches(2.15),Inches(5.2),Inches(0.4),[[(lhead,16,BLUE,True)]])
    if rhead: txt(s,Inches(7.2),Inches(2.15),Inches(5.0),Inches(0.4),[[(rhead,16,TEAL,True)]])
    bullets(s,Inches(1.1),Inches(2.7),Inches(5.2),Inches(3.8),left,size=16)
    bullets(s,Inches(7.2),Inches(2.7),Inches(5.05),Inches(3.8),right,size=16,mcolor=TEAL)
    _source_line(s,source)
    footer(s); return s
def process_v(title,items,kicker=None,color=BLUE,source=None):
    """Vertical numbered process list: numbered circle + title + caption per row."""
    s=head(slide(),title,kicker,kcolor=color)
    n=len(items); X0=Inches(0.85); Y0=Inches(2.0); TOTW=Inches(11.63)
    rowh=int((Inches(4.6)-Inches(0.2)*(n-1))/n); bd=min(Inches(0.7),int(rowh*0.75))
    for i,(t,cap) in enumerate(items):
        y=int(Y0+(rowh+Inches(0.2))*i)
        rect(s,X0,y,TOTW,rowh,LIGHT,shadow=True); rect(s,X0,y,Inches(0.1),rowh,color)
        cy=int(y+rowh/2-bd/2)
        oval(s,X0+Inches(0.3),cy,bd,bd,color,shadow=True)
        txt(s,X0+Inches(0.3),cy,bd,bd,[[(str(i+1),18,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        tx=X0+Inches(0.3)+bd+Inches(0.3); tw=TOTW-(bd+Inches(0.9))
        txt(s,tx,y,tw,rowh,[[(t,16,INK,True)],[(cap,13,GREY,False)]],anchor=MSO_ANCHOR.MIDDLE,space=2)
    _source_line(s,source)
    footer(s); return s
def cards3(title,cards,kicker):
    """Renders 2 or 3 evenly-spaced cards depending on how many are passed —
    never pads with an empty placeholder card."""
    s=head(slide(),title,kicker); n=min(len(cards),3)
    TOTW=Inches(11.63); X0=Inches(0.85); gap=Inches(0.33)
    cw=int((TOTW-gap*(n-1))/n)
    xs=[int(X0+(cw+gap)*i) for i in range(n)]
    for i,c in enumerate(cards[:3]):
        x=xs[i]; col=c[0]
        rect(s,x,Inches(1.95),cw,Inches(4.7),LIGHT,shadow=True); rect(s,x,Inches(1.95),cw,Inches(0.12),col)
        txt(s,x+Inches(0.25),Inches(2.2),cw-Inches(0.5),Inches(0.6),[[(c[1],19,col,True)]])
        bullets(s,x+Inches(0.25),Inches(2.95),cw-Inches(0.5),Inches(3.4),c[2],size=14,mcolor=col,gap=9)
    footer(s); return s
def big_statement(line1,line2,kicker,color=BLUE):
    # line1's font size grades down for a long statement (mirrors quote_callout's
    # tiering) so a 4-line wrap at full size can't run into line2's fixed y-position.
    size=38 if len(line1)<=60 else (30 if len(line1)<=100 else 24)
    s=slide(); rect(s,0,0,SW,SH,WHITE); rect(s,0,0,Inches(0.28),SH,color)
    txt(s,Inches(1.1),Inches(2.2),Inches(11),Inches(0.5),[[(kicker,16,color,True)]])
    txt(s,Inches(1.1),Inches(2.8),Inches(11.3),Inches(2.4),[[(line1,size,INK,True)]])
    if line2: txt(s,Inches(1.12),Inches(4.9),Inches(11),Inches(1.2),[[(line2,20,GREY,False)]])
    footer(s); return s
PALETTE=[BLUE,TEAL,VIOLET,AMBER]
def _source_line(s,text):
    if text:
        txt(s,Inches(0.85),Inches(6.85),Inches(11.6),Inches(0.3),[[(text,10,GREY,False)]])
def tile_grid(title,items,kicker=None,cols=2,size=15,icons=None,accent=BLUE,source=None):
    """Grid of light panels, each with a coloured icon/number badge + text."""
    s=head(slide(),title,kicker,kcolor=accent)
    n=len(items); rows=math.ceil(n/cols)
    X0=Inches(0.85); Y0=Inches(1.95); TOTW=Inches(11.63); AREAH=Inches(4.6 if source else 4.78)
    gx=Inches(0.3); gy=Inches(0.26)
    cw=int((TOTW-gx*(cols-1))/cols); ch=int((AREAH-gy*(rows-1))/rows)
    bd=Inches(0.6)
    for i,it in enumerate(items):
        r=i//cols; c=i%cols
        x=int(X0+(cw+gx)*c); y=int(Y0+(ch+gy)*r); col=PALETTE[i%len(PALETTE)]
        rect(s,x,y,cw,ch,LIGHT,shadow=True); rect(s,x,y,Inches(0.1),ch,col)
        ic=icons[i] if icons else str(i+1)
        icon_badge(s,ic,int(x+Inches(0.28)+bd/2),int(y+ch/2),bd,col,shadow=False)
        tx=x+Inches(1.08); tw=cw-Inches(1.32)
        if isinstance(it,tuple):
            txt(s,tx,int(y+Inches(0.14)),tw,int(ch-Inches(0.2)),
                [[(it[0],size+2,INK,True)],[(it[1],size-2,GREY,False)]],anchor=MSO_ANCHOR.MIDDLE,space=3)
        else:
            txt(s,tx,int(y+Inches(0.1)),tw,int(ch-Inches(0.16)),[[(it,size,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
    _source_line(s,source)
    footer(s); return s
def flow_h(title,steps,kicker=None,color=BLUE,source=None):
    """Horizontal numbered flow: coloured chips connected by chevrons."""
    s=head(slide(),title,kicker,kcolor=color)
    n=len(steps); X0=Inches(0.85); TOTW=Inches(11.63); gap=Inches(0.34)
    cw=int((TOTW-gap*(n-1))/n); y=Inches(2.55); ch=Inches(3.15); bd=Inches(0.82)
    for i,st in enumerate(steps):
        x=int(X0+(cw+gap)*i)
        rect(s,x,y,cw,ch,LIGHT,shadow=True); rect(s,x,y,cw,Inches(0.1),color)
        oval(s,int(x+cw/2-bd/2),int(y+Inches(0.42)),bd,bd,color,shadow=True)
        txt(s,int(x+cw/2-bd/2),int(y+Inches(0.42)),bd,bd,[[(str(i+1),30,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,x+Inches(0.16),int(y+Inches(1.55)),cw-Inches(0.32),int(ch-Inches(1.7)),[[(st,14,INK,False)]],align=PP_ALIGN.CENTER)
        if i<n-1:
            txt(s,int(x+cw-Inches(0.04)),int(y+ch/2-Inches(0.3)),int(gap+Inches(0.08)),Inches(0.6),
                [[("▶",15,color,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    _source_line(s,source)
    footer(s); return s
def sub_divider(kicker,title):
    """Full-bleed light divider for a K/A sub-topic (T1, T2, ...) within a Learning Unit."""
    s=slide(); rect(s,0,0,SW,SH,WHITE)
    rect(s,0,0,SW,Inches(0.14),TEAL); rect(s,0,Inches(7.36),SW,Inches(0.14),TEAL)
    size=32 if len(title)<=50 else (25 if len(title)<=80 else 21)
    txt(s,Inches(1.0),Inches(2.7),Inches(11.3),Inches(2.2),[[(title,size,INK,True)]],anchor=MSO_ANCHOR.MIDDLE)
    txt(s,Inches(1.0),Inches(2.15),Inches(11.3),Inches(0.5),[[(kicker,15,TEAL,True)]])
    footer(s); return s
def table_slide(title,headers,rows,kicker=None,color=BLUE,source=None,col_weights=(0.24,0.36,0.40)):
    """3-column reference table: header row (coloured fill) + N data rows
    (alternating light/white fill), each row (label, meaning, example)."""
    s=head(slide(),title,kicker,kcolor=color)
    X0=Inches(0.85); Y0=Inches(1.95); TOTW=Inches(11.63)
    cw=[int(TOTW*w) for w in col_weights]
    cx=[X0, X0+cw[0], X0+cw[0]+cw[1]]
    hh=Inches(0.55); n=len(rows); rh=int((Inches(4.55)-hh)/n)
    for i,htext in enumerate(headers):
        rect(s,cx[i],Y0,cw[i],hh,color)
        txt(s,cx[i]+Inches(0.12),Y0,cw[i]-Inches(0.2),hh,[[(htext,13,WHITE,True)]],anchor=MSO_ANCHOR.MIDDLE)
    for ri,row in enumerate(rows):
        y=int(Y0+hh+rh*ri); fill=WHITE if ri%2 else LIGHT
        for ci,val in enumerate(row):
            rect(s,cx[ci],y,cw[ci],rh,fill,line=RGBColor(0xE8,0xEC,0xF2))
            bold=(ci==0)
            txt(s,cx[ci]+Inches(0.12),y,cw[ci]-Inches(0.2),rh,
                [[(val,12.5,INK if not bold else color,bold)]],anchor=MSO_ANCHOR.MIDDLE)
    _source_line(s,source)
    footer(s); return s
def stats_bar(title,items,kicker=None,color=BLUE,source=None,unit="%"):
    """Horizontal bar-chart panel: label + proportional bar + value."""
    s=head(slide(),title,kicker,kcolor=color)
    n=len(items); X0=Inches(0.85); Y0=Inches(2.15); TOTW=Inches(11.63)
    rowh=Inches(0.85); gap=Inches(0.18)
    maxv=max(v for _,v in items) or 1
    labelw=Inches(3.0); barx=X0+labelw+Inches(0.2); barw_max=TOTW-labelw-Inches(1.5)
    for i,(label,val) in enumerate(items):
        y=int(Y0+(rowh+gap)*i); col=PALETTE[i%len(PALETTE)]
        txt(s,X0,y,labelw-Inches(0.1),rowh,[[(label,15,INK,True)]],anchor=MSO_ANCHOR.MIDDLE)
        rect(s,barx,int(y+rowh*0.28),int(barw_max),int(rowh*0.44),LIGHT)
        bw=max(int(barw_max*(val/maxv)),Inches(0.15))
        rect(s,barx,int(y+rowh*0.28),bw,int(rowh*0.44),col)
        txt(s,int(barx+bw+Inches(0.15)),y,Inches(1.2),rowh,
            [[(f"{val:g}{unit}",15,col,True)]],anchor=MSO_ANCHOR.MIDDLE)
    _source_line(s,source)
    footer(s); return s
def trainer_slide(kicker,name,role,rows,initials,accent=BLUE):
    """Profile-card layout: avatar badge + name/role panel on the left, labelled
    info tiles on the right. rows: list of (LABEL, value); blank value -> fill-in line."""
    s=head(slide(),"About the Trainer",kicker,kcolor=accent)
    lx=Inches(0.85); lw=Inches(3.65)
    rect(s,lx,Inches(1.95),lw,Inches(4.7),LIGHT); rect(s,lx,Inches(1.95),lw,Inches(0.12),accent)
    bd=Inches(1.7); ax=int(lx+(lw-bd)/2)
    oval(s,ax,Inches(2.5),bd,bd,accent)
    txt(s,ax,Inches(2.5),bd,bd,[[(initials,44,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    txt(s,lx+Inches(0.15),Inches(4.55),lw-Inches(0.3),Inches(0.6),[[(name,21,INK,True)]],align=PP_ALIGN.CENTER)
    txt(s,lx+Inches(0.15),Inches(5.2),lw-Inches(0.3),Inches(1.2),[[(role,13,GREY,False)]],align=PP_ALIGN.CENTER)
    rx=Inches(4.9); rw=Inches(7.6); ry=Inches(1.95); rh=Inches(4.7)
    n=len(rows); gy=Inches(0.2); th=int((rh-gy*(n-1))/n)
    for i,(label,val) in enumerate(rows):
        y=int(ry+(th+gy)*i); col=PALETTE[i%len(PALETTE)]
        rect(s,rx,y,rw,th,LIGHT); rect(s,rx,y,Inches(0.1),th,col)
        vruns=[(val,14,INK,False)] if val else [("____________________________________________",13,LINE,False)]
        txt(s,rx+Inches(0.32),y,rw-Inches(0.6),th,
            [[(label.upper(),11,col,True)],vruns],anchor=MSO_ANCHOR.MIDDLE,space=3)
    footer(s); return s
def brk(kind,dur,color=AMBER):
    s=slide(); rect(s,0,0,SW,SH,WHITE)
    rect(s,0,0,SW,Inches(0.22),color); rect(s,0,Inches(7.28),SW,Inches(0.22),color)
    rect(s,Inches(5.4),Inches(2.35),Inches(2.53),Inches(0.1),color)
    txt(s,0,Inches(2.75),SW,Inches(1.2),[[(kind,48,INK,True)]],align=PP_ALIGN.CENTER)
    txt(s,0,Inches(4.05),SW,Inches(0.8),[[(dur,22,color,True)]],align=PP_ALIGN.CENTER); PAGE["n"]+=1

# ============================================================ EXPANDED VISUAL LIBRARY
# (tertiary-softskills-ppt-design) — native-shape diagrams for richer, magazine-style
# theory slides: pyramid_steps, icon_cards_grad, pros_cons_arrows, journey_loop,
# hex_model, quadrant_2x2, plus quote_callout / playbook_numerals impact accents
# (used sparingly — about once per Learning Unit, never for routine body content).
NAVY2=RGBColor(0x16,0x2A,0x4D); MUTE=RGBColor(0x3A,0x4A,0x6B)
GRADIENTS=[(RGBColor(0x3E,0x92,0xF7),RGBColor(0x0B,0x3E,0xA6)),
           (RGBColor(0x22,0xD3,0xA8),RGBColor(0x0A,0x6E,0x63)),
           (RGBColor(0xF7,0xB0,0x3E),RGBColor(0xC2,0x5A,0x00)),
           (RGBColor(0xAF,0x7C,0xF5),RGBColor(0x5B,0x21,0xB6))]

def ashape(s,kind,x,y,w,h,color,line=None,shadow=False):
    sp=s.shapes.add_shape(kind,x,y,w,h); sp.fill.solid(); sp.fill.fore_color.rgb=color
    if line is None: sp.line.fill.background()
    else: sp.line.color.rgb=line; sp.line.width=Pt(1)
    sp.shadow.inherit=False
    if shadow: add_shadow(sp)
    return sp
def grad_rect(s,kind,x,y,w,h,c1,c2,angle=0,shadow=False):
    sp=s.shapes.add_shape(kind,x,y,w,h); sp.line.fill.background(); sp.shadow.inherit=False
    sp.fill.gradient(); stops=sp.fill.gradient_stops
    stops[0].color.rgb=c1; stops[0].position=0.0
    stops[1].color.rgb=c2; stops[1].position=1.0
    sp.fill.gradient_angle=angle
    if shadow: add_shadow(sp)
    return sp
def conn(s,x1,y1,x2,y2,color,w=1.5):
    cn=s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,x1,y1,x2,y2)
    cn.line.color.rgb=color; cn.line.width=Pt(w); cn.shadow.inherit=False; return cn

# ---------------- semantic vector icons (real autoshapes, not generic glyphs) ----------------
# icon_badge(kind) draws a coloured circle badge with a small, meaningful icon inside it —
# "search" for an audit, "chat" for a conversation, "gear" for a process, etc. — instead of a
# plain star/diamond/checkmark. Falls back to rendering `kind` as a literal text glyph if it
# isn't a recognised icon name, so existing single-character glyphs still work.
ICON_KINDS={"chat","gear","flag","search","chart","refresh","shield","people","clock",
            "target","star","lightning","check","idea","heart"}
def icon_badge(s,kind,cx,cy,d,badge_color,icon_color=None,shadow=True):
    """cx,cy = centre point (EMU). d = badge diameter (EMU)."""
    ic=icon_color or WHITE
    bd=oval(s,int(cx-d/2),int(cy-d/2),d,d,badge_color,shadow=shadow)
    if kind not in ICON_KINDS:
        txt(s,int(cx-d/2),int(cy-d/2),d,d,[[(kind,int(d/914400*26),ic,True)]],
            align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        return bd
    r=int(d*0.30)
    if kind=="search":
        ring=ashape(s,MSO_SHAPE.DONUT,int(cx-r),int(cy-r-d*0.04),int(r*1.7),int(r*1.7),ic)
        ring.adjustments[0]=0.14
        handle=ashape(s,MSO_SHAPE.ROUNDED_RECTANGLE,int(cx+r*0.28),int(cy+r*0.55),int(d*0.32),int(d*0.09),ic)
        handle.rotation=45
    elif kind=="gear":
        # GEAR_6 (chunky teeth) reads far better than GEAR_9 at badge scale.
        ashape(s,MSO_SHAPE.GEAR_6,int(cx-r*1.2),int(cy-r*1.2),int(r*2.4),int(r*2.4),ic)
    elif kind=="chat":
        cal=ashape(s,MSO_SHAPE.ROUNDED_RECTANGULAR_CALLOUT,int(cx-r*1.25),int(cy-r*1.1),int(r*2.5),int(r*1.9),ic)
    elif kind=="flag":
        ashape(s,MSO_SHAPE.RECTANGLE,int(cx-r*1.0),int(cy-r*1.15),int(d*0.07),int(r*2.3),ic)
        ashape(s,MSO_SHAPE.RIGHT_ARROW,int(cx-r*0.9),int(cy-r*1.1),int(r*1.9),int(r*1.15),ic)
    elif kind=="chart":
        bw=int(d*0.12); gap=int(d*0.06); base=int(cy+r*0.9)
        for i,hfac in enumerate([0.55,0.95,1.35]):
            bh=int(r*hfac); x=int(cx-r*1.05+i*(bw+gap))
            ashape(s,MSO_SHAPE.RECTANGLE,x,base-bh,bw,bh,ic)
    elif kind=="refresh":
        # Bigger bounding box — CIRCULAR_ARROW's arrowhead gets clipped/unreadable
        # if drawn too tight at badge scale.
        ashape(s,MSO_SHAPE.CIRCULAR_ARROW,int(cx-r*1.35),int(cy-r*1.35),int(r*2.7),int(r*2.7),ic)
    elif kind=="shield":
        # PENTAGON's un-rotated point faces right (home-plate); rotate 90° so the
        # point faces down — flat top, pointed base reads as a shield/badge.
        pent=ashape(s,MSO_SHAPE.PENTAGON,int(cx-r*1.1),int(cy-r*1.15),int(r*2.2),int(r*2.3),ic)
        pent.rotation=90
    elif kind=="people":
        oval(s,int(cx-r*1.05),int(cy-r*0.5),int(r*1.3),int(r*1.3),ic)
        oval(s,int(cx-r*0.1),int(cy-r*0.7),int(r*1.5),int(r*1.5),ic)
    elif kind=="clock":
        ring=ashape(s,MSO_SHAPE.OVAL,int(cx-r*1.1),int(cy-r*1.1),int(r*2.2),int(r*2.2),ic,line=None)
        oval(s,int(cx-d*0.06),int(cy-d*0.06),int(d*0.12),int(d*0.12),badge_color)
        h1=ashape(s,MSO_SHAPE.RECTANGLE,int(cx-d*0.02),int(cy-r*0.9),int(d*0.045),int(r*0.9),badge_color)
        h2=ashape(s,MSO_SHAPE.RECTANGLE,int(cx-d*0.02),int(cy-r*0.55),int(d*0.045),int(r*0.55),badge_color); h2.rotation=90
    elif kind=="target":
        oval(s,int(cx-r*1.15),int(cy-r*1.15),int(r*2.3),int(r*2.3),ic)
        oval(s,int(cx-r*0.7),int(cy-r*0.7),int(r*1.4),int(r*1.4),badge_color)
        oval(s,int(cx-r*0.25),int(cy-r*0.25),int(r*0.5),int(r*0.5),ic)
    elif kind=="star":
        ashape(s,MSO_SHAPE.STAR_5_POINT,int(cx-r*1.15),int(cy-r*1.15),int(r*2.3),int(r*2.3),ic)
    elif kind=="lightning":
        ashape(s,MSO_SHAPE.LIGHTNING_BOLT,int(cx-r*0.85),int(cy-r*1.2),int(r*1.7),int(r*2.4),ic)
    elif kind=="idea":
        ashape(s,MSO_SHAPE.CLOUD,int(cx-r*1.2),int(cy-r*1.0),int(r*2.4),int(r*2.0),ic)
    elif kind=="heart":
        ashape(s,MSO_SHAPE.HEART,int(cx-r*1.1),int(cy-r*1.1),int(r*2.2),int(r*2.2),ic)
    elif kind=="check":
        # A crisp ✓ glyph reads far better at badge scale than any checkmark-ish autoshape.
        txt(s,int(cx-d/2),int(cy-d/2),d,d,[[("✓",int(d/914400*24),ic,True)]],
            align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    return bd

def pyramid_steps(title,levels,kicker=None,source=None):
    """Ascending stacked-block pyramid (bottom = level 1, widest) with a linked
    explanation card per level, right of the pyramid. levels: [(numeral,heading,caption), ...]."""
    s=head(slide(),title,kicker,kcolor=BLUE); n=len(levels)
    X0=Inches(0.85); AREA_W=Inches(5.5); CX=int(X0+AREA_W/2)
    Y0=Inches(1.95); AREA_H=Inches(4.65); gap=Inches(0.12)
    lh=int((AREA_H-gap*(n-1))/n)
    maxw=AREA_W; minw=int(AREA_W*0.42)
    cardx=Inches(6.85); cardw=Inches(5.63)
    for i,(num,head_txt,cap) in enumerate(levels):
        # i=0 -> bottom (widest); draw bottom-up, narrowing toward the top
        lvl_from_bottom=i
        w=int(maxw-(maxw-minw)*(lvl_from_bottom/max(n-1,1)))
        y=int(Y0+AREA_H-lh-(lh+gap)*lvl_from_bottom)
        x=int(CX-w/2)
        col=GRADIENTS[i%len(GRADIENTS)]
        grad_rect(s,MSO_SHAPE.ROUNDED_RECTANGLE,x,y,w,lh,col[0],col[1],angle=0,shadow=True)
        txt(s,x,y,w,lh,[[(num,26 if lh>Inches(0.7) else 20,WHITE,True)]],
            align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        cy=int(y+lh/2)
        conn(s,int(x+w),cy,cardx,cy,LINE,1.25)
        oval(s,cardx-Inches(0.05),cy-Inches(0.05),Inches(0.1),Inches(0.1),col[0])
        rect(s,cardx,y,cardw,lh,LIGHT,shadow=True); rect(s,cardx,y,Inches(0.08),lh,col[0])
        txt(s,cardx+Inches(0.28),y,cardw-Inches(0.5),lh,
            [[(head_txt,15,INK,True)],[(cap,12.5,GREY,False)]],anchor=MSO_ANCHOR.MIDDLE,space=2)
    _source_line(s,source); footer(s); return s

def icon_cards_grad(title,cards,kicker=None,cols=3,source=None):
    """Grid of cards with a gradient icon-badge header + heading + body.
    cards: [(icon_glyph, heading, body), ...]."""
    s=head(slide(),title,kicker,kcolor=VIOLET); n=len(cards); rows=math.ceil(n/cols)
    X0=Inches(0.85); Y0=Inches(1.95); TOTW=Inches(11.63); AREAH=Inches(4.6 if source else 4.78)
    gx=Inches(0.3); gy=Inches(0.28)
    cw=int((TOTW-gx*(cols-1))/cols); ch=int((AREAH-gy*(rows-1))/rows)
    hh=min(Inches(0.55),int(ch*0.34))
    for i,(icon,hd,body) in enumerate(cards):
        r=i//cols; c=i%cols
        x=int(X0+(cw+gx)*c); y=int(Y0+(ch+gy)*r)
        col=GRADIENTS[i%len(GRADIENTS)]
        rect(s,x,y,cw,ch,LIGHT,shadow=True)
        grad_rect(s,MSO_SHAPE.RECTANGLE,x,y,cw,hh,col[0],col[1],angle=0)
        bd=int(hh*0.62)
        icon_badge(s,icon,int(x+cw-bd/2-Inches(0.12)),int(y+hh/2),bd,WHITE,icon_color=col[1],shadow=False)
        txt(s,x+Inches(0.22),int(y+hh+Inches(0.12)),cw-Inches(0.4),int(ch-hh-Inches(0.2)),
            [[(hd,15,INK,True)],[(body,12.5,GREY,False)]],space=4)
    _source_line(s,source); footer(s); return s

def pros_cons_arrows(title,left_label,left_items,right_label,right_items,kicker=None,source=None):
    """Two opposing block-arrow banners with icon-badge cards fanning out on each side."""
    s=head(slide(),title,kicker,kcolor=BLUE)
    X0=Inches(0.85); TOTW=Inches(11.63); GAPW=Inches(2.5)
    colw=int((TOTW-GAPW)/2); rx=int(X0+colw+GAPW)
    Y0=Inches(2.0); AREAH=Inches(4.55)
    def col_cards(x,items,accent):
        n=len(items); gy=Inches(0.22); ch=int((AREAH-gy*(n-1))/n); bd=Inches(0.55)
        for i,(icon,hd,cap) in enumerate(items):
            y=int(Y0+(ch+gy)*i)
            rect(s,x,y,colw,ch,LIGHT,shadow=True); rect(s,x,y,Inches(0.08),ch,accent)
            icon_badge(s,icon,int(x+Inches(0.22)+bd/2),int(y+ch/2),bd,accent)
            tx=int(x+Inches(0.9)); tw=colw-Inches(1.1)
            txt(s,tx,y,tw,ch,[[(hd,14,INK,True)],[(cap,12,GREY,False)]],anchor=MSO_ANCHOR.MIDDLE,space=2)
    col_cards(X0,left_items,BLUE); col_cards(rx,right_items,TEAL)
    gx=int(X0+colw+Inches(0.15)); gw=int(GAPW-Inches(0.3))
    # Labels can run long ("Reactive — Defensive & Silent") — size the font down and
    # give the arrow enough height that a 2-line wrap never collides with its neighbour.
    def _label_size(label): return 15 if len(label)<=16 else (12.5 if len(label)<=28 else 11)
    ah=Inches(1.05); ay1=Inches(2.35); ay2=Inches(3.75)
    a1=ashape(s,MSO_SHAPE.LEFT_ARROW,gx,ay1,gw,ah,BLUE,shadow=True)
    txt(s,gx,ay1,gw,ah,[[(left_label.upper(),_label_size(left_label),WHITE,True)]],
        align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    a2=ashape(s,MSO_SHAPE.RIGHT_ARROW,gx,ay2,gw,ah,TEAL,shadow=True)
    txt(s,gx,ay2,gw,ah,[[(right_label.upper(),_label_size(right_label),WHITE,True)]],
        align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    _source_line(s,source); footer(s); return s

def journey_loop(title,stages,kicker=None,source=None):
    """Horizontal stage row (numbered chips) linked by chevrons, closed by a
    return arrow underneath — a cycle/journey loop, not a one-way flow."""
    s=head(slide(),title,kicker,kcolor=TEAL)
    n=len(stages); X0=Inches(0.85); TOTW=Inches(11.63); gap=Inches(0.3)
    cw=int((TOTW-gap*(n-1))/n); y=Inches(2.15); ch=Inches(2.95); bd=Inches(0.72)
    for i,(hd,cap) in enumerate(stages):
        x=int(X0+(cw+gap)*i); col=PALETTE[i%len(PALETTE)]
        rect(s,x,y,cw,ch,LIGHT,shadow=True); rect(s,x,y,cw,Inches(0.09),col)
        oval(s,int(x+cw/2-bd/2),int(y+Inches(0.3)),bd,bd,col,shadow=True)
        txt(s,int(x+cw/2-bd/2),int(y+Inches(0.3)),bd,bd,[[(str(i+1),24,WHITE,True)]],
            align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,x+Inches(0.14),int(y+Inches(1.2)),cw-Inches(0.28),int(ch-Inches(1.3)),
            [[(hd,13.5,INK,True)],[(cap,11.5,GREY,False)]],align=PP_ALIGN.CENTER,space=3)
        if i<n-1:
            txt(s,int(x+cw-Inches(0.02)),int(y+Inches(0.28)),int(gap+Inches(0.04)),bd,
                [[("›",20,col,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    loopy=int(y+ch+Inches(0.35))
    ashape(s,MSO_SHAPE.LEFT_ARROW,X0,loopy,TOTW,Inches(0.55),NAVY2)
    txt(s,X0,loopy,TOTW,Inches(0.55),
        [[("THE CYCLE REPEATS — EVERY STAGE FEEDS THE NEXT",13,WHITE,True)]],
        align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    _source_line(s,source); footer(s); return s

def hex_model(title,points,kicker=None,source=None):
    """Row of hexagon nodes (big numeral) with heading/caption beneath each —
    for a 4-6 point named framework."""
    s=head(slide(),title,kicker,kcolor=AMBER); n=len(points)
    X0=Inches(0.85); TOTW=Inches(11.63); gap=Inches(0.22)
    cw=int((TOTW-gap*(n-1))/n); hexw=min(cw,Inches(1.9)); hexh=Inches(1.65)
    y=Inches(2.1)
    for i,(num,hd,cap) in enumerate(points):
        cx0=int(X0+(cw+gap)*i); hx=int(cx0+(cw-hexw)/2); col=PALETTE[i%len(PALETTE)]
        ashape(s,MSO_SHAPE.HEXAGON,hx,y,hexw,hexh,col,shadow=True)
        txt(s,hx,y,hexw,hexh,[[(num,30,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,cx0,int(y+hexh+Inches(0.22)),cw,Inches(0.5),[[(hd,14,INK,True)]],align=PP_ALIGN.CENTER)
        txt(s,cx0,int(y+hexh+Inches(0.68)),cw,Inches(1.9),[[(cap,12,GREY,False)]],align=PP_ALIGN.CENTER)
    _source_line(s,source); footer(s); return s

def quadrant_2x2(title,x_axis,y_axis,quadrants,kicker=None,source=None):
    """2x2 framework matrix (e.g. power/interest). quadrants = [top-left, top-right,
    bottom-left, bottom-right], each (name, color, [short items])."""
    s=head(slide(),title,kicker,kcolor=VIOLET)
    txt(s,Inches(0.85),Inches(1.92),Inches(11.6),Inches(0.3),
        [[(f"Y-axis: {y_axis}   ·   X-axis: {x_axis}",11.5,GREY,True)]])
    X0=Inches(0.85); Y0=Inches(2.3); TOTW=Inches(11.63); TOTH=Inches(4.35)
    gx=Inches(0.22); gy=Inches(0.22)
    cw=int((TOTW-gx)/2); ch=int((TOTH-gy)/2)
    pos=[(X0,Y0),(int(X0+cw+gx),Y0),(X0,int(Y0+ch+gy)),(int(X0+cw+gx),int(Y0+ch+gy))]
    for i,(name,col,items) in enumerate(quadrants):
        x,y=pos[i]
        rect(s,x,y,cw,ch,LIGHT,shadow=True); rect(s,x,y,cw,Inches(0.1),col)
        txt(s,x+Inches(0.22),int(y+Inches(0.22)),cw-Inches(0.4),Inches(0.5),[[(name,15,col,True)]])
        bullets(s,x+Inches(0.22),int(y+Inches(0.75)),cw-Inches(0.4),int(ch-Inches(0.9)),items,size=12.5,gap=5,mcolor=col)
    _source_line(s,source); footer(s); return s

def road_process(title,steps,kicker=None,source=None,color=BLUE):
    """Winding process path — two narrow centre columns of numbered stop
    markers joined by right-angle 'road' connectors, labels in the generous
    margin on the open side of each node. steps: [(icon_kind, heading,
    caption), ...], up to 4 items (2 legs of the zigzag)."""
    s=head(slide(),title,kicker,kcolor=color); n=min(len(steps),4)
    # Node columns sit close to centre so there's always >=3.3in of clear
    # margin on the open side for the label — the #1 failure mode here is a
    # label box that runs off the edge of the slide.
    X0=Inches(4.95); X1=Inches(8.35); Y0=Inches(2.35); Y1=Inches(6.0)
    xs=[X0,X1,X0,X1][:n]
    ys=[int(Y0+(Y1-Y0)*i/max(n-1,1)) for i in range(n)]
    for i in range(n-1):
        cn=s.shapes.add_connector(MSO_CONNECTOR.ELBOW,xs[i],ys[i],xs[i+1],ys[i+1])
        cn.line.color.rgb=RGBColor(0xCE,0xD6,0xE3); cn.line.width=Pt(9)
        cn.shadow.inherit=False
    lw=Inches(3.35)
    for i,(icon,hd,cap) in enumerate(steps[:n]):
        x,y=xs[i],ys[i]; bd=Inches(0.62)
        on_right=(x==X1)  # label goes on the open side, away from the other column
        lx=int(x+bd/2+Inches(0.28)) if on_right else int(x-bd/2-Inches(0.28)-lw)
        align=PP_ALIGN.LEFT if on_right else PP_ALIGN.RIGHT
        txt(s,lx,int(y-Inches(0.5)),lw,Inches(1.0),
            [[(hd,15,INK,True)],[(cap,12,GREY,False)]],align=align,anchor=MSO_ANCHOR.MIDDLE,space=3)
        icon_badge(s,icon,x,y,bd,PALETTE[i%len(PALETTE)])
        txt(s,int(x-Inches(0.3)),int(y-bd/2-Inches(0.34)),Inches(0.6),Inches(0.26),
            [[(str(i+1),12,GREY,True)]],align=PP_ALIGN.CENTER)
    _source_line(s,source); footer(s); return s

def split_letter_cards(title,left,right,kicker=None,source=None):
    """Two-way comparison as big-letter split cards (à la 'F Frameworks vs
    P Platforms'). left/right: (letter_or_short_word, label, [items])."""
    s=head(slide(),title,kicker,kcolor=BLUE)
    X0=Inches(0.85); TOTW=Inches(11.63); gap=Inches(0.3); cw=int((TOTW-gap)/2)
    Y0=Inches(1.95); hh=Inches(1.7); bh=Inches(2.95)
    for i,(letter,label,items) in enumerate([left,right]):
        x=int(X0+(cw+gap)*i); col=GRADIENTS[0 if i==0 else 1]
        grad_rect(s,MSO_SHAPE.ROUNDED_RECTANGLE,x,Y0,cw,hh,col[0],col[1],shadow=True)
        txt(s,x,int(Y0+Inches(0.12)),cw,Inches(1.0),[[(letter,54,WHITE,True)]],align=PP_ALIGN.CENTER)
        txt(s,x,int(Y0+hh-Inches(0.5)),cw,Inches(0.4),[[(label.upper(),14,WHITE,True)]],align=PP_ALIGN.CENTER)
        rect(s,x,int(Y0+hh+Inches(0.1)),cw,bh,LIGHT,shadow=True)
        bullets(s,int(x+Inches(0.3)),int(Y0+hh+Inches(0.35)),cw-Inches(0.6),int(bh-Inches(0.4)),
                items,size=14,mcolor=col[0],gap=8)
    _source_line(s,source); footer(s); return s

def donut_ring(title,items,kicker=None,source=None,color=BLUE):
    """A real, native PowerPoint doughnut chart for a share/split stat —
    editable, animatable, not a hand-drawn approximation. items: [(label,value), ...]."""
    s=head(slide(),title,kicker,kcolor=color)
    cd=CategoryChartData(); cd.categories=[lbl for lbl,_ in items]
    cd.add_series("Share",[v for _,v in items])
    gx=graphic_frame=s.shapes.add_chart(XL_CHART_TYPE.DOUGHNUT,Inches(0.9),Inches(2.0),Inches(5.6),Inches(4.6),cd)
    chart=gx.chart; chart.has_legend=False
    plot=chart.plots[0]; plot.has_data_labels=True
    dls=plot.data_labels; dls.number_format="0%"; dls.number_format_is_linked=False
    dls.show_percentage=True; dls.show_value=False; dls.show_category_name=False
    dls.font.size=Pt(13); dls.font.bold=True; dls.font.color.rgb=WHITE
    for i,pt in enumerate(plot.series[0].points):
        pt.format.fill.solid(); pt.format.fill.fore_color.rgb=PALETTE[i%len(PALETTE)]
        pt.format.line.color.rgb=WHITE; pt.format.line.width=Pt(2)
    lx=Inches(6.9); ly=Inches(2.15); lw=Inches(5.55); rh=int(Inches(4.3)/len(items))
    for i,(lbl,val) in enumerate(items):
        y=int(ly+rh*i); col=PALETTE[i%len(PALETTE)]
        oval(s,lx,int(y+Inches(0.1)),Inches(0.28),Inches(0.28),col)
        txt(s,int(lx+Inches(0.45)),y,int(lw-Inches(0.45)),int(rh-Inches(0.1)),
            [[(f"{lbl} — {val}%",15,INK,True)]],anchor=MSO_ANCHOR.MIDDLE)
    _source_line(s,source); footer(s); return s

_IG_PW=None; _IG_BROWSER=None
def _ig_browser():
    """Lazily launch one shared headless-Chromium instance for all AntV
    infographic renders in this build run (Playwright docs and the reference
    project both warn that launching per-call is slow/flaky)."""
    global _IG_PW,_IG_BROWSER
    if _IG_BROWSER is None:
        from playwright.sync_api import sync_playwright
        _IG_PW=sync_playwright().start()
        _IG_BROWSER=_IG_PW.chromium.launch(headless=True,
            args=["--disable-gpu","--no-sandbox","--disable-dev-shm-usage"])
    return _IG_BROWSER
def _ig_browser_close():
    global _IG_PW,_IG_BROWSER
    if _IG_BROWSER is not None:
        _IG_BROWSER.close(); _IG_PW.stop(); _IG_BROWSER=None; _IG_PW=None

def infographic_slide(title,items,template,kicker=None,source=None):
    """AI-infographic slide — renders items through the AntV Infographic
    engine (courseware/build/infographic_render.py, ported from the
    reference project's deterministic DSL pipeline) via headless Chromium,
    then embeds the PNG. items: same tuple shapes as the native diagram
    helpers — (kind,label), (kind,heading,body), (heading,caption) or
    (label,value). Falls back to a plain text notice if rendering fails
    (e.g. offline) so one bad render never breaks the whole build."""
    s=head(slide(),title,kicker)
    try:
        png_path=IG.render_infographic_png(title,items,template,_ig_browser())
        pw,ph=IG.get_png_size(png_path)
        card_x,card_y=Inches(0.85),Inches(1.85); card_w,card_h=Inches(11.63),Inches(4.85)
        # Some AntV templates (hierarchy trees, small charts, 3-item rows) lay
        # out compactly and leave much of the fixed canvas blank; autocrop then
        # produces a small image relative to the slide's content area. A light
        # card behind it means that space reads as an intentional frame rather
        # than a failed/empty render.
        rect(s,card_x,card_y,card_w,card_h,LIGHT,shadow=True)
        max_w,max_h=card_w-Inches(0.5),card_h-Inches(0.5)
        scale=min(max_w/pw,max_h/ph)
        w,h=int(pw*scale),int(ph*scale)
        x=int(card_x+(card_w-w)/2); y=int(card_y+(card_h-h)/2)
        s.shapes.add_picture(png_path,x,y,width=w,height=h)
    except Exception as e:
        txt(s,Inches(0.85),Inches(2.3),Inches(11.6),Inches(2),
            [[(f"[infographic unavailable: {e}]",13,GREY,False)]])
    _source_line(s,source); footer(s); return s

EMOTION_COLOR=[RGBColor(0xEF,0x44,0x44),RGBColor(0xF5,0x9E,0x0B),RGBColor(0xF5,0x9E,0x0B),
               RGBColor(0x10,0xB9,0x81),RGBColor(0x10,0xB9,0x81)]  # 1..5 -> red..amber..green
def journey_map(title,stages,kicker=None,source=None):
    """Customer journey map: stage nodes across the top, an emotion/satisfaction
    curve underneath (straight-segment polyline — simple and robust, no freeform
    curve maths to get wrong). stages: [(icon_kind, stage_name, touchpoint, emotion_1to5)]."""
    s=head(slide(),title,kicker,kcolor=VIOLET); n=len(stages)
    X0=Inches(0.85); TOTW=Inches(11.63); gap=Inches(0.25)
    cw=int((TOTW-gap*(n-1))/n); topy=Inches(2.05); bd=Inches(0.6)
    curvey0=Inches(4.35); curvey1=Inches(6.15)  # emotion 5 (happiest) plots near curvey0, 1 near curvey1
    pts=[]
    for i,(icon,name,touch,emo) in enumerate(stages):
        cx=int(X0+cw*i+cw/2)
        icon_badge(s,icon,cx,int(topy+bd/2),bd,PALETTE[i%len(PALETTE)])
        # Stage names can wrap to 2 lines in a narrow column (5-6 stages) — size
        # down and give the caption below enough clearance that a 2-line name
        # never collides with it.
        name_size=13.5 if len(name)<=13 else 11.5
        txt(s,int(cx-cw/2+Inches(0.06)),int(topy+bd+Inches(0.1)),int(cw-Inches(0.12)),Inches(0.6),
            [[(name,name_size,INK,True)]],align=PP_ALIGN.CENTER)
        txt(s,int(cx-cw/2+Inches(0.06)),int(topy+bd+Inches(0.75)),int(cw-Inches(0.12)),Inches(0.5),
            [[(touch,11,GREY,False)]],align=PP_ALIGN.CENTER)
        ey=int(curvey1-(curvey1-curvey0)*((emo-1)/4))
        pts.append((cx,ey,emo))
    for i in range(n-1):
        conn(s,pts[i][0],pts[i][1],pts[i+1][0],pts[i+1][1],RGBColor(0xC7,0xD0,0xDE),3)
    for cx,ey,emo in pts:
        col=EMOTION_COLOR[max(1,min(5,emo))-1]
        oval(s,int(cx-Inches(0.11)),int(ey-Inches(0.11)),Inches(0.22),Inches(0.22),col,shadow=True)
    txt(s,X0,int(curvey0-Inches(0.35)),TOTW,Inches(0.3),
        [[("EMOTIONAL EXPERIENCE — HIGHER IS BETTER",11,GREY,True)]],align=PP_ALIGN.CENTER)
    _source_line(s,source); footer(s); return s

def service_blueprint(title,stage_labels,lanes,kicker=None,source=None):
    """Service-blueprint swimlane grid. stage_labels: column headers.
    lanes: [(lane_name, color, [cell_text_per_stage]), ...] — typically
    Customer Actions / Frontstage / Backstage / Support Processes."""
    s=head(slide(),title,kicker,kcolor=BLUE)
    X0=Inches(0.85); Y0=Inches(1.95); TOTW=Inches(11.63)
    lanew=Inches(1.85); colsw=TOTW-lanew; ncols=len(stage_labels)
    cw=int(colsw/ncols); hh=Inches(0.5); nrows=len(lanes)
    rh=int((Inches(4.6)-hh)/nrows)
    for c,label in enumerate(stage_labels):
        x=int(X0+lanew+cw*c)
        rect(s,x,Y0,cw,hh,NAVY2)
        txt(s,x+Inches(0.05),Y0,cw-Inches(0.1),hh,[[(label,11.5,WHITE,True)]],
            align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    for r,(lane_name,col,cells) in enumerate(lanes):
        y=int(Y0+hh+rh*r)
        rect(s,X0,y,lanew,rh,col,shadow=True)
        txt(s,X0+Inches(0.12),y,lanew-Inches(0.2),rh,[[(lane_name,12.5,WHITE,True)]],
            anchor=MSO_ANCHOR.MIDDLE)
        for c,cell in enumerate(cells[:ncols]):
            x=int(X0+lanew+cw*c)
            rect(s,x,y,cw,rh,WHITE if r%2==0 else LIGHT,line=RGBColor(0xE8,0xEC,0xF2))
            txt(s,x+Inches(0.1),y,cw-Inches(0.2),rh,[[(cell,11,INK,False)]],
                align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    _source_line(s,source); footer(s); return s

def funnel_chart(title,stages,kicker=None,source=None):
    """Marketing/sales funnel — index 0 = top of funnel (widest), narrowing
    downward. stages: [(label, value_label, caption), ...]."""
    s=head(slide(),title,kicker,kcolor=VIOLET); n=len(stages)
    X0=Inches(0.85); AREA_W=Inches(5.3); CX=int(X0+AREA_W/2)
    Y0=Inches(2.0); AREA_H=Inches(4.55); gap=Inches(0.12)
    lh=int((AREA_H-gap*(n-1))/n)
    maxw=AREA_W; minw=int(AREA_W*0.38)
    cardx=Inches(6.65); cardw=Inches(5.83)
    for i,(label,val,cap) in enumerate(stages):
        w=int(maxw-(maxw-minw)*(i/max(n-1,1)))
        y=int(Y0+(lh+gap)*i); x=int(CX-w/2)
        col=GRADIENTS[i%len(GRADIENTS)]
        grad_rect(s,MSO_SHAPE.TRAPEZOID,x,y,w,lh,col[0],col[1],angle=90,shadow=True)
        txt(s,x,y,w,lh,[[(val,20 if lh>Inches(0.6) else 16,WHITE,True)]],
            align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        cy=int(y+lh/2)
        conn(s,int(x+w),cy,cardx,cy,LINE,1.25)
        oval(s,cardx-Inches(0.05),cy-Inches(0.05),Inches(0.1),Inches(0.1),col[0])
        rect(s,cardx,y,cardw,lh,LIGHT,shadow=True); rect(s,cardx,y,Inches(0.08),lh,col[0])
        txt(s,cardx+Inches(0.28),y,cardw-Inches(0.5),lh,
            [[(label,15,INK,True)],[(cap,12.5,GREY,False)]],anchor=MSO_ANCHOR.MIDDLE,space=2)
    _source_line(s,source); footer(s); return s

EMPATHY_QUADS=[("Says","chat",BLUE),("Thinks","idea",VIOLET),("Does","target",TEAL),("Feels","heart",AMBER)]
def empathy_map(title,items_says,items_thinks,items_does,items_feels,kicker=None,source=None):
    """Fixed 4-quadrant customer empathy map: Says / Thinks / Does / Feels."""
    s=head(slide(),title,kicker,kcolor=VIOLET)
    X0=Inches(0.85); Y0=Inches(2.0); TOTW=Inches(11.63); TOTH=Inches(4.55)
    gx=Inches(0.22); gy=Inches(0.22)
    cw=int((TOTW-gx)/2); ch=int((TOTH-gy)/2)
    pos=[(X0,Y0),(int(X0+cw+gx),Y0),(X0,int(Y0+ch+gy)),(int(X0+cw+gx),int(Y0+ch+gy))]
    items=[items_says,items_thinks,items_does,items_feels]
    for i,((label,icon,col),it) in enumerate(zip(EMPATHY_QUADS,items)):
        x,y=pos[i]
        rect(s,x,y,cw,ch,LIGHT,shadow=True)
        icon_badge(s,icon,int(x+Inches(0.45)),int(y+Inches(0.42)),Inches(0.5),col)
        txt(s,int(x+Inches(0.8)),int(y+Inches(0.18)),cw-Inches(1.0),Inches(0.5),
            [[(label.upper(),16,col,True)]],anchor=MSO_ANCHOR.MIDDLE)
        bullets(s,x+Inches(0.3),int(y+Inches(0.85)),cw-Inches(0.6),int(ch-Inches(1.0)),it,size=12.5,gap=6,mcolor=col)
    _source_line(s,source); footer(s); return s

def decision_tree(title,root,branches,kicker=None,source=None):
    """Root question box branching into 2-3 outcome cards, joined by elbow
    connectors. branches: [(choice_label, outcome_heading, outcome_caption, color), ...].
    The root box width/height/font adapt to the question's length — a long
    root question is the #1 way this diagram breaks if left at a fixed size."""
    s=head(slide(),title,kicker,kcolor=BLUE); n=len(branches)
    rw=Inches(9.7); rx=int((SW-rw)/2); ry=Inches(1.95)
    size=15 if len(root)<=64 else (13 if len(root)<=100 else 12)
    chars_per_line={15:58,13:70,12:78}[size]
    lines=max(1,math.ceil(len(root)/chars_per_line))
    rh=Inches(0.4+0.36*lines)
    rect(s,rx,ry,rw,rh,NAVY2,shadow=True)
    txt(s,rx+Inches(0.3),ry,rw-Inches(0.6),rh,[[(root,size,WHITE,True)]],
        align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    X0=Inches(0.85); TOTW=Inches(11.63); gap=Inches(0.3)
    cw=int((TOTW-gap*(n-1))/n)
    rootcx=int(rx+rw/2); rootby=int(ry+rh)
    chipy=int(rootby+Inches(0.3)); chiph=Inches(0.4)
    oy=int(chipy+chiph+Inches(0.25))
    oh=min(Inches(2.2),int(Inches(6.85)-oy))
    for i,(choice,heading,cap,col) in enumerate(branches):
        x=int(X0+(cw+gap)*i); cx=int(x+cw/2)
        cn=s.shapes.add_connector(MSO_CONNECTOR.ELBOW,rootcx,rootby,cx,oy)
        cn.line.color.rgb=col; cn.line.width=Pt(2.5); cn.shadow.inherit=False
        chipw=Inches(1.9); chipx=int(cx-chipw/2)
        rect(s,chipx,chipy,chipw,chiph,col,shadow=True)
        txt(s,chipx,chipy,chipw,chiph,[[(choice.upper(),11,WHITE,True)]],
            align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        rect(s,x,oy,cw,oh,LIGHT,shadow=True); rect(s,x,oy,cw,Inches(0.08),col)
        txt(s,x+Inches(0.2),int(oy+Inches(0.2)),cw-Inches(0.4),Inches(0.5),[[(heading,14.5,INK,True)]])
        txt(s,x+Inches(0.2),int(oy+Inches(0.75)),cw-Inches(0.4),int(oh-Inches(0.9)),[[(cap,12,GREY,False)]])
    _source_line(s,source); footer(s); return s

def kpi_dashboard(title,kpis,kicker=None,source=None):
    """Grid of KPI stat cards: big value, label, coloured up/down delta chip.
    kpis: [(value, label, delta, trend), ...] trend in {"up","down","flat"}."""
    s=head(slide(),title,kicker,kcolor=TEAL); n=len(kpis); cols=min(n,4)
    X0=Inches(0.85); Y0=Inches(2.1); TOTW=Inches(11.63); gx=Inches(0.3)
    cw=int((TOTW-gx*(cols-1))/cols); ch=Inches(3.2)
    arrow={"up":"▲","down":"▼","flat":"●"}
    dcolor={"up":TEAL,"down":RGBColor(0xEF,0x44,0x44),"flat":GREY}
    for i,(val,label,delta,trend) in enumerate(kpis):
        x=int(X0+(cw+gx)*i); col=PALETTE[i%len(PALETTE)]
        rect(s,x,Y0,cw,ch,LIGHT,shadow=True); rect(s,x,Y0,cw,Inches(0.09),col)
        txt(s,x+Inches(0.2),int(Y0+Inches(0.35)),cw-Inches(0.4),Inches(1.1),
            [[(val,36,INK,True)]])
        txt(s,x+Inches(0.2),int(Y0+Inches(1.45)),cw-Inches(0.4),Inches(0.6),
            [[(label,13,GREY,False)]])
        dc=dcolor.get(trend,GREY)
        txt(s,x+Inches(0.2),int(Y0+Inches(2.15)),cw-Inches(0.4),Inches(0.5),
            [[(arrow.get(trend,"●")+" ",13,dc,True),(delta,13,dc,True)]])
    _source_line(s,source); footer(s); return s

def persona_card(title,personas,kicker=None,source=None):
    """1-3 customer-persona cards: avatar initials, role tag, goals vs
    frustrations. personas: [(name, role_tag, [goals], [frustrations]), ...]."""
    s=head(slide(),title,kicker,kcolor=VIOLET); n=min(len(personas),3)
    X0=Inches(0.85); TOTW=Inches(11.63); gap=Inches(0.3); cw=int((TOTW-gap*(n-1))/n)
    Y0=Inches(1.95); ch=Inches(4.7)
    for i,(name,role,goals,frustrations) in enumerate(personas[:3]):
        x=int(X0+(cw+gap)*i); col=PALETTE[i%len(PALETTE)]
        rect(s,x,Y0,cw,ch,LIGHT,shadow=True); rect(s,x,Y0,cw,Inches(0.95),col)
        bd=Inches(0.62)
        oval(s,int(x+cw/2-bd/2),int(Y0+Inches(0.15)),bd,bd,WHITE,shadow=True)
        initials="".join(w[0] for w in name.split()[:2]).upper()
        txt(s,int(x+cw/2-bd/2),int(Y0+Inches(0.15)),bd,bd,[[(initials,17,col,True)]],
            align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,x,int(Y0+Inches(0.9)),cw,Inches(0.4),[[(name,15,INK,True)]],align=PP_ALIGN.CENTER)
        txt(s,x,int(Y0+Inches(1.25)),cw,Inches(0.35),[[(role,11.5,col,True)]],align=PP_ALIGN.CENTER)
        gy=int(Y0+Inches(1.75))
        txt(s,x+Inches(0.22),gy,cw-Inches(0.44),Inches(0.3),[[("GOALS",11,col,True)]])
        bullets(s,x+Inches(0.22),int(gy+Inches(0.32)),cw-Inches(0.44),Inches(1.1),goals,size=11.5,mcolor=col,gap=4)
        fy=int(gy+Inches(1.55))
        txt(s,x+Inches(0.22),fy,cw-Inches(0.44),Inches(0.3),[[("FRUSTRATIONS",11,GREY,True)]])
        bullets(s,x+Inches(0.22),int(fy+Inches(0.32)),cw-Inches(0.44),Inches(1.1),frustrations,size=11.5,mcolor=GREY,gap=4)
    _source_line(s,source); footer(s); return s

def ecosystem_map(title,center_label,nodes,kicker=None,source=None):
    """Hub-and-spoke stakeholder/ecosystem map: a central brand node with
    surrounding nodes radiating out, connected by spokes. nodes: [(icon_kind,
    label), ...], 5-8 works best."""
    s=head(slide(),title,kicker,kcolor=BLUE); n=len(nodes)
    # R and cy0 are tuned so the bottom node's label (icon + 0.08in gap + 0.55in
    # label box) always clears the footer band at y=7.05in — don't enlarge R
    # without re-checking that: cy0 + R + badge_r + 0.08 + 0.55 must stay < 7.0.
    cx0,cy0=int(SW/2),Inches(4.3); R=Inches(1.7)
    hub=Inches(1.2)
    for i,(icon,label) in enumerate(nodes):
        ang=-90+360*i/n; rad=math.radians(ang)
        nx=int(cx0+R*math.cos(rad)); ny=int(cy0+R*math.sin(rad))
        conn(s,cx0,cy0,nx,ny,RGBColor(0xD5,0xDC,0xE8),2.25)
    for i,(icon,label) in enumerate(nodes):
        ang=-90+360*i/n; rad=math.radians(ang)
        nx=int(cx0+R*math.cos(rad)); ny=int(cy0+R*math.sin(rad))
        bd=Inches(0.62); col=PALETTE[i%len(PALETTE)]
        icon_badge(s,icon,nx,ny,bd,col)
        lw=Inches(1.7)
        ly=int(ny+bd/2+Inches(0.08))
        txt(s,int(nx-lw/2),ly,lw,Inches(0.55),[[(label,11.5,INK,True)]],align=PP_ALIGN.CENTER)
    oval(s,int(cx0-hub/2),int(cy0-hub/2),hub,hub,NAVY2,shadow=True)
    txt(s,int(cx0-hub/2),int(cy0-hub/2),hub,hub,[[(center_label,13,WHITE,True)]],
        align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    _source_line(s,source); footer(s); return s

def case_study_callout(company,headline,insight,kicker=None,color=BLUE):
    """Light 'Real-World Example' callout card citing a named company — for
    frequent use inline within a topic (unlike quote_callout's dark, rare,
    once-per-LU treatment)."""
    s=head(slide(),headline,kicker,kcolor=color)
    rect(s,Inches(0.85),Inches(1.95),Inches(11.63),Inches(4.6),LIGHT,shadow=True)
    rect(s,Inches(0.85),Inches(1.95),Inches(0.14),Inches(4.6),color)
    rect(s,Inches(1.2),Inches(2.3),Inches(3.1),Inches(0.55),color,shadow=True)
    txt(s,Inches(1.2),Inches(2.3),Inches(3.1),Inches(0.55),[[("REAL-WORLD EXAMPLE",13,WHITE,True)]],
        align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    txt(s,Inches(1.2),Inches(3.15),Inches(10.9),Inches(0.7),[[(company,26,INK,True)]])
    txt(s,Inches(1.2),Inches(3.95),Inches(10.9),Inches(2.4),[[(insight,16,GREY,False)]])
    footer(s); return s

def quote_callout(quote,attribution,kicker=None,color=TEAL):
    """Light full-bleed impact slide for a single big statement/quote —
    use sparingly (about once per Learning Unit), never for routine body content."""
    s=slide(); rect(s,0,0,SW,SH,WHITE); rect(s,0,0,SW,Inches(0.12),color); rect(s,0,Inches(7.38),SW,Inches(0.12),color)
    if kicker: txt(s,Inches(1.1),Inches(1.7),Inches(11),Inches(0.4),[[(kicker,15,color,True)]])
    txt(s,Inches(1.05),Inches(2.0),Inches(1.6),Inches(1.3),[[("“",80,LINE,True)]])
    size=34 if len(quote)<=90 else (27 if len(quote)<=150 else 22)
    txt(s,Inches(1.1),Inches(2.7),Inches(11.1),Inches(3.0),[[(quote,size,INK,True)]],anchor=MSO_ANCHOR.TOP)
    if attribution:
        rect(s,Inches(1.12),Inches(5.9),Inches(0.7),Inches(0.05),color)
        txt(s,Inches(1.1),Inches(6.05),Inches(11),Inches(0.5),[[(attribution,15,GREY,False)]])
    footer(s); return s

def playbook_numerals(title,items,kicker=None,closing=""):
    """Light LU-closer: a colored numeral badge per column, one short
    heading+body under each, closing statement line. Use once per Learning Unit."""
    s=head(slide(),title,kicker,kcolor=TEAL)
    n=len(items); X0=Inches(0.9); TOTW=Inches(11.63); gap=Inches(0.35)
    cw=int((TOTW-gap*(n-1))/n); y=Inches(2.05); bd=Inches(0.65)
    for i,(num,hd,body) in enumerate(items):
        x=int(X0+(cw+gap)*i); cx=int(x+cw/2); col=GRADIENTS[i%len(GRADIENTS)][0]
        oval(s,int(cx-bd/2),y,bd,bd,col,shadow=True)
        txt(s,int(cx-bd/2),y,bd,bd,[[(num,22,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,x,int(y+bd+Inches(0.2)),cw,Inches(0.5),[[(hd,15,INK,True)]])
        txt(s,x,int(y+bd+Inches(0.65)),cw,Inches(2.0),[[(body,12.5,GREY,False)]])
    if closing:
        rect(s,Inches(0.85),Inches(6.15),Inches(11.63),Inches(0.02),LINE)
        txt(s,0,Inches(6.35),SW,Inches(0.6),[[(closing,18,INK,True)]],align=PP_ALIGN.CENTER)
    footer(s); return s

# --------- case-study / role-play activity pattern (replaces step-by-step activities) ---------
CASE_TAG={"case_study":"CASE STUDY","role_play":"ROLE PLAY"}
def scenario_slide(kicker,act_title,case_type,narrative,build,duration):
    """The case narrative as a styled scenario card — tagged Case Study or Role
    Play — never a numbered instruction list."""
    s=head(slide(),act_title,kicker,kcolor=TEAL)
    tag=CASE_TAG.get(case_type,"CASE STUDY")
    rect(s,Inches(0.85),Inches(1.85),Inches(1.85),Inches(0.46),TEAL,shadow=True)
    txt(s,Inches(0.85),Inches(1.89),Inches(1.85),Inches(0.4),[[(tag,13,WHITE,True)]],align=PP_ALIGN.CENTER)
    rect(s,Inches(0.85),Inches(2.5),Inches(11.63),Inches(3.15),LIGHT,shadow=True); rect(s,Inches(0.85),Inches(2.5),Inches(0.1),Inches(3.15),TEAL)
    txt(s,Inches(1.2),Inches(2.72),Inches(10.9),Inches(0.35),[[("THE SITUATION",12,TEAL,True)]])
    paras=[[(p,14.5,INK,False)] for p in narrative]
    txt(s,Inches(1.2),Inches(3.1),Inches(11.0),Inches(2.45),paras,space=8)
    rect(s,Inches(0.85),Inches(5.85),Inches(11.63),Inches(0.75),WHITE,line=LINE,shadow=True)
    txt(s,Inches(1.1),Inches(5.85),Inches(8.0),Inches(0.75),
        [[("You'll produce:  ",13,BLUE,True),(build,13,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
    txt(s,Inches(9.6),Inches(5.85),Inches(2.85),Inches(0.75),
        [[("Duration: ",13,GREY,True),(duration,13,GREY,False)]],anchor=MSO_ANCHOR.MIDDLE,align=PP_ALIGN.RIGHT)
    footer(s); return s
def role_cards_slide(kicker,act_title,roles):
    """Persona cards for role-play activities: role tag, goal, brief."""
    s=head(slide(),act_title,kicker,kcolor=TEAL)
    txt(s,Inches(0.85),Inches(1.88),Inches(9),Inches(0.4),[[("ASSIGN THE ROLES",13,GREY,True)]])
    n=len(roles); X0=Inches(0.85); TOTW=Inches(11.63); gap=Inches(0.3)
    cw=int((TOTW-gap*(n-1))/n); y=Inches(2.4); ch=Inches(4.25)
    for i,(name,goal,brief) in enumerate(roles):
        x=int(X0+(cw+gap)*i); col=PALETTE[i%len(PALETTE)]
        rect(s,x,y,cw,ch,LIGHT,shadow=True); rect(s,x,y,cw,Inches(0.5),col)
        txt(s,x,y,cw,Inches(0.5),[[(name,15,WHITE,True)]],align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        txt(s,int(x+Inches(0.22)),int(y+Inches(0.68)),cw-Inches(0.44),Inches(0.6),[[("GOAL",11,col,True)]])
        txt(s,int(x+Inches(0.22)),int(y+Inches(0.98)),cw-Inches(0.44),Inches(0.9),[[(goal,12.5,INK,True)]])
        txt(s,int(x+Inches(0.22)),int(y+Inches(1.95)),cw-Inches(0.44),Inches(2.2),[[(brief,12,GREY,False)]])
    footer(s); return s
def discussion_slide(kicker,act_title,prompts):
    """Numbered discussion/decision prompts — open questions the group works
    through together, never literal click-by-click steps."""
    s=head(slide(),act_title,kicker,kcolor=TEAL)
    txt(s,Inches(0.85),Inches(1.88),Inches(9),Inches(0.4),[[("DISCUSSION & DECISION PROMPTS",13,GREY,True)]])
    n=len(prompts); X0=Inches(0.85); Y0=Inches(2.35); TOTW=Inches(11.63); gap=Inches(0.16)
    rowh=int((Inches(4.3)-gap*(n-1))/n); bd=min(Inches(0.55),int(rowh*0.68))
    for i,p in enumerate(prompts):
        y=int(Y0+(rowh+gap)*i)
        rect(s,X0,y,TOTW,rowh,LIGHT,shadow=True); rect(s,X0,y,Inches(0.08),rowh,TEAL)
        oval(s,int(X0+Inches(0.22)),int(y+rowh/2-bd/2),bd,bd,TEAL,shadow=True)
        txt(s,int(X0+Inches(0.22)),int(y+rowh/2-bd/2),bd,bd,[[(str(i+1),15,WHITE,True)]],
            align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
        tx=int(X0+Inches(0.22)+bd+Inches(0.28)); tw=int(TOTW-(bd+Inches(0.9)))
        txt(s,tx,y,tw,rowh,[[(p,14.5 if rowh>Inches(0.7) else 13,INK,False)]],anchor=MSO_ANCHOR.MIDDLE)
    footer(s); return s
def reflection_slide(kicker,act_title,reflection_points,debrief_check):
    """Closing reflection questions + the facilitator's debrief check —
    replaces the old pass/fail 'test' slide."""
    s=head(slide(),act_title,kicker,kcolor=TEAL)
    rect(s,Inches(0.85),Inches(1.95),Inches(11.63),Inches(2.9),LIGHT,shadow=True); rect(s,Inches(0.85),Inches(1.95),Inches(0.1),Inches(2.9),VIOLET)
    txt(s,Inches(1.15),Inches(2.15),Inches(11),Inches(0.4),[[("REFLECT & DISCUSS",13,VIOLET,True)]])
    bullets(s,Inches(1.15),Inches(2.6),Inches(11.0),Inches(2.1),reflection_points,size=14.5,mcolor=VIOLET,gap=9)
    rect(s,Inches(0.85),Inches(5.1),Inches(11.63),Inches(1.5),RGBColor(0xE8,0xF7,0xEE),shadow=True)
    txt(s,Inches(1.15),Inches(5.32),Inches(11),Inches(0.4),[[("✓  Facilitator debrief check",15,RGBColor(0x12,0x7A,0x3E),True)]])
    txt(s,Inches(1.15),Inches(5.75),Inches(11.0),Inches(0.8),[[(debrief_check,13,INK,False)]])
    footer(s); return s

# ============================================================ BUILD
SLIDE_MAP={}
cover()

# ---------------- ADMIN (front) ----------------
section("COURSE ADMINISTRATION","Welcome & Housekeeping","")
flow_h("Digital Attendance (Mandatory)",[
 "Mandatory — AM, PM and Assessment digital attendance for WSQ-funded courses.",
 "The trainer/administrator displays the digital attendance QR code from the SSG portal.",
 "Scan the QR code with your mobile phone camera and submit your attendance.",
 "A minimum of 75% attendance is required to be eligible for assessment and funding."],kicker="SSG DIGITAL ATTENDANCE")
SLIDE_MAP["digital_attendance_front"]=PAGE["n"]
trainer_slide("YOUR TRAINER · GENERAL","Your Trainer","General Trainer template —\nto be completed by the trainer",
 [("Name",""),("Title / Designation",""),("Qualifications",""),
  ("Areas of expertise",""),("Training & industry experience",""),("Contact","")],
 initials="?",accent=GREY)
trainer_slide("YOUR TRAINER",C.TRAINER,"Principal Trainer\nTertiary Infotech Academy Pte. Ltd.",
 [("Role",""),("Certification / Credentials",""),
  ("Delivers","WSQ courses on customer-centric branding & communication."),
  ("Contact","")],
 initials="?",accent=BLUE)
content("Let's Know Each Other",[
 "Your name and organisation / role.",
 "Your experience with branding, marketing or communications (if any).",
 "A brand you personally admire — and why it works on you."],kicker="ICE-BREAKER")
tile_grid("Ground Rules",[
 "Set your mobile phone to silent mode.","Actively participate — no question is too small.",
 "Respect each other's views: agree to disagree.","One conversation at a time.",
 "Be punctual; return from breaks on time.","75% attendance is required for funding eligibility."],
 kicker="HOUSEKEEPING",cols=2,size=15)
tile_grid("Skills Framework",[
 ("TSC Title",C.TSC_TITLE),
 ("TSC Code",C.TSC_CODE),
 ("Proficiency Level",C.TSC_LEVEL),
 ("Structure","4 Learning Units (LU1–LU4), each mapped to a Learning Outcome.")],
 kicker="COURSE ACCREDITATION",cols=2,size=15)
tile_grid("Course Outline",
 [(f"{t['code']} — {t['title']}", t["subtitle"]) for t in C.TOPICS],
 kicker="4 LEARNING UNITS",cols=2,size=14)
SLIDE_MAP["lesson_plan_slide"]=None
two_col(f"Lesson Plan — {C.DAYS} Days",
 [(f"Day 1 — {C.DAY_THEMES[1]}",0),
  ("LU1: Stakeholders and Organisation (Activities 1–4)",1),
  ("LU2: Customer Influence (Activities 5–8)",1),
  ("LU3: Branding in Marketing — begins (Activities 9–12)",1)],
 [(f"Day 2 — {C.DAY_THEMES[2]}",0),
  ("LU3: Branding in Marketing — continued",1),
  ("LU4: Branding Effectiveness (Activities 13–17)",1),
  ("Assessment: WA (1h) + Case Study (1h), 4:00–6:00pm",1),
  ("Daily timing",0),("Day 1: 9:30am–6:30pm, 1-hour lunch. Day 2: 9:30am–6:00pm, 45-min lunch (to fit the assessment).",1)],
 kicker="SCHEDULE",lhead="Day 1",rhead="Day 2 & Assessment")
SLIDE_MAP["lesson_plan_slide"]=PAGE["n"]
tile_grid("Learning Outcomes",[
 ("Stakeholders & Organisation","Identify stakeholders/audiences and draft branding designs & reputation assessments."),
 ("Customer Influence","Capture and analyse customer insight through active listening."),
 ("Branding in Marketing","Execute branding campaigns, events and PR activities that build awareness."),
 ("Branding Effectiveness","Evaluate reputation and PR performance against KPIs and recommend improvements.")],
 kicker="WHAT YOU'LL ACHIEVE",cols=2,size=15)
tile_grid("Briefing for Assessment",[
 ("No Phones","Place phones and other materials under the table or on the floor."),
 ("No Recording","No photos or recording of assessment scripts."),
 ("No Discussion","No discussion during the assessment."),
 ("Pen Only","Use a black/blue pen for hard-copy assessments."),
 ("No Correction Tape","No liquid paper / correction tape."),
 ("Time's Up","Scripts are collected when time is up.")],
 kicker="BEFORE YOU BEGIN",cols=3,size=14,icons=["shield","search","chat","check","shield","clock"])
SLIDE_MAP["briefing_assessment"]=PAGE["n"]
tile_grid("Assessment",[
 ("Written Assessment (WA)","Short-Answer Questions (SAQ) — 1 hour, open book."),
 ("Case Study (CS)","One continuous branding scenario, open-ended tasks — 1 hour, open book."),
 ("Format","Open Book — slides, Learner Guide and approved materials only."),
 ("Eligibility & Appeals","Min. 75% attendance, TRAQOM survey completed, assessed as Competent. "
  "An appeal process is available if required.")],
 kicker="FINAL ASSESSMENT",cols=2,size=14,icons=["check","target","shield","idea"])
SLIDE_MAP["assessment_front"]=PAGE["n"]
flow_h("Assessment Flow",[
 "TRAQOM survey — scan the QR code on the LMS",
 "Assessment digital attendance — scan the SSG QR",
 "Sit WA (SAQ) then the Case Study — open book",
 "Submit your answers on the LMS",
 "Sign the Assessment Summary Record"],kicker="ON ASSESSMENT DAY")
content("Courseware & Assessment on the LMS",[
 "Access your course materials, attendance and assessment on the LMS/TMS portal.",
 "Portal: https://lms-tms.tertiaryinfotech.com/",
 "Download the slides and Learner Guide for reference during the open-book assessment."],kicker="COURSE PORTAL")

# ---------------- TOPICS + ACTIVITIES ----------------
# Each Learning Unit (LU) = one Learning Outcome (LO) = several K/A sub-topics (T1, T2, ...).
# Every sub-topic gets: a divider, a "What is X?" concept slide, one supporting data visual,
# THEN the matching in-class activity (scenario/role play -> discussion -> reflection). Theory
# always precedes practice — never jump straight from the LU divider into an activity.
COLOR_TAGS={"blue":BLUE,"teal":TEAL,"violet":VIOLET,"grey":GREY,"amber":AMBER}
def render_what_is(a,t_tag):
    """'What is X?' slot dispatcher — tile (default) / flow / icons (gradient
    icon cards) / ecosystem (hub-and-spoke stakeholder/network map)."""
    kind=a.get("what_is_kind","tile"); title=f"What is {a['t_statement']}?"
    if kind=="flow":
        flow_h(title,a["what_is_items"],kicker=t_tag,source=a.get("what_is_source"))
    elif kind=="icons":
        icon_cards_grad(title,a["what_is_items"],kicker=t_tag,
                         cols=min(len(a["what_is_items"]),4),source=a.get("what_is_source"))
    elif kind=="ecosystem":
        ecosystem_map(title,a["what_is_center"],a["what_is_items"],kicker=t_tag,source=a.get("what_is_source"))
    elif kind=="infographic":
        infographic_slide(title,a["what_is_items"],a["what_is_template"],kicker=t_tag,source=a.get("what_is_source"))
    else:
        tile_grid(title,a["what_is_items"],kicker=t_tag,cols=2,size=14,source=a.get("what_is_source"))
def render_compare(a,t_tag):
    """COMPARE slot dispatcher — two_col (default) / quadrant (2x2 matrix) /
    arrows (pros-cons) / letters (big-letter split cards)."""
    kind=a.get("compare_kind","two_col"); kicker=f"{t_tag} · COMPARE"
    if kind=="quadrant":
        quads=[(name,COLOR_TAGS.get(tag,GREY),items) for name,tag,items in a["compare_quadrants"]]
        quadrant_2x2(a["compare_title"],a["compare_xaxis"],a["compare_yaxis"],quads,
                     kicker=kicker,source=a.get("compare_source"))
    elif kind=="arrows":
        pros_cons_arrows(a["compare_title"],a["compare_lhead"],a["compare_left"],
                          a["compare_rhead"],a["compare_right"],kicker=kicker,source=a.get("compare_source"))
    elif kind=="letters":
        split_letter_cards(a["compare_title"],a["compare_left"],a["compare_right"],
                            kicker=kicker,source=a.get("compare_source"))
    elif kind=="infographic":
        infographic_slide(a["compare_title"],a["compare_items"],a["compare_template"],
                           kicker=kicker,source=a.get("compare_source"))
    else:
        two_col(a["compare_title"],a["compare_left"],a["compare_right"],kicker=kicker,
                lhead=a["compare_lhead"],rhead=a["compare_rhead"],source=a.get("compare_source"))
def render_visual(a,t_tag):
    """SUPPORTING DATA slot dispatcher — bar / tile (defaults) / pyramid / icons /
    loop / hex / donut / journey / blueprint / funnel / empathy / tree / kpi / persona /
    infographic (AntV-rendered PNG — needs visual_template + visual_items, see
    infographic_slide())."""
    kind=a.get("visual_kind","tile"); kicker=f"{t_tag} · SUPPORTING DATA"
    if kind=="bar":
        stats_bar(a["visual_title"],a["visual_items"],kicker=kicker,source=a.get("visual_source"))
    elif kind=="donut":
        donut_ring(a["visual_title"],a["visual_items"],kicker=kicker,source=a.get("visual_source"))
    elif kind=="pyramid":
        pyramid_steps(a["visual_title"],a["visual_items"],kicker=kicker,source=a.get("visual_source"))
    elif kind=="icons":
        icon_cards_grad(a["visual_title"],a["visual_items"],kicker=kicker,
                         cols=min(len(a["visual_items"]),4),source=a.get("visual_source"))
    elif kind=="loop":
        journey_loop(a["visual_title"],a["visual_items"],kicker=kicker,source=a.get("visual_source"))
    elif kind=="hex":
        hex_model(a["visual_title"],a["visual_items"],kicker=kicker,source=a.get("visual_source"))
    elif kind=="journey":
        journey_map(a["visual_title"],a["visual_items"],kicker=kicker,source=a.get("visual_source"))
    elif kind=="blueprint":
        service_blueprint(a["visual_title"],a["visual_stage_labels"],a["visual_items"],
                           kicker=kicker,source=a.get("visual_source"))
    elif kind=="funnel":
        funnel_chart(a["visual_title"],a["visual_items"],kicker=kicker,source=a.get("visual_source"))
    elif kind=="empathy":
        empathy_map(a["visual_title"],a["visual_says"],a["visual_thinks"],a["visual_does"],a["visual_feels"],
                    kicker=kicker,source=a.get("visual_source"))
    elif kind=="tree":
        decision_tree(a["visual_title"],a["visual_root"],a["visual_items"],kicker=kicker,source=a.get("visual_source"))
    elif kind=="kpi":
        kpi_dashboard(a["visual_title"],a["visual_items"],kicker=kicker,source=a.get("visual_source"))
    elif kind=="persona":
        persona_card(a["visual_title"],a["visual_items"],kicker=kicker,source=a.get("visual_source"))
    elif kind=="infographic":
        infographic_slide(a["visual_title"],a["visual_items"],a["visual_template"],
                           kicker=kicker,source=a.get("visual_source"))
    else:
        tile_grid(a["visual_title"],a["visual_items"],kicker=kicker,cols=2,size=14,source=a.get("visual_source"))
def render_process(a,t_tag):
    """HOW IT WORKS slot dispatcher — vertical numbered list (default) / road
    (winding process path with icon nodes, for a 3-4 step production process)."""
    kind=a.get("process_kind","vertical"); kicker=f"{t_tag} · HOW IT WORKS"
    if kind=="road":
        road_process(a["process_title"],a["process_road_items"],kicker=kicker,source=a.get("process_source"))
    elif kind=="infographic":
        infographic_slide(a["process_title"],a["process_items"],a["process_template"],
                           kicker=kicker,source=a.get("process_source"))
    else:
        process_v(a["process_title"],a["process_items"],kicker=kicker,source=a.get("process_source"))
TOPIC_ACTS = {t["num"]: [a for a in ACTIVITIES if a["topic"]==t["num"]] for t in C.TOPICS}
for t in C.TOPICS:
    section(f"{t['code']}", t["title"], t["code"], t["subtitle"])
    SLIDE_MAP[f"topic{t['num']}_section"]=PAGE["n"]
    acts=TOPIC_ACTS[t["num"]]
    for ti,a in enumerate(acts,1):
        t_tag=f"LO{t['num']} · {t['code']} · T{ti}"
        sub_divider(t_tag, a["t_statement"])
        render_what_is(a,t_tag)
        render_process(a,t_tag)
        render_compare(a,t_tag)
        render_visual(a,t_tag)
        if a.get("case_example_company"):
            case_study_callout(a["case_example_company"], a["case_example_headline"],
                                a["case_example_insight"], kicker=f"{t_tag} · REAL-WORLD EXAMPLE")
        act_kicker=f"{t_tag} · ACTIVITY {a['num']}"
        scenario_slide(act_kicker, a["title"], a["case_type"], a["case_scenario"], a["build"], a["duration"])
        SLIDE_MAP[f"activity{a['num']}"]=PAGE["n"]
        if a["case_type"]=="role_play" and a.get("roles"):
            role_cards_slide(act_kicker, a["title"], a["roles"])
        discussion_slide(act_kicker, a["title"], a["discussion_prompts"])
        reflection_slide(act_kicker, a["title"], a["reflection_points"], a["debrief_check"])
    recap_items=list({x["objective"]:x for x in acts}.values())[:6]
    tile_grid(f"Recap — {t['title']}",
              [(a["title"], f"You can now: {a['objective']}.") for a in recap_items],
              kicker=f"{t['code']} RECAP", cols=2, size=14)
    quote_callout(t["closer_quote"], t["closer_attribution"], kicker=f"{t['code']} · WHY IT MATTERS")

playbook_numerals(C.COURSE_PLAYBOOK["title"], C.COURSE_PLAYBOOK["items"],
                   kicker="COURSE WRAP-UP", closing=C.COURSE_PLAYBOOK["closing"])

# ---------------- CLOSE ----------------
# Digital Attendance must be the LAST admin slide before Thank You (WSQ hard rule) —
# nothing else goes after it, so the course-closer playbook slide above sits BEFORE
# this whole admin block, not after it.
section("WRAP-UP","Course Summary & Next Steps","")
tile_grid("What You Achieved",[
 ("Stakeholders & Organisation","Mapped stakeholders and audiences; drafted brand designs and reputation assessments."),
 ("Customer Influence","Captured and documented customer perception through active listening."),
 ("Branding in Marketing","Executed branding and PR campaigns aligned to strategy, plan and budget."),
 ("Branding Effectiveness","Measured reputation and PR performance against KPIs and proposed improvements.")],
 kicker="LEARNING OUTCOMES",cols=2,size=15)
tile_grid("Assessment",[
 ("Written Assessment (WA)","SAQ — 1 hour, open book."),
 ("Case Study (CS)","1 hour, open book."),
 ("Open Book","Slides, Learner Guide and approved materials only."),
 ("Submit","On the LMS — lms-tms.tertiaryinfotech.com")],
 kicker="WRAP-UP",cols=2,size=14,icons=["check","target","shield","refresh"])
SLIDE_MAP["assessment_end"]=PAGE["n"]
flow_h("Assessment Flow",[
 "TRAQOM survey — scan the QR code on the LMS",
 "Assessment digital attendance — scan the SSG QR",
 "Sit WA (SAQ) then the Case Study — open book",
 "Submit your answers on the LMS",
 "Sign the Assessment Summary Record"],kicker="ON ASSESSMENT DAY")
flow_h("Digital Attendance (Mandatory)",[
 "Mandatory — AM, PM and Assessment digital attendance for WSQ-funded courses.",
 "The trainer/administrator displays the digital attendance QR code from the SSG portal.",
 "Scan the QR code with your mobile phone camera and submit your attendance.",
 "A minimum of 75% attendance is required to be eligible for assessment and funding."],kicker="SSG DIGITAL ATTENDANCE")
SLIDE_MAP["digital_attendance_end"]=PAGE["n"]
big_statement("Thank You!","You are now equipped to build customer-centric brand communication that earns trust and drives results.",
              "SEE YOU AT THE NEXT ONE",color=TEAL)

OUT=os.path.join(REPO,"courseware",f"{C.SHORT_TITLE}-{C.VERSION}.pptx")
prs.save(OUT)
with open(os.path.join(HERE,"slide_map.json"),"w") as f:
    json.dump(SLIDE_MAP,f,indent=2)
_ig_browser_close()
print(f"Saved {OUT}  ({len(prs.slides.__iter__.__self__._sldIdLst)} slides)")
print("Saved slide_map.json")



