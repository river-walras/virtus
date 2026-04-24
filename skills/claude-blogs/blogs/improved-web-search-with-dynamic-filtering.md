# Increase Web Search Accuracy and Efficiency with Dynamic Filtering

**Source:** https://claude.com/blog/improved-web-search-with-dynamic-filtering  
**Published:** February 17, 2026  
**Categories:** Product announcements, Claude Platform, Agents

## Overview

Anthropic has released improved web search and web fetch tools that use code execution to dynamically filter results before they reach the context window, delivering better accuracy while reducing token consumption.

## How Dynamic Filtering Works

Rather than loading full HTML files into context, Claude now "automatically writes and executes code to post-process query results." The model can filter search findings before they consume token budget, keeping only relevant information.

## Performance Improvements

**BrowseComp Results:**
- Sonnet 4.6: improved from 33.3% to 46.6% accuracy
- Opus 4.6: improved from 45.3% to 61.6% accuracy

**DeepsearchQA Results:**
- Sonnet 4.6: F1 score improved from 52.6% to 59.4%
- Opus 4.6: F1 score improved from 69.8% to 77.3%

Average: **11% improvement while using 24% fewer input tokens**.

## Additional Tools Released (GA)

- **Code Execution**: Sandbox environment for agents to analyze data or filter context
- **Memory**: Persistent file storage across conversations
- **Programmatic Tool Calling**: Execute complex multi-tool workflows
- **Tool Search**: Dynamically discover tools from large libraries
- **Tool Use Examples**: Sample calls demonstrating proper usage patterns
