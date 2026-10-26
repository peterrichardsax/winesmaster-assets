import os, zipfile, html

OUT = "/home/claude/wm_anim/svg"
os.makedirs(OUT, exist_ok=True)

W, H = 640, 220
CREAM = "#F6F1EA"
CREAM2 = "#EFE6DA"
BURG = "#6B1F33"
BURG2 = "#8A2E45"
GOLD = "#C9A24A"
INK = "#2B1A1F"
MUTED = "#8C6A72"

CATS = [
    (1, "Appearance", "Colour & Rim", "Tilt. Look at the edge."),
    (2, "Appearance", "Viscosity", "Swirl. Watch the legs."),
    (3, "Aroma", "Aroma", "Three short sniffs."),
    (4, "Taste", "Fruit Profile", "What fruit is at the centre?"),
    (5, "Taste", "Secondary Notes", "Look past the fruit."),
    (6, "Taste", "Body", "Skimmed, whole or cream?"),
    (7, "Taste", "Acidity", "How much does your mouth water?"),
    (8, "Taste", "Dryness", "Sugar, or just ripe fruit?"),
    (9, "Taste", "Oak", "Vanilla, toast, cedar?"),
    (10, "Taste", "Aftertaste", "Swallow and count."),
    (11, "Technical Analysis", "Alcohol", "Feel for the warmth."),
    (12, "Technical Analysis", "Blend or Single", "One voice, or layers?"),
    (13, "Technical Analysis", "Grapes", "Add up the clues."),
    (14, "Technical Analysis", "Old or New World", "Restrained, or ripe and bold?"),
    (15, "Technical Analysis", "Country", "Where is this style made?"),
    (16, "Technical Analysis", "Region", "Narrow it down."),
    (17, "Technical Analysis", "Vintage", "Young and fresh, or developed?"),
    (18, "Technical Analysis", "Rating", "What does it deliver?"),
]

# Shared glass path (centered at 0,0 in a 160x160 box, origin at the bowl centre)
GLASS = """
<g id="glass" fill="none" stroke="{burg}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M-34,-52 L34,-52 C36,-10 18,8 0,10 C-18,8 -36,-10 -34,-52 Z"/>
  <path d="M0,10 L0,48"/>
  <path d="M-22,52 L22,52"/>
</g>"""

def wine_clip(id_):
    return f"""<clipPath id="{id_}"><path d="M-34,-52 L34,-52 C36,-10 18,8 0,10 C-18,8 -36,-10 -34,-52 Z"/></clipPath>"""

def ill_1():
    # Colour & Rim: tilted glass, wine colour cycles pale lemon -> gold -> rose -> ruby, rim glint pulses
    return f"""
<style>
@keyframes hue {{ 0%{{fill:#F3E7A4}} 22%{{fill:#E3B94A}} 40%{{fill:#E9A3B4}} 58%{{fill:#C94D6A}} 78%{{fill:#7A1F3A}} 100%{{fill:#F3E7A4}} }}
@keyframes glint {{ 0%,100%{{opacity:.15}} 50%{{opacity:.9}} }}
.wine{{animation:hue 8s ease-in-out infinite}}
.glint{{animation:glint 2.2s ease-in-out infinite}}
</style>
<defs>{wine_clip('c1')}</defs>
<g transform="rotate(-22)">
  <g clip-path="url(#c1)"><rect class="wine" x="-40" y="-30" width="80" height="50"/></g>
  <ellipse class="glint" cx="0" cy="-30" rx="30" ry="5" fill="none" stroke="white" stroke-width="3"/>
  {GLASS.format(burg=BURG)}
</g>"""

def ill_2():
    # Viscosity: legs running down the inside of the bowl
    legs = ""
    for i, x in enumerate([-18, -6, 6, 18]):
        legs += f'<path class="leg" style="animation-delay:{i*0.45}s" d="M{x},-40 L{x},-8" stroke="{BURG2}" stroke-width="3" stroke-linecap="round"/>'
    return f"""
<style>
@keyframes run {{ 0%{{transform:translateY(-14px);opacity:0}} 20%{{opacity:.9}} 100%{{transform:translateY(26px);opacity:0}} }}
.leg{{animation:run 2.4s ease-in infinite}}
</style>
<defs>{wine_clip('c2')}</defs>
<g clip-path="url(#c2)">
  <rect x="-40" y="-8" width="80" height="30" fill="#A3344F" opacity=".85"/>
  <rect x="-40" y="-52" width="80" height="48" fill="#A3344F" opacity=".12"/>
  {legs}
</g>
{GLASS.format(burg=BURG)}"""

