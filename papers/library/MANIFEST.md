---
type: manifest
updated: 2026-09-11
---

# Library manifest

PDFs of the literature live in this directory, named `<source-slug>.pdf` to match
the entry in `sources/`. This file is the index and the download list.

**Why this list exists rather than the files:** this session's egress policy
blocks arxiv.org and every other scholarly host (WebFetch and curl alike —
only WebSearch, which runs through Anthropic's own infrastructure, gets out).
Nothing could be fetched from inside the container. The links below are for
downloading and uploading by hand.

**One note before bulk-adding:** arXiv preprints are fine to keep for personal
reference. Publisher PDFs from paywalled journals (Acta Math., J. Algebra,
Pacific J. Math., Canad. Math. Bull., Comm. Algebra, Forum Math.) are another
matter — prefer the arXiv version where one exists, which for this bibliography
is most of them. Your repo, your call; just worth knowing before it fills up.

---

## Priority 1 — the two open threads

| Slug | Reference | Link |
|---|---|---|
| `wilmot-2025` | **Wilmot, Structure of the Cayley–Dickson algebras** (2025) — the bibliography gap | https://arxiv.org/abs/2505.11747 |
| `cawagas-et-al-2009` | **Cawagas et al., Subalgebra structure of the trigintaduonions** — [9], the priority check | https://arxiv.org/abs/0907.2047 |

## Priority 2 — newly found, not in the v1 bibliography

These turned up in the search and bear directly on claims the paper makes. Ranked
by how much they could cost.

| Slug | Reference | Why it matters | Link |
|---|---|---|---|
| `aryapoor-back-pautrel-2026` | Aryapoor, Bäck, Pautrel, *Involutions in the Cayley–Dickson construction* (2026) | **Classifies all algebra isomorphisms between Cayley doubles extending the identity, hence the resulting \*-algebras up to isomorphism.** That is Theorem 3.6's exact question, published this year. | https://arxiv.org/abs/2606.27798 |
| `bales-2011-catalog` | Bales, *A catalog of Cayley–Dickson-like products* (2011) | Sets out to **catalog all possible variants of the CD doubling product**. If M(A) is in it, "no prior formulation of the mirror double as a construction" needs rewording. | https://arxiv.org/abs/1107.1301 |
| `bales-2016-alternate` | Bales, *An alternate Cayley–Dickson product*, Missouri J. Math. Sci. 28 (2016) | Title is close to the mirror. Abstract suggests it is a **different-but-equivalent** product on a shuffle basis — i.e. isomorphic, not a new algebra — but confirm. | https://arxiv.org/abs/1602.02317 |
| `bales-2017-doubling` | Bales, *The Cayley–Dickson doubling products* (2017) | Appears to be the arXiv version or companion of the cited [2]. **Check which is actually being cited.** | https://arxiv.org/abs/1707.07318 |
| `moreno-2005` | Moreno, *Constructing zero divisors in the higher dimensional Cayley–Dickson algebras* (2005) | A **second Moreno paper**, not cited. Relevant to Open Question 3 (higher mirrors). | https://arxiv.org/abs/math/0512517 |
| `bales-2016-periodicity` | Bales, *Periodicity of the Cayley–Dickson twists* (2016) | Twist structure; bears on the χ orientation-bit analysis in §7. | https://arxiv.org/abs/1602.02843 |
| `bales-2011-twisted` | Bales, *Cayley–Dickson and Clifford algebras as twisted group algebras* (2011) | Same framework as Albuquerque–Majid [1], used in §7. | https://arxiv.org/abs/1107.1375 |

## Priority 3 — arXiv versions of cited references

Most of the bibliography is on arXiv.

| Slug | Ref | Link |
|---|---|---|
| `reggiani-2024` | [19] | https://arxiv.org/abs/2411.18881 |
| `moreno-1998` | [18] | https://arxiv.org/abs/q-alg/9710013 |
| `biss-christensen-dugger-isaksen-2009` | [5] Eigentheory | https://arxiv.org/abs/0905.2987 |
| `biss-christensen-dugger-isaksen-2007` | [4] Large annihilators II | https://arxiv.org/abs/math/0702075 |
| `de-marrais-2000` | [11] | https://arxiv.org/abs/math/0011260 |
| `kirshtein-2012` | [15] | https://arxiv.org/abs/1102.5151 |
| `cawagas-2004` | [8] — open access via EUDML | https://eudml.org/doc/287717 |
| `saniga-holweck-pracna-2015` | [21] — MDPI, open access | search "From Cayley-Dickson algebras to combinatorial Grassmannians" |

Still to locate on arXiv (may be publisher-only): [3] Biss–Dugger–Isaksen 2008,
[10] Chan–Ðoković 2006, [1] Albuquerque–Majid 1999, [2] Bales 2016 AACA,
[20] Salamon–Walpuski 2017.

## Priority 4 — adjacent, worth a look

| Reference | Link |
|---|---|
| *Determinant factorization for left multiplication in the sedenions* (2025) | https://arxiv.org/abs/2512.13002 |
| *The twisted group algebra structure of the Cayley–Dickson algebra* | https://arxiv.org/abs/2205.07986 |
| *A twisted group algebra structure for an algebra obtained by the CD process* | https://arxiv.org/abs/2103.12805 |
| *Flipped non-associative polynomial rings and the CD construction* | https://arxiv.org/abs/2403.03763 |
| *Central products of Cayley–Dickson loops* | https://arxiv.org/abs/2603.20495 |
