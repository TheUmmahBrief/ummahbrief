"""Generates the redesigned Ummah Brief site pages (all except the Rizq Code sales page)."""
import os, sys

SITE = sys.argv[1]

BRIEFS = [
    ("01", "The Riba Exit Brief", "A clear order of steps for leaving interest-bearing debt.", "#C92F3A", "#FFFFFF", "ربا"),
    ("02", "The Zakat Brief", "Work out your zakat correctly in one sitting.", "#F2B632", "#0E1630", "زكاة"),
    ("03", "The Halal Investing Brief", "Know what to check before you put money anywhere.", "#17837C", "#FFFFFF", "حلال"),
    ("04", "The Wasiyyah Brief", "Get your Islamic will started this week.", "#5B2A6E", "#FFFFFF", "وصية"),
    ("05", "The Marriage Money Brief", "Talk about money with your spouse without a fight.", "#D9577B", "#FFFFFF", "زواج"),
    ("06", "The Raising Children Brief", "Teach children money, giving and contentment.", "#2F7FD1", "#FFFFFF", "تربية"),
]


def base_css(root):
    return """
@font-face { font-family: 'Bricolage Grotesque'; src: url('%(r)sfonts/bricolage-grotesque.woff2') format('woff2'); font-weight: 200 800; font-display: swap; }
@font-face { font-family: 'Newsreader'; src: url('%(r)sfonts/newsreader.woff2') format('woff2'); font-weight: 200 800; font-display: swap; }
@font-face { font-family: 'Amiri Words'; src: url('%(r)sfonts/amiri-words.woff2') format('woff2'); font-display: block; }
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --navy: #0F1B3D; --deep: #0A1330; --chalk: #F3F5F8; --white: #FFFFFF;
  --ink: #0E1630; --slate: #4A5672; --rule: rgba(14,22,48,0.16);
  --action: #F26B21; --action-hi: #FF8440; --mark: #FFE066;
  --on-navy: #D4DBEC; --on-navy-dim: #9BA7C4;
  --display: 'Bricolage Grotesque', 'Arial Narrow', Arial, sans-serif;
  --text: 'Newsreader', Georgia, 'Times New Roman', serif;
}
html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%%; }
body { font-family: var(--text); font-size: 19px; line-height: 1.6; background: var(--chalk); color: var(--ink); overflow-x: hidden; -webkit-font-smoothing: antialiased; }
a { color: inherit; }
img { max-width: 100%%; display: block; }
h1, h2, h3 { font-family: var(--display); font-weight: 800; letter-spacing: -0.03em; line-height: 1.02; text-wrap: balance; }
h2 { font-size: clamp(32px, 6.4vw, 56px); margin-bottom: 18px; }
h3 { font-size: 22px; letter-spacing: -0.015em; line-height: 1.2; }
p { max-width: 36em; }
.wrap { max-width: 1120px; margin: 0 auto; padding: 0 22px; }
.ui { font-family: var(--display); }
:focus-visible { outline: 3px solid var(--action); outline-offset: 3px; border-radius: 4px; }
section { padding: 76px 0; }
.navy { background: var(--navy); color: var(--white); }
.navy p { color: var(--on-navy); }
.white { background: var(--white); }
.lede { font-size: clamp(20px, 2.6vw, 23px); line-height: 1.5; color: var(--slate); }
.navy .lede { color: var(--on-navy); }
.small { font-family: var(--display); font-size: 14.5px; font-weight: 500; color: var(--slate); line-height: 1.5; }
.navy .small { color: var(--on-navy-dim); }

/* buttons: orange is used for the main action and nothing else */
.btn { display: inline-block; font-family: var(--display); font-weight: 700; font-size: 17px; letter-spacing: -0.005em; text-decoration: none; text-align: center; cursor: pointer; border: 2px solid transparent; border-radius: 12px; padding: 15px 26px; transition: background .15s, transform .15s, border-color .15s; }
.btn-act { background: var(--action); color: var(--ink); }
.btn-act:hover { background: var(--action-hi); transform: translateY(-2px); }
.btn-line { background: transparent; color: var(--ink); border-color: var(--ink); }
.btn-line:hover { background: var(--ink); color: var(--white); }
.navy .btn-line { color: var(--white); border-color: rgba(255,255,255,0.7); }
.navy .btn-line:hover { background: var(--white); color: var(--navy); }
.btn-sm { font-size: 15px; padding: 9px 16px; border-radius: 10px; }
.btn-block { display: block; width: 100%%; }
.link { font-family: var(--display); font-weight: 600; font-size: 16px; text-underline-offset: 4px; text-decoration-thickness: 2px; }

/* nav */
.nav { position: sticky; top: 0; z-index: 50; background: var(--navy); color: var(--white); }
.nav-in { display: flex; align-items: center; justify-content: space-between; gap: 14px; height: 62px; }
.wordmark { font-family: var(--display); font-weight: 800; font-size: 21px; letter-spacing: -0.03em; text-decoration: none; white-space: nowrap; }
.wordmark { display: inline-flex; align-items: center; }
.mark { width: 32px; height: 32px; margin-right: 10px; border-radius: 50%%; flex: none; }
.foot .mark { width: 40px; height: 40px; }
.nav .btn { white-space: nowrap; }
@media (max-width: 440px) { .nav-in { gap: 8px; } .nav-right { gap: 7px; } .wordmark { font-size: 16.5px; } .mark { width: 28px; height: 28px; margin-right: 8px; } .nav .btn-sm { font-size: 14px; } .nav .btn-sm { padding: 8px 10px; } .menu summary { padding: 8px 10px; font-size: 14px; } }
.nav-links { display: flex; align-items: center; gap: 26px; }
.nav-links a.t { font-family: var(--display); font-weight: 600; font-size: 15.5px; text-decoration: none; color: var(--on-navy); }
.nav-links a.t:hover { color: var(--white); }
.nav-right { display: flex; align-items: center; gap: 10px; }
.menu { display: none; position: relative; }
.menu summary { list-style: none; cursor: pointer; font-family: var(--display); font-weight: 700; font-size: 15px; padding: 9px 14px; border: 2px solid rgba(255,255,255,0.45); border-radius: 10px; }
.menu summary::-webkit-details-marker { display: none; }
.menu[open] summary { background: var(--white); color: var(--navy); border-color: var(--white); }
.menu-list { position: absolute; right: 0; top: calc(100%% + 10px); width: min(78vw, 290px); background: var(--white); color: var(--ink); border-radius: 14px; padding: 8px; box-shadow: 0 24px 60px rgba(4,9,26,0.45); }
.menu-list a { display: block; font-family: var(--display); font-weight: 700; font-size: 18px; text-decoration: none; padding: 13px 14px; border-radius: 9px; }
.menu-list a:hover, .menu-list a:focus-visible { background: var(--chalk); }
@media (max-width: 820px) { .nav-links a.t { display: none; } .menu { display: block; } }

/* forms */
.row-form { display: flex; gap: 10px; max-width: 540px; }
.row-form input[type=email] { flex: 1; min-width: 0; font-family: var(--display); font-size: 17px; color: var(--ink); background: var(--white); border: 2px solid var(--ink); border-radius: 12px; padding: 14px 16px; }
.navy .row-form input[type=email] { border-color: var(--white); }
.row-form input:focus { outline: 3px solid var(--action); outline-offset: 2px; }
.ok { display: none; max-width: 540px; font-family: var(--display); font-weight: 600; font-size: 17px; background: var(--mark); color: var(--ink); border-radius: 12px; padding: 16px 18px; }
@media (max-width: 560px) { .row-form { flex-direction: column; } }

/* sleeves: the square covers of the Briefs */
.sleeve { position: relative; display: flex; flex-direction: column; justify-content: space-between; aspect-ratio: 1; border-radius: 6px; padding: 16px; text-decoration: none; background: var(--c); color: var(--t); box-shadow: 0 14px 30px rgba(4,9,26,0.28); }
.sleeve .no { font-family: var(--display); font-weight: 700; font-size: 14px; letter-spacing: 0.02em; opacity: 0.92; display: flex; justify-content: space-between; align-items: center; }
.sleeve .ar { position: absolute; right: 16px; top: 36px; font-family: 'Amiri Words', serif; font-size: clamp(30px, 3.1vw, 42px); line-height: 1.25; direction: rtl; }
.sleeve .ti { font-family: var(--display); font-weight: 800; font-size: clamp(21px, 2.3vw, 27px); line-height: 0.98; letter-spacing: -0.035em; }
.sleeve .play { width: 26px; height: 26px; border-radius: 50%%; border: 2px solid currentColor; position: relative; }
.sleeve .soon { font-size: 12px; font-weight: 700; border: 1.5px solid currentColor; border-radius: 40px; padding: 1px 9px; }
.sleeve .play::after { content: ''; position: absolute; left: 9px; top: 6px; border-left: 8px solid currentColor; border-top: 5px solid transparent; border-bottom: 5px solid transparent; }

/* highlighter: the yellow marker draws across the words when they scroll into view */
mark.hl { background: linear-gradient(var(--mark), var(--mark)) no-repeat 0 0 / 100%% 100%%; }
.js mark.hl { background-size: 0%% 100%%; transition: background-size .9s cubic-bezier(.2,.7,.2,1) .2s; }
.js mark.hl.on { background-size: 100%% 100%%; }

/* footer */
footer { background: var(--deep); color: var(--on-navy-dim); padding: 46px 0 104px; }
.foot { display: flex; justify-content: space-between; gap: 30px; flex-wrap: wrap; }
.foot .wordmark { color: var(--white); font-size: 24px; }
.foot-links { display: flex; flex-wrap: wrap; gap: 10px 24px; max-width: 560px; }
.foot-links a { font-family: var(--display); font-weight: 600; font-size: 15.5px; color: var(--on-navy); text-decoration: none; }
.foot-links a:hover { color: var(--white); text-decoration: underline; }
.legal { margin-top: 30px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.12); font-family: var(--display); font-size: 14px; line-height: 1.6; }
.legal p { max-width: none; }

/* sticky phone button */
.sticky { position: fixed; left: 0; right: 0; bottom: 0; z-index: 60; background: var(--deep); padding: 10px 14px calc(10px + env(safe-area-inset-bottom)); transform: translateY(110%%); transition: transform .25s ease; }
.sticky.show { transform: translateY(0); }
@media (min-width: 821px) { .sticky { display: none; } footer { padding-bottom: 46px; } }
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } .btn, .sticky, .sleeve { transition: none !important; animation: none !important; } .js mark.hl { transition: none; background-size: 100%% 100%%; } }
""" % {"r": root}


def head(root, title, desc, url, extra_css):
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="color-scheme" content="light">
<meta name="theme-color" content="#0F1B3D">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:type" content="website">
<meta property="og:url" content="%(url)s">
<meta property="og:image" content="https://ummahbrief.com/share.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/favicon-32x32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="%(r)sfonts/bricolage-grotesque.woff2" as="font" type="font/woff2" crossorigin>
<style>%(css)s%(extra)s</style>
</head>
<body>
""" % {"title": title, "desc": desc, "url": url, "r": root, "css": base_css(root), "extra": extra_css}


def nav(root, cta_html):
    links = [("The Briefs", root + "#briefs"), ("The Circle", root + "circle/"), ("The Rizq Code", root + "rizq-code/"), ("Riba Check", root + "riba-check/"), ("Mediation", root + "mediation/"), ("Newsletter", root + "#newsletter")]
    t = "".join('<a class="t" href="%s">%s</a>' % (h, n) for n, h in links)
    m = "".join('<a href="%s">%s</a>' % (h, n) for n, h in links)
    return """<nav class="nav"><div class="wrap nav-in">
  <a class="wordmark" href="%(home)s"><img class="mark" src="%(r)sbrand/logo-96.png" alt="" width="32" height="32">The Ummah Brief</a>
  <div class="nav-links">%(t)s</div>
  <div class="nav-right">
    %(cta)s
    <details class="menu"><summary>Menu</summary><div class="menu-list">%(m)s</div></details>
  </div>
</div></nav>
""" % {"home": root or "./", "t": t, "m": m, "cta": cta_html, "r": root}


def footer(root):
    return """<footer><div class="wrap">
  <div class="foot">
    <a class="wordmark" href="%(home)s"><img class="mark" src="%(r)sbrand/logo-96.png" alt="" width="32" height="32">The Ummah Brief</a>
    <div class="foot-links">
      <a href="%(r)s#briefs">The Briefs</a><a href="%(r)scircle/">The Rizq Circle</a><a href="%(r)srizq-code/">The Rizq Code</a><a href="%(r)sguide/">Free guide</a><a href="%(r)sriba-check/">Riba Check</a><a href="%(r)sledger/">The Ledger</a><a href="%(r)smediation/">Mediation</a><a href="%(r)s#newsletter">Newsletter</a><a href="https://instagram.com/the_ummah_brief" rel="noopener">Instagram</a><a href="%(r)ssponsor/">Sponsor the newsletter</a><a href="mailto:salaam@ummahbrief.com">Contact</a><a href="%(r)sprivacy/">Privacy</a><a href="%(r)sterms/">Terms and refunds</a>
    </div>
  </div>
  <div class="legal"><p>One Ummah. One Pulse. One Purpose.</p><p>&copy; 2026 The Ummah Brief. Everything here is general education. It is not personal financial advice and it is not a fatwa.</p></div>
