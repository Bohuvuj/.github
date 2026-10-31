"""Social preview images (1280x640) for Bohuvuj repositories: og/*.svg, og/*.png.

GitHub shows these when a repository link is shared. Upload each PNG in the
repository's Settings > General > Social preview (GitHub has no API for it).

    python tools/og.py            # SVGs; PNGs are rendered with Playwright
"""
from pathlib import Path
from xml.sax.saxutils import escape

from build import LOGO, MONO, SANS, SERIF, THEMES, lucide

OUT = Path(__file__).resolve().parent.parent / "og"

ITEMS = [
    {"id": "bohuvuj", "title": "Built to ship.", "italic": "Built to last.", "line": "Web platforms, software, mobile apps, and the cloud systems behind them.", "tags": [], "url": "bohuvuj.com", "icon": None, "accent": "red"},
    {"id": "collectra", "title": "Collectra CMS", "line": "Collections and hire-purchase accounts for retail branches, on the web, Android and iPhone.", "tags": ["React", "Supabase", "Capacitor"], "url": "singercms.bohuvuj.com", "icon": "shield-check", "accent": "red"},
    {"id": "autletto", "title": "Autletto", "line": "Your own online store for Facebook and Instagram sellers: stock, bKash and courier booking.", "tags": ["Next.js", "TypeScript"], "url": "autletto.com", "icon": "store", "accent": "gold"},
    {"id": "perfumevault", "title": "Perfume Vault", "line": "A perfume storefront with its own admin and content tools.", "tags": ["Next.js", "Supabase", "Tailwind"], "url": "perfumevaultbd.com", "icon": "spray-can", "accent": "coral"},
    {"id": "subash", "title": "Subash", "line": "A fragrance storefront, from catalogue to checkout.", "tags": ["TypeScript", "React"], "url": "suubas.com", "icon": "flower-2", "accent": "gold"},
    {"id": "beeezee", "title": "BeeEzee", "line": "ERP and CRM for a growing business: sales, stock, people and money.", "tags": ["TypeScript", "PostgreSQL", "Docker"], "url": "beeezee.bohuvuj.com", "icon": "briefcase-business", "accent": "red"},
    {"id": "messmanager", "title": "MessManager", "line": "Meals, groceries and dues for a shared mess: meal rate, ledgers and settlement.", "tags": ["Next.js", "Supabase", "PWA"], "url": "mess.bohuvuj.com", "icon": "utensils-crossed", "accent": "coral"},
    {"id": "bohupay", "title": "BohuPay", "line": "A drop-in payment modal for Bangladeshi gateways, for any website or app.", "tags": ["JavaScript", "Payments"], "url": "bohuvuj.com", "icon": "credit-card", "accent": "gold"},
]


def og(t, it):
    w, h = 1280, 640
    c = t[it["accent"]]
    pills, x = [], 96
    for tag in it["tags"]:
        tw = 28 + len(tag) * 12.5
        pills.append(f'<rect x="{x}" y="470" width="{tw:.0f}" height="44" rx="22" fill="{t["pill"]}"/><text x="{x + tw / 2:.0f}" y="499" class="tag" text-anchor="middle">{escape(tag)}</text>')
        x += tw + 12
    words, lines, cur = it["line"].split(), [], ""
    for wd in words:  # wrap at ~44 characters
        if len(cur) + len(wd) + 1 > 44:
            lines.append(cur)
            cur = wd
        else:
            cur = f"{cur} {wd}".strip()
    lines.append(cur)
    body = "".join(f'<text x="96" y="{350 + i * 44}" class="line">{escape(l)}</text>' for i, l in enumerate(lines[:3]))
    title_y = 270
    title = f'<text x="96" y="{title_y}" class="title">{escape(it["title"])}</text>'
    if it.get("italic"):
        title = (f'<text x="96" y="100" class="by" style="fill:{t["word"]["red"]}">BOHUVUJ SOFTWARES</text>'
                 f'<text x="96" y="210" class="title">{escape(it["title"])}</text>'
                 f'<text x="96" y="310" class="title it">{escape(it["italic"])}</text>')
        body = "".join(f'<text x="96" y="{392 + i * 44}" class="line">{escape(l)}</text>' for i, l in enumerate(lines[:3]))
    mark = (f'<g transform="translate(1040 300)"><path d="M0 -150 L130 -75 V75 L0 150 L-130 75 V-75 Z" fill="{c}" fill-opacity=".08" stroke="{c}" stroke-width="2"/>'
            f'{lucide(it["icon"], c, 120, 1.6)}</g>') if it["icon"] else \
        f'<image href="data:image/png;base64,{LOGO}" x="940" y="170" width="220" height="245"/>'
    small_logo = "" if not it["icon"] else f'<image href="data:image/png;base64,{LOGO}" x="96" y="60" width="44" height="49"/><text x="154" y="94" class="by">Bohuvuj</text>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t['bg1']}"/><stop offset="1" stop-color="{t['bg2']}"/></linearGradient>
    <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="70"/></filter>
    <pattern id="hex" width="34" height="58.9" patternUnits="userSpaceOnUse" patternTransform="scale(1.4)">
      <path d="M17 0 L34 9.8 V29.4 L17 39.3 L0 29.4 V9.8 Z M17 39.3 V58.9" fill="none" stroke="{t['ink']}" stroke-opacity=".05"/>
    </pattern>
  </defs>
  <style>
    .title {{ font: 400 96px {SERIF}; fill: {t['ink']}; letter-spacing: -1.5px; }}
    .it {{ font-style: italic; fill: {t['word']['red']}; }}
    .line {{ font: 400 32px {SANS}; fill: {t['ink2']}; }}
    .tag {{ font: 500 20px {MONO}; fill: {t['ink2']}; }}
    .url {{ font: 600 22px {MONO}; fill: {t['word'][it['accent']]}; letter-spacing: .5px; }}
    .by {{ font: 600 22px {MONO}; fill: {t['ink3']}; letter-spacing: 1px; }}
  </style>
  <rect width="{w}" height="{h}" fill="url(#bg)"/>
  <rect width="{w}" height="{h}" fill="url(#hex)"/>
  <g filter="url(#blur)" opacity="{t['blob']}">
    <ellipse cx="1060" cy="160" rx="260" ry="140" fill="{t['red']}"/>
    <ellipse cx="1180" cy="520" rx="220" ry="130" fill="{t['gold']}"/>
    <ellipse cx="860" cy="560" rx="220" ry="90" fill="{t['coral']}"/>
  </g>
  {mark}
  {small_logo}
  {title}
  {body}
  {''.join(pills)}
  <text x="96" y="{586}" class="url">{escape(it['url'])}</text>
  <rect x="0" y="{h - 8}" width="{w}" height="8" fill="{c}"/>
</svg>
'''


def main():
    OUT.mkdir(exist_ok=True)
    t = THEMES["dark"]
    for it in ITEMS:
        (OUT / f"{it['id']}.svg").write_text(og(t, it), encoding="utf-8")
    print("wrote", len(ITEMS), "svgs to", OUT)


if __name__ == "__main__":
    main()
