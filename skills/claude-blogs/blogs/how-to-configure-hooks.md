# Claude Code Power User Customization: How to Configure Hooks

**Source:** https://claude.com/blog/how-to-configure-hooks  
**Published:** December 11, 2025  
**Categories:** Claude Code

## Overview

Hooks in Claude Code are custom shell commands that execute automatically when specific events occur during coding sessions. They eliminate repetitive manual tasks, enforce project rules, and inject dynamic context.

## The Eight Hook Types

| Hook | Trigger | Primary Uses |
|------|---------|-------------|
| **PreToolUse** | Before tool execution | Block dangerous commands, validate paths, auto-approve safe operations |
| **PermissionRequest** | Before permission dialogs | Auto-approve test commands, block sensitive file access |
| **PostToolUse** | After tool completion | Run formatters, trigger linters, log changes |
| **PreCompact** | Before context compaction | Back up transcripts, preserve important decisions |
| **SessionStart** | Session begins/resumes | Inject git status, load TODO lists, set context |
| **Stop** | Claude finishes responding | Verify task completion, run tests, generate summaries |
| **SubagentStop** | Subagent completes | Validate subagent output, trigger follow-ups |
| **UserPromptSubmit** | User submits prompt | Inject sprint context, validate requests |

## Configuration Locations

- **Project-level**: `.claude/settings.json` (shareable with team)
- **User-level**: `~/.claude/settings.json` (applies across all projects)
- **Local**: `.claude/settings.local.json` (personal, not committed)

## Matcher Syntax

- Simple: `"Write"` matches only the Write tool
- Multiple: `"Write|Edit"` triggers for either
- All tools: `"*"` or empty string
- Argument patterns: `"Bash(npm test*)"` for specific commands
- MCP tools: `"mcp__memory__.*"` format

Matchers are case-sensitive.

## Input & Output

Hooks receive JSON via stdin. Exit codes determine outcomes:
- **Exit 0**: Success
- **Exit 2**: Blocking error; stderr becomes error message
- **Other codes**: Non-blocking errors

Hooks can return structured JSON with fields like `decision` (approve/block), `reason`, `continue`, and `updatedInput`.

## Security

Hooks execute arbitrary shell commands with user permissions. Claude Code requires direct edits to hook configuration files to be reviewed in the `/hooks` menu before taking effect.

## Getting Started

Begin with one simple hook addressing a workflow friction point. The PostToolUse formatter hook is recommended as a first choice due to immediate, visible feedback.
