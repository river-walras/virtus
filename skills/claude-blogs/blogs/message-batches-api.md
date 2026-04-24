# Introducing the Message Batches API

**Source:** https://claude.com/blog/message-batches-api  
**Published:** October 8, 2024  
**Categories:** Product announcements, Claude Platform

## Overview

The Message Batches API processes large volumes of queries asynchronously at 50% lower cost than standard API calls. Accepts batches of up to 10,000 queries, with processing completed within 24 hours.

## Key Features

- **Cost efficiency**: 50% discount on both input and output tokens
- **Enhanced throughput**: Higher rate limits for larger request volumes without impacting standard API limits
- **Scalability**: Supports dataset analysis, classification, and model evaluations

## Models Supported

Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku—each with 200K context windows.

## Pricing

| Model | Input | Output |
|-------|-------|--------|
| Claude 3.5 Sonnet | $1.50/MTok | $7.50/MTok |
| Claude 3 Opus | $7.50/MTok | $37.50/MTok |
| Claude 3 Haiku | $0.125/MTok | $0.625/MTok |

## Customer Spotlight

**Quora**: Uses Batches API for summarization and highlight extraction. "It's very convenient to submit a batch and download results within 24 hours, instead of dealing with complexity of running many parallel live queries."

## Availability

Generally available on Anthropic's platform. Batch inference supported on Amazon Bedrock; preview on Google Cloud Vertex AI.
