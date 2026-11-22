"""Builds the free guide 'Where did it go?' as a PDF, using the site's own fonts."""
import sys, os
from playwright.sync_api import sync_playwright

SITE = sys.argv[1]
OUT = os.path.join(SITE, "guide", "where-did-it-go.pdf")
FONTS = os.path.join(SITE, "fonts")

LEAKS = [
    ("#C92F3A", "#FFFFFF", "Interest you never see",
     "Riba is the leak most people have and fewest people measure. You know your monthly payments. You probably do not know how much of each payment is interest.",
     ["You carry a credit card balance from one month to the next.",
      "You have car finance, a personal loan or a store account.",
      "You usually pay the minimum, or close to it."],
     "For each debt, take the balance, multiply it by the yearly interest rate, and divide by 12. Add the results together. That total is roughly what interest costs you every month.",
     "Interest I pay each month",
     "Stop it growing. Today, remove your card from your phone wallet and from every online shop. You are not cancelling anything yet. You are making new debt hard to reach.",
     "Allah has permitted trade and forbidden riba. (Al-Baqarah 2:275)"),
    ("#F2B632", "#0E1630", "Money that leaves while you sleep",
     "Subscriptions, app charges, bank fees and free trials that quietly became paid. Each one is small. Together they are often a bill you would never agree to in one go.",
     ["You cannot list all your subscriptions from memory.",
      "You have paid for something this year that you forgot you had.",
      "You have never added up your bank fees."],
     "Open last month's statement. Circle every payment that repeats and that you did not actively choose that month. Add them up.",
     "Automatic payments each month",
     "Cancel two of them before you put this guide down. Not later. Now, while the statement is open.",
     None),
    ("#17837C", "#FFFFFF", "A lifestyle that grew with the salary",
     "Each raise felt like relief for a month or two. Then the spending rose to meet it: a better car, a newer phone, a bigger rent. The income went up. What was left over did not.",
     ["You earn more than you did three years ago, but save about the same.",
      "A raise or bonus is usually spent before it arrives.",
      "Some of your spending is mostly so that others can see it."],
     "Write down what you earned each month three years ago, and what you kept. Write today's numbers beside them. Your income has probably grown. Has your saving grown by the same amount?",
     "My saving grew by",
     "Decide the job of your next raise or bonus before it lands. Send half of it straight to a goal, on the day it arrives.",
     "The servants of the Most Merciful are those who, when they spend, are neither wasteful nor miserly, but keep to a middle way. (Al-Furqan 25:67)"),
    ("#5B2A6E", "#FFFFFF", "Giving without a plan",
     "Supporting your parents and your family is an honour, and giving is never the problem. The leak is giving with no plan: amounts you did not choose, at times you did not expect, and loans that do not come back.",
     ["You help relatives whenever asked, in amounts you had not planned for.",
      "You have lent money that has not been returned.",
      "You feel guilty when you say no, and stretched when you say yes."],
     "Add up everything you gave or lent to family and friends over the last three months, planned or not. Divide by three.",
     "Unplanned giving each month",
     "Choose a monthly amount for family and for sadaqah in advance, and give it gladly. When it is used up, the answer becomes: next month, insha'Allah.",
     None),
    ("#2F7FD1", "#FFFFFF", "Money with no job",
     "Whatever is left after the bills has no name and no destination. It sits in the same account you spend from, so it gets spent. And because there is no buffer, every surprise becomes a new debt.",
     ["You have no savings goal with a name and a number.",
      "A surprise cost of one week's pay would have to go on credit.",
      "On payday, nothing is moved anywhere. It all stays in one account."],
     "On your last payday, how much money was given a specific job before you started spending? Write that number down, even if it is zero.",
     "Money given a job on payday",
     "On your next payday, move one fixed amount to a separate account the same day. Give that account a name: Emergency, Hajj, Home.",
     None),
]

