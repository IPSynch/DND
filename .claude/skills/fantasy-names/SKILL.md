---
name: fantasy-names
description: Generates fantasy character names in ten defined naming styles (Anglo-Gothic, High Sindarin, Kenning-Byname, Concept-Loan, Portmanteau-Root, Apostrophe-Clan, Sentence-Name, Imperial Rolling, Compact Duotone, Harsh Particle), tuned to this author's personal naming taste. Use this skill whenever the user needs a name for a character, NPC, villain, player character, house, clan, order, or god — in D&D, a novel, a campaign, a one-shot, a homebrew subclass, or worldbuilding of any kind. Trigger it even when the user doesn't say the word "name": "what should I call this guy", "I need an NPC for tonight", "give me a warlock for Curse of Strahd", "rename this subclass", "my BBEG needs something scarier" all mean this skill. Also use it to critique, fix, or explain the etymology of names the user already has.
---

# Fantasy Names

## What this skill is

A naming system reverse-engineered from this author's own characters and stated
influences. It is not a random name generator — every style here encodes
*meaning* under the sound, because that is what the author's own names do.
`Mordekaisa` is *morde* (bite/death) + *kaisar* (emperor): a woman who killed
her own empire. The name argues for the character before anyone reads her sheet.

Hold onto that. A name that sounds cool but means nothing will pass a glance and
fail at the table on session four.

## The method

**1. Write the character in one sentence.** Not the class — the contradiction.
"An eighty-year-old king who still personally kills demons on the battlefield."
"A duelist prodigy who retired at twenty to fish." The name has to carry that
tension, so you need it in words first.

**2. Pull the two load-bearing nouns** out of that sentence. King + endurance.
Blade + renunciation. Those are your roots.

**3. Pick a style** from the index below by *register*, not by vibe — how should
this name sound when it's said out loud at a table? Announced in a throne room
(Imperial Rolling)? Muttered in a cell (Harsh Particle)? Carved on a barrow
(Anglo-Gothic)?

**4. Build the name using that style's rules** in `references/styles.md`. That
file is the substance of this skill — read the entry for your chosen style
before writing anything. The per-style morpheme inventories live in
`references/phonetics.md`.

**5. Say it aloud.** These names get spoken across a table thirty times a
session. If it snags the tongue, cut a syllable. If it's boring to say, add a
hard consonant.

**6. Layer a second style on top** — see below. This is the single biggest
quality jump available.

## The layering principle

Almost every strong name in the author's corpus is **two styles at once**,
usually a *given name* in one register and a *second name* in another:

| Name | Given name style | Second name style |
|---|---|---|
| Origajima **Foldspire** | Portmanteau-Root | Kenning-Byname |
| Priest Dondarrion **Ravensway** | High Sindarin (Westerosi cut) | Kenning-Byname |
| Bartholomew **Grimsditch** | plain archaic English | Anglo-Gothic |
| Seshen **Thalion** | Concept-Loan (Egyptian) | High Sindarin epithet |
| Merveya **Ashe'kani** | Portmanteau-Root (French *merveille*) | Apostrophe-Clan |
| Kaladin **Stormblessed** | Compact | Kenning-Byname |

The collision is the character. A soft Egyptian lotus-word welded to a
hard Sindarin war-epithet *is* a woman who turns into demons. Single-style names
read as generic; two-style names read as a person from somewhere specific.

Default to layering unless the user asks for a mononym.

## Style index

Full definitions, rules, and word-banks: **`references/styles.md`**.

| # | Style | One-line definition | Author's exemplar |
|---|---|---|---|
| 1 | **Anglo-Gothic** | Ordinary archaic English given name + ominous English place-surname | Bartholomew Grimsditch |
| 2 | **High Sindarin** | Liquid-consonant name + an epithet-surname that *means* something ancient | Seshen Thalion, Luztherin Theramon |
| 3 | **Kenning-Byname** | Plain-English compound that states the power or the deed | Origajima Foldspire, Kaladin Stormblessed |
| 4 | **Concept-Loan** | Every element is a real word from a real language, chosen for meaning | Yuddha Rama Samsara, Ankara Citra |
| 5 | **Portmanteau-Root** | Two meaning-roots from two languages welded into one word | Mordekaisa, Balaurung |
| 6 | **Apostrophe-Clan** | Apostrophe marks a real lineage-joint or glottal stop, never decoration | Merveya Ashe'kani, Xochimeh Tepoch'onnya |
| 7 | **Sentence-Name** | A hyphenated clause naming the moment, not the person | Stranger-Comes-Knocking |
| 8 | **Imperial Rolling** | Long, open-voweled, reduplicated — built to be announced | Damarion Chimamandara |
| 9 | **Compact Duotone** | Two short names, two syllables each, from two different phonetic families | Norra Kaida |
| 10 | **Harsh Particle** | Deliberately ugly name with an aristocratic particle stranded in it | Sand dan Glokta |