def ill_3():
    # Aroma: scent waves rising from the glass
    waves = ""
    for i, x in enumerate([-16, 0, 16]):
        waves += f'<path class="wave" style="animation-delay:{i*0.6}s" d="M{x},-62 c6,-8 -6,-16 0,-24 c6,-8 -6,-16 0,-24" fill="none" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>'
    return f"""
<style>
@keyframes rise {{ 0%{{transform:translateY(16px);opacity:0}} 30%{{opacity:1}} 100%{{transform:translateY(-22px);opacity:0}} }}
.wave{{animation:rise 2.6s ease-out infinite}}
</style>
<defs>{wine_clip('c3')}</defs>
<g transform="translate(0,22)">
  <g clip-path="url(#c3)"><rect x="-40" y="-14" width="80" height="30" fill="#A3344F" opacity=".85"/></g>
  {GLASS.format(burg=BURG)}
  {waves}
</g>"""

def ill_4():
    # Fruit profile: four fruit dots popping in sequence
    fruits = [("#E9D64C", -42, -10, "lemon"), ("#8FBF5A", -14, -30, "apple"), ("#F2A66B", 14, -10, "peach"), ("#4A1E3A", 42, -30, "berry")]
    dots = ""
    for i, (c, x, y, _n) in enumerate(fruits):
        dots += f'<circle class="pop" style="animation-delay:{i*0.5}s" cx="{x}" cy="{y}" r="16" fill="{c}"/>'
        dots += f'<path class="pop" style="animation-delay:{i*0.5}s" d="M{x},{y-16} q6,-8 12,-10" fill="none" stroke="#5E8B3A" stroke-width="2.5" stroke-linecap="round"/>'
    return f"""
<style>
@keyframes pop {{ 0%,15%{{transform:scale(0);opacity:0}} 30%,70%{{transform:scale(1);opacity:1}} 85%,100%{{transform:scale(0);opacity:0}} }}
.pop{{transform-box:fill-box;transform-origin:center;animation:pop 3.6s ease-in-out infinite}}
</style>
<g transform="translate(0,16)">{dots}
<path d="M-56,26 h112" stroke="{GOLD}" stroke-width="2" stroke-dasharray="3 6" stroke-linecap="round"/></g>"""

def ill_5():
    # Secondary notes: leaf, flower, stone orbiting a glass
    return f"""
<style>
@keyframes orbit {{ from{{transform:rotate(0deg)}} to{{transform:rotate(360deg)}} }}
@keyframes counter {{ from{{transform:rotate(0deg)}} to{{transform:rotate(-360deg)}} }}
.orb{{animation:orbit 9s linear infinite;transform-origin:0 0}}
.item{{animation:counter 9s linear infinite;transform-origin:0 0}}
</style>
<defs>{wine_clip('c5')}</defs>
<g transform="scale(.8) translate(0,8)">
  <g clip-path="url(#c5)"><rect x="-40" y="-14" width="80" height="30" fill="#A3344F" opacity=".85"/></g>
  {GLASS.format(burg=BURG)}
</g>
<g class="orb">
  <g transform="translate(0,-66)"><g class="item"><path d="M0,-10 c10,0 12,14 0,20 c-12,-6 -10,-20 0,-20z" fill="#5E8B3A"/><path d="M0,-6 v14" stroke="#F6F1EA" stroke-width="1.5"/></g></g>
  <g transform="translate(57,33)"><g class="item"><circle r="4" fill="{GOLD}"/><circle cx="0" cy="-8" r="4" fill="#E6B8C5"/><circle cx="7" cy="4" r="4" fill="#E6B8C5"/><circle cx="-7" cy="4" r="4" fill="#E6B8C5"/><circle cx="0" cy="8" r="4" fill="#E6B8C5"/></g></g>
  <g transform="translate(-57,33)"><g class="item"><path d="M-10,4 l6,-12 l12,-2 l6,10 l-8,8 l-12,-1z" fill="#9A9A9A"/></g></g>
</g>"""

