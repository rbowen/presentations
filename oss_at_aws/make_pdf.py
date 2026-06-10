# /// script
# requires-python = ">=3.10"
# dependencies = ["fpdf2", "Pillow"]
# ///

from fpdf import FPDF
from PIL import Image
import re, os

SLIDE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(SLIDE_DIR, "slides.md")) as f:
    content = f.read()

slides = re.split(r'\n---\n', content)
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
W = lambda: pdf.w - pdf.l_margin - pdf.r_margin

def clean(raw):
    out = []
    for line in raw.splitlines():
        s = line.strip()
        if not s or re.match(r'!\[', s) or s.startswith('<') or s.startswith('class:'):
            continue
        s = re.sub(r'^#+\s*', '', s)
        s = re.sub(r'\*\*(.+?)\*\*', r'\1', s)
        s = re.sub(r'^\*\s+', '- ', s)
        out.append(s)
    return out

for i, slide in enumerate(slides):
    parts = slide.split("???")
    body = parts[0].strip()
    notes = parts[1].strip() if len(parts) > 1 else ""

    pdf.add_page()

    # Slide number
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(W(), 4, f"Slide {i + 1}", align="R")
    pdf.ln(4)
    pdf.set_text_color(0, 0, 0)

    # Images
    for img_path in re.findall(r'!\[.*?\]\((.*?)\)', body):
        full = os.path.join(SLIDE_DIR, img_path)
        if not os.path.exists(full):
            continue
        if full.endswith(".webp"):
            im = Image.open(full)
            tmp = full.replace(".webp", "_tmp.png")
            im.save(tmp, "PNG")
            full = tmp
        pw = W()
        im = Image.open(full)
        w, h = im.size
        rh = min(pw * h / w, 85)
        rw = rh * w / h
        y0 = pdf.get_y()
        pdf.image(full, x=pdf.l_margin, y=y0, w=rw, h=rh)
        pdf.set_y(y0 + rh + 3)
        pdf.set_x(pdf.l_margin)

    # Slide text
    text = clean(body)
    if text:
        pdf.set_font("Helvetica", "B", 12)
        for line in text:
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(w=0, h=6, text=line)
        pdf.ln(2)

    # Speaker notes
    if notes:
        pdf.set_x(pdf.l_margin)
        pdf.set_draw_color(0, 120, 200)
        pdf.set_line_width(0.5)
        pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
        pdf.ln(2)
        pdf.set_font("Helvetica", "BI", 10)
        pdf.set_text_color(0, 80, 160)
        pdf.set_x(pdf.l_margin)
        pdf.cell(0, 5, "Speaker Notes")
        pdf.ln(5)
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(60, 60, 60)
        for line in clean(notes):
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(w=0, h=4.5, text=line)
        pdf.set_text_color(0, 0, 0)

out = os.path.join(SLIDE_DIR, "slides_with_notes.pdf")
pdf.output(out)
print(f"Created {out}")
