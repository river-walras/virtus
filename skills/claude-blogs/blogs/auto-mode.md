# Auto mode for Claude Code

**Source:** https://claude.com/blog/auto-mode  
**Published:** March 24, 2026  
**Categories:** Claude Code, Coding

## Overview

Claude Code now features auto mode, a new permissions system that allows Claude to make approval decisions independently while maintaining safety guardrails. Rolling out as a research preview to Team plan users.

## How It Works

The default Claude Code permissions require manual approval for each file write and bash command. Auto mode offers a middle ground between constant prompts and completely disabled permissions.

Before executing any tool call, a classifier analyzes the action to identify potentially destructive behaviors like "mass deleting files, sensitive data exfiltration, or malicious code execution." Safe actions proceed automatically; risky ones get blocked with Claude redirected toward alternative approaches.

## Limitations

- The classifier may occasionally permit risky actions when user intent is ambiguous
- Benign operations might be incorrectly blocked
- May slightly increase token consumption, costs, and tool call latency
- Users should still employ auto mode within isolated environments for maximum safety

## Getting Started

- **CLI**: Run `claude --enable-auto-mode` and cycle to it with Shift+Tab
- **Desktop/VS Code**: Enable through Settings, then select from the permission mode dropdown
- **Admins**: Can disable auto mode via managed settings configuration
