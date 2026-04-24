# How Carta Healthcare gets AI to reason like a clinical abstractor

**Source:** https://claude.com/blog/carta-healthcare-clinical-abstractor  
**Published:** April 8, 2026  
**Categories:** Enterprise AI, Claude Platform, Business

## Overview

Carta Healthcare built Lighthouse, a clinical data abstraction platform that processes 22,000 surgical cases annually, achieving 99% accuracy through strategic use of Claude and context engineering.

## The Clinical Data Abstraction Problem

Clinical registries depend on standardized data to benchmark outcomes and identify care gaps. Converting patient records into registry-ready data requires trained abstractors who read through charts, reconcile conflicting documentation, and apply clinical judgment where records are ambiguous.

A single routine case takes approximately 60 minutes to abstract; complex cases require 5-6 hours. Large health systems spend over 11,000 hours annually on abstraction for a single registry program.

Traditional automation tools fail because clinical documentation lacks consistency. The same finding might appear as structured data at one hospital and buried in free-text notes at another.

## From Pattern Matching to Clinical Reasoning

Carta Healthcare initially used NLP-based extraction, but this proved inadequate for nuanced clinical questions such as:
- "What was the most recent glucose before the procedure?"
- "Was aspirin prescribed at discharge?"

These questions require understanding temporal relationships, distinguishing between different documentation contexts, and weighing conflicting evidence—capabilities beyond pattern recognition.

## Context Engineering as Core Infrastructure

The breakthrough came from context engineering—providing AI systems with precisely scoped, well-organized information:

**Patient-Specific Time Windows**: Rather than asking "find a weight in the record," the system specifies "find weight documented before [specific procedure start time]."

**Document Sequencing**: Clinical records are ordered by relevance and temporal relationship to the question, not simply by chronology.

**Temporal Logic**: The system enforces clinical reasoning rules by embedding temporal constraints in the context provided to the model.

## Results

- 99% accuracy across 22,000 cases annually
- Scalability across 125+ hospitals with varying documentation practices
