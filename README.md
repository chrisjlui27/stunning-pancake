# Assistant

An all-purpose chat assistant that lives inside Claude Code.

Claude Code is built for coding, but the machinery underneath it (a model, a
shell, the web, connectors, git) is general. This branch adds a thin layer on
top so a session can be a conversation rather than a coding task: a custom
agent with its own instructions, a slash command to reach it, and a memory
that survives between sessions.

## Use it

```
/chat what's a good way to structure a reading list for a new field?
/chat draft a reply to the email from Sam about Thursday
/chat I'm trying to decide between X and Y, talk me through it
```

Or just talk. The agent definition is also registered as a subagent named
`assistant`, so the main session can hand conversational requests to it.

## What is here

```
.claude/agents/assistant.md    the agent: who it is and how it works
.claude/skills/chat/SKILL.md   the /chat command that puts a session in that mode
assistant/PROFILE.md           who it is talking with and how they like to work
assistant/MEMORY.md            what it has learned across conversations
```

## Memory

Sessions run in fresh containers with no memory of each other. The assistant
reads `assistant/MEMORY.md` at the start of every conversation and appends to
it at the end of any conversation that produced something worth keeping, then
commits. Preferences about how it should behave go in `assistant/PROFILE.md`
instead. Edit either file by hand whenever you like; the assistant treats them
as the source of truth.

## Adjust it

- **Change how it behaves:** edit the body of `.claude/agents/assistant.md`.
- **Restrict or widen what it can do:** edit the `tools` line in that file's
  frontmatter.
- **Pin a model:** set `model:` in the frontmatter to `sonnet`, `opus`, or
  `haiku` instead of `inherit`.
- **Add a specialist:** drop another `.md` file in `.claude/agents/` with the
  same frontmatter shape.