CSS = """
@font-face { font-family: 'Bricolage Grotesque'; src: url('file://%(f)s/bricolage-grotesque.woff2') format('woff2'); font-weight: 200 800; }
@font-face { font-family: 'Newsreader'; src: url('file://%(f)s/newsreader.woff2') format('woff2'); font-weight: 200 800; }
@page { size: 148mm 210mm; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: 'Newsreader', Georgia, serif; font-size: 11pt; line-height: 1.46; color: #0E1630; }
.page { width: 148mm; height: 210mm; padding: 15mm 14mm 16mm; position: relative; page-break-after: always; overflow: hidden; background: #F3F5F8; }
.page:last-child { page-break-after: auto; }
h1, h2, h3, .d { font-family: 'Bricolage Grotesque', Arial, sans-serif; font-weight: 800; letter-spacing: -0.035em; line-height: 0.98; }
.foot { position: absolute; left: 14mm; right: 14mm; bottom: 8mm; display: flex; justify-content: space-between; font-family: 'Bricolage Grotesque', Arial, sans-serif; font-size: 8pt; font-weight: 600; color: #4A5672; }
.navy .foot { color: #9BA7C4; }
.navy { background: #0F1B3D; color: #FFFFFF; }
.cover h1 { font-size: 66pt; letter-spacing: -0.05em; line-height: 0.88; margin-top: 30mm; }
.cover .sub { font-size: 16pt; line-height: 1.35; color: #D4DBEC; margin-top: 9mm; max-width: 105mm; }
.cover .brand { font-family: 'Bricolage Grotesque'; font-weight: 800; font-size: 13pt; letter-spacing: -0.02em; }
.cover .chips { position: absolute; left: 14mm; bottom: 22mm; display: flex; gap: 3mm; }
.cover .chips i { width: 15mm; height: 15mm; border-radius: 1.4mm; display: block; }
h2 { font-size: 30pt; margin-bottom: 6mm; }
p { margin-bottom: 3mm; }
.lede { font-size: 13.4pt; line-height: 1.42; color: #4A5672; }
mark { background: #FFE066; color: inherit; padding: 0 0.12em; }
.need { border-top: 1mm solid #0E1630; margin: 7mm 0; }
.need div { display: flex; gap: 5mm; align-items: baseline; padding: 3.4mm 0; border-bottom: 0.25mm solid rgba(14,22,48,0.2); }
.need b { font-family: 'Bricolage Grotesque'; font-weight: 800; font-size: 19pt; letter-spacing: -0.03em; min-width: 12mm; }
.band { margin: -15mm -14mm 6mm; padding: 12mm 14mm 7.5mm; background: var(--c); color: var(--t); }
.band .n { font-family: 'Bricolage Grotesque'; font-weight: 700; font-size: 10.5pt; }
.band h2 { font-size: 28pt; margin: 2.5mm 0 0; }
h3 { font-size: 12.2pt; letter-spacing: -0.015em; line-height: 1.2; margin: 4mm 0 1.6mm; }
.ticks { list-style: none; }
.ticks li { position: relative; padding-left: 8mm; margin-bottom: 1.8mm; }
.ticks li::before { content: ''; position: absolute; left: 0; top: 1.1mm; width: 4.2mm; height: 4.2mm; border: 0.5mm solid #0E1630; border-radius: 0.8mm; background: #fff; }
.fill { display: flex; align-items: flex-end; gap: 3mm; margin: 3mm 0 1mm; font-family: 'Bricolage Grotesque'; font-weight: 700; font-size: 11pt; }
.fill span { flex: 1; border-bottom: 0.5mm solid #0E1630; height: 8mm; background: #fff; }
.fix { background: #fff; border: 0.5mm solid #0E1630; border-radius: 2.4mm; padding: 3.4mm 4.4mm; margin-top: 4mm; }
.fix h3 { margin-top: 0; }
.fix p { margin: 0; }
.verse { font-size: 9.6pt; line-height: 1.38; color: #4A5672; margin-top: 3.4mm; font-style: italic; }
table { width: 100%%; border-collapse: collapse; margin: 4mm 0 3mm; font-family: 'Bricolage Grotesque'; }
th { text-align: left; font-size: 9pt; font-weight: 700; color: #4A5672; padding: 0 0 2mm; border-bottom: 1mm solid #0E1630; }
td { padding: 2.4mm 0; border-bottom: 0.25mm solid rgba(14,22,48,0.25); font-size: 11.5pt; font-weight: 700; }
td.sw { width: 8mm; } td.sw i { display: block; width: 5mm; height: 5mm; border-radius: 0.8mm; }
td.amt { width: 38mm; } td.amt span, .line { display: block; border-bottom: 0.5mm solid #0E1630; height: 7mm; background: #fff; }
tr.total td { border-bottom: none; font-size: 13pt; font-weight: 800; padding-top: 4mm; }
.next { border-top: 0.25mm solid rgba(255,255,255,0.25); padding: 4.6mm 0; }
.next h3 { font-size: 16pt; letter-spacing: -0.03em; margin: 0 0 1.2mm; }
.next p { color: #D4DBEC; margin: 0; }
.next .url { font-family: 'Bricolage Grotesque'; font-weight: 700; color: #FFE066; font-size: 11pt; margin-top: 2mm; }
.fine { font-family: 'Bricolage Grotesque'; font-size: 8pt; line-height: 1.45; color: #9BA7C4; position: absolute; left: 14mm; right: 14mm; bottom: 15mm; }
""" % {"f": FONTS}


def foot(n):
    return '<div class="foot"><span>The Ummah Brief</span><span>%d</span></div>' % n


html = "<!DOCTYPE html><html><head><meta charset='utf-8'><title>Where did it go?</title><style>%s</style></head><body>" % CSS

# cover
html += """<div class="page navy cover">
  <div class="brand">The Ummah Brief</div>
  <h1>Where did it go?</h1>
  <p class="sub">The five places a halal income disappears, and how to find yours in 15 minutes.</p>
  <div class="chips">%s</div>
  <div class="foot"><span>A free guide</span><span>ummahbrief.com</span></div>
</div>""" % "".join('<i style="background:%s"></i>' % l[0] for l in LEAKS)

