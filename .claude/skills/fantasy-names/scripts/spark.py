#!/usr/bin/env python3
"""spark.py - raw naming material for the fantasy-names skill.

This does NOT produce finished names. It produces *seeds*: root pairs, syllable
runs, and compound halves drawn from the banks in references/phonetics.md.

It exists because language models converge hard on the same two dozen fantasy
names (Aelar, Kaelen, Lyra, Malakar...). Random seeds break that attractor by
handing you material you would not have thought of, which you then sand into
something real. Expect to discard two thirds of what comes out.

Usage:
    python3 spark.py --style portmanteau-root --count 12
    python3 spark.py --all
    python3 spark.py --list
    python3 spark.py --style anglo-gothic --seed 42   # reproducible
"""

import argparse
import random
import sys

# ---------------------------------------------------------------- word banks

ARCHAIC_GIVEN = """Bartholomew Ambrose Cuthbert Ezekiel Horatio Obadiah Percival
Alaric Mordecai Thaddeus Barnaby Silas Josiah Hezekiah Tobias Wilfred Erasmus
Cornelius Ignatius Aldous Grenville Peregrine Bertram Osric Wilhelmina Prudence
Temperance Millicent Hester Agatha Dorcas Rosamund Cordelia Winifred Bathsheba
Eugenia Maud Clemency""".split()

GRIM_MOD = """ash grim crow thorn gallow nettle sorrow wain black bell cold mourn
quill hollow rook brack sallow pike winter dun brine cinder glass tally
lantern rust""".split()

LANDFORM = """ditch barrow moor hollow thwaite combe stoke worth wick marsh fen
mire reach hallow church yard crook bourne shaw holt mere garth cote stead
spire gate""".split()

POWER_HALF = """fold storm ash grave dawn iron salt thorn ember wake hush tide
bone frost gild rust vow cinder lantern glass tally brine""".split()

DEED_HALF = """blessed breaker walker bearer fall wright kept shorn bound tender
crowned sung touched given sworn taken lit fed read counted marked owed
way spire march""".split()

SIND_ROOT = ["thal", "gal", "galad", "mor", "cel", "ael", "luin", "nim", "ross",
             "tir", "dun", "lin", "ear", "cur", "bel", "fir", "nar", "orod",
             "rond", "thar", "maeg", "heru", "gwath", "brann", "iaur"]

SIND_END = ["ion", "iel", "on", "in", "or", "eth", "as", "ir", "il", "ath",
            "uin", "ael", "amon", "ain", "ith", "dor", "wen", "mir"]