Two cross-cutting dials, both covered in `references/styles.md`:

- **Stacking** — 1 part (Balaurung) / 2 parts (most) / 3 parts (Lews Therin
  Telamon, Yuddha Rama Samsara) / 4 parts (Samantha Princesza Jazzyka Engka).
  More parts = older, grander, or more ceremonial. Three parts is the sweet spot
  for a legend; two for someone you'll actually talk to.
- **Epithets and titles** — the `, the Black Dread` / `Lord of the Morning`
  layer that sits *on top* of a finished name. See `references/epithets.md`.

## Output format

Unless the user asks for something else, return a **slate of 6–10 candidates
spread across at least three styles**, because the author picks by ear and
needs range to pick from. For each:

```
**Name** — *Style* · what it encodes
```

Example:

```
**Vashti Corrowmere** — *Anglo-Gothic* · Persian "beautiful/best" over an
English drowned-lake surname (corrow ← sorrow + carrion); a fair name sinking.

**Ashkarun the Unlit** — *Portmanteau-Root + Epithet* · ash + *karun* (Persian,
"of the deep"); the epithet is what his order took from him.
```

Then offer, in one line, to go deeper on any of them — variants, a house name,
a title, or the same concept re-run in a different style.

Keep the etymology to one clause. The author wants the meaning available, not a
lecture.

## Craft rules

These are what separate the author's names from generic fantasy output.

- **Bury the meaning.** `Mordekaisa`, not `Murderkaiser`. A reader who knows
  Latin gets a second layer; everyone else just hears music. The moment the
  meaning is legible in English, the name becomes a label.
- **Two cultures, one name.** Norra (Nordic) + Kaida (Japanese). Luz (Spanish) +
  -therin (Jordan-ish). Origami + -jima. Monocultural names sound like
  placeholders; the seam is where character lives.
- **Let the given name be boring.** Bartholomew is a parish clerk's name. That's
  the joke and the horror — the surname does the work. Resist making both halves
  exotic.
- **Concrete nouns beat abstractions.** `-ditch`, `-spire`, `-way`, `-barrow`
  land; `-doom`, `-fate`, `-shadow` are worn smooth. Grimsditch is a *ditch*.
- **One weird mark per name, maximum.** One apostrophe or one x/tz cluster.
  Two makes it look typed rather than spoken.
- **Match register to role.** An eighty-year-old king gets six syllables of
  rolling vowels. A fisherman who was the best swordsman alive gets three short
  Sanskrit words. The syllable count is characterization.

## Anti-patterns

Language models converge hard on a small set of fantasy names. If you find
yourself writing any of these, you've stopped generating and started
remembering — throw it out and roll fresh seeds:

> Aelar, Kaelen, Lyra, Elara, Sylvara, Seraphina, Thorne, Draven, Malakar,
> Zephyr, Nyx, Vex, Raven, Kael, Aeliana, Valdris, Xander, Zarina, Eldrin,
> Grimjaw, Shadowbane, Darkblade, Bloodfang, Ironheart, Stormrider

Tells that a name is generic: it starts with a vowel + "e" (Ae-, Ea-), it ends
in `-ara`/`-yn`/`-iel` with nothing behind it, its surname is
`[Dark thing][Weapon]`, or it has an apostrophe holding no joint.

**When you feel the pull toward those**, run the seed roller — it exists
specifically to break the attractor:

```bash
python3 scripts/spark.py --style portmanteau-root --count 12
python3 scripts/spark.py --all
```

It emits *raw material*, not finished names: root pairs, syllable seeds, and
landform kits per style. Refine what it gives you — sand the seams, fix the
vowels, discard two-thirds. A seed is a starting point, never an answer.

## Reference files

- **`references/styles.md`** — the ten styles in full: rules, phonetics,
  formulas, worked examples, and what each is for. Read the relevant entry
  before generating. Also holds the stacking dial.
- **`references/phonetics.md`** — the sound toolkit: root and suffix
  inventories by language family, consonant-weight tables, ending banks.
  Use when you need raw material for a specific style.
- **`references/corpus.md`** — the author's own names, dissected one by one.
  Read this when the user asks *why* a name works, when you need to match an
  existing character's family or culture, or when a slate keeps missing the
  author's taste.
- **`references/epithets.md`** — titles, bynames, house names, orders, and
  the `, the X Y` construction. Read when naming anything that isn't a person,
  or when adding a title layer on top of a finished name.
- **`references/name-bank.md`** — 200 finished names, 10 male and 10 female per
  style, each glossed. Read it when you want calibration for what a style looks
  like done right, when the user wants a batch rather than a slate, or when you
  need parts to recombine — the surnames in particular transplant cleanly onto
  other given names.
