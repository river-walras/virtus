# Long context prompting for Claude 2.1

**Source:** https://claude.com/blog/claude-2-1-prompting  
**Published:** December 6, 2023  
**Categories:** Product announcements

## Overview

Claude 2.1 performs well at retrieving information across its 200,000 token context window (roughly 500 pages). Compared to Claude 2.0: 30% reduction in incorrect answers, 3-4x lower rates of falsely claiming documents support unsupported claims.

## The Reluctance Challenge

Testing revealed Claude 2.1 sometimes refuses to answer questions about sentences appearing out of context within longer documents. Researchers embedded a sentence about San Francisco activities within Paul Graham essays—Claude frequently responded there was insufficient context to answer, rather than retrieving the relevant sentence.

## The Prompting Solution

A simple prompt modification produced dramatic improvements. Adding the instruction before Claude's response:

> "Here is the most relevant sentence in the context:"

Raised accuracy from **27% to 98%** on the original evaluation (90-95% on previously challenging tasks).

**Why it works**: Directing the model to identify relevant sentences first overrides its reluctance to answer based on individual sentences appearing displaced within longer documents.
