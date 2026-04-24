# Claude 3.5 Haiku on AWS Trainium2 and Model Distillation in Amazon Bedrock

**Source:** https://claude.com/blog/trainium2-and-distillation  
**Published:** December 3, 2024  
**Categories:** Product announcements, Claude Enterprise

## Overview

Claude 3.5 Haiku now supports latency-optimized inference on AWS Trainium2 via Amazon Bedrock, plus model distillation to transfer performance from larger to smaller models.

## Trainium2 Infrastructure

Anthropic collaborated with AWS on Project Rainier—an EC2 UltraCluster with hundreds of thousands of Trainium2 chips, delivering more than 5x the computing power (in exaflops) used to train current-generation models.

Claude 3.5 Haiku with latency optimization delivers **up to 60% faster inference**, suitable for code completions, content moderation, and chatbots.

**Pricing**: Available in US East (Ohio) via cross-region inference at $1/million input tokens and $5/million output tokens.

## Model Distillation

Transfers knowledge from larger models to smaller ones. With distillation, "Claude 3 Haiku can now achieve significant performance gains, reaching Claude 3.5 Sonnet-like accuracy for specific tasks—at the same price and speed."

The distillation process automates synthetic data generation, training, evaluation, and model hosting. Applies various data synthesis methods for custom tasks like RAG and data analysis.

## Pricing Updates

Claude 3.5 Haiku pricing reduced to **$0.80/million input tokens** and **$4/million output tokens** across all platforms.
