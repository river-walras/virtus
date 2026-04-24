# Claude can now use tools

**Source:** https://claude.com/blog/tool-use-ga  
**Published:** May 30, 2024  
**Categories:** Product announcements, Claude Platform

## Overview

Tool use is now generally available across the entire Claude 3 model family on the Anthropic Messages API, Amazon Bedrock, and Google Cloud Vertex AI. Claude can interact with external tools and APIs to perform tasks, manipulate data, and provide more dynamic and accurate responses.

## Tool Use Capabilities

Define a toolset and describe your request in natural language. Claude selects the appropriate tool:

- **Extract structured data**: Pull names, dates, and amounts from invoices
- **Natural language to API calls**: Enable self-service actions (e.g., "cancel subscription")
- **Database search**: Provide instant, accurate responses in support chatbots
- **Automate tasks**: Minimize errors in data entry or file management
- **Orchestrate subagents**: Automatically find optimal meeting times based on attendee availability

## Developer Experience Improvements

- **Streaming**: Reduces wait times for real-time responses in chatbots
- **Forced tool use**: Developers can specify which tools Claude should use
- **Image support**: Tools work with image inputs in live applications
- **Thinking tags**: Opus includes `<thinking>` tags to clarify reasoning and simplify debugging

## Customer Spotlights

- **StudyFetch**: 42% increase in positive human feedback for AI tutor after implementing tool use
- **Intuned**: "Claude 3 Haiku with tool use has been a game changer—quality, speed, and price combination is unmatched"
- **Hebbia**: Uses Claude 3 Haiku for live suggestions, automated prompt writing, and metadata extraction from long documents

## Getting Started

Available on Anthropic Messages API, Amazon Bedrock, and Google Cloud Vertex AI. Resources: official documentation, tool use tutorials, and Anthropic Cookbooks.
