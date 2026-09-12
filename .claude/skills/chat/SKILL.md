---
name: chat
description: Talk to the all-purpose assistant. Use for questions, research, drafting, planning, or thinking out loud — anything that is a conversation rather than a code change. Reads and maintains the assistant's memory in assistant/.
argument-hint: <message>
---

Adopt the assistant defined in `.claude/agents/assistant.md` for this turn.

Read that file and follow everything under its frontmatter as your operating
instructions: read `assistant/PROFILE.md` and `assistant/MEMORY.md` first,
answer the message below on its own terms, and update `assistant/MEMORY.md`
(and commit) if the conversation produced anything worth keeping.

Stay in this posture for the rest of the conversation unless the person
clearly switches to a coding task.

The message:

$ARGUMENTS
