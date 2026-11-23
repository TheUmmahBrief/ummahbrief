"""Builds the printable monthly leak sheet (A4 landscape): the reward for replying to the free guide's first email.
Run from the top of the repository: python3 _build/leak_sheet_pdf.py "$(pwd)"
"""
import sys, os
from playwright.sync_api import sync_playwright

SITE = os.path.abspath(sys.argv[1])
OUT = os.path.join(SITE, "guide", "monthly-leak-sheet.pdf")
FONTS = os.path.join(SITE, "fonts")

LEAKS = [("#C92F3A", "Interest you never see"),
         ("#F2B632", "Money that leaves while you sleep"),
         ("#17837C", "A lifestyle that grew with the salary"),
         ("#5B2A6E", "Giving without a plan"),
         ("#2F7FD1", "Money with no job")]
MONTHS = 6

CSS = """
@font-face { font-family: 'Bricolage Grotesque'; src: url('file://%(f)s/bricolage-grotesque.woff2') format('woff2'); font-weight: 200 800; }
@font-face { font-family: 'Newsreader'; src: url('file://%(f)s/newsreader.woff2') format('woff2'); font-weight: 200 800; }
@page { size: 297mm 210mm; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; color: #0E1630; font-family: 'Newsreader', Georgia, serif; }
.page { width: 297mm; height: 210mm; padding: 13mm 15mm; position: relative; background: #FFFFFF; }
.top { display: flex; justify-content: space-between; align-items: baseline; border-bottom: 1.2mm solid #0E1630; padding-bottom: 3mm; }
h1 { font-family: 'Bricolage Grotesque'; font-weight: 800; font-size: 30pt; letter-spacing: -0.04em; margin: 0; line-height: 1; }
.brand { font-family: 'Bricolage Grotesque'; font-weight: 700; font-size: 11pt; }
.lede { font-size: 12pt; margin: 3.5mm 0 4mm; color: #4A5672; }
table { width: 100%%; border-collapse: collapse; font-family: 'Bricolage Grotesque'; }
th { font-size: 9.5pt; font-weight: 700; color: #4A5672; text-align: left; padding: 0 2mm 2mm; }
th.m { text-align: center; }
th.m span { display: block; border-bottom: 0.4mm solid #0E1630; height: 6mm; margin: 0 1mm; }
td { border-top: 0.25mm solid rgba(14,22,48,0.25); padding: 0 2mm; height: 16mm; font-size: 11pt; font-weight: 700; }
td.sw { width: 7mm; padding: 0; } td.sw i { display: block; width: 5mm; height: 5mm; border-radius: 0.8mm; }
td.name { width: 70mm; }
td.box { border-left: 0.25mm solid rgba(14,22,48,0.25); }
tr.total td { border-top: 1mm solid #0E1630; font-weight: 800; font-size: 12pt; }
tr.fix td { height: 24mm; font-weight: 600; font-size: 10pt; color: #4A5672; }
.how { position: absolute; left: 15mm; right: 15mm; bottom: 11mm; display: flex; justify-content: space-between; font-family: 'Bricolage Grotesque'; font-size: 8.5pt; color: #4A5672; }
"""


def build():
    heads = "".join('<th class="m">Month<span></span></th>' for _ in range(MONTHS))
    boxes = "".join('<td class="box"></td>' for _ in range(MONTHS))
    rows = "".join('<tr><td class="sw"><i style="background:%s"></i></td><td class="name">%s</td>%s</tr>' % (c, n, boxes) for c, n in LEAKS)
    return """<!DOCTYPE html><html><head><meta charset="utf-8"><title>The monthly leak sheet</title><style>%s</style></head><body>
<div class="page">
  <div class="top"><h1>The monthly leak sheet</h1><div class="brand">The Ummah Brief</div></div>
  <p class="lede">Do this on the same day each month, with last month's bank statement. Write each leak's number in that month's column, then choose one leak to fix. Watch the total come down.</p>
  <table>
    <tr><th></th><th>Leak</th>%s</tr>
    %s
    <tr class="total"><td></td><td class="name">Leaving each month, unplanned</td>%s</tr>
    <tr class="fix"><td></td><td class="name">The one leak I am fixing this month</td>%s</tr>
  </table>
  <div class="how"><span>How to find each number: see the free guide, Where did it go? at ummahbrief.com/guide</span><span>General education. Not personal financial advice and not a fatwa.</span></div>
</div></body></html>""" % (CSS % {"f": FONTS}, heads, rows, boxes, boxes)


os.makedirs("/home/claude/build", exist_ok=True)
src = "/home/claude/build/leak_sheet_src.html"
open(src, "w", encoding="utf-8").write(build())
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox", "--allow-file-access-from-files"])
    pg = b.new_page()
    pg.goto("file://" + src)
    pg.wait_for_timeout(1200)
    print("fonts", pg.evaluate("[document.fonts.check('800 20px \"Bricolage Grotesque\"'), document.fonts.check('400 20px Newsreader')]"))
    print("overflow", pg.evaluate("[...document.querySelectorAll('.page')].map((el,i)=>[i+1, el.scrollHeight-el.clientHeight]).filter(x=>x[1]>1)"))
    pg.pdf(path=OUT, width="297mm", height="210mm", print_background=True, prefer_css_page_size=True)
    b.close()
print("written", OUT, os.path.getsize(OUT))
