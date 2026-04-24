# Prompt Caching with Claude

**Source:** https://claude.com/blog/prompt-caching  
**Published:** August 14, 2025  
**Categories:** Product announcements, Claude Platform, Coding

## Overview

Prompt caching lets developers cache frequently used context between API calls, reducing costs by up to 90% and latency by up to 85% for long prompts. Generally available on the Anthropic API; preview on Amazon Bedrock and Google Cloud Vertex AI.

## Use Cases

- **Conversational agents**: Reduce cost/latency for extended conversations with long instructions or uploaded documents
- **Coding assistants**: Enhance autocomplete and codebase Q&A with summarized codebase information
- **Large document processing**: Incorporate complete long-form material and images without increasing latency
- **Detailed instruction sets**: Share extensive instructions and diverse examples for better performance
- **Agentic search and tool use**: Improve multiple tool calls and iterative changes
- **Knowledge base integration**: Embed entire documents into prompts for Q&A

## Performance Improvements

| Use Case | Latency Without | Latency With | Cost Reduction |
|----------|-----------------|--------------|----------------|
| Chat with 100K-token book | 11.5s | 2.4s (-79%) | -90% |
| Many-shot prompting (10K tokens) | 1.6s | 1.1s (-31%) | -86% |
| Multi-turn conversation (10-turn) | ~10s | ~2.5s (-75%) | -53% |

## Pricing Structure

Cache writes cost 25% more than base input pricing; cache reads cost only 10% of base rate.

**Claude 3.5 Sonnet**: Input $3/MTok → Cache read $0.30/MTok  
**Claude 3 Opus**: Input $15/MTok → Cache read $1.50/MTok  
**Claude 3 Haiku**: Input $0.25/MTok → Cache read $0.03/MTok

## Models Supported

Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku.
