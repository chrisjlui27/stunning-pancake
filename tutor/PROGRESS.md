# Progress

> The learner's record. The tutor reads this at the start of every session
> and appends before the end of any session that taught something. Dated,
> short, factual. Anything that outgrows a screen moves to its own file under
> `tutor/` with a pointer here.

## Solid

Concepts the learner has shown they can use in a new setting, not only
recall.

- None recorded yet.

## Shaky

Concepts covered but not yet demonstrated, or where an error appeared.
Each entry names the misconception if one was found.

- **Dot product.** Computed the outer product u v^T (correctly) when asked
  for u . v, and described the result as "a vector orthogonal to both" (the
  cross product). *Misconception:* the three products (dot = number, cross =
  vector, outer = matrix) are one blurred idea.
- **Linear independence.** *Misconception:* "independent = orthogonal".
  Counterexample to use: (1,0), (1,1) are independent, but their dot product is 1.
  Gave the right verdict on (1,0,1), (0,1,1), (1,1,2) (dependent) for a
  surface reason ("overlap among elements").
- **Span.** Said those same three vectors span R^3. They span a plane (rank 2;
  third = first + second). *Misconception:* n vectors in R^n reach everything.
  In fact they span R^n only when they are also independent.
- **Matrix as a map.** Called [[0,-1],[1,0]] "scales and rotates". It is a
  rotation by 90 degrees and does not scale (|A(3,1)| = |(3,1)| = sqrt(10)). No
  method yet for reading a matrix off its columns.
- Correct: a vector can be treated as an n x 1 matrix.

## Review queue

What to open the next session with, oldest first. Remove an item once it
has been checked and moved to Solid.

- Dot product: compute u . v for u = (1,2,2), v = (2,-1,0) and say what 0 means.
- Columns of a matrix = where (1,0) and (0,1) go; use this to read off
  [[0,-1],[1,0]].
- Independence vs orthogonality: explain why (1,0), (1,1) are independent.

## Sessions

- 2026-09-12 — Tutor set up. Background and goals gathered; plan written to
  `LEARNER.md`. No teaching yet. Next session: the placement check above,
  then Axler ch. 1 from wherever it lands.
- 2026-09-23 — Placement check done. Result: start phase 1 at the very
  beginning (Axler ch. 1, then 2A span and independence). Supplement Axler
  with concrete R^2/R^3 computation, because Axler puts dot products late.
  Three misconceptions found; see Shaky. The learner's comment: "I feel like
  I did not do good". Framed placement as finding the start, not a test.