# (root, gloss) pairs - the gloss is what makes a seed usable
CONCEPT = [
    ("yuddha", "war, Skt"), ("shanti", "peace, Skt"), ("agni", "fire, Skt"),
    ("vayu", "wind, Skt"), ("kala", "time/death, Skt"), ("maya", "illusion, Skt"),
    ("tejas", "radiance, Skt"), ("vajra", "thunderbolt, Skt"),
    ("ananta", "endless, Skt"), ("mrityu", "death, Skt"), ("atman", "self, Skt"),
    ("karuna", "compassion, Skt"), ("virya", "valor, Skt"), ("shakti", "power, Skt"),
    ("samsara", "the wheel, Skt"), ("moksha", "release, Skt"), ("rudra", "howler, Skt"),
    ("citra", "many-hued, Skt"), ("ojas", "vigor, Skt"), ("smara", "memory, Skt"),
    ("seshen", "lotus, Egy"), ("akhet", "horizon, Egy"), ("sekhem", "power, Egy"),
    ("duat", "underworld, Egy"), ("maat", "order, Egy"), ("ren", "true name, Egy"),
    ("heka", "magic, Egy"), ("khepri", "becoming, Egy"), ("nebu", "gold, Egy"),
    ("benu", "rebirth, Egy"), ("amenti", "the west/the dead, Egy"),
    ("darya", "sea, Per"), ("azar", "fire, Per"), ("mehr", "sun/love, Per"),
    ("shahin", "falcon, Per"), ("yildiz", "star, Tur"), ("kaya", "rock, Tur"),
    ("zarrin", "golden, Per"), ("simurgh", "great bird, Per"), ("alp", "hero, Tur"),
    ("demir", "iron, Tur"), ("gece", "night, Tur"), ("kurt", "wolf, Tur"),
    ("deniz", "sea, Tur"),
    ("morde", "to bite, Lat"), ("lux", "light, Lat"), ("luz", "light, Spa"),
    ("umbra", "shade, Lat"), ("vesper", "evening, Lat"), ("nox", "night, Lat"),
    ("ferrum", "iron, Lat"), ("gelu", "frost, Lat"), ("oblivium", "forgetting, Lat"),
    ("merveille", "marvel, Fra"), ("detresse", "distress, Fra"), ("cendre", "ash, Fra"),
    ("orage", "storm, Fra"), ("deuil", "mourning, Fra"), ("voile", "veil, Fra"),
    ("balaur", "dragon, Rom"), ("gar", "spear, Ger"), ("mund", "protection, Ger"),
    ("brand", "sword/fire, Ger"), ("hild", "battle, Ger"), ("grim", "mask/fierce, Nor"),
    ("vargr", "wolf, Nor"), ("geist", "ghost, Ger"), ("kaiser", "emperor, Ger"),
    ("norr", "north, Swe"), ("fjall", "mountain, Nor"), ("eisen", "iron, Ger"),
    ("kaida", "little dragon, Jpn"), ("kage", "shadow, Jpn"), ("yuki", "snow, Jpn"),
    ("ori", "fold, Jpn"), ("kiri", "mist, Jpn"), ("hono", "flame, Jpn"),
    ("tsuki", "moon, Jpn"), ("hagane", "steel, Jpn"), ("kumo", "cloud, Jpn"),
    ("tsurugi", "blade, Jpn"), ("sora", "sky, Jpn"), ("kami", "spirit, Jpn"),
    ("chi", "personal spirit, Igb"), ("eze", "king, Igb"), ("ade", "crown, Yor"),
    ("olu", "chief, Yor"), ("moyo", "heart, Swa"), ("nuru", "light, Swa"),
    ("simba", "lion, Swa"),
]

WELD_END = ["ung", "in", "a", "is", "oth", "ar", "eya", "aine", "ova", "esh",
            "im", "ai", "un", "or", "ka", "ja", "ren", "thal", "jima", "gar"]

CLAN_ROOT = ["ashe", "kae", "zul", "vash", "dre", "ith", "sul", "kha", "orr",
             "tsae", "ny", "vor", "sha", "eze"]
CLAN_SEPT = ["kani", "meth", "thi", "ra", "jin", "vek", "aan", "oru", "isk",
             "endi", "ashi", "uun", "oth"]

NAHUATL = ["xochi", "coatl", "itz", "teo", "mictl", "quetzal", "ocelo", "tepoch",
           "tlalli", "ehecatl", "citlal", "atl", "tonal", "nahual", "cuauh",
           "yollotl", "calli"]
NAHUATL_END = ["meh", "tzin", "tli", "tlan", "onnya", "ca", "teuc"]

SENT_SUBJ = """Stranger Crow Door Ash Winter Lantern Salt Wolf Mother Rope
Question Tally Ledger Bell Thread Hound Lamp Tide Widow Road""".split()
SENT_VERB = """Comes Waits Opens Counts Remembers Sings Walks Knocks Listens
Forgets Never-Sleeps Does-Not-Turn Answers Keeps Follows Returns""".split()
SENT_COMP = ["Knocking", "In-Salt", "Inward", "The-Sleeping", "At-The-Ford",
             "Twice", "Your-Road", "The-Doors", "Burning", "Upward", "Again",
             "The-Long-Way", "Unbidden", "Last", "The-Hours"]

