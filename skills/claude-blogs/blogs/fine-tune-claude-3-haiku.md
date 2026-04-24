# Fine-tune Claude 3 Haiku in Amazon Bedrock

**Source:** https://claude.com/blog/fine-tune-claude-3-haiku  
**Published:** July 10, 2024  
**Categories:** Product announcements, Claude Platform

## Overview

Claude 3 Haiku can now be fine-tuned in Amazon Bedrock with custom training data, enabling faster, more accurate performance at lower cost.

## How It Works

Prepare high-quality prompt-completion pairs representing ideal outputs for your task. The fine-tuning API creates a custom Claude 3 Haiku trained on your data. Use the Amazon Bedrock console or API to test and refine until performance goals are met.

## Benefits

- **Better results on specialized tasks**: Enhanced performance for domain-specific actions—classification, custom API interactions, industry-specific data interpretation
- **Faster speeds at lower cost**: Replace Sonnet or Opus in production deployments
- **Consistent, brand-aligned formatting**: Consistently structured outputs to exact specifications
- **Safe and secure**: Proprietary training data remains within customers' AWS environment

**Measured impact**: In a moderation use case, fine-tuning improved classification accuracy from 81.5% to **99.6%** while reducing tokens per query by **85%**.

## Customer Spotlight

- **SK Telecom**: 73% increase in positive feedback for agent responses; 37% improvement in KPIs for telecom-related tasks
- **Thomson Reuters**: Anticipated faster and more relevant results—"already seen positive results with Claude 3 Haiku"

## Getting Started

Preview available in US West (Oregon). Text-based fine-tuning supported with up to 32K token context. Vision capabilities planned for the future. Contact AWS account team or submit a support ticket.