def ill_6():
    # Body: glass fill grows from light to full, with a weight label
    return f"""
<style>
@keyframes fill6 {{ 0%,10%{{transform:translateY(34px)}} 45%,55%{{transform:translateY(0)}} 90%,100%{{transform:translateY(34px)}} }}
@keyframes op6 {{ 0%,10%{{opacity:.35}} 45%,55%{{opacity:.95}} 90%,100%{{opacity:.35}} }}
.body{{animation:fill6 5s ease-in-out infinite, op6 5s ease-in-out infinite}}
</style>
<defs>{wine_clip('c6')}</defs>
<g transform="translate(0,6)">
  <g clip-path="url(#c6)"><rect class="body" x="-40" y="-36" width="80" height="60" fill="#A3344F"/></g>
  {GLASS.format(burg=BURG)}
</g>
<text x="-62" y="60" font-family="Georgia, serif" font-size="12" fill="{MUTED}">light</text>
<text x="40" y="60" font-family="Georgia, serif" font-size="12" fill="{MUTED}">full</text>"""

def ill_7():
    # Acidity: a lemon slice with zing sparks pulsing
    sparks = ""
    for i, a in enumerate([20, 70, 120, 200, 250, 300]):
        sparks += f'<g transform="rotate({a})"><path class="spark" style="animation-delay:{i*0.25}s" d="M0,-46 l0,-14" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/></g>'
    return f"""
<style>
@keyframes zing {{ 0%,100%{{opacity:.1;transform:scale(.9)}} 50%{{opacity:1;transform:scale(1.08)}} }}
.spark{{transform-origin:0 0;animation:zing 1.6s ease-in-out infinite}}
@keyframes drip {{ 0%{{transform:translateY(0);opacity:0}} 30%{{opacity:1}} 100%{{transform:translateY(40px);opacity:0}} }}
.drop{{animation:drip 2.2s ease-in infinite}}
</style>
<g>
  <circle r="36" fill="#F3D95B" stroke="#E2BE2F" stroke-width="4"/>
  <circle r="28" fill="#FBF1B0"/>
  <g stroke="#E2BE2F" stroke-width="2">
    <path d="M0,-28 v56"/><path d="M-28,0 h56"/><path d="M-20,-20 l40,40"/><path d="M20,-20 l-40,40"/>
  </g>
  {sparks}
  <path class="drop" d="M30,36 c6,8 6,14 0,16 c-6,-2 -6,-8 0,-16z" fill="#7FB5D6"/>
</g>"""

def ill_8():
    # Dryness: slider from Dry to Sweet, knob sliding, sugar cube fading in on the sweet side
    return f"""
<style>
@keyframes slide {{ 0%,15%{{transform:translateX(-60px)}} 45%,60%{{transform:translateX(60px)}} 90%,100%{{transform:translateX(-60px)}} }}
@keyframes cube {{ 0%,20%{{opacity:.15}} 45%,60%{{opacity:1}} 90%,100%{{opacity:.15}} }}
.knob{{animation:slide 5s ease-in-out infinite}}
.cube{{animation:cube 5s ease-in-out infinite}}
</style>
<rect x="-70" y="-4" width="140" height="8" rx="4" fill="{CREAM2}" stroke="{BURG}" stroke-width="1.5"/>
<circle class="knob" r="12" fill="{BURG}" stroke="{CREAM}" stroke-width="3"/>
<text x="-70" y="30" font-family="Georgia, serif" font-size="13" fill="{INK}">Dry</text>
<text x="40" y="30" font-family="Georgia, serif" font-size="13" fill="{INK}">Sweet</text>
<g class="cube" transform="translate(56,-40)"><rect x="-11" y="-11" width="22" height="22" rx="3" fill="white" stroke="{MUTED}" stroke-width="1.5"/><path d="M-11,-11 l6,-6 h22 l-6,6z M11,-11 l6,-6 v22 l-6,6z" fill="{CREAM2}" stroke="{MUTED}" stroke-width="1.5"/></g>"""