</div></footer>
""" % {"r": root, "home": root or "./"}


FORM_JS = """
// Sends a form without leaving the page, then shows its confirmation message.
document.querySelectorAll('form[data-ok]').forEach(function (form) {
  form.addEventListener('submit', async function (e) {
    e.preventDefault();
    var btn = form.querySelector('button[type="submit"]'); var label = btn.textContent;
    btn.textContent = 'Sending...'; btn.disabled = true;
    try {
      var res = await fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } });
      if (res.ok) {
        if (form.dataset.next) { window.location.href = form.dataset.next; return; }
        form.style.display = 'none'; document.querySelector(form.dataset.ok).style.display = 'block'; return;
      }
    } catch (err) {}
    btn.textContent = 'That did not send. Try again'; btn.disabled = false;
    setTimeout(function () { btn.textContent = label; }, 4000);
  });
});
// Highlighter: draw the yellow marker when the words come into view.
(function () {
  var marks = document.querySelectorAll('mark.hl');
  if (!marks.length || !('IntersectionObserver' in window)) return;
  document.documentElement.classList.add('js');
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('on'); io.unobserve(en.target); } });
  }, { threshold: 0.9, rootMargin: '0px 0px -12% 0px' });
  marks.forEach(function (m) { io.observe(m); });
})();
// Close the phone menu after a link is tapped.
document.querySelectorAll('.menu-list a').forEach(function (a) { a.addEventListener('click', function () { a.closest('details').removeAttribute('open'); }); });
"""


def sticky_js(hide_at):
    return """
(function () {
  var bar = document.getElementById('sticky'), hero = document.getElementById('top'), stop = document.querySelector('%s');
  function update() {
    var past = hero.getBoundingClientRect().bottom < 0;
    var r = stop.getBoundingClientRect(); var at = r.top < window.innerHeight && r.bottom > 0;
    bar.classList.toggle('show', past && !at);
  }
  window.addEventListener('scroll', update, { passive: true }); update();
})();
""" % hide_at


def write(path, html):
    full = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(html)


# ───────────────────────── HOMEPAGE ─────────────────────────
home_css = """
.hero { padding: 54px 0 170px; }
.hero h1 { font-size: clamp(46px, 11.2vw, 112px); line-height: 0.93; letter-spacing: -0.045em; max-width: 10.5em; text-wrap: balance; }
.hero h1 span { display: block; }
.hero .lede { max-width: 30em; margin: 26px 0 30px; }
.hero-actions { display: flex; flex-wrap: wrap; align-items: center; gap: 16px 24px; }
.hero .btn-act { font-size: 19px; padding: 18px 32px; }
.hero .link { color: var(--white); }
.hero .small { margin-top: 22px; }

