# Homebrew Base Classes (D&D 2014 / 2024 — interchangeable)

Full custom base classes built on the **Bodily Fluids & Body Tissues** concept: d12,
Constitution-based special-casters that produce **Fluidic Abilities** (spells mimicked with the
body's own blood, milk, seed, gas, filth, acid, sweat, and tissue) and pay for them in **Hit
Points** rather than spell slots.

## Shared rules

- **[Fluidic Abilities](./fluidic-abilities.md)** — the casting rules (HP costs, the
  can't-drop-below-1 / Exhaustion clause, Counterspell interaction) and the reskinned ability
  list, shared by every class here.

## The classes

| Class | Identity | Vibe |
|-------|----------|------|
| [The Visceralist](./visceralist.md) | The body unleashed | Feral body-horror; raw, aggressive, near-naked brute-caster **(finalized — has subclasses)** |
| [The Secretionist](./secretionist.md) | The body as a chemistry set | Clinical mad-flesh-alchemist; preserved as the alternate-flavor twin |

**The Visceralist is the maintained class going forward** — its twelve subclasses ("Visceral
Disciplines") live in [`subclasses/visceralist/`](../subclasses/visceralist/README.md). The
Secretionist remains as its mechanically identical alternate skin.

### Visceralist vs. Secretionist — how to choose

These two are **mechanical twins by design** — same d12 chassis, same Constitution casting, same
Unarmored Defense (10 + CON + DEX), same Sanguine Reserve (10 × level), same Primed Metabolism,
same level-7/14/20 base features, same Fluidic Abilities. **The choice is aesthetic, and it sets
which subclasses feel native:**

- **Visceralist** — a feral, unhinged, in-your-face performer. Its *Rut* is a berserk
  engorgement. Natural home for the loud, gross combat disciplines (fart, feces, sweat-bomb,
  hand-to-hand, elongated limbs).
- **Secretionist** — a cold, exacting biochemist. Its *Glandular Surge* is a controlled reaction.
  Natural home for the precise, support, and utility disciplines (urine buffs, the healer,
  transmutation, pheromone/toxin work).

Pick the voice you want at the table; the numbers play identically. (Subclasses — "Visceral
Disciplines" / "Secretory Specializations" — are next.)

## Shared design notes

- **Constitution does everything** (attacks/DC, AC, HP, saves, Concentration) — single-stat by
  design, so DEX and WIS are light secondary stats.
- **HP-as-fuel** is kept survivable by **Sanguine Reserve (10 × level)** plus passive regen; the
  can't-die-from-casting clause (drop to 1 + a level of Exhaustion) means the biggest abilities
  are always castable in a pinch, at a real cost.
- Level-by-level cadence: Base features at **1, 2, 7 (self-only Aura-of-Protection analog), 14
  (Spell Mastery + metabolic immunities), 20 (very strong capstone)**; subclass features at
  **3, 6, 10, 18 (subclass capstone)**; ASI/Feat at **4, 8, 12, 16, 19**.
</content>
