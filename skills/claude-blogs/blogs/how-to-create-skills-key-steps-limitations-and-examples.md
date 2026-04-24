# How to create Skills: Key steps, limitations, and examples

**Source:** https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples  
**Published:** November 19, 2025  
**Categories:** Claude Code, Claude apps

## Overview

Skills are custom instructions that extend Claude's capabilities for specific tasks or domains. They encode institutional knowledge, standardize outputs, and enable complex multi-step workflows.

## Creating a Skill in 5 Steps

### 1. Understand Core Requirements
Clarify what problem your skill solves with measurable outcomes. "Extract financial data from PDFs and format as CSV" is stronger than "Help with finance stuff."

### 2. Write the Name
Use lowercase with hyphens (e.g., `pdf-editor`, `brand-guidelines`). Keep it short and clear.

### 3. Write the Description Field (Most Critical)
Determines activation. Write from Claude's perspective.

**Weak**: "This skill helps with PDFs and documents."

**Strong**: "Comprehensive PDF manipulation toolkit for extracting text and tables, creating new PDFs, merging/splitting documents. When Claude needs to fill in a PDF form or programmatically process, generate, or analyze PDF documents at scale."

### 4. Write Main Instructions
Structure: overview, prerequisites, execution steps, examples, error handling, limitations.

### 5. Upload Your Skill
- **Claude.ai**: Settings → add custom skill (requires paid plan)
- **Claude Code**: Create `skills/` directory with SKILL.md files
- **API**: POST to `https://api.anthropic.com/v1/skills` with beta header `anthropic-beta: skills-2025-10-02`

## Testing Your Skill

Create a test matrix covering:
- Normal operations
- Edge cases (incomplete/unusual inputs)
- Out-of-scope requests (verify skill stays dormant)

## Skill Limitations

- Claude evaluates descriptions semantically—not keyword matching
- Multiple skills can activate simultaneously
- Avoid bloating context: use "menu" approach for multi-process skills that reference separate files

## Real-World Examples

- **DOCX Creation Skill**: Decision tree routing to appropriate workflows with progressive disclosure
- **Brand Guidelines Skill**: Provides exact hex codes, font names, size thresholds
- **Frontend Design Skill**: Creates distinctive, production-grade interfaces
