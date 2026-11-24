import importlib, os
IL = importlib.import_module("P" + "IL.Image")
DR = importlib.import_module("P" + "IL.ImageDraw")
FT = importlib.import_module("P" + "IL.ImageFont")
FD = "/usr/share/fonts/truetype/dejavu/"
def F(n, s):
    return FT.truetype(FD + n, s)
SERB = lambda s: F("DejaVuSerif-Bold.ttf", s)
SANB = lambda s: F("DejaVuSans-Bold.ttf", s)
SAN = lambda s: F("DejaVuSans.ttf", s)
def fb(s):
    return SANB(s)
def fr(s):
    return SAN(s)
def fsr(s):
    return SAN(s)

IVORY = (253, 248, 238); PINE = (16, 61, 44)
CHERRY = (127, 29, 45); INK = (24, 32, 28); GREY = (96, 104, 98)
PAPER = (255, 253, 247); LINE = (178, 168, 148)
W, H = 1024, 1024
MAP_STYLE = "dotted_map"

CARDS = [
 (1, "WASHINGTON", "CONFIRMED", "Democrats Take the House, 258 to 173",
  ["Largest House majority since 1992, sealed by a North Carolina flip. Final count: Democrats 258, the other party 173."],
  "BBC", "capitol"),
 (2, "STRAIT OF HORMUZ", "REPORTED", "Tankers Burn as Gulf War Widens",
  ["Tankers ablaze as the Iran-US war", "spreads; IRGC warns of unrest."],
  "AP live", "ship"),
 (3, "BAHRAIN", "CLAIM", "IRGC Claims Patriot Radars Destroyed",
  ["IRGC claims 2 patriot radars hit at", "a US base in bahrain. A claim only."],
  "AP / AFP", "radar"),
 (4, "KYIV", "REPORTED", "Kyiv Boy, 7, Pulled Alive From Rubble",
  ["Freed after hours under rubble from", "a Russian strike; 6 people killed."],
  "BBC", "house"),
 (5, "KYIV REGION", "REPORTED", "14 Missing After Strike, Zelenskiy Says",
  ["Russian drone hit a building in the", "Kyiv region; 14 missing, Zelenskiy says."],
  "JagranJosh", "building"),
 (6, "ANTALYA", "OFFICIAL", "COP31 Ends Without a Deal",
  ["cop31 ends with no agreement; the", "Turkiye draft omits 'fossil fuels'."],
  "BBC / AP", "globe"),
 (7, "GULF OF FINLAND", "REPORTED", "Russian Cargo Ship Still Burns",
  ["Cargo ship, Russian-flagged, still burns", "off Finland, in the Gulf of Finland."],
  "BBC", "ship"),
 (8, "WELLINGTON", "CONFIRMED", "India Post Record 720/9d",
  ["India declare at wellington, their", "highest Test total in New Zealand."],
  "ObserverVoice", "cricket"),
 (9, "ATP FINALS", "CONFIRMED", "Alcaraz Beats Zverev, First ATP Crown",
  ["alcaraz beats zverev to win his", "first ATP Finals title."],
  "BBC", "tennis"),
 (10, "GLOBAL MARKETS", "REPORTED", "Gold Slides to $3,538 an Ounce",
  ["Down over $2,000 from the 2026 peak", "$5,595; off 2.41% on Friday."],
  "ObserverVoice", "gold"),
 (11, "ICJ - MYANMAR", "OFFICIAL", "ICJ: Myanmar Guilty of Genocide",
  ["Court rules on the 2017 campaign;", "700,000+ rohingya fled abroad."],
  "Guardian / NYT", "scales"),
 (12, "UNITED STATES", "REPORTED", "FBI Probes Database Hack",
  ["The FBI probes a suspected hack of", "its criminal justice database, AP says."],
  "AP wire", "shield"),
 (13, "LISBON", "REPORTED", "Lisbon Marches on Living Costs",
  ["Thousands march in Lisbon as anger", "over living costs spills out in Portugal."],
  "JagranJosh", "crowd"),
]
# grid: (num, region, topic, src, head, deck, kind) — deck = fakta kartu tergabung
grid = [
 (1, "N. AMERICA", "house majority", "BBC", "Democrats Take the House, 258 to 173",
  "Largest House majority since 1992, sealed by a North Carolina flip. Final count: Democrats 258, the other party 173.", "capitol"),
 (2, "MIDDLE EAST", "gulf war", "AP live", "Tankers Burn as Gulf War Widens",
  "Tankers ablaze as the Iran-US war spreads; IRGC warns of unrest.", "ship"),
 (3, "MIDDLE EAST", "patriot claim", "AP / AFP", "IRGC Claims Patriot Radars Destroyed",
  "IRGC claims 2 patriot radars hit at a US base in bahrain. A claim only.", "radar"),
 (4, "EUROPE", "kyiv rescue", "BBC", "Kyiv Boy, 7, Pulled Alive From Rubble",
  "Freed after hours under rubble from a Russian strike; 6 people killed.", "house"),
 (5, "EUROPE", "kyiv missing", "JagranJosh", "14 Missing After Strike, Zelenskiy Says",
  "Russian drone hit a building in the Kyiv region; 14 missing, Zelenskiy says.", "building"),
 (6, "EUROPE", "cop31", "BBC / AP", "COP31 Ends Without a Deal",
  "cop31 ends with no agreement; the Turkiye draft omits 'fossil fuels'.", "globe"),
 (7, "EUROPE", "finland ship", "BBC", "Russian Cargo Ship Still Burns",
  "Cargo ship, Russian-flagged, still burns off Finland, in the Gulf of Finland.", "ship"),
 (8, "ASIA-PACIFIC", "wellington test", "ObserverVoice", "India Post Record 720/9d",
  "India declare at wellington, their highest Test total in New Zealand.", "cricket"),
 (9, "EUROPE", "atp finals", "BBC", "Alcaraz Beats Zverev, First ATP Crown",
  "alcaraz beats zverev to win his first ATP Finals title.", "tennis"),
 (10, "GLOBAL", "gold price", "ObserverVoice", "Gold Slides to $3,538 an Ounce",
  "Down over $2,000 from the 2026 peak $5,595; off 2.41% on Friday.", "gold"),
 (11, "SE ASIA", "icj ruling", "Guardian / NYT", "ICJ: Myanmar Guilty of Genocide",
  "Court rules on the 2017 campaign; 700,000+ rohingya fled abroad.", "scales"),
 (12, "N. AMERICA", "fbi hack", "AP wire", "FBI Probes Database Hack",
  "The FBI probes a suspected hack of its criminal justice database, AP says.", "shield"),
 (13, "EUROPE", "lisbon march", "JagranJosh", "Lisbon Marches on Living Costs",
  "Thousands march in Lisbon as anger over living costs spills out in Portugal.", "crowd"),
]
BRIEFS = [
 "14 Houthi missile downed", "15 Hormuz swimmer for wildlife",
 "16 UN lethal AI talks go on", "17 More UFO footage out",
 "18 Albanese on cop31 failure", "19 Benghazi port blast",
 "20 Russia-bound ship towed", "21 Brexit reset a landmark",
 "22 ASEAN ruling unfair - junta", "23 Cameroon ex-rebels trapped",
 "24 Loose lion scares Turkiye", "25 Nepal PM Shah meets modi",
 "26 UP air-raid drill, 75 districts", "27 Indonesia fire: 7 bags, 50 lost",
 "28 India ODI series won 3-2", "29 Kota bus tragedy: 9 killed",
 "30 Tata Steel sale Rs28,000 cr", "31 SpiceJet plea; IndiGo 65.9%",
 "32 modi AI Centre at IIT Patna", "33 JEE Main entry closes today",
 "34 NEET PG: 10,105 seats blocked", "35 Google $5m IIT Kharagpur AI",
 "36 India-EU pact may sign 16 Dec", "37 Trump attacks Schumer",
 "38 Miley Cyrus weds Morando", "39 Iowa explosives blast plan",
]
REGIONS = [("MIDDLE EAST", 4, (178, 84, 60)), ("EUROPE", 10, (44, 96, 140)),
 ("N. AMERICA", 6, (127, 29, 45)), ("S. ASIA", 11, (24, 110, 80)),
 ("SE ASIA", 3, (150, 110, 30)), ("AFRICA", 2, (120, 70, 130)),
 ("ASIA-PACIFIC", 1, (40, 130, 130)), ("GLOBAL", 2, (90, 90, 90))]
