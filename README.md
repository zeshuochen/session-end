# 🌙 session-end

**A structured closing ritual for AI coding sessions.**  
Stop losing context. Stop repeating yourself next conversation.

---

每次对话结束时，AI 会忘记一切。`session-end` 是一套 6 步收尾流程——进度、经验、待办全部写入记忆，下次对话开口就能接着来。

*When the session ends, AI forgets everything. `session-end` is a 6-step closing ritual — progress, lessons, and todos are saved so the next conversation picks up right where you left off.*

---

## What it does / 做什么

```
/session-end
```

| Step | EN | 中文 |
|------|----|----|
| 1 | ✅ Task Audit | 逐条核查本次任务完成情况 |
| 2 | 🔍 Retrospective | 找出失误（不是总结成果） |
| 3 | 🧠 Decide what to update | 判断哪些记忆/规则需要更新 |
| 4 | 📝 Execute updates | 执行记忆、CLAUDE.md、Skill 更新 |
| 5 | ✨ Memory compression | 压缩整理记忆文件（Claude Code: `dream` skill） |
| 6 | 📋 Next session plan | 写下下次对话的 Top 5 待办 |

The retrospective step is intentional: **find mistakes, not just celebrate wins.** Known pitfalls walked into again, wrong tool choices, undefended scripts — all get surfaced and written to memory so they don't repeat.

复盘步骤刻意聚焦于错误：已知的坑又踩了、工具选择绕路了、脚本没有防御性——全部记录，下次不再重犯。

---

## Install / 安装

### Claude Code (plugin — recommended)

```bash
claude plugins install github:zeshuochen/session-end
```

Then invoke with `/session-end`.

To also install the automatic trigger hooks, merge `hooks/hooks.json` into your `~/.claude/settings.json` under the `"hooks"` key.

### Claude Code (manual)

```bash
mkdir -p ~/.claude/skills/session-end
curl -o ~/.claude/skills/session-end/SKILL.md \
  https://raw.githubusercontent.com/zeshuochen/session-end/main/skills/session-end/SKILL.md
```

### Other agents / 其他 Agent

The skill is plain markdown — paste `skills/session-end/SKILL.md` into your agent's context, system prompt, or skill system as-is. Steps 1–4 and 6 are fully agent-agnostic. Step 5 references `dream`, a Claude Code–specific skill; skip or replace with your own memory tool.

---

## Hooks / 自动触发（可选）

The hook watches every message for trigger phrases and injects structured instructions automatically.

| Trigger phrase | Effect |
|---|---|
| `end session` / `结束对话` | Injects instruction to invoke `/session-end` immediately |

**Install:** merge the contents of `hooks/hooks.json` into your `~/.claude/settings.json`:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python \"${CLAUDE_PLUGIN_ROOT}/hooks/trigger.py\"",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

The hook requires Python 3 (stdlib only, no dependencies).

---

## Memory system / 记忆系统

`session-end` is most powerful paired with a persistent memory structure:

```
~/.claude/
├── CLAUDE.md                    ← global rules and conventions
└── projects/<project>/
    └── memory/
        ├── MEMORY.md            ← index of all memory files
        ├── project_*.md         ← project state
        ├── feedback_*.md        ← lessons and corrections
        └── reference_*.md       ← external resource pointers
```

Each session-end run updates these files. The `start session` hook reads them back on next open. No context lost.

---

## Agent compatibility / 兼容性

| Agent | Skill | Hooks | Notes |
|---|---|---|---|
| Claude Code | ✅ `/session-end` via plugin | ✅ `UserPromptSubmit` | Full support incl. `dream` compression |
| Gemini CLI | ✅ via `activate_skill` | ⚠️ Adapt format | See `gemini-extension.json` |
| Copilot CLI | ✅ Paste as context | ❌ No hook system | Manual invoke only |
| Cursor | ✅ Add to `.cursorrules` | ⚠️ See `.cursor-plugin/` | Manual invoke |
| Codex / others | ✅ Paste as context | ❌ | Manual invoke |

---

## License

MIT © [Zeshuo Chen](https://github.com/zeshuochen)