def ill_9():
    # Oak: barrel with vanilla wisps rising
    wisps = ""
    for i, x in enumerate([-14, 2, 18]):
        wisps += f'<path class="wisp" style="animation-delay:{i*0.7}s" d="M{x},-52 c5,-6 -5,-12 0,-18 c5,-6 -5,-12 0,-18" fill="none" stroke="{GOLD}" stroke-width="2.5" stroke-linecap="round"/>'
    return f"""
<style>
@keyframes rise9 {{ 0%{{transform:translateY(12px);opacity:0}} 30%{{opacity:.9}} 100%{{transform:translateY(-18px);opacity:0}} }}
.wisp{{animation:rise9 2.8s ease-out infinite}}
</style>
<g transform="translate(0,12)">
  <path d="M-36,-44 c-6,30 -6,58 0,88 h72 c6,-30 6,-58 0,-88z" fill="#B9834A" stroke="#7A4E25" stroke-width="3"/>
  <g stroke="#7A4E25" stroke-width="2" opacity=".6"><path d="M-18,-44 c-3,30 -3,58 0,88"/><path d="M0,-44 v88"/><path d="M18,-44 c3,30 3,58 0,88"/></g>
  <g fill="none" stroke="#4A3A2A" stroke-width="5"><path d="M-38,-26 h76"/><path d="M-39,26 h78"/></g>
</g>
{wisps}"""

def ill_10():
    # Aftertaste: stopwatch hand sweeping, a flavour tail that extends then fades
    return f"""
<style>
@keyframes sweep {{ from{{transform:rotate(0deg)}} to{{transform:rotate(360deg)}} }}
.hand{{animation:sweep 4s linear infinite;transform-origin:0 0}}
@keyframes tail {{ 0%{{stroke-dashoffset:120;opacity:1}} 60%{{stroke-dashoffset:0;opacity:1}} 100%{{stroke-dashoffset:0;opacity:0}} }}
.tail{{stroke-dasharray:120;animation:tail 4s ease-out infinite}}
</style>
<g transform="translate(0,-6)">
  <circle r="40" fill="white" stroke="{BURG}" stroke-width="3"/>
  <path d="M0,-40 v-10 M-8,-50 h16" stroke="{BURG}" stroke-width="3" stroke-linecap="round"/>
  <g stroke="{MUTED}" stroke-width="2"><path d="M0,-32 v6"/><path d="M32,0 h-6"/><path d="M0,32 v-6"/><path d="M-32,0 h6"/></g>
  <path class="hand" d="M0,0 L0,-28" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>
  <circle r="4" fill="{BURG}"/>
</g>
<path class="tail" d="M-44,62 h88" stroke="#A3344F" stroke-width="6" stroke-linecap="round"/>"""

def ill_11():
    # Alcohol: thermometer with level rising, % label
    return f"""
<style>
@keyframes merc {{ 0%,10%{{transform:scaleY(.25)}} 50%,60%{{transform:scaleY(1)}} 90%,100%{{transform:scaleY(.25)}} }}
.merc{{transform-box:fill-box;transform-origin:bottom;animation:merc 5s ease-in-out infinite}}
@keyframes warm {{ 0%,10%{{opacity:.2}} 50%,60%{{opacity:1}} 90%,100%{{opacity:.2}} }}
.warm{{animation:warm 5s ease-in-out infinite}}
</style>
<g transform="translate(-10,0)">
  <rect x="-12" y="-62" width="24" height="104" rx="12" fill="white" stroke="{BURG}" stroke-width="3"/>
  <rect class="merc" x="-6" y="-52" width="12" height="80" rx="6" fill="#A3344F"/>
  <circle cy="46" r="18" fill="#A3344F" stroke="{BURG}" stroke-width="3"/>
  <g stroke="{MUTED}" stroke-width="2"><path d="M14,-40 h8"/><path d="M14,-20 h8"/><path d="M14,0 h8"/><path d="M14,20 h8"/></g>
</g>
<text class="warm" x="40" y="-14" font-family="Georgia, serif" font-size="22" font-weight="bold" fill="{BURG}">%</text>
<g class="warm" transform="translate(50,22)"><path d="M0,0 c4,-8 -4,-14 0,-22 c4,-8 -4,-14 0,-22" fill="none" stroke="{GOLD}" stroke-width="2.5" stroke-linecap="round"/></g>"""