ROLL_GIVEN = ["Dama", "Kesa", "Olu", "Ade", "Tewo", "Mena", "Zala", "Ifea",
              "Bara", "Nsia", "Amara", "Oyo", "Taresa"]
ROLL_GEND = ["rion", "ion", "ius", "aro", "ande", "ike", "eze", "mide"]
ROLL_SYL = ["chi", "ma", "da", "ra", "na", "la", "ne", "to", "sa", "be", "ro",
            "ka", "mi", "yo", "wa", "du", "si", "ba"]

DUO_A = ["Norra", "Vasha", "Runa", "Suri", "Talla", "Kesi", "Mira", "Onda",
         "Hessa", "Ilva", "Zora", "Anka", "Rhea", "Sela", "Tuva"]
DUO_B = ["Kaida", "Kirin", "Teshka", "Valdan", "Citra", "Morran", "Senka",
         "Hollan", "Yuriv", "Danji", "Kessel", "Ravna", "Toma", "Ishri"]

UGLY_GIVEN = """Sand Jez Caul Bayaz Nic Fenn Ruth Corm Vell Hale Ost Bryn
Marsh Grell Pol Tam""".split()
PARTICLE = ["dan", "ven", "ap", "el", "ter", "zo", "na", "vor", "dis", "sur"]
UGLY_SURNAME = """Glokta Vetch Krast Burr Sult Pike Nubb Skarn Gorst Brack
Tellik Vosk Hurd Grist Kroy Mauthe Sneck Drubb Rache Stang Pfaltz Knock""".split()

# ------------------------------------------------------------------ builders


def anglo_gothic(r):
    given = r.choice(ARCHAIC_GIVEN)
    mod, land = r.choice(GRIM_MOD), r.choice(LANDFORM)
    # the linking -s- / -en- is what makes these read as real toponyms
    link = r.choice(["", "", "s", "en"])
    return f"{given} {mod.capitalize()}{link}{land}"


def high_sindarin(r):
    a, b = r.sample(SIND_ROOT, 2)
    end = r.choice(SIND_END)
    given = (a + b).capitalize()
    epithet = (r.choice(SIND_ROOT) + end).capitalize()
    return f"{given} {epithet}"


def kenning_byname(r):
    return f"{r.choice(POWER_HALF).capitalize()}{r.choice(DEED_HALF)}"


def concept_loan(r):
    picks = r.sample(CONCEPT, 3)
    words = " ".join(w.capitalize() for w, _ in picks)
    gloss = " + ".join(g.split(",")[0] for _, g in picks)
    return f"{words}   [{gloss}]"


VOWELS = "aeiouy"


def _clip(word, r, lo=3, hi=5):
    """Trim a root to a name-sized chunk, cutting on a syllable-ish boundary.

    Real welds use clipped roots, not whole words: morde from mordere, ori from
    origami, balaur kept whole only because it is already short. Without this
    the fusions come out as eight-syllable sludge.
    """
    if len(word) <= hi:
        return word
    n = r.randint(lo, hi)
    # prefer to cut just after a vowel so the chunk stays pronounceable
    for i in range(n, min(n + 2, len(word))):
        if word[i - 1] in VOWELS and word[i] not in VOWELS:
            return word[:i]
    return word[:n]


def portmanteau_root(r):
    (a, ga), (b, gb) = r.sample(CONCEPT, 2)
    head, tail = _clip(a, r), _clip(b, r, 2, 4)
    # overlap on a shared sound at the seam, the way morde|kaisar -> Mordekaisa
    if head[-1] == tail[0]:
        tail = tail[1:]
    fused = head + tail
    # an ending only when the weld does not already resolve on a vowel
    if fused[-1] not in VOWELS and r.random() < 0.7:
        fused += r.choice(WELD_END)
    return f"{fused.capitalize()}   [{a}={ga} + {b}={gb}]"