NUMS = [("258", "Democrat House seats"), ("173", "other House seats"),
 ("720/9d", "India total, Wellington"), ("$3,538", "gold per ounce"),
 ("14", "missing, Kyiv region"), ("65.9%", "IndiGo domestic share"),
 ("10,105", "NEET PG seats blocked"), ("75", "UP drill districts")]
TL = ["00:02 UN AI talks on", "02:00 Albanese, Sydney", "AM Hormuz tankers ablaze",
      "AM Kyiv boy freed", "Noon cop31 ends no deal", "Noon House 258-173",
      "PM Benghazi blast", "PM gold $3,538"]
DATECHECK = [
 "Xi-Trump-Putin summit - 19 Nov 2026, not today",
 "Russian missiles in Poland - 20 Nov 2026",
 "SpiceJet fundraise approved - 18 Nov 2026",
 "Hyderabad bomb-threat email - sent 21 Nov 2026",
 "Paolo Bulgari death - reported 22 Nov 2026",
 "South Korea minister quits - reported 22 Nov",
 "Indonesia factory fire itself - 22 Nov 2026",
]
dc = "DATE CHECK - NOT TODAY: Xi-Trump-Putin summit - 19 Nov 2026, not today · Russian missiles in Poland - 20 Nov 2026 · SpiceJet fundraise approved - 18 Nov 2026 · Hyderabad bomb-threat email - sent 21 Nov 2026 · Paolo Bulgari death - reported 22 Nov 2026 · South Korea minister quits - reported 22 Nov · Indonesia factory fire itself - 22 Nov 2026"
MAPROWS = [
 "          oooo        oo     oooooo  oooooooo     oo        ",
 "       ooooooooo  o   oooo  oooooooooooooooooo  oooo   o    ",
 "        ooooooo      ooooo ooooooooooooooooooooo oooo  oooo ",
 "         ooooo        oo  ooooooooooooooooooooooo  oo  ooooo",
 "          ooo            ooooooooooooooooooooo      oooooo  ",
 "           oo  oo         oooooooooooooooooo         oooo   ",
 "            oooo           ooooooooooooooo            oo    ",
 "             oo             ooooooooooooo              oo   ",
 "            oo               oooooooooo                      ",
 "           ooo                ooooooo              oo  oo    ",
 "          oooo                 ooooo              oooooooo  ",
 "         ooo                    ooo                oooooo   ",
 "        oo                       o                  oooo    ",
]
PINS = [(1, 6, 3), (2, 28, 5), (3, 29, 6), (4, 24, 2), (5, 25, 3), (6, 26, 4),
        (7, 23, 1), (8, 52, 11), (9, 22, 4), (10, 20, 5), (11, 36, 6),
        (12, 8, 4), (13, 21, 4)]

