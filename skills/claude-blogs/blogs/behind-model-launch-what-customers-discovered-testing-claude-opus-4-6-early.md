# Behind the Model Launch: What Customers Discovered Testing Claude Opus 4.6 Early

**Source:** https://claude.com/blog/behind-model-launch-what-customers-discovered-testing-claude-opus-4-6-early  
**Published:** February 9, 2026  
**Categories:** Enterprise AI

## Overview

Before Claude Opus 4.6 became publicly available, four major companies—Harvey, bolt.new, Shopify, and Lovable—participated in early access testing.

## Key Results

### Harvey's Legal Achievements
Harvey's BigLaw Bench showed **90.2% performance**—the first Anthropic model surpassing 90% on this benchmark. 40% of tasks received perfect scores.

### bolt.new's Code Quality Improvements
Opus 4.6 identified a complex bug immediately: eight parallel HubSpot API searches firing simultaneously, with additional queries bypassing rate limits through raw fetch instead of the project's protected wrapper. The bug had resisted five previous attempts with earlier models.

### Shopify's Development Acceleration
Staff Engineer Paulo Arruda: "I asked Opus 4.6 to move something from one page into another menu item—that's all I said. It not only moved it but went above and beyond, creating details I hadn't specified. It anticipated my next ask."

Ben Lafferty tasked the model with porting a large TypeScript library to Ruby. The model created a test shim and ported nearly the entire specification in one attempt while validating against existing tests.

### Lovable's Autonomous Capabilities
Alexandre Pesant: "You can feel a difference in autonomy" when the model uses the browser and tests independently within Lovable's environment.

## Key Quotes

- **Garrett Serviss (bolt.new)**: "Opus 4.6 diagnosed bugs on the first try that we'd failed to fix across five-plus attempts with previous models. The jump in reasoning depth is real."
- **Ben Lafferty (Shopify)**: "Opus 4.6 is the first model that feels like a true collaborator in my day-to-day work."
- **Fabian Hedin (Lovable co-founder)**: "Claude Opus 4.6 is an uplift in design quality and more autonomous."
