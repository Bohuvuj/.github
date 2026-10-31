"""Draws the Bohuvuj organisation profile: profile/assets/*.svg and profile/README.md.

GitHub shows README images through its image proxy: SVG with CSS and SMIL
animation plays; scripts and web fonts do not. So: plain shapes, system
fonts, declarative motion that stops for people who ask for reduced motion.

    python tools/build.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "profile" / "assets"
LOGO = (Path(__file__).resolve().parent / "src" / "bohuvuj-logo.b64").read_text().strip()
# Bump when the artwork changes: GitHub caches images by URL.
V = 2

SANS = "Inter,'Segoe UI Variable Display','Segoe UI',-apple-system,BlinkMacSystemFont,Helvetica,Arial,sans-serif"
SERIF = "'Instrument Serif','Iowan Old Style','Palatino Linotype',Georgia,serif"
MONO = "'JetBrains Mono','Cascadia Code',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
ICONS = Path(__file__).resolve().parent / "src" / "icons"


def lucide(name, color, size=32, width=2.0):
    """A Lucide icon (ISC licence, tools/src/icons) centred on 0,0."""
    raw = (ICONS / f"{name}.svg").read_text(encoding="utf-8")
    inner = raw[raw.index(">", raw.index("<svg")) + 1: raw.rindex("</svg>")].strip()
    k = size / 24
    return (f'<g transform="translate({-size / 2:.1f} {-size / 2:.1f}) scale({k:.4f})" fill="none" stroke="{color}" '
            f'stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round">{inner}</g>')


REDUCED = "@media (prefers-reduced-motion: reduce){*{animation:none!important}}"

# The brand: Bohuvuj red, warm charcoal and paper, a little gold.
THEMES = {
    "dark": {
        "bg1": "#141416", "bg2": "#1d1b20", "ink": "#f2f1ef", "ink2": "#b4b6bd", "ink3": "#7b7e88",
        "red": "#ee4a5e", "coral": "#ff8091", "gold": "#f5c451", "line": "#2a2b30", "card": "#19191c", "pill": "#26262b",
        "word": {"red": "#ff7385", "gold": "#f5c451", "coral": "#ff9aa8"}, "blob": ".5",
    },
    "light": {
        "bg1": "#fbfaf8", "bg2": "#f2f1ef", "ink": "#141416", "ink2": "#4a4d57", "ink3": "#7b7e88",
        "red": "#dd2e44", "coral": "#ff8091", "gold": "#f5c451", "line": "#e4e1dc", "card": "#ffffff", "pill": "#f2f1ef",
        "word": {"red": "#c8263b", "gold": "#8a5d00", "coral": "#b83a52"}, "blob": ".32",
    },
}


def hero(t):
    w, h = 1200, 380
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Bohuvuj, a digital product studio. Built to ship. Built to last.">
  <title>Bohuvuj, digital product studio</title>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t['bg1']}"/><stop offset="1" stop-color="{t['bg2']}"/></linearGradient>
    <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="56"/></filter>
    <clipPath id="frame"><rect width="{w}" height="{h}" rx="24"/></clipPath>
    <pattern id="hex" width="34" height="58.9" patternUnits="userSpaceOnUse" patternTransform="scale(1.2)">
      <path d="M17 0 L34 9.8 V29.4 L17 39.3 L0 29.4 V9.8 Z M17 39.3 V58.9" fill="none" stroke="{t['ink']}" stroke-opacity=".05" stroke-width="1"/>
    </pattern>
  </defs>
  <style>
    .kicker {{ font: 600 15px {MONO}; fill: {t['word']['red']}; letter-spacing: 1.5px; }}
    .title {{ font: 400 70px {SERIF}; fill: {t['ink']}; letter-spacing: -1px; }}
    .title2 {{ font: italic 400 70px {SERIF}; fill: {t['word']['red']}; letter-spacing: -1px; }}
    .sub {{ font: 400 21px {SANS}; fill: {t['ink2']}; }}
    .meta {{ font: 500 14px {MONO}; fill: {t['ink3']}; letter-spacing: .4px; }}
    .drift {{ animation: drift 20s ease-in-out infinite alternate; }}
    @keyframes drift {{ from{{transform:translate(-30px,10px)}} to{{transform:translate(40px,-14px)}} }}
    .spin {{ transform-origin: 1010px 190px; animation: spin 40s linear infinite; }}
    @keyframes spin {{ to{{transform:rotate(360deg)}} }}
    .float {{ animation: float 6s ease-in-out infinite; }}
    @keyframes float {{ 0%,100%{{transform:translateY(0)}} 50%{{transform:translateY(-8px)}} }}
    {REDUCED}
  </style>
  <g clip-path="url(#frame)">
    <rect width="{w}" height="{h}" fill="url(#bg)"/>
    <rect width="{w}" height="{h}" fill="url(#hex)"/>
    <g filter="url(#blur)" opacity="{t['blob']}" class="drift">
      <ellipse cx="980" cy="120" rx="230" ry="120" fill="{t['red']}"/>
      <ellipse cx="1110" cy="300" rx="190" ry="110" fill="{t['gold']}"/>
      <ellipse cx="820" cy="330" rx="200" ry="80" fill="{t['coral']}"/>
    </g>
    <!-- the logo, floating in a slowly turning hexagon -->
    <g class="spin" opacity=".55">
      <path d="M1010 40 L1140 115 V265 L1010 340 L880 265 V115 Z" fill="none" stroke="{t['red']}" stroke-width="1.5" stroke-dasharray="6 10"/>
    </g>
    <g class="float">
      <image href="data:image/png;base64,{LOGO}" x="930" y="100" width="160" height="178" preserveAspectRatio="xMidYMid meet"/>
    </g>
    <text x="80" y="92" class="kicker">BOHUVUJ SOFTWARES</text>
    <text x="80" y="176" class="title">Built to ship.</text>
    <text x="80" y="252" class="title2">Built to last.</text>
    <text x="80" y="300" class="sub">Web platforms, software, mobile apps, and the cloud systems behind them.</text>
    <text x="80" y="342" class="meta">Dhaka, Bangladesh <tspan fill="{t['word']['red']}">/</tspan> bohuvuj.com <tspan fill="{t['word']['red']}">/</tspan> working worldwide</text>
    <rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="24" fill="none" stroke="{t['line']}"/>
  </g>
</svg>
'''


SERVICES = [
    ("web", "Web platforms", ["Dashboards, portals and", "storefronts people use daily."]),
    ("code", "Custom software", ["The internal tools a team", "actually runs on."]),
    ("phone", "Mobile apps", ["Android and iPhone, offline", "first when the field needs it."]),
    ("cloud", "Cloud systems", ["Databases, backups, monitoring:", "the part nobody sees."]),
]


def icon(kind, c):
    return lucide({"web": "globe", "code": "code-xml", "phone": "smartphone", "cloud": "cloud"}[kind], c, 34)


def services(t):
    w, h = 1200, 170
    col = w / 4
    cells = []
    for i, (k, title, lines) in enumerate(SERVICES):
        x = i * col
        c = [t["red"], t["gold"], t["coral"], t["red"]][i]
        sep = f'<path d="M{x:.0f} 34 V136" stroke="{t["line"]}"/>' if i else ""
        body = "".join(f'<text x="{x + 34:.0f}" y="{108 + j * 22}" class="b">{escape(l)}</text>' for j, l in enumerate(lines))
        cells.append(f'{sep}<g transform="translate({x + 54:.0f} 52)"><g class="ic" style="animation-delay:-{i * 1.5}s">{icon(k, c)}</g></g>'
                     f'<text x="{x + 90:.0f}" y="59" class="h">{escape(title)}</text>{body}')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="What we build: web platforms, custom software, mobile apps, cloud systems">
  <title>What we build</title>
  <style>
    .h {{ font: 700 19px {SANS}; fill: {t['ink']}; }}
    .b {{ font: 400 15px {SANS}; fill: {t['ink2']}; }}
    .ic {{ animation: bob 6s ease-in-out infinite; }}
    @keyframes bob {{ 0%,100%{{transform:translate(0,0)}} 50%{{transform:translate(0,-3px)}} }}
    {REDUCED}
  </style>
  <rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="20" fill="{t['card']}" stroke="{t['line']}"/>
  {"".join(cells)}
</svg>
'''


PRODUCTS = [
    {"id": "collectra", "icon": "shield-check", "title": "Collectra CMS", "status": "Live", "accent": "red", "wide": True,
     "lines": ["Collections and hire-purchase accounts for retail branches,", "on the web, Android and iPhone, with offline capture in the field."],
     "tags": ["React", "Supabase", "Capacitor"], "url": "https://singercms.bohuvuj.com/"},
    {"id": "autletto", "icon": "store", "title": "Autletto", "status": "Live", "accent": "gold",
     "lines": ["Own online store for Facebook and Instagram", "sellers: stock, bKash, courier booking."],
     "tags": ["Next.js", "TypeScript", "Payments"], "url": "https://www.autletto.com/"},
    {"id": "perfumevault", "icon": "spray-can", "title": "Perfume Vault", "status": "Live", "accent": "coral",
     "lines": ["A perfume storefront with its own admin", "and content tools."],
     "tags": ["Next.js", "Supabase", "Tailwind"], "url": "https://perfumevaultbd.com/"},
    {"id": "subash", "icon": "flower-2", "title": "Subash", "status": "Live", "accent": "gold",
     "lines": ["A fragrance storefront, from catalogue", "to checkout."],
     "tags": ["TypeScript", "React"], "url": "https://suubas.com/"},
    {"id": "beeezee", "icon": "briefcase-business", "title": "BeeEzee", "status": "Live", "accent": "red",
     "lines": ["ERP and CRM for a growing business:", "sales, stock, people and money."],
     "tags": ["TypeScript", "PostgreSQL", "Docker"], "url": "https://beeezee.bohuvuj.com/"},
]


def card(t, p):
    w, h = (1180 if p.get("wide") else 580), 200
    c = t[p["accent"]]
    pills, x = [], 32
    for tag in p["tags"]:
        tw = 16 + len(tag) * 8.2
        pills.append(f'<rect x="{x}" y="150" width="{tw:.0f}" height="28" rx="14" fill="{t["pill"]}"/><text x="{x + tw / 2:.0f}" y="169" class="tag" text-anchor="middle">{escape(tag)}</text>')
        x += tw + 8
    lines = "".join(f'<text x="32" y="{104 + i * 24}" class="body">{escape(l)}</text>' for i, l in enumerate(p["lines"]))
    dot_x = w - 46 - len(p["status"]) * 6.6
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(p['title'])}: {escape(' '.join(p['lines']))} {escape(p['status'])}.">
  <title>{escape(p['title'])}</title>
  <defs>
    <radialGradient id="glow" cx="1" cy="0" r="1"><stop offset="0" stop-color="{c}" stop-opacity=".22"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></radialGradient>
    <clipPath id="frame"><rect width="{w}" height="{h}" rx="18"/></clipPath>
  </defs>
  <style>
    .title {{ font: 400 34px {SERIF}; fill: {t['ink']}; }}
    .body {{ font: 400 16px {SANS}; fill: {t['ink2']}; }}
    .tag {{ font: 500 13px {MONO}; fill: {t['ink2']}; }}
    .status {{ font: 600 13px {SANS}; fill: {t['word'][p['accent']]}; }}
    .glow {{ animation: breathe 7s ease-in-out infinite; }}
    @keyframes breathe {{ 0%,100%{{opacity:.65}} 50%{{opacity:1}} }}
    .dot {{ animation: ping 2.4s ease-out infinite; transform-origin: center; transform-box: fill-box; }}
    @keyframes ping {{ 0%{{transform:scale(1);opacity:.7}} 80%,100%{{transform:scale(2.6);opacity:0}} }}
    {REDUCED}
  </style>
  <g clip-path="url(#frame)">
    <rect width="{w}" height="{h}" fill="{t['card']}"/>
    <rect width="{w}" height="{h}" fill="url(#glow)" class="glow"/>
    <path d="M{w - 64} 30 L{w - 40} 44 V72 L{w - 64} 86 L{w - 88} 72 V44 Z" fill="{c}" fill-opacity=".1" stroke="{c}" stroke-width="1.5"/>
    <g transform="translate({w - 64} 58)">{lucide(p['icon'], c, 26)}</g>
    <text x="32" y="66" class="title">{escape(p['title'])}</text>
    {lines}
    {''.join(pills)}
    <text x="{w - 32}" y="169" class="status" text-anchor="end">{escape(p['status'])}</text>
    <circle cx="{dot_x:.0f}" cy="164" r="4.5" fill="{c}" class="dot"/>
    <circle cx="{dot_x:.0f}" cy="164" r="4.5" fill="{c}"/>
    <rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="18" fill="none" stroke="{t['line']}"/>
  </g>
</svg>
'''


def footer(t):
    w, h = 1200, 90
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="We cook and eat the codes.">
  <title>We cook and eat the codes.</title>
  <style>
    .t {{ font: italic 400 26px {SERIF}; fill: {t['ink2']}; }}
    .run {{ stroke-dasharray: 80 1200; animation: run 7s linear infinite; }}
    @keyframes run {{ to{{stroke-dashoffset:-1280}} }}
    {REDUCED}
  </style>
  <path d="M0 70 H1200" stroke="{t['line']}"/>
  <path d="M0 70 H1200" stroke="{t['red']}" stroke-width="2" class="run"/>
  <text x="600" y="40" class="t" text-anchor="middle">We cook and eat the codes.</text>
</svg>
'''


def pic(name, alt, width="100%"):
    return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="assets/{name}-dark.svg?v={V}">'
            f'<img alt="{alt}" src="assets/{name}-light.svg?v={V}" width="{width}"></picture>')


def readme():
    cards = "\n".join(f'  <a href="{p["url"]}">{pic("card-" + p["id"], p["title"] + ": " + " ".join(p["lines"]), "100%" if p.get("wide") else "49%")}</a>' for p in PRODUCTS)
    stack = "%2C".join(["ts", "react", "nextjs", "vite", "tailwind", "nodejs", "postgres", "supabase", "prisma", "redis", "docker", "nginx", "cloudflare", "vercel", "githubactions", "flutter"])
    links = [
        ("Website", "https://bohuvuj.com/", "https://cdn.simpleicons.org/googlechrome/8b8e96"),
        ("LinkedIn", "https://www.linkedin.com/company/bohuvuj/", "assets/linkedin.svg"),
        ("Facebook", "https://www.facebook.com/bohuvujsoft", "https://cdn.simpleicons.org/facebook/8b8e96"),
        ("Instagram", "https://www.instagram.com/bohuvujsoft/", "https://cdn.simpleicons.org/instagram/8b8e96"),
        ("Email", "mailto:bohuvujsoft@gmail.com", "https://cdn.simpleicons.org/gmail/8b8e96"),
    ]
    social = "&nbsp;&nbsp;\n".join(f'  <a href="{u}"><img alt="{n}" src="{s}" height="22"></a>' for n, u, s in links)
    return f"""<a href="https://bohuvuj.com/">
  {pic("hero", "Bohuvuj, a digital product studio. Built to ship. Built to last.")}
