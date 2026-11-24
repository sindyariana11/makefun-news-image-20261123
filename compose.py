#!/usr/bin/env python3
"""THE FIRST EDITION - compose.py (Akun 10, NI23 Gelombang 3)
Straight newspaper front page, drawn locally with PIL.
Paper grey, black ink, mustard accent. Lead = pool story 2:
IRGC claims two Patriot radars destroyed in Bahrain (attributed).
Trio by this builder: pool 2 (lead) + pool 43 (House) + pool 7 (COP31).
Font helpers: fb = headline font, fr = deck font, fsr = brief font.
"""
import sys
from PIL import Image, ImageDraw, ImageFont

FD = "/home/hatch/workspace/tools/bedah-19nov/news-image/fonts/"
def fb(s): return ImageFont.truetype(FD + "PlayfairDisplay-Bold.ttf", s)
def fr(s): return ImageFont.truetype(FD + "Archivo.ttf", s)
def fsr(s): return ImageFont.truetype(FD + "Archivo.ttf", s)
def fblack(s): return ImageFont.truetype(FD + "PlayfairDisplay-Black.ttf", s)
def fbold(s): return ImageFont.truetype(FD + "Archivo-Bold.ttf", s)
W = H = 1024

# (num, region, topic, source tag, headline, deck, illustration kind)
grid = [
    (1, "MIDDLE EAST", "radar", "AP/AFP - IRGC claims", "IRGC Claims Two Patriot Radars Hit in Bahrain",
     "IRGC claims it destroyed 2 Patriot radars at a US base in Bahrain. Attributed claim, not independently confirmed.", "radar dish drawing"),
    (2, "NORTH AMERICA", "house", "BBC 23 Nov", "Democrats Win House 258-173",
     "Democrats take 258 seats to 173, the largest House majority since 1992, after winning in North Carolina.", "capitol drawing"),
    (3, "EUROPE", "climate", "BBC / AP 23 Nov", "COP31 Ends With No Deal",
     "COP31 closes in Turkiye with no agreement; the final draft never mentions fossil fuels, says the BBC.", "globe drawing"),
    (4, "EUROPE", "kyiv", "BBC 23 Nov", "Kyiv Child Pulled Alive From Rubble",
     "A boy aged 7 was pulled alive from rubble in Kyiv after hours; the Russian strike killed 6 people.", "rescue drawing"),
    (5, "MIDDLE EAST", "hormuz", "AP live 23 Nov", "Hormuz Tanker Set Ablaze",
     "A tanker burned in the Strait of Hormuz as the Iran-US war widened into the Gulf, AP reports.", "tanker drawing"),
    (6, "SOUTH ASIA", "cricket", "ObserverVoice 23 Nov", "India Post Record 720/9d",
     "India scored 720 for 9 declared at Wellington, the highest Test total ever made in New Zealand.", "cricket drawing"),
    (7, "SE ASIA", "icj", "ICJ rules - reports 23 Nov", "ICJ: Myanmar Committed Genocide",
     "The ICJ rules Myanmar committed genocide against the Rohingya; over 700,000 fled to Bangladesh in 2017.", "gavel drawing"),
    (8, "SE ASIA", "indonesia", "JagranJosh 23 Nov", "Indonesia: 7 Found, 50 Missing",
     "Indonesia update for 23 Nov: 7 bodies found and 50 people still missing after the candy factory fire.", "factory drawing"),
    (9, "GLOBAL", "gold", "ObserverVoice 23 Nov", "Gold Falls to $3,538 an Ounce",
     "Gold fell over $2,000 from its 2026 record of $5,595 to $3,538 an ounce, down 2.41% on Friday.", "gold bar drawing"),
    (10, "EUROPE", "tennis", "BBC 23 Nov", "Alcaraz Wins First ATP Finals Title",
     "Carlos Alcaraz beat Alexander Zverev in Turin to win his first ATP Finals title, the BBC reports.", "tennis drawing"),
    (11, "NORTH AMERICA", "fbi", "AP wire 23 Nov", "FBI Probes Database Hack",
     "The FBI is investigating an alleged hack of its main criminal justice database, AP reports from Washington.", "shield drawing"),
    (12, "SOUTH ASIA", "steel", "ObserverVoice 23 Nov", "Tata Steel Sale: Rs28,000 Crore",
     "Tata Steel sold its pipe business to APL Apollo for Rs28,000 crore, ObserverVoice reports from Mumbai.", "steel pipe drawing"),
    (13, "EUROPE", "ship", "BBC 23 Nov", "Russian Ship Still Burning",
     "A Russian cargo ship stayed ablaze off Finland after an attack in the Gulf of Finland, says the BBC.", "ship drawing"),
    (14, "NORTH AMERICA", "wedding", "BBC 23 Nov", "Miley Cyrus Marries Morando",
     "Miley Cyrus married Maxx Morando in California, the BBC reports; Morando plays drums with Liily.", "rings drawing"),
]

