# Research vault — operating instructions

This repo is a research and synthesis vault. Claude Code sessions have **no
cross-session memory**: the container is ephemeral and is reclaimed when the
session ends. This file is loaded into every session automatically, so it — plus
what is committed here — is the only thing that persists.

**Implication: if it isn't committed, it didn't happen.** Commit and push before
the session ends, even for work in progress.

## Read this first, every session

1. Read `STATE.md` — open threads, current focus, what was last worked on.
2. Skim `synthesis/` for anything relevant to the request.
3. Only then start new work.

## Where things go

| Directory | Holds | Lifecycle |
|---|---|---|
| `notes/` | Raw capture — meeting notes, dumps, half-formed thinking | Append-only, dated |
| `sources/` | One file per source, with the claims taken from it | Grows, rarely edited |
| `synthesis/` | The actual output — argued, structured documents | Revised over time |
| `templates/` | Starting points for the three above | Stable |

Rule of thumb: `notes/` is input, `sources/` is evidence, `synthesis/` is the
product. Never let a synthesis document assert something without a source file
behind it.

## Conventions

- Filenames: `YYYY-MM-DD-short-slug.md` in `notes/`, `slug.md` elsewhere.
- Every file starts with the YAML front matter its template shows.
- Cite sources by their filename: `[[sources/some-paper.md]]`.
- Mark uncertainty inline as `<!-- UNVERIFIED: ... -->` rather than deleting it.
  Unresolved uncertainty is information; silently dropping it is not.

## Maintaining memory

At the end of any session that changed something meaningful, update `STATE.md`:
what moved, what is now open, what the next session should pick up. This is the
handoff. Treat it as the most important file in the repo.

## Connectors

Sessions here can reach Gmail, Google Calendar, and Google Drive. Pulling
material in from Drive is expected; pushing anything outward is not — confirm
before sending, sharing, or emailing.
