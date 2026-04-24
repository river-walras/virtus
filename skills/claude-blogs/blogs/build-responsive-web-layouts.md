# Build Responsive Web Layouts

**Source:** https://claude.com/blog/build-responsive-web-layouts  
**Published:** October 10, 2025  
**Categories:** Claude Code

## Overview

Responsive layouts frequently exhibit unpredictable behavior across viewport sizes. Claude and Claude Code help design and refactor responsive CSS systematically.

## Traditional Responsive Design Workflows

- **Manual media query writing**: Add breakpoints at 768px/1024px, override properties per breakpoint—requires experience to pick appropriate breakpoints for your content
- **Device testing**: Browser dev tools + physical devices, but can't cover every device-browser combination
- **Framework utilities**: Bootstrap/Tailwind provide responsive classes but enforce predefined breakpoints that may not match your design

## Using Claude for Responsive Design

**Claude.ai for Prototyping**: Accept layout requirements, generate complete responsive HTML/CSS with proper viewport configuration and media queries. Validates design patterns before investing in custom implementation.

**Claude Code for Codebase Refactoring**: Analyzes existing stylesheets across projects, identifies viewport-specific issues, and implements targeted fixes.

```bash
npm install -g @anthropic-ai/claude-code
claude
```

## Systematic Refactoring Workflow

Claude Code:
1. Audits layouts and identifies fixed-width styles causing overflow on smaller screens
2. Implements responsive alternatives (replacing fixed widths with `max-width` and flexible grid)
3. Tests at specific viewport sizes to confirm proper reflow
4. Generates Playwright test suites validating responsive behavior across device sizes

## Quick Start

Begin with Claude.ai for layout generation and pattern learning. For multi-stylesheet issues affecting entire applications, Claude Code provides systematic analysis and implementation across project files.