</a>

<br>

**Bohuvuj** is a digital product studio in Dhaka. We design and engineer web platforms, custom software, mobile apps and the cloud systems underneath them, for teams who intend to still be running what we build in five years.

### What we build

{pic("services", "What we build: web platforms, custom software, mobile apps, cloud systems.")}

### In production

<p>
{cards}
</p>

Also from the studio: **BohuPay**, a drop-in payment modal for Bangladeshi gateways, and **[MessManager](https://mess.bohuvuj.com/)**, meals and dues for a shared mess.

### How we work

- **Built to last.** We pick boring, well-supported tools and write code the next engineer can read.
- **Typed end to end.** TypeScript and a typed database schema, so a change breaks at build time, not in front of a customer.
- **Small, reviewed steps.** Every change goes branch, pull request, review, merge. Nothing goes straight to production.
- **Watched in production.** Health checks, backups and alerts come with the product, not after the first outage.

### Stack

<p>
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i={stack}&theme=dark"><img alt="TypeScript, React, Next.js, Vite, Tailwind, Node.js, PostgreSQL, Supabase, Prisma, Redis, Docker, nginx, Cloudflare, Vercel, GitHub Actions, Flutter" src="https://skillicons.dev/icons?i={stack}&theme=light" height="44"></picture>
</p>

### Work with us

Co-founded by **[Redwan Rashid](https://github.com/Redwan002117)**, our Chief Architect. Tell us what you are building: **[bohuvujsoft@gmail.com](mailto:bohuvujsoft@gmail.com)** or **[bohuvuj.com](https://bohuvuj.com/)**.

<p>
{social}
</p>

{pic("footer", "We cook and eat the codes.")}

<!-- Generated by tools/build.py: edit there, then run python tools/build.py. -->
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for mode, t in THEMES.items():
        (OUT / f"hero-{mode}.svg").write_text(hero(t), encoding="utf-8")
        (OUT / f"services-{mode}.svg").write_text(services(t), encoding="utf-8")
        (OUT / f"footer-{mode}.svg").write_text(footer(t), encoding="utf-8")
        for p in PRODUCTS:
            (OUT / f"card-{p['id']}-{mode}.svg").write_text(card(t, p), encoding="utf-8")
    (OUT / "linkedin.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-label="LinkedIn"><title>LinkedIn</title>'
        '<rect x="1" y="1" width="22" height="22" rx="4" fill="#8b8e96"/><path d="M6.2 9.6h2.6V18H6.2zM7.5 5.5a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3zM10.4 9.6h2.5v1.2c.4-.7 1.3-1.4 2.7-1.4 2.8 0 3.3 1.8 3.3 4.2V18h-2.6v-3.9c0-.9 0-2.2-1.3-2.2s-1.6 1-1.6 2.1v4h-2.6z" fill="#fff"/></svg>',
        encoding="utf-8")
    (ROOT / "profile" / "README.md").write_text(readme(), encoding="utf-8", newline="\n")
    print("wrote", len(list(OUT.glob("*.svg"))), "svgs and profile/README.md")


if __name__ == "__main__":
    main()
