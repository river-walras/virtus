# Best practices for prompt engineering

**Source:** https://claude.com/blog/best-practices-for-prompt-engineering  
**Published:** November 10, 2025  
**Categories:** Agents, Claude apps, Productivity

## Core Techniques

### Be Explicit and Clear
State exactly what you want. Lead with direct action verbs (Write, Analyze, Generate, Create). Skip preambles.

### Provide Context and Motivation
Explaining *why* something matters helps models deliver more targeted responses. Instead of "Never use bullet points," say "I prefer flowing prose because it feels more conversational."

### Be Specific
Include clear constraints (word count, format), relevant context (audience, goal), desired output structure, and requirements.

### Use Examples (One-shot / Few-shot)
Examples clarify subtle requirements that resist pure description. Start with one example; add more only if results remain inconsistent.

### Give Permission to Express Uncertainty
"Analyze this financial data and identify trends. If data is insufficient for conclusions, say so rather than speculating."

## Advanced Techniques

### Prefill the AI's Response
Start the AI's response to guide format, tone, or structure. To enforce JSON output, begin with an opening brace so the AI continues from there.

### Chain of Thought Prompting
Request step-by-step reasoning before answering. Three implementations:
1. **Basic**: Add "Think step-by-step"
2. **Guided**: Provide specific reasoning stages
3. **Structured**: Use `<thinking>` tags to separate reasoning from final answer

### Prompt Chaining
Break complex tasks into smaller sequential steps. Each prompt handles one stage, with output feeding into the next.

**Trade-off**: Increases latency through multiple calls but dramatically improves accuracy for complex tasks.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Response too generic | Add specificity, examples, or request comprehensive output |
| Inconsistent format | Add examples or use prefilling |
| Made-up information | Give explicit permission to say "I don't know" |
| Suggests changes instead of implementing | Be explicit: "Change this function" not "Suggest changes" |

## Modern Considerations

- XML tags and heavy role prompting are less necessary with modern models
- Don't over-engineer—longer prompts aren't always better
- Prompt engineering is the foundation for context engineering
