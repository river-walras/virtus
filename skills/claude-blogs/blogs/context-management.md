# Managing context on the Claude Developer Platform

**Source:** https://claude.com/blog/context-management  
**Published:** September 29, 2025  
**Categories:** Product announcements, Claude Platform

## Overview

Two new capabilities for managing agent context: **context editing** and a **memory tool**. Both work with Claude Sonnet 4.5 to help developers build agents that handle extended tasks without hitting context limits.

## The Problem

Production agents handling complex work often exhaust their context windows, forcing developers to choose between truncating transcripts or accepting reduced performance.

## Context Editing

Automatically removes stale tool calls and results as agents approach token limits. Preserves conversation flow while eliminating outdated content. Extends agent operation duration and improves model focus on relevant information.

## The Memory Tool

Enables Claude to store and retrieve information outside the context window through a file-based system. Agents can create, read, update, and delete files in a dedicated memory directory that persists across conversations. Operates client-side through tool calls—developers have complete control over storage backend and persistence.

## Performance Impact

Testing on agentic search tasks:
- **Context editing alone**: 29% improvement over baseline
- **Memory tool + context editing**: 39% improvement over baseline
- In 100-turn web search evaluation: enabled workflows that would otherwise fail, reduced token consumption by **84%**

## Use Cases

- **Coding**: Preserve debugging insights and architectural decisions while clearing old file reads
- **Research**: Store findings while removing outdated search results
- **Data processing**: Maintain intermediate results while clearing raw data

## Availability

Public beta on the Claude Developer Platform, Amazon Bedrock, and Google Cloud Vertex AI.
