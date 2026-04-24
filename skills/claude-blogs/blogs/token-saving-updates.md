# Token-saving updates on the Anthropic API

**Source:** https://claude.com/blog/token-saving-updates  
**Published:** March 13, 2025  
**Categories:** Product announcements, Claude Platform, Coding

## Overview

Three API updates to maximize throughput and reduce token consumption for Claude 3.7 Sonnet.

## Prompt Caching Improvements

**Cache-aware rate limits**: Prompt cache read tokens no longer count against Input Tokens Per Minute (ITPM) limits for Claude 3.7 Sonnet. Developers can leverage extensive cached content without consuming standard rate allowances.

**Automatic cache management**: Claude automatically identifies and utilizes the longest previously cached prefix—no manual segment management needed. Frees additional tokens for productive use.

## Token-Efficient Tool Use

Claude 3.7 Sonnet now supports more efficient tool invocation:
- Reduces output token consumption by up to **70%** (typical users see ~14% reductions)
- Activate by adding a specific beta header to requests

**New `text_editor` tool**: Enables targeted edits to specific text portions, reducing token consumption and latency for document collaboration.

## Industry Adoption

Cognition (applied AI lab): "Prompt caching allows us to provide more context about the codebase to get higher quality results while reducing cost and latency."

## Availability

Immediately available across the Anthropic API, Amazon Bedrock, and Google Cloud Vertex AI.
