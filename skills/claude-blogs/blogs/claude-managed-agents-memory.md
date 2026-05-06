# Built-in memory for Claude Managed Agents

**Source:** https://claude.com/blog/claude-managed-agents-memory  
**Published:** April 23, 2026  
**Categories:** Product announcements, Claude Platform

## Overview

Memory for Claude Managed Agents entered public beta. Agents can now learn across sessions using a filesystem-based memory layer that developers can export, manage through the API, audit, and control.

## How Memory Works

Memory mounts onto a filesystem so Claude can use the same bash and code execution abilities that support agentic tasks. Anthropic says filesystem-based memory helps models save more organized memories and decide more carefully what to retain.

## Enterprise Controls

Memory stores can be shared across agents with scoped permissions. Examples include org-wide read-only stores and per-user read/write stores. Changes include audit logs, rollback, redaction, and visibility in Claude Console session events.

## Customer Examples

- Netflix agents use memory to retain multi-turn insights and human corrections.
- Rakuten reports 97% fewer first-pass errors, lower cost, and lower latency for task-based agents.
- Wisedocs uses cross-session memory in document verification and reports a 30% speedup.
- Ando uses Managed Agents memory instead of building custom memory infrastructure.

## Availability

Memory on Managed Agents is available in public beta on the Claude Platform through Claude Console and a CLI.

## When to Use This Blog

Use this source for questions about Claude Managed Agents memory, cross-session learning, filesystem memories, memory stores, audit logs, enterprise controls, and production agent memory patterns.
