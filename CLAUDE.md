# session-end — Contributor Guidelines

## Overview

`session-end` is a single-skill plugin providing a structured closing ritual for AI coding sessions. The skill is intentionally agent-agnostic — steps 1–4 and 6 work on any AI agent; only step 5 (`dream`) is Claude Code–specific.

## Contribution Principles

- **Keep it agent-agnostic.** Do not add Claude Code–specific behavior to steps 1–4 or 6.
- **The retrospective step (Step 2) must stay mistake-focused.** Do not soften it into a wins-summary. The asymmetry is intentional.
- **No new dependencies.** The hook uses stdlib Python only (`json`, `sys`). Keep it that way.
- **One skill, one job.** This plugin does session closing. Extensions for session opening, memory management, or other workflows belong in separate plugins.

## Modifying the skill

Changes to `skills/session-end/SKILL.md` that alter agent behavior (step structure, wording of criteria) should be tested across at least one agent before submitting a PR.

## File structure

```
.claude-plugin/plugin.json   ← Claude Code manifest
.cursor-plugin/plugin.json   ← Cursor manifest
skills/session-end/SKILL.md  ← The skill content
hooks/hooks.json             ← UserPromptSubmit hook config
hooks/trigger.py             ← Hook logic (stdlib Python only)
gemini-extension.json        ← Gemini CLI support
GEMINI.md                    ← Gemini context include
```