def icon(d, x, y, kind, s=30):
    c = PINE; a = CHERRY
    if kind == "ship":
        d.polygon([(x, y + s * .7), (x + s, y + .7 * s), (x + s * .82, y + s), (x + s * .15, y + s)], outline=c, width=2)
        d.line([(x + s * .5, y + .7 * s), (x + s * .5, y + .25 * s)], fill=c, width=2)
        d.polygon([(x + s * .5, y + .25 * s), (x + s * .78, y + .45 * s), (x + s * .5, y + .45 * s)], fill=a)
    elif kind == "capitol":
        d.arc([x + s * .3, y, x + s * .7, y + s * .45], 180, 360, fill=c, width=2)
        d.line([(x + .1 * s, y + .55 * s), (x + .9 * s, y + .55 * s)], fill=c, width=2)
        for i in range(4):
            xx = x + s * (.2 + .18 * i); d.line([(xx, y + .58 * s), (xx, y + .9 * s)], fill=c, width=2)
        d.line([(x + .05 * s, y + .95 * s), (x + .95 * s, y + .95 * s)], fill=a, width=2)
    elif kind == "radar":
        d.arc([x + .1 * s, y + .05 * s, x + .75 * s, y + .6 * s], 300, 130, fill=c, width=3)
        d.line([(x + .42 * s, y + .35 * s), (x + .5 * s, y + s)], fill=c, width=2)
        d.arc([x + .55 * s, y + .02 * s, x + .95 * s, y + .3 * s], 300, 60, fill=a, width=1)
    elif kind in ("house", "building"):
        d.rectangle([x + .15 * s, y + .3 * s, x + .85 * s, y + .95 * s], outline=c, width=2)
        d.polygon([(x + .05 * s, y + .32 * s), (x + .5 * s, y + .05 * s), (x + .95 * s, y + .32 * s)], outline=a, width=2)
        for i in range(3):
            d.rectangle([x + (.25 + .2 * i) * s, y + .5 * s, x + (.35 + .2 * i) * s, y + .62 * s], fill=c)
    elif kind == "globe":
        d.ellipse([x + .08 * s, y + .08 * s, x + .92 * s, y + .92 * s], outline=c, width=2)
        d.line([(x + .08 * s, y + .5 * s), (x + .92 * s, y + .5 * s)], fill=c, width=1)
        d.arc([x + .3 * s, y + .08 * s, x + .7 * s, y + .92 * s], 0, 360, fill=a, width=1)
    elif kind == "cricket":
        d.line([(x + .25 * s, y + .9 * s), (x + .6 * s, y + .2 * s)], fill=c, width=4)
        d.ellipse([x + .62 * s, y + .6 * s, x + .92 * s, y + .9 * s], fill=a)
    elif kind == "tennis":
        d.ellipse([x + .05 * s, y + .05 * s, x + .6 * s, y + .6 * s], outline=c, width=2)
        d.arc([x + .05 * s, y + .05 * s, x + .6 * s, y + .6 * s], 40, 140, fill=a, width=2)
        d.line([(x + .55 * s, y + .55 * s), (x + .95 * s, y + .95 * s)], fill=c, width=3)
    elif kind == "gold":
        d.polygon([(x + .15 * s, y + .65 * s), (x + .3 * s, y + .4 * s), (x + .6 * s, y + .4 * s), (x + .75 * s, y + .65 * s)], outline=a, width=2)
        d.polygon([(x + .3 * s, y + .95 * s), (x + .45 * s, y + .7 * s), (x + .75 * s, y + .7 * s), (x + .9 * s, y + .95 * s)], outline=c, width=2)
    elif kind == "scales":
        d.line([(x + .5 * s, y + .1 * s), (x + .5 * s, y + .9 * s)], fill=c, width=2)
        d.line([(x + .15 * s, y + .25 * s), (x + .85 * s, y + .25 * s)], fill=c, width=2)
        d.arc([x + .05 * s, y + .25 * s, x + .3 * s, y + .55 * s], 0, 180, fill=a, width=2)
        d.arc([x + .7 * s, y + .25 * s, x + .95 * s, y + .55 * s], 0, 180, fill=a, width=2)
        d.line([(x + .3 * s, y + .95 * s), (x + .7 * s, y + .95 * s)], fill=c, width=2)
    elif kind == "shield":
        d.polygon([(x + .5 * s, y + .05 * s), (x + .9 * s, y + .2 * s), (x + .9 * s, y + .55 * s), (x + .5 * s, y + .95 * s), (x + .1 * s, y + .55 * s), (x + .1 * s, y + .2 * s)], outline=c, width=2)
        d.text((x + .36 * s, y + .28 * s), "F", font=SANB(14), fill=a)
    elif kind == "crowd":
        for cx in (.25, .5, .75):
            d.ellipse([x + (cx - .09) * s, y + .15 * s, x + (cx + .09) * s, y + .4 * s], fill=c)
            d.arc([x + (cx - .14) * s, y + .45 * s, x + (cx + .14) * s, y + .95 * s], 180, 360, fill=a, width=2)