def ill_12():
    # Blend or single: one circle, then three circles converge and overlap
    return f"""
<style>
@keyframes left {{ 0%,15%{{transform:translateX(0)}} 50%,65%{{transform:translateX(34px)}} 100%{{transform:translateX(0)}} }}
@keyframes right {{ 0%,15%{{transform:translateX(0)}} 50%,65%{{transform:translateX(-34px)}} 100%{{transform:translateX(0)}} }}
.l{{animation:left 5s ease-in-out infinite}}
.r{{animation:right 5s ease-in-out infinite}}
</style>
<g opacity=".85">
  <circle class="l" cx="-52" cy="0" r="30" fill="#A3344F"/>
  <circle class="r" cx="52" cy="0" r="30" fill="{GOLD}"/>
  <circle cx="0" cy="0" r="30" fill="#4A1E3A"/>
</g>"""

def ill_13():
    # Grapes: bunch filling in one by one
    pos = [(0,-44),(-14,-30),(14,-30),(-28,-16),(0,-16),(28,-16),(-14,-2),(14,-2),(-28,12),(0,12),(28,12),(-14,26),(14,26),(0,40)]
    dots = ""
    for i, (x, y) in enumerate(pos):
        dots += f'<circle class="g" style="animation-delay:{i*0.18}s" cx="{x}" cy="{y}" r="9" fill="#5B2A52" stroke="{CREAM}" stroke-width="1.5"/>'
    return f"""
<style>
@keyframes fillg {{ 0%{{opacity:.12;transform:scale(.6)}} 20%,75%{{opacity:1;transform:scale(1)}} 100%{{opacity:.12;transform:scale(.6)}} }}
.g{{transform-box:fill-box;transform-origin:center;animation:fillg 4.5s ease-in-out infinite}}
</style>
<g transform="translate(0,4)">
  <path d="M0,-52 c0,-10 6,-16 14,-18" fill="none" stroke="#5E8B3A" stroke-width="3" stroke-linecap="round"/>
  <path d="M2,-56 c10,-14 26,-12 30,-2 c-12,4 -24,4 -30,2z" fill="#6FA14A"/>
  {dots}
</g>"""

def ill_14():
    # Old or New World: globe with rotating meridians
    return f"""
<style>
@keyframes spin {{ from{{transform:translateX(-40px)}} to{{transform:translateX(40px)}} }}
.m{{animation:spin 6s linear infinite}}
</style>
<defs><clipPath id="c14"><circle r="44"/></clipPath></defs>
<circle r="44" fill="#DDE9F2" stroke="{BURG}" stroke-width="3"/>
<g clip-path="url(#c14)" fill="none" stroke="{BURG2}" stroke-width="2" opacity=".7">
  <g class="m">
    <ellipse rx="16" ry="44"/><ellipse cx="-40" rx="16" ry="44"/><ellipse cx="40" rx="16" ry="44"/><ellipse cx="-80" rx="16" ry="44"/><ellipse cx="80" rx="16" ry="44"/>
    <path d="M-120,-22 h240 M-120,22 h240"/>
  </g>
</g>
<g clip-path="url(#c14)" fill="#8FB58A" opacity=".9">
  <g class="m"><path d="M-30,-20 c10,-8 20,-2 18,10 c-2,8 -14,10 -20,2z"/><path d="M20,-6 c8,-10 22,-6 20,8 c-4,10 -18,8 -20,-8z"/><path d="M-70,10 c8,-8 18,-2 14,8 c-4,6 -14,6 -14,-8z"/><path d="M70,-24 c8,-8 18,-2 14,8 c-4,6 -14,6 -14,-8z"/></g>
</g>
<circle r="44" fill="none" stroke="{BURG}" stroke-width="3"/>"""

def ill_15():
    # Country: map pin dropping with ripple
    return f"""
<style>
@keyframes drop {{ 0%{{transform:translateY(-70px);opacity:0}} 35%{{transform:translateY(0);opacity:1}} 45%{{transform:translateY(-10px)}} 55%,85%{{transform:translateY(0)}} 100%{{transform:translateY(0);opacity:0}} }}
.pin{{animation:drop 4s ease-out infinite}}
@keyframes ripple {{ 0%,35%{{transform:scale(.2);opacity:0}} 50%{{opacity:.8}} 100%{{transform:scale(1.6);opacity:0}} }}
.rip{{transform-box:fill-box;transform-origin:center;animation:ripple 4s ease-out infinite}}
</style>
<g transform="scale(.82) translate(0,-6)">
<path d="M-70,50 c20,-30 50,-30 70,-10 c20,-20 50,-20 70,10 l-10,20 h-120z" fill="{CREAM2}" stroke="{MUTED}" stroke-width="2"/>
<ellipse class="rip" cx="0" cy="40" rx="30" ry="10" fill="none" stroke="{GOLD}" stroke-width="3"/>
<g class="pin"><path d="M0,40 c-22,-24 -26,-34 -26,-46 a26,26 0 0 1 52,0 c0,12 -4,22 -26,46z" fill="{BURG}"/><circle cy="-6" r="10" fill="{CREAM}"/></g>
</g>"""

