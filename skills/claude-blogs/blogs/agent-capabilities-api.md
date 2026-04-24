# New capabilities for building agents on the Anthropic API

**Source:** https://claude.com/blog/agent-capabilities-api  
**Published:** May 22, 2025  
**Categories:** Product announcements, Claude Platform

## Overview

Four new beta features for the API empower developers to build sophisticated AI agents: code execution, MCP server connections, file storage, and extended prompt caching—eliminating custom infrastructure needs.

## Code Execution Tool

Claude can run Python code in a sandboxed environment for computational analysis and data visualizations. Transforms Claude from a code-writing tool into an active data analyst capable of iterating on outputs within single API calls.

**Use cases**: Financial modeling, scientific computing, business intelligence, document processing, statistical analysis.

**Pricing**: 50 free hours daily; additional usage at $0.05 per hour per container.

## MCP Connector

Removes complexity of building custom client harnesses. The API handles connection management, tool discovery, and error handling automatically when remote MCP servers are configured. Immediately access third-party capabilities from Zapier, Asana, and others without one-off integrations.

## Files API

Upload documents once and reference them repeatedly across sessions—no re-uploading per request. Integrates with code execution tool so Claude can access and process uploaded files during analysis.

## Extended Prompt Caching

Opt for a **1-hour TTL** cache duration instead of standard 5-minute option at additional cost—a "12x improvement" for long-running agent workflows. Reduces expenses up to 90% and latency up to 85% for lengthy prompts.

## Availability

All four features available now in public beta on the Anthropic API.