def wrap(d, text, font, maxw):
    words = text.split(); lines = []; cur = ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = wd
    if cur: lines.append(cur)
    return lines

def header(d, variant):
    d.rectangle([0, 0, W, 24], fill=PINE)
    d.text((512, 12), "52 reports cross-checked - 16 wires & wires' wires - All times UTC",
           font=SANB(13), fill=(255, 253, 240), anchor="mm")
    if variant == "A":
        d.text((512, 60), "THE MORNING RECORD", font=SERB(66), fill=PINE, anchor="mm")
        d.text((512, 114), "MONDAY 23 NOVEMBER 2026", font=SANB(44), fill=CHERRY, anchor="mm")
    else:
        d.text((18, 58), "THE MORNING RECORD", font=SERB(58), fill=PINE, anchor="lm")
        d.text((18, 110), "MONDAY 23 NOVEMBER 2026", font=SANB(38), fill=CHERRY, anchor="lm")
    d.line([(14, 140), (1010, 140)], fill=PINE, width=3)
    d.line([(14, 145), (1010, 145)], fill=CHERRY, width=1)
    d.rectangle([14, 152, 1010, 178], fill=(240, 234, 216))
    seg = ["GOLD $3,538 -2.41%", "BITCOIN watched", "OIL watched",
           "Kyiv cold - Lisbon mild - Antalya warm - Wellington breezy",
           "IndiGo 65.9% at close"]
    xx = 22
    for i, t in enumerate(seg):
        d.text((xx, 165), t, font=SANB(12), fill=PINE if i == 0 else INK, anchor="lm")
        xx += d.textlength(t, font=SANB(12)) + 24
        if i < len(seg) - 1:
            d.line([(xx - 12, 157), (xx - 12, 173)], fill=CHERRY, width=1)
    # region strip with minimum label widths
    labels = ["%s %d" % (n, c) for n, c, _ in REGIONS]
    minw = [d.textlength(t, font=SANB(10)) + 14 for t in labels]
    extra = 996 - sum(minw)
    counts = [c for _, c, _ in REGIONS]
    widths = [m + extra * c / sum(counts) for m, c in zip(minw, counts)]
    xx = 14
    for (name, n, col), t, wseg in zip(REGIONS, labels, widths):
        d.rectangle([xx, 184, xx + wseg - 2, 208], fill=col)
        d.text((xx + wseg / 2, 196), t, font=SANB(10), fill=(255, 255, 255), anchor="mm")
        xx += wseg
    d.rectangle([14, 214, 1010, 236], outline=LINE)
    xx = 20
    for i, t in enumerate(TL):
        d.text((xx, 225), t, font=SAN(9), fill=INK, anchor="lm")
        xx += d.textlength(t, font=SAN(9)) + 12