def ill_16():
    # Region: focusing rings closing in on a point
    rings = ""
    for i, r in enumerate([70, 52, 34]):
        rings += f'<circle class="ring" style="animation-delay:{i*0.5}s" r="{r}" fill="none" stroke="{BURG2}" stroke-width="2.5"/>'
    return f"""
<style>
@keyframes focus {{ 0%{{transform:scale(1.4);opacity:0}} 40%{{opacity:.9}} 100%{{transform:scale(.3);opacity:0}} }}
.ring{{transform-origin:0 0;animation:focus 3s ease-in infinite}}
</style>
<g transform="scale(.62)">
<path d="M-80,-30 l40,-20 l50,14 l40,-10 l30,26 l-20,40 l-60,10 l-50,-14 l-40,-20z" fill="{CREAM2}" stroke="{MUTED}" stroke-width="2"/>
{rings}
<circle r="9" fill="{GOLD}" stroke="{BURG}" stroke-width="2.5"/>
</g>"""

def ill_17():
    # Vintage: years cycling, calendar frame
    years = ["2018", "2020", "2022", "2024"]
    txt = ""
    for i, y in enumerate(years):
        txt += f'<text class="yr" style="animation-delay:{i*1.25}s" x="0" y="18" text-anchor="middle" font-family="Georgia, serif" font-size="34" font-weight="bold" fill="{BURG}">{y}</text>'
    return f"""
<style>
@keyframes yr {{ 0%{{opacity:0;transform:translateY(10px)}} 8%,20%{{opacity:1;transform:translateY(0)}} 28%,100%{{opacity:0;transform:translateY(-10px)}} }}
.yr{{animation:yr 5s ease-in-out infinite;opacity:0}}
</style>
<rect x="-56" y="-46" width="112" height="96" rx="10" fill="white" stroke="{BURG}" stroke-width="3"/>
<rect x="-56" y="-46" width="112" height="26" rx="10" fill="{BURG}"/>
<rect x="-56" y="-30" width="112" height="10" fill="{BURG}"/>
<g stroke="{CREAM}" stroke-width="4" stroke-linecap="round"><path d="M-30,-54 v16"/><path d="M30,-54 v16"/></g>
{txt}"""

def ill_18():
    # Rating: five stars filling gold one by one
    star = "M0,-16 L4.7,-5.5 L16,-4.9 L7.6,2.8 L9.9,14 L0,8.3 L-9.9,14 L-7.6,2.8 L-16,-4.9 L-4.7,-5.5 Z"
    stars = ""
    for i, x in enumerate([-72, -36, 0, 36, 72]):
        stars += f'<g transform="translate({x},0)"><path d="{star}" fill="none" stroke="{GOLD}" stroke-width="2"/><path class="s" style="animation-delay:{i*0.4}s" d="{star}" fill="{GOLD}"/></g>'
    return f"""
<style>
@keyframes star {{ 0%{{opacity:0;transform:scale(.4)}} 15%,70%{{opacity:1;transform:scale(1)}} 85%,100%{{opacity:0;transform:scale(.4)}} }}
.s{{transform-box:fill-box;transform-origin:center;animation:star 4.5s ease-in-out infinite}}
</style>
<g transform="translate(0,-4) scale(.92)">{stars}</g>
<text x="0" y="52" text-anchor="middle" font-family="Georgia, serif" font-size="13" fill="{MUTED}">out of 5</text>"""

ILLS = {1: ill_1, 2: ill_2, 3: ill_3, 4: ill_4, 5: ill_5, 6: ill_6, 7: ill_7, 8: ill_8, 9: ill_9, 10: ill_10,
        11: ill_11, 12: ill_12, 13: ill_13, 14: ill_14, 15: ill_15, 16: ill_16, 17: ill_17, 18: ill_18}