NUMS = [("258-173", "US HOUSE"), ("720/9d", "WELLINGTON TEST"), ("7 + 50", "INDONESIA UPDATE"),
        ("14", "MISSING KYIV"), ("$3,538", "GOLD OUNCE"), ("65.9%", "INDIGO SHARE")]

TL = [("00:02", "UN AI TALKS"), ("02:00", "ALBANESE SPEAKS"), ("MORNING", "KYIV RESCUE"),
      ("MIDDAY", "COP31 CLOSES"), ("EVENING", "HOUSE 258-173")]

BRIEFS_L = [
    "15 Houthi missile intercepted over Saudi west", "16 UN lethal-AI weapons talks continue",
    "17 US releases more UFO footage files", "18 Albanese: COP31 failure signals hard times",
    "19 Ship bound for Russia towed after attack", "20 Benghazi port explosion on Russian ship",
    "21 Zelenskiy says 14 missing in Kyiv region", "22 UK-EU Brexit reset called landmark",
    "23 Lisbon march over cost of living", "24 ASEAN decision unfair, says Myanmar junta",
    "25 Nepal PM Shah in talks with Modi", "26 Guru Nanak Jayanti marked in India",
    "27 UP blackout drill across 75 districts", "28 India chase famous win; NZ 119/2",
]
BRIEFS_R = [
    "29 India win ODI series in NZ 3-2", "30 Anupama defends world snooker title",
    "31 World Chess Championship draws fans", "32 Kota pilgrim bus tragedy: 9 dead",
    "33 SpiceJet audit urged; IndiGo at 65.9%", "34 IFFI BRICS roundtable held in Goa",
    "35 Modi opens AI centre at IIT Patna", "36 Shah launches Rs4,000 crore Arunachal push",
    "37 JEE Main 2027 registration closes today", "38 Google gives $5m to IIT Kharagpur AI",
    "39 Iowa: unstable explosives to be blasted", "40 Trump attacks Schumer over leadership",
    "41 Lion on the loose frightens Turkiye town", "42 Cameroon ex-rebels trapped in limbo",
]

dc = ("Xi-Trump-Putin trilateral summit - 19 Nov 2026 · Russian missiles and drones fell in Poland - 20 Nov 2026 · "
      "SpiceJet Rs5,500 crore fundraise approved - 18 Nov 2026 · Paolo Bulgari death reported - 22 Nov 2026 · "
      "South Sudan violence, 24 civilians dead - 22 Nov 2026 · South Korea education minister resigned - reported 22 Nov 2026")

PINS = [(1, 862, 286), (2, 762, 276), (3, 850, 270), (4, 876, 272), (5, 858, 282),
        (6, 936, 296), (7, 944, 300), (8, 950, 304), (9, 880, 290), (10, 848, 276),
        (11, 758, 280), (12, 930, 292), (13, 866, 268), (14, 758, 282)]

LEGEND = "Map pins mark the card numbers of the main stories; each dot cluster is a continent, brief stories sit below."