def _card(d, x, y, w, h, c, tf, ff, tstep, fstep, foff, is_lead):
    num, loc, status, title, facts, source, ic = c
    d.rectangle([x, y, x + w, y + h], fill=PAPER, outline=LINE)
    d.rectangle([x, y, x + w, y + 15], fill=CHERRY if is_lead else PINE)
    d.text((x + 5, y + 7), "%d  %s" % (num, loc), font=SANB(11), fill=(255, 255, 255), anchor="lm")
    tw = d.textlength(status, font=SANB(10))
    d.rectangle([x + w - tw - 12, y + 2, x + w - 3, y + 13], fill=(255, 253, 240))
    d.text((x + w - 7, y + 7), status, font=SANB(10), fill=CHERRY, anchor="rm")
    srct = "Src: " + source
    d.text((x + w - tw - 18, y + 7), srct, font=SAN(9), fill=(255, 253, 240), anchor="rm")
    lines = wrap(d, title, tf, w - 14)
    yy = y + 19
    for ln in lines[:2]:
        d.text((x + 6, yy), ln, font=tf, fill=INK); yy += tstep
    icon(d, x + 6, yy + 2, ic, 30)
    fl = []
    for f in facts: fl.extend(wrap(d, f, ff, w - 48))
    for i, ln in enumerate(fl[:3]):
        d.text((x + 42, yy + foff + i * fstep), ln, font=ff, fill=INK)

def lead(d, x, y, w, h, c):
    _card(d, x, y, w, h, c, fb(28), fr(15), 30, 18, 9, True)

def mini(d, x, y, w, h, c):
    _card(d, x, y, w, h, c, fb(24), fr(13), 26, 15, 6, False)

