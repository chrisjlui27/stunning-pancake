# stunning-pancake

A research and synthesis vault, kept in git.

## Why a repo and not assistant memory

Claude chat and Cowork remember across conversations. Claude Code sessions do
not — each one starts in a fresh container that is destroyed afterwards. Keeping
the research in a repo trades invisible, automatic memory for memory that is
explicit, versioned, diffable, and readable by every surface including a human.

The tradeoff is real: this only works if things get written down and committed.
`CLAUDE.md` and `STATE.md` are what make that habitual rather than optional.

## Layout

```
CLAUDE.md      loaded into every Claude Code session — the operating rules
STATE.md       open threads and current focus — the session-to-session handoff
notes/         raw capture, dated, append-only
sources/       one file per source, with the claims drawn from it
synthesis/     the output: argued, structured documents
templates/     starting points for the three above
papers/        own papers: PDF, verification code, run logs
tutor/         the maths tutor's learner record — see tutor/README.md
```

## Working in it

Start a session and say what you're after. The session reads `STATE.md`, works,
commits, and updates `STATE.md` on the way out.

## The tutor

The repo also houses a mathematics tutor. Run `/tutor` in any session opened on
this repo, or just ask a mathematics question. It reads its learner record from
`tutor/`, teaches rather than answers, and runs every computation before
asserting it. See `tutor/README.md`.
