# Claude Sonnet 4 now supports 1M tokens of context

**Source:** https://claude.com/blog/1m-context  
**Published:** August 12, 2025  
**Categories:** Product announcements, Claude apps

## Overview

Claude Sonnet 4 expanded to support up to 1 million tokens of context—five times the previous capacity. Enables processing extensive codebases (75,000+ lines) or dozens of research papers in a single API request.

## Availability

Public beta on Anthropic API for Tier 4 and custom rate limit customers. Also available on Amazon Bedrock and Google Cloud Vertex AI (as of August 26, 2025).

## Key Use Cases

- **Large-scale code analysis**: Load complete codebases with source files, tests, and documentation to understand architecture and cross-file dependencies
- **Document synthesis**: Process extensive legal contracts, research papers, or technical specs while analyzing relationships across multiple documents
- **Context-aware agents**: Build agents maintaining coherence across hundreds of tool calls and multi-step workflows

## Pricing

| Token Range | Input | Output |
|------------|-------|--------|
| ≤ 200K | $3/MTok | $15/MTok |
| > 200K | $6/MTok | $22.50/MTok |

Optimize costs with prompt caching and batch processing (additional 50% savings).

## Customer Applications

- **Bolt.new**: "Claude Sonnet 4 remains our go-to model for code generation"—expanded context enables significantly larger projects
- **iGent AI Maestro**: Autonomous software engineering agent—1M context "has supercharged autonomous capabilities" enabling multi-day sessions on real-world codebases
