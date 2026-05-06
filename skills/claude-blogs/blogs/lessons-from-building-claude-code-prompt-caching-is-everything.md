# Lessons from building Claude Code: Prompt caching is everything

**Source:** https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything  
**Published:** April 30, 2026  
**Categories:** Claude Code

## Overview

Anthropic shares prompt-caching lessons from Claude Code. The core message is that long-running agentic products depend on high cache hit rates to reduce latency and cost.

## Prompt Layout

Prompt caching works by prefix matching. Claude Code structures requests so stable content appears first and dynamic content appears later:

1. Static system prompt and tools
2. `CLAUDE.md`
3. Session context
4. Conversation messages

Changing stable prefixes, such as timestamps, tool order, or tool definitions, can break the cache.

## Cache-Safe Updates

Claude Code prefers messages for changing state rather than editing the system prompt. It uses system-reminder-style messages for updated information.

## Avoid Mid-Session Model or Tool Changes

Prompt caches are model-specific, so switching models mid-session can be more expensive than staying with the current model. Anthropic recommends subagents for model handoffs. Tool sets should also remain stable; use tool-mode transitions or deferred loading rather than adding and removing tools.

## Plan Mode and Tool Search

Plan Mode keeps tool definitions stable by representing mode changes through tools and messages. Tool search uses lightweight deferred stubs so full tool schemas are loaded only when needed without changing the cached prefix.

## Compaction

Claude Code performs cache-safe forking for compaction by reusing the same system prompt, user context, system context, tools, and conversation prefix, then appending a compaction request.

## Lessons

The post recommends designing agent harnesses around prefix matching, monitoring cache hit rate like uptime, avoiding tool/model churn, and making side computations share the parent request prefix.

## When to Use This Blog

Use this source for prompt caching in Claude Code, cache-safe prompt layout, tool search, Plan Mode design, deferred tools, compaction, and reducing latency/cost in long-running agents.
