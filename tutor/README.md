# Math tutor

A dedicated mathematics tutor that lives in this repo alongside the research
vault, and is available in any Claude Code session opened on it.

A chat window can explain mathematics. A Claude Code session can also run it:
every derivative, identity, matrix, and counterexample the tutor states is
computed with sympy or numpy before it is said, practice sets come with
machine-checked answer keys, and the learner record is a set of files in git
that survive between sessions. The tutor teaches Socratically, hints before
answers, and tracks what is solid, what is shaky, and what is due for review.

## Use it

```
/tutor I don't see why the derivative of x^x is what it is
/tutor give me five problems on eigenvalues, one hard
/tutor here's my proof that sqrt(2) is irrational, check it
/tutor review
```

Or just ask a mathematics question. The tutor is also registered as a subagent
named `tutor`, so a session can hand it a question.

## What is here

```
.claude/agents/tutor.md        the tutor: how it teaches, its standard of rigor
.claude/skills/tutor/SKILL.md  the /tutor command that puts a session in that mode
tutor/LEARNER.md               who is being taught, at what level, toward what
tutor/PROGRESS.md              the record: solid, shaky, review queue, sessions
tutor/exercises/               practice sets and plots the tutor writes
```

## Memory

Sessions run in fresh containers with no memory of each other. The tutor reads
`LEARNER.md` and `PROGRESS.md` at the start of every session, opens with a
review item when one is due, and appends a dated entry to `PROGRESS.md` before
the session ends, then commits. Edit either file by hand whenever you like; the
tutor treats them as the source of truth.

## Boundary with the vault

The tutor writes only inside `tutor/`. The research vault directories
(`papers/`, `sources/`, `synthesis/`, `notes/`, `STATE.md`) belong to the vault
workflow described in the repo's `CLAUDE.md`, and the tutor reads them for
context but does not edit them.

## Adjust it

- **Change how it teaches:** edit the body of `.claude/agents/tutor.md`.
- **Change the level or goals:** edit `LEARNER.md`, or tell the tutor and it will.
- **Pin a model:** set `model:` in the agent's frontmatter to `sonnet`, `opus`,
  or `haiku` instead of `inherit`.
- **Add a specialist** (a proof checker, a problem generator): another `.md`
  file in `.claude/agents/` with the same frontmatter shape.
