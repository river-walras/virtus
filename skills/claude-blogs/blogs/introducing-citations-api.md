# Introducing Citations on the Anthropic API

**Source:** https://claude.com/blog/introducing-citations-api  
**Published:** June 23, 2025  
**Categories:** Product announcements

## Overview

Citations enables Claude to reference specific passages from source documents, providing verifiable responses with built-in source tracking.

## Key Benefits

- Claude provides detailed references to exact sentences and passages used to generate responses
- Built-in citation capabilities outperform most custom implementations, **increasing recall accuracy by up to 15%**
- Reduces complexity developers previously faced with custom prompt engineering implementations

## Technical Implementation

- Processes source documents (PDFs and plain text) by chunking them into sentences
- Chunks combined with user context and queries enable Claude to generate responses with precise citations
- Integrates seamlessly with the Messages API—no file storage required

## Pricing

Standard token-based pricing. Processing documents consumes additional input tokens, but users don't pay for output tokens returning quoted text.

## Use Cases

- Document summarization with source linking
- Complex Q&A across document corpora
- Customer support systems citing product documentation

## Models Supported

Claude 3.5 Sonnet and Claude 3.5 Haiku.

## Availability

Generally available on the Anthropic API and Google Cloud Vertex AI. Available on Amazon Bedrock as of June 30, 2025.

## Customer Results

**Endex**: Reduced source hallucinations and formatting issues from 10% to 0%; saw a 20% increase in references per response.
