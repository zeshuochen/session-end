---
name: session-end
description: Structured end-of-session ritual — task audit, retrospective, memory update, skill creation, dream compression, and next-session planning.
user-invocable: true
---

# Session End

A 6-step closing ritual that ensures nothing gets lost between conversations.

## Step 1 — Task Audit

Review every task the user explicitly requested this session. List each with status:
- Task name → ✅ Done / ❌ Not done / 🔄 Partial

If any are incomplete or partial, surface them immediately and wait for user confirmation before continuing.

## Step 2 — Retrospective

**Focus: find mistakes, not celebrate wins.** One sentence on outcomes, then enumerate errors:
- Wrong judgment calls (acted when should have asked)
- Known pitfalls walked into anyway (documented in memory/CLAUDE.md but not anticipated)
- Roundabout tool/approach choices (took 3 steps where 1 existed)
- Agent prompt design flaws (caused repeated reports, unclear scope, etc.)
- Scripts/code without defensive design (missing precondition checks, unhandled failure states)

If no mistakes: say "No significant mistakes." — do not skip this step.

New error patterns found that **haven't been seen before and could recur** → append to feedback memory in Step 4.

## Step 3 — Decide What to Update

Scan the conversation. For each category, decide independently:

**Memory files (almost always needed)**
- Project state changed? → Update corresponding `project_*.md`
- New feedback/lessons? → Write or update `feedback_*.md`
- New external resources? → Write `reference_*.md`
- User info changed? → Update `user_profile.md`

**Global CLAUDE.md** (only if: affects behavior across all projects)
- New rule that applies everywhere?
- User corrected a global behavior?
- New disk/tool/env conventions?
- → Yes: edit `~/.claude/CLAUDE.md`

**Project CLAUDE.md** (only if: affects current project conventions)
- New dev norms or architecture decisions for this project?
- → Yes: edit the project's `CLAUDE.md`

**New Skill** (needs at least 2 of these):
- Used a reusable multi-step workflow this session?
- Future conversations likely need it again?
- No existing skill covers it?
- → Yes: create using the appropriate skill-authoring tool

## Step 4 — Execute Updates

Execute each item from Step 3 in sequence. Brief confirmation after each.

## Step 5 — Memory Compression

Call the `dream` skill (or equivalent memory compression tool) to deduplicate and compress memory files.

> **Note:** `dream` is a Claude Code–specific skill. On other agents, skip this step or replace with your own memory compression workflow.

## Step 6 — Next Session Plan

List the top todos for next session (max 5, only genuinely important ones).