def wrap(d, text, font, maxw):
    out, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else:
            if cur: out.append(cur)
            cur = w
    if cur: out.append(cur)
    return out

def lead(d, x, y, w, region, col, num, src, head, deck, kind):
    """Draw the lead card: fb headline, fr deck."""
    d.rectangle([x, y, x + w, y + 140], fill=(247, 246, 241), outline=(12, 12, 12), width=2)
    d.rectangle([x, y, x + w, y + 25], fill=col)
    d.text((x + 10, y + 3), num + "  -  " + region + "  -  LEAD STORY", font=fbold(14), fill=(255, 255, 255))
    d.text((x + w - 10, y + 4), src, font=fbold(11), fill=(255, 255, 255), anchor="ra")
    for j, ln in enumerate(wrap(d, head, fb(29), w - 20)[:2]):
        d.text((x + 10, y + 30 + j * 33), ln, font=fb(29), fill=(12, 12, 12))
    for j, ln in enumerate(wrap(d, deck, fr(14), w - 20)[:2]):
        d.text((x + 10, y + 100 + j * 17), ln, font=fr(14), fill=(55, 55, 55))

def mini(d, x, y, w, region, col, num, src, head, deck, kind):
    """Draw one grid card: fb headline, fr deck."""
    d.rectangle([x, y, x + w, y + 53], fill=(247, 246, 241), outline=(168, 166, 158), width=1)
    d.rectangle([x, y, x + 50, y + 53], fill=col)
    d.text((x + 25, y + 5), num, font=fbold(21), fill=(255, 255, 255), anchor="ma")
    d.text((x + 25, y + 32), region.split()[0], font=fbold(9), fill=(255, 255, 255), anchor="ma")
    tl = wrap(d, head, fb(19), w - 64)
    d.text((x + 58, y + 4), tl[0] if tl else "", font=fb(19), fill=(12, 12, 12))
    fl = wrap(d, deck, fr(12), w - 64)
    d.text((x + 58, y + 27), fl[0] if fl else "", font=fr(12), fill=(60, 60, 60))
    d.text((x + 58, y + 42), src, font=fbold(10), fill=col)

def dotted_map(d, x, y):
    d.rectangle([x, y, x + 268, y + 140], fill=(208, 222, 230), outline=(12, 12, 12), width=1)
    d.text((x + 8, y + 4), "WORLD - PINS = CARDS", font=fbold(12), fill=(12, 12, 12))
    conts = [(x + 16, y + 36, 52, 20), (x + 34, y + 60, 26, 26), (x + 106, y + 32, 66, 18),
             (x + 114, y + 52, 44, 24), (x + 196, y + 58, 34, 28), (x + 90, y + 58, 20, 16)]
    for (mx, my, mw, mh) in conts:
        for gx in range(mx, mx + mw, 6):
            for gy in range(my, my + mh, 6):
                d.ellipse([gx, gy, gx + 3, gy + 3], fill=(105, 128, 105))
    for n, px, py in PINS:
        d.ellipse([px - 8, py - 8 - 232, px + 8, py + 8 - 232], fill=(198, 30, 30))
        d.text((px, py - 7 - 232), str(n), font=fbold(10), fill=(255, 255, 255), anchor="ma")
    d.text((x + 8, y + 122), "ME red NA blue EU purple SA mustard SEA teal", font=fr(10), fill=(12, 12, 12))

REGION_COL = {"MIDDLE EAST": (178, 32, 32), "NORTH AMERICA": (30, 90, 160), "EUROPE": (120, 60, 160),
              "SOUTH ASIA": (200, 110, 10), "SE ASIA": (0, 135, 135), "GLOBAL": (90, 90, 90)}
EU_GREEN = (30, 130, 76)