# how to use
html += """<div class="page">
  <h2>You earn halal. So why is nothing left?</h2>
  <p class="lede">It is rarely about how much you earn. Most households that feel stuck do not have an income problem. They have <mark>leaks they have never measured.</mark></p>
  <p>This guide names the five most common ones. For each, you get three signs that you have it, a three-minute way to put a number on it, and one fix to start with.</p>
  <div class="need">
    <div><b>1</b><span>Get last month's bank statement and a pen.</span></div>
    <div><b>2</b><span>Go through the five leaks. Tick every sign you recognise and write your number.</span></div>
    <div><b>3</b><span>Copy your numbers onto the leak sheet at the end.</span></div>
    <div><b>4</b><span>Fix the biggest leak first. Only that one. Leave the rest for next month.</span></div>
  </div>
  <p>Fifteen minutes is enough. You do not need a budget, an app or a spreadsheet. You need to see where it goes.</p>
  %s
</div>""" % foot(2)

for i, (c, t, name, intro, signs, find, label, fix, verse) in enumerate(LEAKS):
    html += """<div class="page">
  <div class="band" style="--c:%s;--t:%s"><div class="n">Leak %d of 5</div><h2>%s</h2></div>
  <p>%s</p>
  <h3>You have this leak if</h3>
  <ul class="ticks">%s</ul>
  <h3>Find it in three minutes</h3>
  <p>%s</p>
  <div class="fill">%s <span></span></div>
  <div class="fix"><h3>Your first fix</h3><p>%s</p></div>
  %s
  %s
</div>""" % (c, t, i + 1, name, intro, "".join("<li>%s</li>" % s for s in signs), find, label, fix,
             ('<p class="verse">%s</p>' % verse) if verse else "", foot(i + 3))

# leak sheet
rows = "".join('<tr><td class="sw"><i style="background:%s"></i></td><td>%s</td><td class="amt"><span></span></td></tr>' % (l[0], l[2]) for l in LEAKS)
html += """<div class="page">
  <h2>Your leak sheet</h2>
  <p class="lede">Copy your five numbers here. Seeing them side by side is the point of this guide.</p>
  <table>
    <tr><th></th><th>Leak</th><th>Each month</th></tr>
    %s
    <tr class="total"><td></td><td>Leaving each month, unplanned</td><td class="amt"><span></span></td></tr>
  </table>
  <h3>The one leak I will fix this month</h3>
  <div class="line"></div>
  <h3>I will have started by this date</h3>
  <div class="line"></div>
  <p class="verse" style="margin-top:5mm">The most beloved deeds to Allah are the most consistent, even if they are small. (Sahih al-Bukhari, Sahih Muslim)</p>
  %s
</div>""" % (rows, foot(8))

# what next
html += """<div class="page navy">
  <h2 style="font-size:29pt;margin-bottom:6mm">You found the leaks. Here is what to do next.</h2>
  <div class="next"><h3>If riba was your biggest number</h3><p>The Riba Exit Brief is a short audio with a clear order of steps for leaving interest-bearing debt. Join the list to hear when it is out.</p><p class="url">ummahbrief.com/briefs/riba-exit</p></div>
  <div class="next"><h3>If you want the whole plan</h3><p>The Rizq Code is a 60-page halal wealth framework with a 30-day action plan, an audit checklist and a pathway workbook. $39, with a 30-day money-back guarantee.</p><p class="url">ummahbrief.com/rizq-code</p></div>
  <div class="next" style="border-bottom:0.25mm solid rgba(255,255,255,0.25)"><h3>If a dispute over money is dividing your family</h3><p>We offer Islamic mediation. It is free, and it always will be.</p><p class="url">ummahbrief.com/mediation</p></div>
  <p class="fine">This guide is general education. It is not personal financial advice and it is not a fatwa. For a decision about your own money, speak to a qualified adviser. For a religious ruling, ask a scholar you trust.</p>
  <div class="foot"><span>The Ummah Brief</span><span>One Ummah. One Pulse. One Purpose.</span></div>
</div></body></html>"""

os.makedirs(os.path.dirname(OUT), exist_ok=True)
src = "/home/claude/build/guide_src.html"
open(src, "w", encoding="utf-8").write(html)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox", "--allow-file-access-from-files"])
    pg = b.new_page()
    pg.goto("file://" + src)
    pg.wait_for_timeout(1200)
    print("fonts", pg.evaluate("[document.fonts.check('800 20px \"Bricolage Grotesque\"'), document.fonts.check('400 20px Newsreader')]"))
    # report any page whose content overflows its fixed height
    print("overflow", pg.evaluate("[...document.querySelectorAll('.page')].map((el,i)=>[i+1, el.scrollHeight-el.clientHeight]).filter(x=>x[1]>1)"))
    pg.pdf(path=OUT, width="148mm", height="210mm", print_background=True, prefer_css_page_size=True)
    b.close()
print("written", OUT, os.path.getsize(OUT))