def card(num, group, title, cue):
    ill = ILLS[num]()
    t = html.escape(title)
    g = html.escape(group.upper())
    c = html.escape(cue)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{t}">
<style>
@keyframes fadeUp {{ from{{opacity:0;transform:translateY(8px)}} to{{opacity:1;transform:translateY(0)}} }}
.t1{{animation:fadeUp .8s ease-out both}}
.t2{{animation:fadeUp .8s .25s ease-out both}}
.t3{{animation:fadeUp .8s .5s ease-out both}}
@keyframes rule {{ from{{stroke-dashoffset:120}} to{{stroke-dashoffset:0}} }}
.rule{{stroke-dasharray:120;animation:rule 1.2s .4s ease-out both}}
</style>
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{CREAM}"/><stop offset="1" stop-color="{CREAM2}"/></linearGradient>
  <radialGradient id="halo" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="white" stop-opacity=".9"/><stop offset="1" stop-color="white" stop-opacity="0"/></radialGradient>
</defs>
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<rect x="0" y="0" width="8" height="{H}" fill="{BURG}"/>
<circle cx="150" cy="110" r="96" fill="url(#halo)"/>
<circle cx="150" cy="110" r="84" fill="white" stroke="{GOLD}" stroke-width="1.5" opacity=".9"/>
<g transform="translate(150,110)">{ill}</g>
<g transform="translate(292,0)">
  <text class="t1" x="0" y="66" font-family="Helvetica, Arial, sans-serif" font-size="13" letter-spacing="3" fill="{MUTED}">{g}</text>
  <text class="t2" x="0" y="112" font-family="Georgia, 'Times New Roman', serif" font-size="38" font-weight="bold" fill="{INK}">{t}</text>
  <path class="rule" d="M0,128 h120" stroke="{GOLD}" stroke-width="2" stroke-linecap="round"/>
  <text class="t3" x="0" y="160" font-family="Georgia, 'Times New Roman', serif" font-style="italic" font-size="18" fill="{BURG}">{c}</text>
  <text x="0" y="196" font-family="Helvetica, Arial, sans-serif" font-size="11" letter-spacing="2" fill="{MUTED}">QUESTION {num} OF 18</text>
</g>
</svg>"""

files = []
for num, group, title, cue in CATS:
    slug = title.lower().replace(" & ", "-").replace(" ", "-")
    fn = f"{num:02d}-{slug}.svg"
    path = os.path.join(OUT, fn)
    with open(path, "w") as f:
        f.write(card(num, group, title, cue))
    files.append((num, group, title, fn))

# preview page with inline SVGs
cards_html = ""
for num, group, title, fn in files:
    svg = open(os.path.join(OUT, fn)).read()
    cards_html += f'<figure><div class="card">{svg}</div><figcaption>{num:02d} {html.escape(title)} <span>{fn}</span></figcaption></figure>\n'

preview = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wines Master section headers</title>
<style>
body{{margin:0;background:#2B1A1F;color:#F6F1EA;font-family:Georgia,serif;padding:24px 16px}}
h1{{font-size:22px;font-weight:normal;margin:0 0 4px}}
p{{margin:0 0 20px;color:#C9A24A;font-size:14px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:18px}}
figure{{margin:0}}
.card{{border-radius:14px;overflow:hidden;box-shadow:0 8px 24px rgba(0,0,0,.35)}}
.card svg{{display:block;width:100%;height:auto}}
figcaption{{font-size:13px;margin-top:8px;color:#E6D8C8}}
figcaption span{{color:#8C6A72;font-family:monospace;font-size:11px;margin-left:8px}}
</style></head><body>
<h1>Wines Master: animated section headers</h1>
<p>18 SVG cards, 640 x 220, each a few KB. They animate inside a normal image tag.</p>
<div class="grid">{cards_html}</div>
</body></html>"""
open("/home/claude/wm_anim/preview.html", "w").write(preview)

with zipfile.ZipFile("/home/claude/wm_anim/wines-master-section-headers.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for num, group, title, fn in files:
        z.write(os.path.join(OUT, fn), arcname=f"section-headers/{fn}")
sizes = {fn: os.path.getsize(os.path.join(OUT, fn)) for _, _, _, fn in files}
print(len(files), "cards;", "max bytes", max(sizes.values()), "total", sum(sizes.values()))
