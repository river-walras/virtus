# How Kepler built verifiable AI for financial services with Claude

**Source:** https://claude.com/blog/how-kepler-built-verifiable-ai-for-financial-services-with-claude  
**Published:** April 30, 2026  
**Categories:** Enterprise AI, Claude Platform

## Overview

This startup story explains how Kepler uses Claude as a reasoning layer for verifiable financial research. Kepler indexes SEC filings, earnings call transcripts, IR presentations, consensus estimates, private documents, and company data so analysts can ask plain-English questions and trace answers back to source documents.

## Scale

Kepler reports indexing more than 26 million SEC filings, 50 million public documents, 1 million private documents, and 14,000+ companies across 27 global markets in under three months.

## Why Claude

Kepler benchmarked frontier models and found Claude best at long, multi-step financial reasoning where constraints must persist across several stages. Claude was also more likely to flag ambiguity and ask the analyst to decide rather than silently choosing an interpretation.

## Architecture

Kepler separates Claude's reasoning from deterministic infrastructure:

- Claude interprets user intent, decomposes tasks, and produces structured plans.
- Deterministic systems handle retrieval, formula execution, period resolution, provenance, and access control.
- Opus 4.7 handles complex reasoning; Sonnet 4.6 handles constrained high-throughput stages.
- Automated evaluations test prompt changes, model upgrades, and context changes before production.

## Best Practices

Kepler recommends giving Claude the right job, matching models to pipeline stages, investing in evaluation before prompt tweaks, and building provenance from day one.

## When to Use This Blog

Use this source for financial-services AI architecture, verifiable AI, provenance, deterministic execution around Claude, financial research agents, multi-stage model pipelines, and Kepler customer-story details.