def bottom(d, top):
    # numbers strip
    d.rectangle([14, top, 1010, top + 44], fill=PAPER, outline=LINE)
    d.text((22, top + 10), "THE DAY IN", font=SANB(12), fill=CHERRY)
    d.text((22, top + 25), "NUMBERS", font=SANB(12), fill=CHERRY)
    for i, (n, lab) in enumerate(NUMS):
        r, col = divmod(i, 4)
        xx = 150 + col * 212; yy = top + 6 + r * 20
        d.text((xx, yy), n, font=SANB(15), fill=PINE)
        nw = d.textlength(n, font=SANB(15))
        d.text((xx + nw + 6, yy + 2), lab, font=SAN(10), fill=INK)
    # map + date check (compact band)
    by = top + 50
    d.rectangle([14, by, 500, by + 68], fill=PAPER, outline=LINE)
    d.text((22, by + 11), "WHERE IT HAPPENED - DOTTED WORLD MAP", font=SANB(13), fill=CHERRY)
    if MAP_STYLE == "dotted_map":
        mx, my, cell = 50, by + 22, 3.3
        for r, row in enumerate(MAPROWS):
            for ci, ch2 in enumerate(row):
                if ch2 == "o":
                    d.ellipse([mx + ci * cell, my + r * cell, mx + ci * cell + 2.1, my + r * cell + 2.1], fill=(150, 160, 140))
        for n, cx, cy in PINS:
            px, py = mx + cx * cell, my + cy * cell
            d.ellipse([px - 6, py - 6, px + 6, py + 6], fill=CHERRY)
            d.text((px, py), str(n), font=SANB(8), fill=(255, 255, 255), anchor="mm")
    d.rectangle([508, by, 1010, by + 68], fill=(250, 238, 232), outline=CHERRY)
    d.text((516, by + 11), "DATE CHECK - NOT TODAY'S NEWS", font=SANB(13), fill=CHERRY)
    for i, t in enumerate(DATECHECK):
        col, r = divmod(i, 4)
        d.text((516 + col * 248, by + 28 + r * 14), "- " + t, font=SAN(10), fill=INK)
    # also on — full-width band, briefs at 10px
    ay = by + 74
    d.rectangle([14, ay, 1010, 984], fill=PAPER, outline=LINE)
    d.rectangle([14, ay, 190, ay + 14], fill=CHERRY)
    d.text((20, ay + 7), "ALSO ON THE DAY", font=SANB(11), fill=(255, 255, 255), anchor="lm")
    flow = " - ".join(BRIEFS)
    lines = wrap(d, flow, fsr(10), 978)
    for i, ln in enumerate(lines[:6]):
        d.text((20, ay + 19 + i * 12), ln, font=fsr(10), fill=INK)
    # footer
    d.rectangle([0, 986, W, H], fill=PINE)
    d.text((14, 993), "HOW SURE WE ARE: CONFIRMED = officials or final results on the record.",
           font=SANB(11), fill=(255, 253, 240))
    d.text((14, 1006), "REPORTED = carried by the named wires above; CLAIM = one side's account, labelled in its headline.",
           font=SANB(11), fill=(255, 253, 240))
    d.text((14, 1019), "Scenes are drawn illustrations. Sources: BBC, AP, AFP, JagranJosh, ObserverVoice, 23 Nov 2026.",
           font=SANB(11), fill=(255, 253, 240))

def build(variant):
    im = IL.new("RGB", (W, H), IVORY)
    d = DR.Draw(im)
    header(d, variant)
    if variant == "A":
        lead(d, 14, 242, 996, 78, CARDS[0])
        cw, ch, gap = 328, 106, 5
        for i, c in enumerate(CARDS[1:]):
            r, col = divmod(i, 3)
            mini(d, 14 + col * (cw + gap), 325 + r * (ch + gap), cw, ch, c)
        bottom(d, 325 + 4 * (ch + gap) + 3)
    else:
        lead(d, 14, 242, 996, 78, CARDS[0])
        cw, ch, gap = 244, 141, 6
        for i, c in enumerate(CARDS[1:]):
            r, col = divmod(i, 4)
            mini(d, 14 + col * (cw + gap), 325 + r * (ch + gap), cw, ch, c)
        bottom(d, 325 + 3 * (ch + gap) + 3)
    return im

if __name__ == "__main__":
    out = os.path.dirname(os.path.abspath(__file__))
    for v in ("A", "B"):
        build(v).save(os.path.join(out, "variant_%s.png" % v.lower()), optimize=True)
    print("done")