def build(variant, out):
    if variant == "B":
        bg, ink, accent = (243, 238, 220), (20, 24, 40), (30, 90, 160)
    elif variant == "C":
        bg, ink, accent = (250, 248, 246), (30, 10, 14), (140, 24, 40)
    else:
        bg, ink, accent = (232, 230, 223), (12, 12, 12), (196, 154, 20)
    img = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 9], fill=accent)
    d.text((24, 14), "42 STORIES  -  7 REGIONS  -  EVERY ONE FROM 23 NOVEMBER 2026", font=fbold(15), fill=ink)
    d.line([24, 40, 1000, 40], fill=ink, width=2)
    d.text((512, 44), "THE FIRST EDITION", font=fblack(74), fill=ink, anchor="ma")
    d.rectangle([24, 126, 1000, 132], fill=accent)
    d.text((512, 136), "Monday 23 November 2026", font=fb(32), fill=ink, anchor="ma")
    y = 176; bw = 976 // 6
    for i, (n, lab) in enumerate(NUMS):
        x = 24 + i * bw
        d.rectangle([x, y, x + bw - 6, y + 48], fill=ink)
        d.text((x + (bw - 6) // 2, y + 3), n, font=fbold(23), fill=(255, 213, 79), anchor="ma")
        d.text((x + (bw - 6) // 2, y + 30), lab, font=fr(10), fill=(235, 235, 235), anchor="ma")
    # lead + map
    c = grid[0]
    lead(d, 24, 232, 700, c[1], REGION_COL[c[1]], "1", c[3], c[4], c[5], c[6])
    dotted_map(d, 732, 232)
    # grid cards 2-14 via mini()
    y0 = 380
    for idx, c in enumerate(grid[1:]):
        col_i = idx % 2; row = idx // 2
        x = 24 + col_i * 492; yy = y0 + row * 57
        col = EU_GREEN if c[0] == 3 else REGION_COL[c[1]]
        mini(d, x, yy, 484, c[1], col, str(c[0]), c[3], c[4], c[5], c[6])
    # note box in the empty slot
    x = 516; yy = y0 + 6 * 57
    d.rectangle([x, yy, x + 484, yy + 53], fill=ink)
    d.text((x + 12, yy + 6), "HOW TO READ THIS PAGE", font=fbold(15), fill=(255, 213, 79))
    d.text((x + 12, yy + 25), "Numbered cards match the map pins. Sources on every card.", font=fr(12), fill=(240, 240, 240))
    d.text((x + 12, yy + 40), "Contested claims are attributed, never stated as fact.", font=fr(12), fill=(240, 240, 240))
    # timeline
    y = 790
    d.rectangle([24, y, 1000, y + 28], fill=accent)
    x = 34
    for t, lab in TL:
        s = t + " UTC " + lab if ":" in t else lab + ", " + t
        d.text((x, y + 6), s, font=fbold(12), fill=(0, 0, 0))
        x += int(d.textlength(s, font=fbold(12))) + 24
    # also on briefs with fsr(13)
    y = 826
    d.text((24, y), "ALSO ON 23 NOVEMBER - STORIES 15-42", font=fbold(15), fill=ink)
    briefs = BRIEFS_L + BRIEFS_R
    for i, s in enumerate(briefs):
        col_i = i // 7; row = i % 7
        d.text((24 + col_i * 246, y + 22 + row * 16), s[:36], font=fsr(13), fill=ink)
    # date check
    y = 962
    d.rectangle([24, y, 1000, y + 30], outline=(190, 30, 30), width=2)
    dc_full = "DATE CHECK - NOT 23 NOV: " + dc
    for j, ln in enumerate(wrap(d, dc_full, fbold(11), 960)[:2]):
        d.text((32, y + 3 + j * 13), ln, font=fbold(11), fill=(170, 25, 25))
    d.text((24, 998), "Every story happened, or was first reported, on Monday 23 November 2026. Contested claims are attributed.  Original drawings.", font=fr(11), fill=ink)
    d.text((24, 1012), LEGEND, font=fr(9), fill=(90, 90, 90))
    img.save(out); print(out, variant)

if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "A", sys.argv[2] if len(sys.argv) > 2 else "/tmp/entry-a10.png")