.shelf-sec { padding: 0 0 76px; }
.shelf { display: grid; grid-template-columns: repeat(6, 1fr); gap: 14px; margin-top: -118px; }
.shelf .sleeve { transition: transform .18s ease; animation: rise .7s cubic-bezier(.2,.8,.2,1) both; }
.shelf .sleeve:nth-child(2) { animation-delay: .06s; } .shelf .sleeve:nth-child(3) { animation-delay: .12s; }
.shelf .sleeve:nth-child(4) { animation-delay: .18s; } .shelf .sleeve:nth-child(5) { animation-delay: .24s; } .shelf .sleeve:nth-child(6) { animation-delay: .30s; }
.shelf a.sleeve:hover { transform: translateY(-8px) rotate(-1.5deg); }
.shelf a.sleeve { cursor: pointer; }
@keyframes rise { from { opacity: 0; transform: translateY(46px); } to { opacity: 1; transform: none; } }
@media (max-width: 980px) {
  .shelf { display: flex; overflow-x: auto; scroll-snap-type: x mandatory; gap: 12px; margin-left: -22px; margin-right: -22px; padding: 0 22px 26px; scrollbar-width: none; }
  .shelf::-webkit-scrollbar { display: none; }
  .shelf .sleeve { flex: 0 0 min(58vw, 230px); scroll-snap-align: center; }
  .shelf .sleeve .ti { font-size: 27px; } .shelf .sleeve .ar { font-size: 60px; top: 48px; right: 18px; }
}
.briefs-intro { display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 56px; align-items: start; margin-top: 56px; }
.first-out { background: var(--white); border: 2px solid var(--ink); border-radius: 16px; padding: 26px; scroll-margin-top: 84px; border-top: 10px solid var(--pick, #C92F3A); }
.first-out h3 { font-size: 27px; letter-spacing: -0.03em; line-height: 1.05; margin-bottom: 8px; }
.first-out p { font-size: 17.5px; color: var(--slate); margin-bottom: 18px; }
.facts { font-family: var(--display); font-weight: 600; font-size: 15px; color: var(--ink); margin-bottom: 18px; }
@media (max-width: 860px) { .briefs-intro { grid-template-columns: 1fr; gap: 30px; margin-top: 26px; } }

.ledger { border-top: 3px solid var(--ink); margin: 34px 0 30px; max-width: 760px; }
.ledger div { display: grid; grid-template-columns: 110px 1fr; gap: 18px; align-items: baseline; padding: 20px 0; border-bottom: 1px solid var(--rule); }
.ledger dt { font-family: var(--display); font-weight: 700; font-size: 17px; color: var(--slate); font-variant-numeric: tabular-nums; }
.ledger dd { font-family: var(--display); font-weight: 700; font-size: clamp(24px, 4.6vw, 36px); letter-spacing: -0.03em; line-height: 1.08; }
.ledger mark { color: inherit; padding: 0 0.16em; box-decoration-break: clone; -webkit-box-decoration-break: clone; }
@media (max-width: 520px) { .ledger div { grid-template-columns: 72px 1fr; gap: 12px; } }

.cover-list { border-top: 3px solid var(--ink); margin-top: 34px; }
.cover-list li { list-style: none; display: grid; grid-template-columns: 220px 1fr auto; gap: 24px; align-items: baseline; padding: 24px 0; border-bottom: 1px solid var(--rule); }
.cover-list b { font-family: var(--display); font-weight: 800; font-size: clamp(28px, 4.4vw, 40px); letter-spacing: -0.035em; line-height: 1; }
.cover-list span { color: var(--slate); }
@media (max-width: 760px) { .cover-list li { grid-template-columns: 1fr; gap: 8px; padding: 22px 0; } }

.rc { display: grid; grid-template-columns: 300px 1fr; gap: 60px; align-items: center; }
.rc { grid-template-columns: 420px 1fr; }
.rc img { width: 100%; height: auto; }
.cobalt { background: #1D3FCB; color: #fff; }
.cobalt .lede { color: #EEF1FF; }
.cobalt .small { color: #C9D3FF; }
.cobalt .rc li { border-color: rgba(255,255,255,0.28); color: #fff; }
.emerald { background: #0E6B4F; color: #fff; }
.emerald .lede { color: #E6F5EE; }
.emerald .small { color: #BFE3D2; }
.circ { display: grid; grid-template-columns: 340px 1fr; gap: 60px; align-items: center; }
.circ ul { list-style: none; margin: 22px 0 26px; }
.circ li { padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.28); }
.circ li:first-child { border-top: 1px solid rgba(255,255,255,0.28); }
.circ-sleeve { width: 100%; transform: rotate(-2deg); }
.circ-sleeve .ti { font-size: 40px; }
.circ-sleeve .ar { font-size: 96px; top: 54px; right: 24px; }
.price .per { font-size: 22px; letter-spacing: -0.02em; margin-left: 4px; }
@media (max-width: 820px) { .circ { grid-template-columns: 1fr; gap: 30px; } .circ-sleeve { max-width: 260px; } .circ-sleeve .ti { font-size: 28px; } .circ-sleeve .ar { font-size: 64px; top: 46px; } }
.rc ul { list-style: none; margin: 22px 0 26px; }
.rc li { padding: 12px 0; border-bottom: 1px solid var(--rule); }
.rc li:first-child { border-top: 1px solid var(--rule); }
.buy { display: flex; flex-wrap: wrap; align-items: center; gap: 18px 26px; }
.price { font-family: var(--display); font-weight: 800; font-size: 60px; letter-spacing: -0.05em; line-height: 1; }
@media (max-width: 820px) { .rc { grid-template-columns: 1fr; gap: 30px; } .rc img { max-width: 340px; } .buy .btn { flex: 1 1 100%; } }

.med h2 { font-size: clamp(40px, 9vw, 92px); line-height: 0.95; letter-spacing: -0.045em; max-width: 10em; }
.med .lede { margin: 24px 0 30px; max-width: 32em; }
.news h2 { max-width: 12em; }
.news .lede { margin-bottom: 26px; }
.news .small { margin-top: 14px; }
"""

sleeves = ""
for i, (no, title, promise, c, t, ar) in enumerate(BRIEFS):
    short = title.replace("The ", "", 1).replace(" Brief", "")
    if i == 0:
        sleeves += '<a class="sleeve" style="--c:%s;--t:%s" href="briefs/riba-exit/" aria-label="%s"><span class="no">Brief %s <span class="play" aria-hidden="true"></span></span><span class="ar" lang="ar" aria-hidden="true">%s</span><span class="ti">%s</span></a>\n      ' % (c, t, title, no, ar, short)
    else:
        sleeves += '<a class="sleeve js-pick" style="--c:%s;--t:%s" href="#waitlist" data-brief="%s" data-promise="%s" aria-label="%s, coming soon. Join the waiting list"><span class="no">Brief %s <span class="soon">Soon</span></span><span class="ar" lang="ar" aria-hidden="true">%s</span><span class="ti">%s</span></a>\n      ' % (c, t, title, promise, title, no, ar, short)

home = head("", "The Ummah Brief | Halal wealth, family and unity for the Muslim household",
            "You earn halal. So why is nothing left at the end of the month? Get the free guide, and see the Briefs: short audio guides for Muslim households.",
            "https://ummahbrief.com/", home_css)
home += """
<!--
  EDIT POINTS (all at the bottom of this file)
  GUIDE_URL       where every "free guide" button goes. It points at the guide page on this site.
  BRIEF_ON_SALE   set to true once the Riba Exit Brief can be bought. The waiting list becomes a buy button.
  The forms post to Formspree for now. Replace the form actions when email moves to Systeme.
-->
"""
home += nav("", '<a class="btn btn-act btn-sm js-guide" href="guide/">Free guide</a>')
home += """
<header class="hero navy" id="top">
  <div class="wrap">
    <h1><span>You earn halal.</span> So why is nothing left at the end of the month?</h1>
    <p class="lede">It is rarely about how much you earn. The free guide shows the five places a halal income disappears, and how to find yours in 15 minutes.</p>
    <div class="hero-actions">
      <a class="btn btn-act js-guide" href="guide/">Get the free guide</a>
      <a class="link" href="#briefs">Or see the Briefs</a>
    </div>
    <p class="small">Free, no card needed. The Ummah Brief covers wealth, family, knowledge and unity, rooted in Quran and Sunnah.</p>
  </div>
</header>

<section class="shelf-sec" id="briefs">
  <div class="wrap">
    <div class="shelf">
      %(sleeves)s
    </div>
    <div class="briefs-intro">
      <div>
        <h2>One problem. One short audio. One evening of action.</h2>
        <p class="lede">A Brief is an audio guide you can finish on a commute, with a one-page action sheet that tells you exactly what to do next. Each one costs $9.</p>
      </div>
      <div class="first-out" id="waitlist">
        <h3 id="wlTitle">First out: The Riba Exit Brief</h3>
        <p id="wlText">You know riba is haram. Nobody showed you the way out. This is a clear order of steps for leaving interest-bearing debt.</p>
        <p class="facts" id="wlFacts">About 18 minutes. Six chapters. Action sheet and transcript. $9.</p>
        <div class="js-brief-wait">
          <form class="row-form" id="briefForm" data-ok="#briefOk" action="https://formspree.io/f/xnjyanyb" method="POST">
            <input type="email" name="email" id="wlEmail" placeholder="Your email address" aria-label="Your email address" autocomplete="email" required>
            <input type="hidden" name="source" id="wlSource" value="Riba Exit Brief waiting list (homepage)">
            <input type="hidden" name="brief" id="wlBrief" value="The Riba Exit Brief">
            <button class="btn btn-act" type="submit">Tell me when it is out</button>
          </form>
          <div class="ok" id="briefOk" role="status">You are on the list. You will hear from us first, insha'Allah.</div>
          <p class="small" id="wlMore" style="margin:14px 0 0">Arriving soon. <a href="briefs/riba-exit/">See what is inside</a></p>
        </div>
        <div class="js-brief-buy" style="display:none">
          <a class="btn btn-act btn-block" href="briefs/riba-exit/">Get the Brief for $9</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="white">
  <div class="wrap">
    <h2>The month, as it actually goes.</h2>
    <dl class="ledger">
      <div><dt>Day 1</dt><dd>The salary arrives.</dd></div>
      <div><dt>Day 21</dt><dd><mark class="hl">It is gone.</mark></dd></div>
      <div><dt>Day 30</dt><dd>You prayed, you gave, you worked hard, and you still feel behind.</dd></div>
    </dl>
    <p class="lede">You are not irresponsible, and you are not lacking in imaan. Nobody ever showed you a halal plan for money.</p>
    <p style="margin-top:28px;display:flex;flex-wrap:wrap;gap:16px 24px;align-items:center;max-width:none"><a class="btn btn-act js-guide" href="guide/">Get the free guide</a><a class="link" href="riba-check/">Or check how much riba you pay</a></p>
  </div>
</section>

<section id="pillars">
  <div class="wrap">
    <h2>Wealth is where we start. It is not where we stop.</h2>
    <p class="lede">The Ummah Brief was built for the whole Muslim, not just the wallet.</p>
    <ul class="cover-list">
      <li><b>Wealth</b><span>Halal provision, income, and a way out of riba.</span><a class="link" href="rizq-code/">The Rizq Code</a></li>
      <li><b>Family</b><span>Households with purpose, and children raised with values.</span><a class="link" href="#briefs">The Briefs</a></li>
      <li><b>Knowledge</b><span>One short email every Friday. Always free.</span><a class="link" href="#newsletter">Subscribe</a></li>
      <li><b>Unity</b><span>Free mediation for families, businesses and communities in dispute.</span><a class="link" href="mediation/">Request mediation</a></li>
    </ul>
  </div>
</section>

<section class="emerald" id="circle">
  <div class="wrap circ">
    <a class="sleeve circ-sleeve" style="--c:#0A5640;--t:#FFFFFF" href="circle/" aria-label="The Rizq Circle"><span class="no">Membership <span class="soon">Soon</span></span><span class="ar" lang="ar" aria-hidden="true" style="color:#FFD84D">حلقة</span><span class="ti">The Rizq Circle</span></a>
    <div>
      <h2>The Rizq Circle</h2>
      <p class="lede">For the price of one Brief, every Brief. A money plan every month, an answer to your questions every month, and a circle of Muslim households working through it with you.</p>
      <ul>
        <li>Every Brief, and each new one as it comes out</li>
        <li>One focus, one checklist and one short audio every month</li>
        <li>One membership covers your whole household</li>
      </ul>
      <div class="buy">
        <div class="price">$9<span class="per">/month</span></div>
        <a class="btn btn-act" href="circle/">See the Circle</a>
      </div>
      <p class="small" style="margin-top:16px">Or $79 a year, with The Rizq Code included. Cancel anytime. Opening soon: join the waiting list.</p>
    </div>
  </div>
</section>

<section class="cobalt" id="product">
  <div class="wrap rc">
    <img src="rizq-code/rizq-code-cover.png" alt="The Rizq Code framework with its three companion tools" width="742" height="728">
    <div>
      <h2>The Rizq Code</h2>
      <p class="lede">The halal wealth strategy Muslim families were never taught. A 60-page framework built on Qur'an and Sunnah, with three tools to put it to work.</p>
      <ul>
        <li>The Law of Rizq: how provision flows in Islam</li>
        <li>Ten halal income pathways, and how to find yours</li>
        <li>A 30-day action plan, an audit checklist and a workbook</li>
      </ul>
      <div class="buy">
        <div class="price">$39</div>
        <a class="btn btn-act" href="rizq-code/">See what is inside</a>
      </div>
      <p class="small" style="margin-top:16px">One payment. Instant access. Money back within 30 days if it does not help.</p>
    </div>
  </div>
</section>

<section class="navy med" id="revival">
  <div class="wrap">
    <h2>The Ummah cannot rise divided.</h2>
    <p class="lede">If a dispute is dividing your family, your business or your community, we offer Islamic mediation to help resolve it. It is free, and it always will be.</p>
    <a class="btn btn-line" href="mediation/">Request free mediation</a>
  </div>
</section>

<section class="news" id="newsletter">
  <div class="wrap">
    <h2>One short email, every Friday.</h2>
    <p class="lede">Wealth, family and faith. No noise, no filler, and always free.</p>
    <form class="row-form" data-ok="#nlOk" action="https://formspree.io/f/xnjyanyb" method="POST">
      <input type="email" name="email" placeholder="Your email address" aria-label="Your email address" autocomplete="email" required>
      <input type="hidden" name="source" value="homepage newsletter">
      <button class="btn btn-act" type="submit">Subscribe free</button>
    </form>
    <div class="ok" id="nlOk" role="status">You are subscribed. Look out for us on Friday, insha'Allah.</div>
    <p class="small">Unsubscribe anytime. Here is our <a href="privacy/">privacy notice</a>.</p>
  </div>
</section>
""" % {"sleeves": sleeves}
home += footer("")
home += """<div class="sticky" id="sticky"><a class="btn btn-act btn-block js-guide" href="guide/">Get the free guide</a></div>
<script>
var GUIDE_URL = 'guide/';
var BRIEF_ON_SALE = false;

document.querySelectorAll('.js-guide').forEach(function (a) { a.href = GUIDE_URL; });
if (BRIEF_ON_SALE) {
  document.querySelectorAll('.js-brief-wait').forEach(function (el) { el.style.display = 'none'; });
  document.querySelectorAll('.js-brief-buy').forEach(function (el) { el.style.display = 'block'; });
}

// Tapping a Brief that is not out yet turns the card into that Brief's waiting list.
document.querySelectorAll('.js-pick').forEach(function (a) {
  a.addEventListener('click', function (e) {
    e.preventDefault();
    var name = a.dataset.brief, card = document.getElementById('waitlist');
    document.getElementById('wlTitle').textContent = 'Coming soon: ' + name;
    document.getElementById('wlText').textContent = a.dataset.promise + ' Leave your email and we will tell you the day it is out.';
    document.getElementById('wlFacts').style.display = 'none';
    document.getElementById('wlMore').style.display = 'none';
    document.getElementById('wlSource').value = name + ' waiting list (homepage)';
    document.getElementById('wlBrief').value = name;
    card.style.setProperty('--pick', a.style.getPropertyValue('--c'));
    document.querySelectorAll('.js-brief-buy').forEach(function (el) { el.style.display = 'none'; });
    document.querySelectorAll('.js-brief-wait').forEach(function (el) { el.style.display = 'block'; });
    var form = document.getElementById('briefForm'), ok = document.getElementById('briefOk');
    form.style.display = ''; ok.style.display = 'none';
    var btn = form.querySelector('button'); btn.disabled = false; btn.textContent = 'Tell me when it is out';
    card.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'center' });
    setTimeout(function () { document.getElementById('wlEmail').focus({ preventScroll: true }); }, 500);
  });
});
%s%s
</script>
</body>
</html>
""" % (sticky_js("#newsletter"), FORM_JS)
write("index.html", home)

# ───────────────────────── MEDIATION ─────────────────────────
med_css = """
.hero { padding: 54px 0 70px; }
.hero h1 { font-size: clamp(44px, 10.5vw, 104px); line-height: 0.94; letter-spacing: -0.045em; max-width: 10em; }
.hero .lede { margin: 26px 0 30px; max-width: 32em; }
.principles { border-top: 3px solid var(--ink); margin-top: 34px; }
.principles li { list-style: none; display: grid; grid-template-columns: 240px 1fr; gap: 24px; align-items: baseline; padding: 24px 0; border-bottom: 1px solid var(--rule); }
.principles b { font-family: var(--display); font-weight: 800; font-size: clamp(26px, 4.2vw, 36px); letter-spacing: -0.035em; line-height: 1; }
.principles span { color: var(--slate); }
.steps { list-style: none; counter-reset: s; margin-top: 30px; max-width: 760px; }
.steps li { counter-increment: s; display: grid; grid-template-columns: 62px 1fr; gap: 14px; align-items: baseline; padding: 20px 0; border-bottom: 1px solid var(--rule); }
.steps li::before { content: counter(s); font-family: var(--display); font-weight: 800; font-size: 44px; letter-spacing: -0.04em; line-height: 0.9; }
.steps b { font-family: var(--display); font-weight: 700; font-size: 22px; letter-spacing: -0.02em; display: block; margin-bottom: 2px; }
.steps span { color: var(--slate); }
.form-card { background: var(--white); border: 2px solid var(--ink); border-radius: 18px; padding: 30px; max-width: 760px; margin-top: 30px; }
.field { margin-bottom: 18px; }
.field label { display: block; font-family: var(--display); font-weight: 700; font-size: 16px; margin-bottom: 7px; }
.field input, .field textarea, .field select { width: 100%; min-width: 0; max-width: 100%; font-family: var(--display); font-size: 17px; color: var(--ink); background: var(--chalk); border: 2px solid var(--ink); border-radius: 12px; padding: 13px 15px; }
.field textarea { min-height: 140px; resize: vertical; }
.field input:focus, .field textarea:focus, .field select:focus { outline: 3px solid var(--action); outline-offset: 2px; }
.two { display: grid; grid-template-columns: minmax(0,1fr) minmax(0,1fr); gap: 16px; }
.form-card form { min-width: 0; }
.note { border-left: 4px solid var(--ink); padding: 4px 0 4px 18px; margin-top: 30px; color: var(--slate); font-size: 17.5px; max-width: 760px; }
@media (max-width: 760px) { .principles li { grid-template-columns: 1fr; gap: 8px; } .two { grid-template-columns: 1fr; gap: 0; } .form-card { padding: 22px 18px; } }
"""
med = head("../", "Free Islamic mediation | The Ummah Brief",
           "If a dispute is dividing your family, your business or your community, The Ummah Brief offers free, confidential Islamic mediation.",
           "https://ummahbrief.com/mediation/", med_css)
med += "\n<!-- Check the three steps under 'How it works' against how you actually run mediation, and correct them if needed. -->\n"
med += nav("../", '<a class="btn btn-act btn-sm" href="#request">Request</a>')
med += """
<header class="hero navy" id="top">
  <div class="wrap">
    <h1>The Ummah cannot rise divided.</h1>
    <p class="lede">If a dispute is dividing your family, your business or your community, we offer Islamic mediation to help resolve it. It is free, and it always will be.</p>
    <a class="btn btn-act" href="#request">Request mediation</a>
  </div>
</header>

<section>
  <div class="wrap">
    <h2>What you can expect from us.</h2>
    <ul class="principles">
      <li><b>Unbiased</b><span>We take no side. We help both parties reach a resolution they both accept.</span></li>
      <li><b>Islamic</b><span>Guided by the principles of sulh, reconciliation, in Quran and Sunnah.</span></li>
      <li><b>Confidential</b><span>What you share is read only to respond to you. It is never published and never used for marketing.</span></li>
      <li><b>Free</b><span>There is no charge, now or later. This service is why The Ummah Brief exists.</span></li>
    </ul>
  </div>
</section>

<section class="white">
  <div class="wrap">
    <h2>How it works.</h2>
    <ol class="steps">
      <li><div><b>You tell us what is happening</b><span>Use the form below. A short description is enough at this stage.</span></div></li>
      <li><div><b>We reply within 5 working days</b><span>By email, to the address you give us.</span></div></li>
      <li><div><b>If everyone is willing, we begin</b><span>Mediation only works when all parties agree to take part.</span></div></li>
    </ol>
  </div>
</section>

<section id="request">
  <div class="wrap">
    <h2>Request mediation.</h2>
    <p class="lede">Everything on this form is confidential.</p>
    <div class="form-card">
      <form id="mediationForm" data-ok="#medOk" action="https://formspree.io/f/xkoezjkb" method="POST">
        <div class="two">
          <div class="field"><label for="m-name">Your name</label><input id="m-name" type="text" name="name" autocomplete="name" required></div>
          <div class="field"><label for="m-email">Email address</label><input id="m-email" type="email" name="email" autocomplete="email" required></div>
        </div>
        <div class="field"><label for="m-type">What kind of dispute is it?</label><input id="m-type" type="text" name="dispute_type" placeholder="Family, business, community" required></div>
        <div class="field"><label for="m-desc">Describe it briefly</label><textarea id="m-desc" name="description" placeholder="You do not need to share every detail yet." required></textarea></div>
        <div class="field"><label for="m-will">Are all parties willing to take part?</label>
          <select id="m-will" name="parties_willing"><option>Yes</option><option>No</option><option selected>Unsure</option></select></div>
        <button type="submit" class="btn btn-act btn-block">Send my request</button>
        <p class="small" style="margin-top:14px">We reply within 5 working days. See our <a href="../privacy/">privacy notice</a> for how your information is handled.</p>
      </form>
      <div class="ok" id="medOk" role="status">Your request has been received. We will reply within 5 working days, insha'Allah. JazakAllahu khayran.</div>
    </div>
    <p class="note">Mediation is voluntary. It is not legal advice and it does not replace a court, a lawyer or the authorities. If anyone is at risk of harm, contact your local emergency services first.</p>
  </div>
</section>
"""
med += footer("../")
med += """<div class="sticky" id="sticky"><a class="btn btn-act btn-block" href="#request">Request mediation</a></div>
<script>%s%s</script>
</body>
</html>
""" % (sticky_js("#request"), FORM_JS)
write("mediation/index.html", med)

# ───────────────────────── RIBA EXIT BRIEF ─────────────────────────
no, title, promise, c, t, ar = BRIEFS[0]
brief_css = """
.hero { padding: 46px 0 64px; }
.hero-grid { display: grid; grid-template-columns: 1fr 290px; gap: 56px; align-items: center; }
.hero h1 { font-size: clamp(42px, 9.6vw, 88px); line-height: 0.94; letter-spacing: -0.045em; }
.hero .lede { margin: 24px 0 14px; max-width: 30em; }
.hero .facts { font-family: var(--display); font-weight: 600; font-size: 16px; color: var(--white); margin-bottom: 26px; }
.hero .sleeve { transform: rotate(3deg); }
.hero .sleeve .ti { font-size: 42px; }
.hero .sleeve .ar { font-size: 88px; right: 26px; top: 54px; }
.hero .small { margin-top: 14px; }
@media (max-width: 860px) { .hero-grid { grid-template-columns: 1fr; gap: 26px; } .hero-grid .sleeve { order: -1; width: 150px; padding: 12px; } .hero .sleeve .ti { font-size: 23px; } .hero .sleeve .ar { font-size: 44px; right: 12px; top: 34px; } .hero .btn { display: block; width: 100%%; } }
.pull { font-family: var(--display); font-weight: 800; font-size: clamp(28px, 5.4vw, 46px); letter-spacing: -0.035em; line-height: 1.04; max-width: 18em; margin: 30px 0; }
.pull mark { color: inherit; padding: 0 0.14em; box-decoration-break: clone; -webkit-box-decoration-break: clone; }
.rows { border-top: 3px solid var(--ink); margin-top: 30px; max-width: 820px; }
.rows li { list-style: none; padding: 20px 0; border-bottom: 1px solid var(--rule); }
.rows b { font-family: var(--display); font-weight: 700; font-size: 23px; letter-spacing: -0.02em; display: block; }
.rows span { color: var(--slate); }
.chapters { list-style: none; counter-reset: c; border-top: 3px solid var(--ink); margin-top: 30px; max-width: 820px; }
.chapters li { counter-increment: c; display: grid; grid-template-columns: 62px 1fr; gap: 14px; align-items: baseline; padding: 18px 0; border-bottom: 1px solid var(--rule); }
.chapters li::before { content: counter(c); font-family: var(--display); font-weight: 800; font-size: 44px; letter-spacing: -0.04em; line-height: 0.9; color: %(c)s; }
.chapters b { font-family: var(--display); font-weight: 700; font-size: 23px; letter-spacing: -0.02em; display: block; }
.chapters span { color: var(--slate); }
.fit { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-top: 30px; max-width: 900px; }
.fit div { border: 2px solid var(--ink); border-radius: 16px; padding: 24px; background: var(--white); }
.fit h3 { margin-bottom: 8px; }
.fit p { color: var(--slate); font-size: 18px; }
@media (max-width: 700px) { .fit { grid-template-columns: 1fr; } }
.get h2 { font-size: clamp(40px, 9vw, 84px); line-height: 0.95; letter-spacing: -0.045em; max-width: 11em; }
.get .price { font-family: var(--display); font-weight: 800; font-size: clamp(90px, 20vw, 170px); letter-spacing: -0.06em; line-height: 0.9; margin: 26px 0 8px; }
.get .lede { margin-bottom: 26px; }
.get .small { margin-top: 14px; }
.guar { border-left: 4px solid var(--white); padding: 4px 0 4px 18px; margin-top: 26px; max-width: 34em; }
.faq dt { font-family: var(--display); font-weight: 700; font-size: 23px; letter-spacing: -0.02em; line-height: 1.2; margin-top: 28px; }
.faq dd { color: var(--slate); margin-top: 6px; max-width: 36em; }
""" % {"c": c}
brief = head("../../", "The Riba Exit Brief | The Ummah Brief",
             "You know riba is haram. Nobody showed you the way out. A short audio Brief with a clear order of steps for leaving interest-bearing debt. $9.",
             "https://ummahbrief.com/briefs/riba-exit/", brief_css)
brief += """
<!--
  HOW TO PUT THIS BRIEF ON SALE
  Set CHECKOUT_URL (at the bottom of this file) to the Systeme checkout link.
  While it is empty, the page collects a waiting list.
  Before launch, confirm the audio length and the refund period, and name the scholar who reviewed it.
-->
"""
brief += nav("../../", '<a class="btn btn-act btn-sm js-nav-cta" href="#get">Join the list</a>')
brief += """
<header class="hero navy" id="top">
  <div class="wrap hero-grid">
    <div>
      <h1>You know riba is haram. Nobody showed you the way out.</h1>
      <p class="lede">A short audio Brief with a clear order of steps for leaving interest-bearing debt. Listen once. Start tonight.</p>
      <p class="facts">About 18 minutes. Six chapters. Action sheet and transcript. $9.</p>
      <div class="js-wait">
        <form class="row-form" data-ok="#ok1" action="https://formspree.io/f/xnjyanyb" method="POST">
          <input type="email" name="email" placeholder="Your email address" aria-label="Your email address" autocomplete="email" required>
          <input type="hidden" name="source" value="Riba Exit Brief waiting list (brief page)">
          <button class="btn btn-act" type="submit">Tell me when it is out</button>
        </form>
        <div class="ok" id="ok1" role="status">You are on the list. You will hear from us first, insha'Allah.</div>
        <p class="small">Arriving soon. One email when it is ready.</p>
      </div>
      <div class="js-buy" style="display:none">
        <a class="btn btn-act js-checkout" href="#">Get the Brief for $9</a>
        <p class="small">One payment. Instant access. Pay securely with PayPal.</p>
      </div>
    </div>
    <div class="sleeve" style="--c:%(c)s;--t:%(t)s" aria-hidden="true"><span class="no">Brief 01 <span class="play"></span></span><span class="ar" lang="ar">ربا</span><span class="ti">Riba Exit Brief</span></div>
  </div>
</header>

<section>
  <div class="wrap">
    <h2>You know your minimum payments. Do you know what the debt costs you?</h2>
    <p class="lede">Most Muslims in debt can tell you what they pay each month. Very few can tell you how much of it is riba.</p>
    <p class="pull">This Brief starts by <mark class="hl">finding that number.</mark> Then it gives you the order for bringing it to zero.</p>
    <p class="lede">No lecture, and no guilt. Millions of Muslims were handed a credit card at eighteen and a loan at twenty-two, and nobody explained the cost.</p>
  </div>
</section>

<section class="white">
  <div class="wrap">
    <h2>What you get.</h2>
    <ul class="rows">
      <li><b>The audio</b><span>Six short chapters you can finish on a commute.</span></li>
      <li><b>The one-page action sheet</b><span>Your Riba Map, your exit order and a monthly tracker.</span></li>
      <li><b>The full transcript</b><span>For when you would rather read than listen.</span></li>
      <li><b>One gift copy</b><span>Send the Brief to someone you care about, free.</span></li>
    </ul>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Six chapters, about three minutes each.</h2>
    <ol class="chapters">
      <li><div><b>Why you are here</b><span>What the Qur'an says about riba, and the door it leaves open.</span></div></li>
      <li><div><b>The freeze</b><span>Stop new riba entering your life before you pay off a cent.</span></div></li>
      <li><div><b>The Riba Map</b><span>Find the exact amount of interest leaving your account each month.</span></div></li>
      <li><div><b>The order of exit</b><span>Which debt to attack first, and why the order matters.</span></div></li>
      <li><div><b>Finding the money</b><span>Three places it comes from, and two calls most people never make.</span></div></li>
      <li><div><b>Staying out</b><span>The habits that replace the credit card for good.</span></div></li>
    </ol>
  </div>
</section>

<section class="white">
  <div class="wrap">
    <h2>Is this Brief for you?</h2>
    <div class="fit">
      <div><h3>Yes, if</h3><p>You carry a credit card balance, a personal loan, car finance or an overdraft, and you want out.</p></div>
      <div><h3>No, if</h3><p>You want a ruling on your mortgage, or personal financial advice. This is education, and it says so plainly.</p></div>
    </div>
  </div>
</section>

<section class="navy get" id="get">
  <div class="wrap">
    <h2>One evening. One clear order of steps.</h2>
    <div class="price">$9</div>
    <p class="lede">One payment. No subscription.</p>
    <div class="js-wait">
      <form class="row-form" data-ok="#ok2" action="https://formspree.io/f/xnjyanyb" method="POST">
        <input type="email" name="email" placeholder="Your email address" aria-label="Your email address" autocomplete="email" required>
        <input type="hidden" name="source" value="Riba Exit Brief waiting list (brief page, bottom)">
        <button class="btn btn-act" type="submit">Tell me when it is out</button>
      </form>
      <div class="ok" id="ok2" role="status">You are on the list. You will hear from us first, insha'Allah.</div>
      <p class="small">Arriving soon. One email when it is ready.</p>
    </div>
    <div class="js-buy" style="display:none">
      <a class="btn btn-act js-checkout" href="#">Get the Brief for $9</a>
      <p class="guar">Listen to it. If it does not help, reply to your delivery email within 14 days and you will be refunded in full.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Before you decide.</h2>
    <dl class="faq">
      <dt>Will this tell me what to do about my home loan?</dt>
      <dd>No. Scholars differ on home finance, and your country and circumstances matter. The Brief tells you which three actions to take, and deals fully with every other kind of interest-bearing debt.</dd>
      <dt>I am not good with numbers. Will I manage?</dt>
      <dd>Yes. The action sheet asks for four things per debt and one simple sum. If you can read a bank statement, you can do this.</dd>
      <dt>How do I listen?</dt>
      <dd>You get a link by email. Play it in your browser or download the audio to your phone.</dd>
      <dt>Is this financial advice?</dt>
      <dd>No. It is general education. It is not personal financial advice and it is not a fatwa.</dd>
    </dl>
  </div>
</section>
""" % {"c": c, "t": t}
brief += footer("../../")
brief += """<div class="sticky" id="sticky"><a class="btn btn-act btn-block js-sticky" href="#get">Join the waiting list</a></div>
<script>
var CHECKOUT_URL = '';

if (CHECKOUT_URL) {
  document.querySelectorAll('.js-wait').forEach(function (el) { el.style.display = 'none'; });
  document.querySelectorAll('.js-buy').forEach(function (el) { el.style.display = 'block'; });
  document.querySelectorAll('.js-checkout').forEach(function (a) { a.href = CHECKOUT_URL; });
  var n = document.querySelector('.js-nav-cta'); n.textContent = 'Get it for $9'; n.href = CHECKOUT_URL;
  var s = document.querySelector('.js-sticky'); s.textContent = 'Get the Brief for $9'; s.href = CHECKOUT_URL;
}
%s%s
</script>
</body>
</html>
""" % (sticky_js("#get"), FORM_JS)
write("briefs/riba-exit/index.html", brief)

# ───────────────────────── PRIVACY AND TERMS ─────────────────────────
doc_css = """
main { padding: 54px 0 80px; }
main .wrap { max-width: 760px; }
main h1 { font-size: clamp(40px, 9vw, 72px); letter-spacing: -0.045em; line-height: 0.96; margin-bottom: 10px; }
main h2 { font-size: 26px; letter-spacing: -0.025em; line-height: 1.15; margin: 38px 0 8px; }
main p, main li { margin-bottom: 12px; }
main ul { padding-left: 22px; }
main .small { margin-bottom: 30px; }
footer { padding-bottom: 46px; }
"""
privacy = """
<p>The Ummah Brief respects your privacy. This notice explains what we collect, why, and the choices you have.</p>
<h2>Who we are</h2>
<p>The Ummah Brief publishes educational content and digital products at ummahbrief.com. You can reach us at <a href="mailto:salaam@ummahbrief.com">salaam@ummahbrief.com</a>.</p>
<h2>What we collect</h2>
<ul>
<li><strong>Newsletter, free guide and waiting lists:</strong> your email address, and your first name if you give it.</li>
<li><strong>Purchases:</strong> your name, email address and order details. Payment is handled by PayPal. We never see or store your card details.</li>
<li><strong>Mediation requests:</strong> your name, email address and what you choose to tell us about the dispute.</li>
<li><strong>The Riba Check:</strong> the debt figures you type are worked out inside your own browser. They are never sent to us or stored. Only your email address is sent, if you choose to enter it.</li>
<li><strong>The Ledger:</strong> the story you submit and your email address. Stories are only ever published with identifying details removed.</li>
<li><strong>Messages:</strong> whatever you send us by email.</li>
</ul>
<h2>How we use it</h2>
<ul>
<li>To send what you asked for: the guide, the newsletter, your purchase.</li>
<li>To reply to your mediation request or message.</li>
<li>To tell you about our own products. Every email has an unsubscribe link.</li>
</ul>
<p>We do not sell your information, and we do not share it with other organisations for their marketing. Newsletter sponsors never receive your details.</p>
<h2>Mediation requests</h2>
<p>What you share in a mediation request is treated as confidential. It is read only for the purpose of responding to you, it is never used for marketing, and it is never published.</p>
<h2>Services we use</h2>
<p>We use trusted providers to run the site and deliver email, and they process your information on our behalf: Formspree (forms), Beehiiv and Systeme.io (email and checkout), PayPal (payments), and GitHub Pages and Netlify (hosting). Some of them store data outside your country.</p>
<h2>How long we keep it</h2>
<p>We keep your email address until you unsubscribe or ask us to delete it. We keep purchase records for as long as tax law requires. We delete mediation requests once the matter is closed, unless you ask us to keep them.</p>
<h2>Your rights</h2>
<p>You can ask to see, correct or delete the information we hold about you, and you can unsubscribe at any time. Email <a href="mailto:salaam@ummahbrief.com">salaam@ummahbrief.com</a> and we will respond within 30 days. Depending on where you live, you also have the right to complain to your data protection regulator.</p>
<h2>Changes</h2>
<p>If this notice changes, the new version will be posted here with a new date.</p>
"""
terms = """
<p>These terms apply when you use ummahbrief.com or buy from The Ummah Brief.</p>
<h2>What we sell</h2>
<p>We sell digital educational products, including The Rizq Code and the Briefs. Prices are shown in US dollars and are charged once unless a product clearly says it is a subscription.</p>
<h2>Delivery</h2>
<p>Digital products are delivered by email straight after payment. If yours has not arrived within an hour, check your spam folder, then email <a href="mailto:salaam@ummahbrief.com">salaam@ummahbrief.com</a>.</p>
<h2>Refunds</h2>
<p>The Rizq Code has a 30-day money-back guarantee. Email <a href="mailto:salaam@ummahbrief.com">salaam@ummahbrief.com</a> within 30 days of purchase and we will refund you in full to your original payment method. You do not need to give a reason.</p>
<p>Briefs can be refunded within 14 days of purchase in the same way.</p>
<h2>The Rizq Circle (subscription)</h2>
<p>The Rizq Circle is a subscription, billed through PayPal every month or every year until you cancel. You can cancel at any time from your PayPal account or by emailing us, and you keep access until the end of the period you have paid for. If the Circle is not for you, email us within 14 days of your first payment and we will refund it in full. Later payments are not refunded, but you can cancel before the next one. Briefs are available to members for as long as they stay members. The Rizq Code included with a yearly membership is yours to keep.</p>
<h2>Education, not advice</h2>
<p>Everything we publish is general education. It is not personal financial, investment, tax or legal advice, and it is not a fatwa. We do not know your circumstances. Before making a financial decision, speak to a qualified adviser, and take religious questions to a scholar you trust. We make no promise about the income or results you will achieve.</p>
<h2>Your licence</h2>
<p>When you buy a product, it is for your own personal use. Please do not resell it, publish it or share your download with others. If someone you know would benefit, send them to the site.</p>
<h2>Sponsored content</h2>
<p>The Friday email may carry a clearly labelled sponsor. Sponsors never pay for our opinion, never see our readers' details, and are chosen against published standards (see ummahbrief.com/sponsor). A sponsor's offer is theirs, not ours, so check it as you would any other.</p>
<h2>Mediation</h2>
<p>Our mediation service is free and voluntary. It is not legal advice and does not replace a court, a lawyer or the authorities. If anyone is at risk of harm, contact your local emergency services.</p>
<h2>Liability</h2>
<p>To the extent the law allows, our liability to you for any product is limited to the amount you paid for it. Nothing in these terms removes rights you have under consumer law where you live.</p>
<h2>Contact</h2>
<p>Questions about these terms: <a href="mailto:salaam@ummahbrief.com">salaam@ummahbrief.com</a>.</p>
"""
for slug, ttl, body in [("privacy", "Privacy notice", privacy), ("terms", "Terms and refunds", terms)]:
    page = head("../", ttl + " | The Ummah Brief", ttl + " for The Ummah Brief.", "https://ummahbrief.com/%s/" % slug, doc_css)
    page += "\n<!-- DRAFT written November 2026. Read it, correct anything that is not true of how you operate, and have it checked before relying on it. -->\n"
    page += nav("../", "")
    page += '<main><div class="wrap"><h1>%s</h1><p class="small">Last updated 15 November 2026</p>%s</div></main>\n' % (ttl, body)
    page += footer("../")
    page += "<script>%s</script>\n</body>\n</html>\n" % FORM_JS
    write("%s/index.html" % slug, page)


# ───────────────────────── FREE GUIDE ─────────────────────────
LEAK_ROWS = [("#C92F3A", "Interest you never see", "The riba inside your monthly payments."),
             ("#F2B632", "Money that leaves while you sleep", "Subscriptions, fees and forgotten debits."),
             ("#17837C", "A lifestyle that grew with the salary", "Every raise spent before it arrives."),
             ("#5B2A6E", "Giving without a plan", "Generosity in amounts you never chose."),
             ("#2F7FD1", "Money with no job", "What is left over has no destination.")]
guide_css = """
.hero { padding: 48px 0 66px; }
.hero-grid { display: grid; grid-template-columns: 1fr 300px; gap: 60px; align-items: center; }
.hero h1 { font-size: clamp(54px, 13vw, 124px); line-height: 0.88; letter-spacing: -0.05em; }
.hero .lede { margin: 24px 0 26px; max-width: 28em; }
.hero .small { margin-top: 14px; max-width: 34em; }
.pdf { transform: rotate(3deg); border-radius: 6px; box-shadow: 0 30px 70px rgba(4,9,26,0.6), 0 0 0 1.5px rgba(255,255,255,0.35); width: 100%; height: auto; }
@media (max-width: 860px) { .hero-grid { grid-template-columns: 1fr; gap: 34px; } .pdf { max-width: 210px; margin-left: 6px; } }
.leaks { list-style: none; counter-reset: l; border-top: 3px solid var(--ink); margin-top: 30px; max-width: 860px; }
.leaks li { counter-increment: l; display: grid; grid-template-columns: 62px 1fr; gap: 14px; align-items: baseline; padding: 18px 0; border-bottom: 1px solid var(--rule); }
.leaks li::before { content: counter(l); font-family: var(--display); font-weight: 800; font-size: 44px; letter-spacing: -0.04em; line-height: 0.9; color: var(--c); }
.leaks b { font-family: var(--display); font-weight: 700; font-size: 24px; letter-spacing: -0.025em; display: block; line-height: 1.15; }
.leaks span { color: var(--slate); }
.need { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 30px; max-width: 860px; }
.need div { border: 2px solid var(--ink); border-radius: 16px; padding: 22px; background: var(--chalk); }
.need b { font-family: var(--display); font-weight: 800; font-size: 30px; letter-spacing: -0.035em; display: block; line-height: 1; margin-bottom: 6px; }
.need span { color: var(--slate); font-size: 17.5px; }
@media (max-width: 700px) { .need { grid-template-columns: 1fr; } }
.again h2 { font-size: clamp(40px, 9vw, 84px); line-height: 0.95; letter-spacing: -0.045em; max-width: 11em; }
.again .lede { margin: 22px 0 26px; }
footer { padding-bottom: 46px; }
"""
form_html = """<form class="row-form" data-ok="#%(ok)s" data-next="thanks/" action="https://formspree.io/f/xnjyanyb" method="POST">
        <input type="email" name="email" placeholder="Your email address" aria-label="Your email address" autocomplete="email" required>
        <input type="hidden" name="source" value="Free guide: Where did it go? (%(where)s)">
        <button class="btn btn-act" type="submit">Send me the guide</button>
      </form>
      <div class="ok" id="%(ok)s" role="status">Done. <a href="thanks/">Open your guide</a></div>"""
g = head("../", "Where did it go? A free guide | The Ummah Brief",
         "The five places a halal income disappears, and how to find yours in 15 minutes. A free guide from The Ummah Brief.",
         "https://ummahbrief.com/guide/", guide_css)
g += "\n<!-- The guide signups arrive in Formspree labelled 'Free guide: Where did it go?'. After signing up, people go to thanks/ where the PDF is. -->\n"
g += nav("../", "")
g += """
<header class="hero navy" id="top">
  <div class="wrap hero-grid">
    <div>
      <h1>Where did it go?</h1>
      <p class="lede">You earn halal, and by the end of the month nothing is left. This free guide shows the five places it disappears, and how to find yours in 15 minutes.</p>
      %(form1)s
      <p class="small">Free. You will also get one short email every Friday, and you can unsubscribe anytime. See our <a href="../privacy/">privacy notice</a>.</p>
    </div>
    <img class="pdf" src="cover.png" alt="Cover of the guide: Where did it go?" width="437" height="620">
  </div>
</header>

<section>
  <div class="wrap">
    <h2>The five leaks.</h2>
    <p class="lede">Most households that feel stuck do not have an income problem. They have leaks they have never measured.</p>
    <ol class="leaks">
      %(rows)s
    </ol>
  </div>
</section>

<section class="white">
  <div class="wrap">
    <h2>For each leak, you get three things.</h2>
    <div class="need">
      <div><b>Three signs</b><span>Tick the ones you recognise, so you know if the leak is yours.</span></div>
      <div><b>A number</b><span>A three-minute way to work out what it costs you each month.</span></div>
      <div><b>One fix</b><span>A first step you can take the same day.</span></div>
    </div>
    <p class="lede" style="margin-top:30px">All you need is last month's bank statement, a pen and 15 minutes.</p>
  </div>
</section>

<section class="navy again">
  <div class="wrap">
    <h2>Find out where yours goes.</h2>
    <p class="lede">Nine short pages. No budget, no app, no spreadsheet.</p>
    %(form2)s
  </div>
</section>
""" % {"form1": form_html % {"ok": "gOk1", "where": "top"}, "form2": form_html % {"ok": "gOk2", "where": "bottom"},
       "rows": "\n      ".join('<li style="--c:%s"><div><b>%s</b><span>%s</span></div></li>' % r for r in LEAK_ROWS)}
g += footer("../")
g += "<script>%s</script>\n</body>\n</html>\n" % FORM_JS
write("guide/index.html", g)

thanks_css = """
.hero { padding: 56px 0 70px; }
.hero h1 { font-size: clamp(46px, 11vw, 104px); line-height: 0.92; letter-spacing: -0.045em; max-width: 9em; }
.hero .lede { margin: 24px 0 30px; max-width: 30em; }
.hero .btn-act { font-size: 19px; padding: 18px 32px; }
.hero .small { margin-top: 16px; }
.nexts { border-top: 3px solid var(--ink); margin-top: 30px; max-width: 860px; }
.nexts a { display: grid; grid-template-columns: 1fr auto; gap: 20px; align-items: center; padding: 24px 0; border-bottom: 1px solid var(--rule); text-decoration: none; }
.nexts b { font-family: var(--display); font-weight: 800; font-size: clamp(24px, 4vw, 32px); letter-spacing: -0.035em; line-height: 1.05; display: block; }
.nexts span { color: var(--slate); }
.nexts i { font-family: var(--display); font-style: normal; font-weight: 700; font-size: 16px; text-decoration: underline; text-underline-offset: 4px; white-space: nowrap; }
@media (max-width: 600px) { .nexts a { grid-template-columns: 1fr; gap: 8px; } }
footer { padding-bottom: 46px; }
"""
t = head("../../", "Your guide is ready | The Ummah Brief", "Download Where did it go?, the free guide from The Ummah Brief.",
         "https://ummahbrief.com/guide/thanks/", thanks_css).replace('<meta name="color-scheme" content="light">', '<meta name="color-scheme" content="light">\n<meta name="robots" content="noindex">')
t += nav("../../", "")
t += """
<header class="hero navy" id="top">
  <div class="wrap">
    <h1>Your guide is ready.</h1>
    <p class="lede">JazakAllahu khayran. Open it now, with last month's bank statement and a pen beside you. It takes 15 minutes.</p>
    <a class="btn btn-act" href="../where-did-it-go.pdf">Open the guide</a>
    <p class="small">It opens as a PDF. Save it to your phone so you can come back to your leak sheet.</p>
  </div>
</header>

<section>
  <div class="wrap">
    <h2>When you have found your leaks.</h2>
    <div class="nexts">
      <a href="../../briefs/riba-exit/"><div><b>If riba was your biggest number</b><span>The Riba Exit Brief is a short audio with a clear order of steps for leaving interest-bearing debt.</span></div><i>Join the list</i></a>
      <a href="../../rizq-code/"><div><b>If you want the whole plan</b><span>The Rizq Code is the complete halal wealth framework, with a 30-day action plan.</span></div><i>See what is inside</i></a>
      <a href="../../mediation/"><div><b>If money is dividing your family</b><span>We offer Islamic mediation. It is free, and it always will be.</span></div><i>Request mediation</i></a>
    </div>
  </div>
</section>
"""
t += footer("../../")
t += "<script>%s</script>\n</body>\n</html>\n" % FORM_JS
write("guide/thanks/index.html", t)


# ───────────────────────── RIBA CHECK ─────────────────────────
rc_css = """
.hero { padding: 48px 0 58px; }
.hero h1 { font-size: clamp(46px, 11vw, 104px); line-height: 0.9; letter-spacing: -0.05em; max-width: 9.5em; }
.hero .lede { margin: 22px 0 0; max-width: 30em; }
.tool { padding: 44px 0 76px; }
.card { background: var(--white); border: 2px solid var(--ink); border-radius: 18px; padding: 26px; max-width: 860px; }
.cur { display: flex; align-items: center; gap: 12px; margin-bottom: 18px; font-family: var(--display); font-weight: 700; font-size: 16px; }
.cur select, .debt input { font-family: var(--display); font-size: 17px; color: var(--ink); background: var(--chalk); border: 2px solid var(--ink); border-radius: 10px; padding: 11px 12px; width: 100%; min-width: 0; }
.cur select { width: auto; }
.debt { display: grid; grid-template-columns: 1.3fr 1fr 0.8fr 1fr 36px; gap: 10px; align-items: end; padding: 14px 0; border-top: 1px solid var(--rule); }
.debt label { display: block; font-family: var(--display); font-weight: 700; font-size: 13.5px; margin-bottom: 5px; color: var(--slate); }
.debt input:focus, .cur select:focus { outline: 3px solid var(--action); outline-offset: 2px; }
.rm { width: 36px; height: 46px; border: none; background: none; font-family: var(--display); font-size: 24px; font-weight: 700; color: var(--slate); cursor: pointer; border-radius: 8px; }
.rm:hover { color: var(--ink); background: var(--chalk); }
.add { margin-top: 14px; font-family: var(--display); font-weight: 700; font-size: 16px; background: none; border: 2px dashed var(--ink); border-radius: 12px; padding: 12px 18px; cursor: pointer; color: var(--ink); }
.add:hover { background: var(--chalk); }
.hint { font-family: var(--display); font-size: 14.5px; color: var(--slate); margin-top: 14px; max-width: none; }
@media (max-width: 720px) {
  .card { padding: 20px 16px; }
  .debt { grid-template-columns: 1fr 1fr; gap: 10px 10px; }
  .debt .f-name { grid-column: 1 / -1; }
  .debt .rm { grid-column: 2; justify-self: end; height: 36px; }
}
.out { margin-top: 26px; max-width: 860px; display: none; }
.out.show { display: block; }
.big { background: var(--navy); color: var(--white); border-radius: 18px; padding: 28px 26px; }
.big .lab { font-family: var(--display); font-weight: 600; font-size: 17px; color: var(--on-navy); }
.big .num { font-family: var(--display); font-weight: 800; font-size: clamp(58px, 15vw, 120px); letter-spacing: -0.055em; line-height: 0.95; margin: 6px 0 10px; overflow-wrap: anywhere; }
.big .sub { font-family: var(--display); font-weight: 600; font-size: 18px; color: var(--mark); }
.gate { background: var(--white); border: 2px solid var(--ink); border-radius: 18px; padding: 26px; margin-top: 16px; }
.gate h3 { font-size: 27px; letter-spacing: -0.03em; line-height: 1.05; margin-bottom: 8px; }
.gate p { color: var(--slate); font-size: 17.5px; margin-bottom: 16px; }
.plan { display: none; margin-top: 16px; }
.plan.show { display: block; }
.rows { border-top: 3px solid var(--ink); }
.rows div { display: grid; grid-template-columns: 1fr auto; gap: 16px; align-items: baseline; padding: 16px 0; border-bottom: 1px solid var(--rule); }
.rows span { color: var(--slate); }
.rows b { font-family: var(--display); font-weight: 800; font-size: clamp(22px, 4.6vw, 30px); letter-spacing: -0.035em; text-align: right; }
.rows .good b { background: var(--mark); padding: 0 0.16em; }
.rows .extra { display: inline-flex; align-items: center; gap: 4px; }
.rows .extra input { width: 7.5em; padding: 4px 8px; font: inherit; font-family: var(--display); font-weight: 700; color: var(--ink); border: 2px solid var(--ink); border-radius: 8px; background: var(--white); }
.plan .note { color: var(--slate); font-size: 16.5px; margin: 10px 0 0; }
.order { list-style: none; counter-reset: o; margin: 8px 0 0; }
.order li { counter-increment: o; display: grid; grid-template-columns: 44px 1fr; gap: 10px; align-items: baseline; padding: 12px 0; border-bottom: 1px solid var(--rule); font-family: var(--display); font-weight: 700; font-size: 18px; }
.order li::before { content: counter(o); font-weight: 800; font-size: 30px; letter-spacing: -0.04em; color: #C92F3A; }
.order small { display: block; font-family: var(--text); font-weight: 400; font-size: 16px; color: var(--slate); }
.plan h3 { font-size: 24px; margin: 30px 0 4px; }
.warn { font-family: var(--display); font-weight: 600; font-size: 16px; background: #FDE7E2; border-left: 5px solid #C92F3A; padding: 12px 14px; border-radius: 0 10px 10px 0; margin-top: 14px; display: none; }
.after { display: flex; flex-wrap: wrap; gap: 14px 22px; align-items: center; margin-top: 26px; }
.steps3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 30px; }
.steps3 div { border: 2px solid var(--ink); border-radius: 16px; padding: 22px; background: var(--chalk); }
.steps3 b { font-family: var(--display); font-weight: 800; font-size: 26px; letter-spacing: -0.035em; display: block; line-height: 1.05; margin-bottom: 6px; }
.steps3 span { color: var(--slate); font-size: 17.5px; }
@media (max-width: 700px) { .steps3 { grid-template-columns: 1fr; } }
footer { padding-bottom: 46px; }
"""
rc = head("../", "The Riba Check: how much riba do you pay? | The Ummah Brief",
          "A free two-minute tool. Enter your debts and see how much interest leaves your account every month, and how to bring it to zero.",
          "https://ummahbrief.com/riba-check/", rc_css)
rc += "\n<!-- All sums run in the visitor's browser. Only the email address is sent (to Formspree, labelled 'Riba Check'). -->\n"
rc += nav("../", "")
rc += """
<header class="hero navy" id="top">
  <div class="wrap">
    <h1>How much riba do you pay?</h1>
    <p class="lede">You know your monthly payments. This free check shows how much of them is interest, in about two minutes.</p>
  </div>
</header>

<section class="tool">
  <div class="wrap">
    <div class="card">
      <div class="cur"><label for="cur">Currency</label>
        <select id="cur"><option value="$">$ Dollar</option><option value="£">£ Pound</option><option value="AED ">AED Dirham</option><option value="R">R Rand</option><option value="€">€ Euro</option><option value="">Other</option></select>
      </div>
      <div id="debts"></div>
      <button type="button" class="add" id="add">Add another debt</button>
      <p class="hint">Enter each credit card, loan, car finance or overdraft. You can leave your home loan out. The interest rate is the yearly rate on your statement.</p>
      <div class="after" style="margin-top:20px"><button type="button" class="btn btn-act" id="calc">Show my number</button></div>
      <div class="warn" id="err" role="alert"></div>
    </div>

    <div class="out" id="out" aria-live="polite">
      <div class="big">
        <div class="lab">Riba leaving your account every month</div>
        <div class="num" id="perMonth"></div>
        <div class="sub"><span id="perDay"></span> every day. About <span id="perYear"></span> over the next 12 months.</div>
      </div>

      <div class="gate" id="gate">
        <h3>See your way out.</h3>
        <p>Enter your email to see when you will be debt-free, how much riba is still to come, and the order to clear your debts in. Your figures stay on your device. Only your email is sent.</p>
        <form class="row-form" id="gateForm" action="https://formspree.io/f/xnjyanyb" method="POST">
          <input type="email" name="email" placeholder="Your email address" aria-label="Your email address" autocomplete="email" required>
          <input type="hidden" name="source" value="Riba Check">
          <button class="btn btn-act" type="submit">Show my plan</button>
        </form>
        <p class="small" style="margin:12px 0 0">Free. You will also get one short email every Friday, and you can unsubscribe anytime. See our <a href="../privacy/">privacy notice</a>.</p>
      </div>

      <div class="plan" id="plan">
        <div class="rows">
          <div><span>Debt-free at your current payments</span><b id="freeNow"></b></div>
          <div><span>Riba still to pay at your current payments</span><b id="ribaNow"></b></div>
          <div class="good"><span>Debt-free if you follow the exit order, with no extra money</span><b id="freeRoll"></b></div>
          <div class="good"><span>Riba that avoids</span><b id="savedRoll"></b></div>
          <div class="good"><span>Debt-free if you also add <span class="extra"><span id="curLab"></span><input id="extra" type="number" inputmode="decimal" min="0" step="any" aria-label="Extra amount each month"></span> a month</span><b id="freePlan"></b></div>
          <div class="good"><span>Riba that avoids</span><b id="saved"></b></div>
        </div>
        <p class="note">Change the extra amount to see how it moves your date. Moving each cleared debt's payment onto the next one saves riba even with no extra money.</p>
        <div class="warn" id="never"></div>
        <h3>Your exit order</h3>
        <p class="lede" style="font-size:18px">Pay the minimum on everything. Put every spare amount on the first debt. When it is gone, move its payment to the next.</p>
        <ol class="order" id="order"></ol>
        <div class="after">
          <a class="btn btn-act" href="../briefs/riba-exit/">See the Riba Exit Brief</a>
          <button type="button" class="btn btn-line" id="share">Share the Riba Check</button>
        </div>
        <p class="small" style="margin-top:14px" id="shareMsg"></p>
      </div>
      <p class="hint">These are estimates based on what you entered. They are general education, not personal financial advice and not a fatwa.</p>
    </div>
  </div>
</section>

<section class="white">
  <div class="wrap">
    <h2>What the check gives you.</h2>
    <div class="steps3">
      <div><b>Your number</b><span>The riba leaving your account each month and each day, and what it adds up to over the next year.</span></div>
      <div><b>Your date</b><span>When you will be debt-free at your current payments.</span></div>
      <div><b>Your order</b><span>Which debt to clear first, and what that saves you.</span></div>
    </div>
  </div>
</section>
"""
rc += footer("../")
rc += """<script>
(function () {
  var wrap = document.getElementById('debts'), n = 0, last = null;
  function row() {
    n++;
    var d = document.createElement('div'); d.className = 'debt';
    d.innerHTML = '<div class="f-name"><label for="n' + n + '">Name it</label><input id="n' + n + '" class="i-name" type="text" placeholder="e.g. Car finance"></div>' +
      '<div><label for="b' + n + '">Balance owed</label><input id="b' + n + '" class="i-bal" type="number" inputmode="decimal" min="0" step="any" placeholder="0"></div>' +
      '<div><label for="r' + n + '">Rate % a year</label><input id="r' + n + '" class="i-rate" type="number" inputmode="decimal" min="0" max="100" step="any" placeholder="0"></div>' +
      '<div><label for="p' + n + '">Monthly payment</label><input id="p' + n + '" class="i-pay" type="number" inputmode="decimal" min="0" step="any" placeholder="0"></div>' +
      '<button type="button" class="rm" aria-label="Remove this debt">&times;</button>';
    d.querySelector('.rm').addEventListener('click', function () { if (wrap.children.length > 1) d.remove(); });
    wrap.appendChild(d);
  }
  row(); row();
  document.getElementById('add').addEventListener('click', function () { if (wrap.children.length < 8) row(); });

  function cur() { return document.getElementById('cur').value; }
  function money(x) { return cur() + Math.round(x).toLocaleString('en-US'); }
  function when(months) {
    if (!isFinite(months)) return 'Never';
    var d = new Date(); d.setMonth(d.getMonth() + months);
    return d.toLocaleString('en-US', { month: 'short', year: 'numeric' });
  }
  function read() {
    var out = [];
    wrap.querySelectorAll('.debt').forEach(function (d, i) {
      var bal = parseFloat(d.querySelector('.i-bal').value), rate = parseFloat(d.querySelector('.i-rate').value), pay = parseFloat(d.querySelector('.i-pay').value);
      if (!(bal > 0)) return;
      out.push({ name: (function (v) { return v && !/^[\\d\\s.,]+$/.test(v) ? v : 'Debt ' + (i + 1); })(d.querySelector('.i-name').value.trim()), bal: bal, rate: rate >= 0 ? rate : 0, pay: pay >= 0 ? pay : 0 });
    });
    return out;
  }
  // Each debt paid on its own, at its own payment.
  function alone(debts) {
    var months = 0, interest = 0, stuck = [];
    debts.forEach(function (d) {
      var b = d.bal, r = d.rate / 1200, m = 0, paid = 0;
      if (d.pay <= b * r + 0.005) { stuck.push(d.name); months = Infinity; return; }
      while (b > 0.005 && m < 1200) { var it = b * r; paid += it; b = b + it - d.pay; m++; }
      interest += paid; if (m > months) months = m;
    });
    return { months: months, interest: interest, stuck: stuck };
  }
  // Exit order: highest rate first. Where rates are equal, the smaller balance goes first.
  function rank(x, y) { return (y.r - x.r) || (x.b - y.b); }
  // Minimums on everything, every spare amount on the first debt in the order, payments roll over.
  function exit(debts, extra) {
    var ds = debts.map(function (d) { return { b: d.bal, r: d.rate / 1200, p: d.pay }; });
    var budget = extra + ds.reduce(function (a, d) { return a + d.p; }, 0), m = 0, interest = 0;
    while (ds.some(function (d) { return d.b > 0.005; }) && m < 1200) {
      var left = budget;
      ds.forEach(function (d) { if (d.b > 0.005) { var it = d.b * d.r; interest += it; d.b += it; } });
      ds.forEach(function (d) { if (d.b > 0.005) { var pay = Math.min(d.p, d.b, left); d.b -= pay; left -= pay; } });
      ds.filter(function (d) { return d.b > 0.005; }).sort(rank).forEach(function (d) { var pay = Math.min(left, d.b); d.b -= pay; left -= pay; });
      m++;
    }
    return { months: m >= 1200 ? Infinity : m, interest: interest };
  }
  function span(months) {
    if (!isFinite(months)) return '';
    var y = Math.floor(months / 12), mo = months % 12;
    return (y ? y + (y === 1 ? ' year' : ' years') : '') + (y && mo ? ' ' : '') + (mo ? mo + (mo === 1 ? ' month' : ' months') : '') || 'under a month';
  }
  document.getElementById('calc').addEventListener('click', function () {
    var err = document.getElementById('err'), debts = read();
    if (!debts.length) { err.textContent = 'Enter at least one debt with a balance.'; err.style.display = 'block'; return; }
    err.style.display = 'none'; last = debts;
    var perMonth = debts.reduce(function (a, d) { return a + d.bal * d.rate / 1200; }, 0);
    document.getElementById('perMonth').textContent = money(perMonth);
    document.getElementById('perDay').textContent = money(perMonth * 12 / 365);
    var year = debts.reduce(function (a, d) { var b = d.bal, r = d.rate / 1200, t = 0; for (var k = 0; k < 12 && b > 0.005; k++) { var it = b * r; t += it; b = b + it - Math.min(d.pay, b + it); } return a + t; }, 0);
    document.getElementById('perYear').textContent = money(year);
    document.getElementById('out').classList.add('show');
    if (document.getElementById('plan').classList.contains('show')) plan();
    document.getElementById('out').scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
  function plan() {
    var debts = last, a = alone(debts), total = debts.reduce(function (x, d) { return x + d.pay; }, 0);
    var box = document.getElementById('extra');
    if (box.value === '' || box.dataset.auto === '1') { box.value = Math.max(Math.round(total * 0.1 / 10) * 10, 10); box.dataset.auto = '1'; }
    var extra = Math.max(parseFloat(box.value) || 0, 0), e = exit(debts, extra), z = exit(debts, 0);
    document.getElementById('curLab').textContent = cur();
    function saving(x) { return isFinite(a.months) && isFinite(x.months) ? money(Math.max(a.interest - x.interest, 0)) : (isFinite(x.months) ? 'All of it' : 'None yet'); }
    document.getElementById('freeRoll').textContent = isFinite(z.months) ? when(z.months) : 'Never';
    document.getElementById('savedRoll').textContent = saving(z);
    document.getElementById('freeNow').textContent = isFinite(a.months) ? when(a.months) : 'Never';
    document.getElementById('ribaNow').textContent = isFinite(a.months) ? money(a.interest) : 'No end';
    document.getElementById('freePlan').textContent = isFinite(e.months) ? when(e.months) : 'Never';
    document.getElementById('saved').textContent = saving(e);
    var nv = document.getElementById('never');
    if (a.stuck.length) { nv.textContent = 'At the payment you entered, this debt never clears because the payment does not cover its interest: ' + a.stuck.join(', ') + '.'; nv.style.display = 'block'; } else nv.style.display = 'none';
    var ol = document.getElementById('order'); ol.innerHTML = '';
    debts.slice().sort(function (x, y) { return rank({ r: x.rate, b: x.bal }, { r: y.rate, b: y.bal }); }).forEach(function (d) {
      var li = document.createElement('li'), div = document.createElement('div'), sm = document.createElement('small');
      div.textContent = d.name; sm.textContent = d.rate + '% a year, costing ' + money(d.bal * d.rate / 1200) + ' a month in riba'; div.appendChild(sm); li.appendChild(div); ol.appendChild(li);
    });
    document.getElementById('plan').classList.add('show');
  }
  document.getElementById('extra').addEventListener('input', function () { this.dataset.auto = '0'; if (last) plan(); });
  document.getElementById('gateForm').addEventListener('submit', async function (ev) {
    ev.preventDefault();
    var form = ev.target, btn = form.querySelector('button'), label = btn.textContent;
    btn.textContent = 'Working it out...'; btn.disabled = true;
    try {
      var res = await fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } });
      if (res.ok) { document.getElementById('gate').style.display = 'none'; plan(); return; }
    } catch (e) {}
    btn.textContent = 'That did not send. Try again'; btn.disabled = false;
    setTimeout(function () { btn.textContent = label; }, 4000);
  });
  document.getElementById('share').addEventListener('click', async function () {
    var data = { title: 'The Riba Check', text: 'I just checked how much riba I pay each month. Have you?', url: 'https://ummahbrief.com/riba-check/' };
    var msg = document.getElementById('shareMsg');
    try {
      if (navigator.share) { await navigator.share(data); return; }
      await navigator.clipboard.writeText(data.text + ' ' + data.url); msg.textContent = 'Link copied. Paste it anywhere.';
    } catch (e) { msg.textContent = 'Share this link: ' + data.url; }
  });
  window.__riba = { alone: alone, exit: exit };
})();
""" + FORM_JS + """
</script>
</body>
</html>
"""
write("riba-check/index.html", rc)

# ───────────────────────── THE LEDGER ─────────────────────────
lg_css = """
.hero { padding: 48px 0 62px; }
.hero h1 { font-size: clamp(46px, 11vw, 104px); line-height: 0.9; letter-spacing: -0.05em; max-width: 9em; }
.hero .lede { margin: 22px 0 0; max-width: 31em; }
.how { list-style: none; counter-reset: s; margin-top: 30px; max-width: 760px; border-top: 3px solid var(--ink); }
.how li { counter-increment: s; display: grid; grid-template-columns: 62px 1fr; gap: 14px; align-items: baseline; padding: 18px 0; border-bottom: 1px solid var(--rule); }
.how li::before { content: counter(s); font-family: var(--display); font-weight: 800; font-size: 44px; letter-spacing: -0.04em; line-height: 0.9; }
.how b { font-family: var(--display); font-weight: 700; font-size: 22px; letter-spacing: -0.02em; display: block; }
.how span { color: var(--slate); }
.form-card { background: var(--white); border: 2px solid var(--ink); border-radius: 18px; padding: 30px; max-width: 760px; margin-top: 30px; }
.field { margin-bottom: 18px; }
.field label, .field legend { display: block; font-family: var(--display); font-weight: 700; font-size: 16px; margin-bottom: 7px; }
.field .tip { font-family: var(--display); font-size: 14px; color: var(--slate); margin: -3px 0 7px; max-width: none; }
.field input[type=text], .field input[type=email], .field textarea, .field select { width: 100%; min-width: 0; font-family: var(--display); font-size: 17px; color: var(--ink); background: var(--chalk); border: 2px solid var(--ink); border-radius: 12px; padding: 13px 15px; }
.field textarea { min-height: 130px; resize: vertical; }
.field input:focus, .field textarea:focus, .field select:focus { outline: 3px solid var(--action); outline-offset: 2px; }
.two { display: grid; grid-template-columns: minmax(0,1fr) minmax(0,1fr); gap: 16px; }
.check { display: grid; grid-template-columns: 26px 1fr; gap: 10px; align-items: start; font-size: 17px; margin-bottom: 12px; }
.check input { width: 22px; height: 22px; margin-top: 3px; accent-color: #0F1B3D; }
@media (max-width: 700px) { .two { grid-template-columns: 1fr; gap: 0; } .form-card { padding: 22px 18px; } }
footer { padding-bottom: 46px; }
"""
lg = head("../", "The Ledger: send us your money story | The Ummah Brief",
          "Send your real money situation, anonymously. Each week we publish one story with every identifying detail removed, and three steps we would take.",
          "https://ummahbrief.com/ledger/", lg_css)
lg += "\n<!-- Ledger stories arrive in Formspree labelled 'Ledger story'. -->\n"
lg += nav("../", '<a class="btn btn-act btn-sm" href="#send">Send</a>')
lg += """
<header class="hero navy" id="top">
  <div class="wrap">
    <h1>The Ledger.</h1>
    <p class="lede">Real money stories from Muslim households, published without names. Send us yours, and we may answer it with the three steps we would take.</p>
  </div>
</header>

<section>
  <div class="wrap">
    <h2>How it works.</h2>
    <ol class="how">
      <li><div><b>You send your situation</b><span>Rough numbers are fine. Nobody sees your name or your email.</span></div></li>
      <li><div><b>We choose one story a week</b><span>We remove anything that could identify you and round your numbers into bands.</span></div></li>
      <li><div><b>We publish it with three steps</b><span>On Instagram and in the Friday email. You get the reply by email first.</span></div></li>
    </ol>
  </div>
</section>

<section class="white" id="send">
  <div class="wrap">
    <h2>Send your story.</h2>
    <p class="lede">Share only what you are comfortable with. Every field marked optional can be left empty.</p>
    <div class="form-card">
      <form data-ok="#lgOk" action="https://formspree.io/f/xnjyanyb" method="POST">
        <input type="hidden" name="source" value="Ledger story">
        <div class="field"><label for="l-email">Your email address</label><p class="tip">So we can send you the reply. It is never published.</p><input id="l-email" type="email" name="email" autocomplete="email" required></div>
        <div class="two">
          <div class="field"><label for="l-country">Country</label><input id="l-country" type="text" name="country" autocomplete="country-name" required></div>
          <div class="field"><label for="l-age">Your age</label><select id="l-age" name="age_band" required><option value="">Choose</option><option>18 to 24</option><option>25 to 34</option><option>35 to 44</option><option>45 to 54</option><option>55 or over</option></select></div>
        </div>
        <div class="field"><label for="l-house">Your household</label><select id="l-house" name="household" required><option value="">Choose</option><option>Single</option><option>Married, no children</option><option>Married, with children</option><option>Single parent</option><option>Supporting parents or relatives</option><option>Other</option></select></div>
        <div class="field"><label for="l-income">Household income each month, roughly (optional)</label><p class="tip">Include the currency. We only ever publish a band, never the figure.</p><input id="l-income" type="text" name="income_monthly"></div>
        <div class="field"><label for="l-debts">What you owe (optional)</label><p class="tip">For example: two credit cards, about 4,000 in total. Car finance, 9,000.</p><textarea id="l-debts" name="debts" style="min-height:96px"></textarea></div>
        <div class="field"><label for="l-story">What is happening, in your own words</label><textarea id="l-story" name="story" required></textarea></div>
        <div class="field"><label for="l-q">The one question you most want answered</label><input id="l-q" type="text" name="question" required></div>
        <label class="check"><input type="checkbox" name="consent_publish" value="yes" required><span>You may publish my story with my name, email and anything that could identify me removed.</span></label>
        <label class="check"><input type="checkbox" name="consent_education" value="yes" required><span>I understand the reply is general education, not personal financial advice and not a religious ruling.</span></label>
        <button type="submit" class="btn btn-act btn-block" style="margin-top:8px">Send my story</button>
        <p class="small" style="margin-top:14px">We cannot reply to every story. See our <a href="../privacy/">privacy notice</a> for how your information is handled.</p>
      </form>
      <div class="ok" id="lgOk" role="status">Your story has been received. JazakAllahu khayran for trusting us with it. If we choose it, you will hear from us by email first.</div>
    </div>
  </div>
</section>
"""
lg += footer("../")
lg += "<script>%s</script>\n</body>\n</html>\n" % FORM_JS
write("ledger/index.html", lg)

# ───────────────────────── THE RIZQ CIRCLE ─────────────────────────
CIRCLE_MONTHS = [
    ("Ramadan", "Purify and plan", "Work out your zakat, plan your sadaqah, and enter the month with your money in order."),
    ("Shawwal", "The freeze", "Stop new riba coming in, and put every debt in the order you will clear it."),
    ("Month 3", "A job for every rand, dollar or pound", "Give each part of your income a purpose before payday."),
    ("Month 4", "The cushion", "Build one month of essentials, so the next surprise is not a crisis."),
    ("Month 5", "Your wasiyyah", "Start your Islamic will, with the Wasiyyah Brief."),
    ("Month 6", "A second door", "Choose one halal income pathway and take the first step."),
    ("Month 7", "Before you invest", "Learn what to check before you put money anywhere, with the Halal Investing Brief."),
    ("Month 8", "Children and money", "Teach giving, saving and contentment at home, with the Raising Children Brief."),
    ("Month 9", "The money talk", "Talk about money with your spouse without a fight, with the Marriage Money Brief."),
    ("Month 10", "Giving with a plan", "Decide your giving before others decide it for you."),
    ("Month 11", "The year in review", "Look back at what grew and what lasted."),
    ("Month 12", "Goals with names", "Hajj, a home, education: give each one a number and a date."),
]
circle_css = """
.hero { padding: 54px 0 70px; overflow: hidden; }
.chero { display: grid; grid-template-columns: minmax(0,1fr) 380px; gap: 56px; align-items: center; }
.hero h1 { font-size: clamp(50px, 10vw, 104px); line-height: 0.9; letter-spacing: -0.05em; }
.hero .lede { margin: 22px 0 26px; max-width: 30em; }
.kick { font-family: var(--display); font-weight: 700; color: #FFD84D; margin-bottom: 12px; }
.emerald { background: #0E6B4F; color: #fff; }
.emerald p, .emerald .lede { color: #E6F5EE; }
.emerald .small { color: #BFE3D2; }
.big-sleeve { width: 100%; transform: rotate(3deg); }
.big-sleeve .ti { font-size: 44px; }
.big-sleeve .ar { font-size: 120px; top: 64px; right: 28px; }
.compare { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 30px; }
.compare > div { border: 2px solid var(--ink); border-radius: 18px; padding: 26px; background: var(--white); }
.compare > div.best { border-color: #0E6B4F; box-shadow: 0 0 0 4px rgba(14,107,79,0.15); }
.compare h3 { font-size: 24px; letter-spacing: -0.025em; }
.compare .amt { font-family: var(--display); font-weight: 800; font-size: 44px; letter-spacing: -0.04em; margin: 8px 0 14px; }
.compare ul { list-style: none; }
.compare li { padding: 9px 0; border-top: 1px solid var(--rule); }
.compare li.no { color: var(--slate); text-decoration: line-through; text-decoration-thickness: 1px; }
.gets { list-style: none; margin-top: 26px; border-top: 3px solid var(--ink); }
.gets li { display: grid; grid-template-columns: 240px 1fr; gap: 24px; padding: 20px 0; border-bottom: 1px solid var(--rule); align-items: baseline; }
.gets b { font-family: var(--display); font-weight: 800; font-size: 22px; letter-spacing: -0.02em; line-height: 1.1; }
.gets span { color: var(--slate); }
.year { display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 14px; margin-top: 28px; }
.year > div { background: var(--white); border-radius: 14px; padding: 18px 18px 16px; border-top: 5px solid #0E6B4F; }
.year .m { font-family: var(--display); font-weight: 700; font-size: 14px; color: var(--slate); }
.year h3 { font-size: 20px; letter-spacing: -0.02em; margin: 4px 0 6px; line-height: 1.1; }
.year p { font-size: 16px; color: var(--slate); margin: 0; }
.flow { list-style: none; counter-reset: s; margin-top: 26px; max-width: 780px; border-top: 3px solid #fff; }
.flow li { counter-increment: s; display: grid; grid-template-columns: 62px 1fr; gap: 14px; padding: 18px 0; border-bottom: 1px solid rgba(255,255,255,0.25); align-items: baseline; }
.flow li::before { content: counter(s); font-family: var(--display); font-weight: 800; font-size: 40px; line-height: 0.9; color: #FFD84D; }
.flow b { font-family: var(--display); font-weight: 700; font-size: 21px; display: block; color: #fff; }
.plans { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 28px; }
.plan { background: var(--white); border: 2px solid var(--ink); border-radius: 18px; padding: 28px; display: flex; flex-direction: column; }
.plan.best { border-color: #0E6B4F; box-shadow: 0 0 0 4px rgba(14,107,79,0.15); }
.plan .tag { font-family: var(--display); font-weight: 700; font-size: 14px; color: #0E6B4F; min-height: 20px; }
.plan h3 { font-size: 26px; letter-spacing: -0.025em; margin-top: 4px; }
.plan .amt { font-family: var(--display); font-weight: 800; font-size: 56px; letter-spacing: -0.05em; line-height: 1; margin: 12px 0 6px; }
.plan .amt span { font-size: 20px; letter-spacing: -0.01em; color: var(--slate); }
.plan ul { list-style: none; margin: 14px 0 22px; flex: 1; }
.plan li { padding: 9px 0; border-top: 1px solid var(--rule); }
.plan .btn { width: 100%; }
.faq { margin-top: 26px; max-width: 800px; border-top: 3px solid var(--ink); }
.faq details { border-bottom: 1px solid var(--rule); padding: 16px 0; }
.faq summary { font-family: var(--display); font-weight: 700; font-size: 20px; cursor: pointer; letter-spacing: -0.015em; }
.faq details p { margin: 10px 0 0; color: var(--slate); max-width: 40em; }
.join { background: var(--white); border: 2px solid var(--ink); border-radius: 18px; padding: 30px; max-width: 760px; margin-top: 26px; }
.join select, .join input[type=email] { width: 100%; font-family: var(--display); font-size: 17px; color: var(--ink); background: var(--chalk); border: 2px solid var(--ink); border-radius: 12px; padding: 13px 15px; margin-bottom: 14px; }
.join label { display: block; font-family: var(--display); font-weight: 700; margin-bottom: 7px; }
@media (max-width: 860px) {
  .chero { grid-template-columns: 1fr; gap: 26px; } .big-sleeve { max-width: 250px; order: -1; } .big-sleeve .ti { font-size: 28px; } .big-sleeve .ar { font-size: 70px; top: 46px; right: 16px; }
  .compare, .plans { grid-template-columns: 1fr; } .gets li { grid-template-columns: 1fr; gap: 6px; } .year { grid-template-columns: 1fr 1fr; } .join { padding: 22px 18px; }
}
@media (max-width: 520px) { .year { grid-template-columns: 1fr; } }
footer { padding-bottom: 46px; }
"""
months_html = "".join('<div><div class="m">%s</div><h3>%s</h3><p>%s</p></div>' % m for m in CIRCLE_MONTHS)
ci = head("../", "The Rizq Circle: every Brief, a money plan every month | The Ummah Brief",
          "For the price of one Brief, every Brief. A money plan every month, answers to your questions, and one membership for your whole household. $9 a month.",
          "https://ummahbrief.com/circle/", circle_css)
ci += """
<!-- EDIT POINTS: when the Circle opens, paste the two Systeme checkout links below.
     While they are empty, every button sends people to the waiting list. -->
"""
ci += nav("../", '<a class="btn btn-act btn-sm js-join" href="#join">Join the list</a>')
ci += """
<header class="hero emerald" id="top">
  <div class="wrap chero">
    <div>
      <p class="kick">Membership from The Ummah Brief</p>
      <h1>The Rizq Circle.</h1>
      <p class="lede">For the price of one Brief, every Brief. A money plan every month, an answer to your questions every month, and a circle of Muslim households working through it with you.</p>
      <a class="btn btn-act js-join" href="#join">Join the waiting list</a>
      <p class="small" style="margin-top:14px">$9 a month, or $79 a year with The Rizq Code included. Cancel anytime.</p>
    </div>
    <div class="sleeve big-sleeve" style="--c:#0A5640;--t:#FFFFFF" aria-hidden="true"><span class="no">Membership</span><span class="ar" lang="ar" style="color:#FFD84D">حلقة</span><span class="ti">The Rizq Circle</span></div>
  </div>
</header>

<section>
  <div class="wrap">
    <h2>For the price of one Brief.</h2>
    <p class="lede">A Brief solves one problem, once. The Circle keeps solving them, month after month.</p>
    <div class="compare">
      <div><h3>One Brief</h3><div class="amt">$9 once</div><ul><li>One audio Brief and its action sheet</li><li class="no">Every other Brief</li><li class="no">A plan every month</li><li class="no">Your questions answered</li><li class="no">Your whole household</li></ul></div>
      <div class="best"><h3>The Rizq Circle</h3><div class="amt">$9 a month</div><ul><li>Every Brief, and each new one</li><li>A money plan every month</li><li>Your questions answered every month</li><li>The member tools</li><li>Your whole household</li></ul></div>
    </div>
  </div>
</section>

<section class="white">
  <div class="wrap">
    <h2>What members get.</h2>
    <ul class="gets">
      <li><b>Every Brief</b><span>The full library of audio Briefs, each with its action sheet and transcript, and every new Brief the day it comes out.</span></li>
      <li><b>The monthly plan</b><span>On the first of each month: one focus, a short audio of about ten minutes, and a four-week checklist. Small enough to finish, big enough to matter.</span></li>
      <li><b>The monthly Ask</b><span>Send us your money questions. Once a month we answer the most common ones in an audio for members. Faith questions are checked with a scholar first.</span></li>
      <li><b>Member tools</b><span>The riba exit tracker, the zakat worksheet and the household budget sheet, ready to fill in.</span></li>
      <li><b>One household, one price</b><span>Your spouse joins on the same membership. Money changes when the whole house is on the same plan.</span></li>
    </ul>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>A year in the Circle.</h2>
    <p class="lede">Twelve months, twelve focuses. Each one builds on the last, and new Briefs arrive alongside them.</p>
    <div class="year">""" + months_html + """</div>
    <p class="small" style="margin-top:16px">Planned focuses. The order may change as new Briefs are released.</p>
  </div>
</section>

<section class="emerald">
  <div class="wrap">
    <h2>How a month works.</h2>
    <ol class="flow">
      <li><div><b>The first of the month</b><span>The month's focus arrives: a short audio and a four-week checklist.</span></div></li>
      <li><div><b>Weeks one to three</b><span>One small task a week. Most take less than half an hour.</span></div></li>
      <li><div><b>Week four</b><span>A check-in, and your chance to send questions for the Ask.</span></div></li>
      <li><div><b>The Ask</b><span>Answers to members' most common questions, in one audio.</span></div></li>
    </ol>
  </div>
</section>

<section class="white" id="plans">
  <div class="wrap">
    <h2>Choose how you pay.</h2>
    <div class="plans">
      <div class="plan"><div class="tag"></div><h3>Monthly</h3><div class="amt">$9<span> a month</span></div><ul><li>Everything in the Circle</li><li>Your whole household</li><li>Cancel anytime</li></ul><a class="btn btn-line js-buy" data-plan="monthly" href="#join">Join monthly</a></div>
      <div class="plan best"><div class="tag">Best value: save $29</div><h3>Yearly</h3><div class="amt">$79<span> a year</span></div><ul><li>Everything in the Circle</li><li>The Rizq Code included, yours to keep ($39 on its own)</li><li>Your whole household</li></ul><a class="btn btn-act js-buy" data-plan="yearly" href="#join">Join yearly</a></div>
    </div>
    <p class="small" style="margin-top:16px">Paid securely through PayPal. Not for you? Email us within 14 days of your first payment for a full refund. Already bought a Brief? Your first month is free.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Questions.</h2>
    <div class="faq">
      <details><summary>Can I cancel?</summary><p>Yes, at any time, from your PayPal account or by emailing salaam@ummahbrief.com. You keep access until the end of the period you paid for.</p></details>
      <details><summary>What happens to the Briefs if I leave?</summary><p>Briefs are part of the membership, so access ends when it ends. If you joined yearly, The Rizq Code is yours to keep.</p></details>
      <details><summary>Is this financial advice?</summary><p>No. Everything in the Circle is general education for Muslim households. It is not personal financial advice and it is not a fatwa. For your own situation, speak to a qualified adviser and a scholar you trust.</p></details>
      <details><summary>Who answers the questions?</summary><p>The Ummah Brief team. Questions about rulings are checked with a scholar before we answer, and we never give a personal ruling.</p></details>
      <details><summary>Is it private?</summary><p>Yes. Your questions are answered without your name, and we never share your details with anyone.</p></details>
      <details><summary>I am not in debt. Is it for me?</summary><p>Yes. Debt is two months of the year. The rest is zakat, a cushion, your will, a second income, children, marriage and giving.</p></details>
    </div>
  </div>
</section>

<section class="white" id="join">
  <div class="wrap">
    <h2>Join the waiting list.</h2>
    <p class="lede">The Circle opens soon. People on the list hear first, and get the first week to join.</p>
    <div class="join">
      <form data-ok="#joinOk" action="https://formspree.io/f/xnjyanyb" method="POST">
        <input type="hidden" name="source" value="Rizq Circle waiting list">
        <input type="hidden" name="plan_interest" id="planInterest" value="">
        <label for="j-email">Your email address</label>
        <input id="j-email" type="email" name="email" autocomplete="email" required>
        <label for="j-help">What would help you most this year?</label>
        <select id="j-help" name="most_help" required><option value="">Choose one</option><option>Getting out of riba debt</option><option>Getting zakat right</option><option>A budget that works</option><option>Starting my Islamic will</option><option>A second halal income</option><option>Money and family</option></select>
        <button type="submit" class="btn btn-act btn-block">Join the waiting list</button>
        <p class="small" style="margin-top:12px">One email when the Circle opens, plus the Friday email. Unsubscribe anytime. <a href="../privacy/">Privacy</a></p>
      </form>
      <div class="ok" id="joinOk" role="status">You are on the list. You will hear first when the Circle opens, insha'Allah.</div>
    </div>
  </div>
</section>
"""
ci += footer("../")
ci += """<script>
// EDIT POINTS: paste the Systeme checkout links here when the Circle opens.
var CIRCLE_MONTHLY_URL = '';
var CIRCLE_YEARLY_URL = '';
(function () {
  var open = CIRCLE_MONTHLY_URL && CIRCLE_YEARLY_URL;
  document.querySelectorAll('.js-buy').forEach(function (a) {
    var url = a.dataset.plan === 'yearly' ? CIRCLE_YEARLY_URL : CIRCLE_MONTHLY_URL;
    if (open) { a.href = url; }
    else { a.addEventListener('click', function () { document.getElementById('planInterest').value = a.dataset.plan; }); }
  });
  if (open) {
    document.querySelectorAll('.js-join').forEach(function (a) { a.href = '#plans'; a.textContent = a.classList.contains('btn-sm') ? 'Join' : 'Join the Circle'; });
    var j = document.getElementById('join'); if (j) j.style.display = 'none';
  }
})();
""" + FORM_JS + "</script>\n</body>\n</html>\n"
write("circle/index.html", ci)

# ───────────────────────── SPONSOR THE NEWSLETTER ─────────────────────────
sp_css = lg_css + """
.std { list-style: none; margin-top: 24px; max-width: 800px; border-top: 3px solid var(--ink); }
.std li { display: grid; grid-template-columns: 34px 1fr; gap: 10px; padding: 14px 0; border-bottom: 1px solid var(--rule); }
.std li::before { content: ''; width: 18px; height: 18px; border-radius: 50%; margin-top: 5px; background: #0E6B4F; }
.std.no li::before { background: #C92F3A; }
.slots { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 26px; max-width: 900px; }
.slots > div { background: var(--white); border: 2px solid var(--ink); border-radius: 18px; padding: 24px; }
.slots h3 { font-size: 22px; letter-spacing: -0.02em; }
.slots p { color: var(--slate); margin: 8px 0 0; }
@media (max-width: 700px) { .slots { grid-template-columns: 1fr; } }
"""
spg = head("../", "Sponsor the Friday email | The Ummah Brief",
           "Reach Muslim households who are working on their money, through one clearly labelled sponsor in The Ummah Brief's Friday email.",
           "https://ummahbrief.com/sponsor/", sp_css)
spg += "\n<!-- Sponsor enquiries arrive in Formspree labelled 'Sponsor enquiry'. -->\n"
spg += nav("../", '<a class="btn btn-act btn-sm" href="#enquire">Enquire</a>')
spg += """
<header class="hero navy" id="top">
  <div class="wrap">
    <h1>Sponsor the Friday email.</h1>
    <p class="lede">Every Friday, Muslim households open one short email from us: a reflection, a real money story and one link. Each issue carries at most one sponsor, clearly labelled, and only one we would be comfortable recommending to our own family.</p>
  </div>
</header>

<section>
  <div class="wrap">
    <h2>Who reads it.</h2>
    <p class="lede">Practising Muslims, mostly working adults with families, who want their money to be halal and in order. They found us through our free tools, our Briefs and The Ledger. We share current subscriber numbers, open rates and clicks with every serious enquiry.</p>
    <p class="lede">Sponsorship opens once the list passes 2,500 readers. Register your interest now and we will contact you then.</p>
  </div>
</section>

<section class="white">
  <div class="wrap">
    <h2>What we say yes to.</h2>
    <ul class="std">
      <li><span>Products and services a Muslim household can use with a clear conscience: books, courses, tools, food, clothing, travel, education.</span></li>
      <li><span>Muslim-owned businesses, especially small ones.</span></li>
      <li><span>Islamic will-writing, charities with transparent accounts, and halal services with independent shariah certification.</span></li>
    </ul>
    <h2 style="margin-top:44px">What we always say no to.</h2>
    <ul class="std no">
      <li><span>Anything built on riba: loans, credit cards, buy now pay later, interest-bearing accounts.</span></li>
      <li><span>Speculation and gambling, including crypto trading schemes and "get rich" offers.</span></li>
      <li><span>Multi-level marketing and income promises.</span></li>
      <li><span>Anything we would not recommend to our own family.</span></li>
    </ul>
    <p class="small" style="margin-top:16px">Financial products are considered only with independent shariah certification and the right regulatory permissions, and may still be declined.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>The two placements.</h2>
    <div class="slots">
      <div><h3>The main sponsor</h3><p>One per issue. A short paragraph in our voice, a link, and the label "Sponsor". Priced per issue, based on the current list size.</p></div>
      <div><h3>The classified</h3><p>Up to two short lines near the end of the email, for small Muslim businesses. A lower price, the same standards.</p></div>
    </div>
    <p class="small" style="margin-top:16px">Rates start from about $25 for every 1,000 subscribers, per issue. We never share readers' details with sponsors, and a sponsor never buys our opinion.</p>
  </div>
</section>

<section class="white" id="enquire">
  <div class="wrap">
    <h2>Enquire.</h2>
    <div class="form-card">
      <form data-ok="#spOk" action="https://formspree.io/f/xnjyanyb" method="POST">
        <input type="hidden" name="source" value="Sponsor enquiry">
        <div class="two">
          <div class="field"><label for="s-name">Your name</label><input id="s-name" type="text" name="name" autocomplete="name" required></div>
          <div class="field"><label for="s-email">Email address</label><input id="s-email" type="email" name="email" autocomplete="email" required></div>
        </div>
        <div class="field"><label for="s-biz">Business and website</label><input id="s-biz" type="text" name="business" required></div>
        <div class="field"><label for="s-what">What you would like to promote</label><textarea id="s-what" name="offer" required></textarea></div>
        <div class="field"><label for="s-cert">Shariah certification, if relevant (optional)</label><input id="s-cert" type="text" name="certification"></div>
        <button type="submit" class="btn btn-act btn-block">Send enquiry</button>
      </form>
      <div class="ok" id="spOk" role="status">Thank you. We reply to every enquiry within five working days.</div>
    </div>
  </div>
</section>
"""
spg += footer("../")
spg += "<script>%s</script>\n</body>\n</html>\n" % FORM_JS
write("sponsor/index.html", spg)

print("pages written")