def apostrophe_clan(r):
    if r.random() < 0.4:
        root, end = r.choice(NAHUATL), r.choice(NAHUATL_END)
        split = max(2, len(root) - r.randint(1, 2))
        return f"{root[:split].capitalize()}'{root[split:]}{end}"
    return f"{r.choice(CLAN_ROOT).capitalize()}'{r.choice(CLAN_SEPT)}"


def sentence_name(r):
    return f"{r.choice(SENT_SUBJ)}-{r.choice(SENT_VERB)}-{r.choice(SENT_COMP)}"


def imperial_rolling(r):
    given = r.choice(ROLL_GIVEN) + r.choice(ROLL_GEND)
    syls = r.sample(ROLL_SYL, 3)
    echo = r.choice(syls)                    # reduplication = dynasty
    surname = "".join(syls[:2] + [echo] + syls[2:])
    return f"{given.capitalize()} {surname.capitalize()}"


def compact_duotone(r):
    return f"{r.choice(DUO_A)} {r.choice(DUO_B)}"


def harsh_particle(r):
    return f"{r.choice(UGLY_GIVEN)} {r.choice(PARTICLE)} {r.choice(UGLY_SURNAME)}"


STYLES = {
    "anglo-gothic":     (anglo_gothic,     "archaic given + grim English place-surname"),
    "high-sindarin":    (high_sindarin,    "liquid given + meaning-bearing epithet"),
    "kenning-byname":   (kenning_byname,   "plain-English compound stating the power"),
    "concept-loan":     (concept_loan,     "real words from real languages, with glosses"),
    "portmanteau-root": (portmanteau_root, "two roots welded - SEAMS NEED SANDING"),
    "apostrophe-clan":  (apostrophe_clan,  "lineage joint or glottal stop"),
    "sentence-name":    (sentence_name,    "a hyphenated clause naming a moment"),
    "imperial-rolling": (imperial_rolling, "long, open-voweled, reduplicated"),
    "compact-duotone":  (compact_duotone,  "two short names, two phonetic families"),
    "harsh-particle":   (harsh_particle,   "ugly surname + aristocratic particle"),
}

FOOTER = """
These are SEEDS, not names. Before using one: say it aloud, fix the vowel at any
audible seam, cut or add a syllable to match the character's weight, and throw
out anything that sounds like a name you've read before. See references/styles.md
for the rules of whichever style you're working in."""


def emit(name, r, count):
    fn, blurb = STYLES[name]
    print(f"\n### {name}  -  {blurb}")
    seen = []
    # sample generously and dedupe; small banks can repeat
    for _ in range(count * 6):
        if len(seen) >= count:
            break
        s = fn(r)
        if s not in seen:
            seen.append(s)
    for s in seen:
        print(f"  {s}")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--style", help="style id (see --list)")
    p.add_argument("--count", type=int, default=8, help="seeds per style (default 8)")
    p.add_argument("--all", action="store_true", help="roll every style")
    p.add_argument("--list", action="store_true", help="list style ids")
    p.add_argument("--seed", type=int, help="fix the RNG for reproducible output")
    a = p.parse_args()

    if a.list:
        for k, (_, blurb) in STYLES.items():
            print(f"  {k:<18} {blurb}")
        return 0

    r = random.Random(a.seed)

    if a.all:
        for k in STYLES:
            emit(k, r, a.count)
    elif a.style:
        key = a.style.strip().lower()
        if key not in STYLES:
            print(f"unknown style: {a.style}\n", file=sys.stderr)
            print("known styles:", file=sys.stderr)
            for k in STYLES:
                print(f"  {k}", file=sys.stderr)
            return 1
        emit(key, r, a.count)
    else:
        p.print_help()
        return 0

    print(FOOTER)
    return 0


if __name__ == "__main__":
    sys.exit(main())
