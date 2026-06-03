# Routing Tests

This file contains test cases for task classification (routing) to verify the skill correctly identifies the user's intent.

## Test Case 1: Academic Research (Clear)

### User Request
```
Help me find recent papers on GLP-1 and kidney transplant outcomes.
I need literature published between 2020-2026.
```

### Expected Classification
- **Mode:** Academic Research
- **Topic:** GLP-1 and kidney transplant outcomes
- **Time range:** 2020-2026
- **Output format:** Literature matrix + thematic synthesis

### Classification Keywords Matched
- "papers" → Academic Research
- "find recent papers" → Academic Research
- "literature" → Academic Research

### Pass Criteria
- [ ] Correctly classifies as "Academic Research"
- [ ] Extracts topic: "GLP-1 and kidney transplant outcomes"
- [ ] Extracts time range: "2020-2026"
- [ ] Does NOT ask clarifying question (clear intent)

---

## Test Case 2: Competitor Analysis (Clear)

### User Request
```
I'm developing an AI meeting assistant and need to analyze the competitive landscape.
Please compare Otter.ai, Fireflies.ai, and Fathom.
```

### Expected Classification
- **Mode:** Competitor Analysis
- **Target:** AI meeting assistant (user's product)
- **Competitors:** Otter.ai, Fireflies.
### Classification Keywords Matched
- "competitive landscape" → Competitor Analysis
- "compare" → Competitor Analysis
- "Otter.ai, Fireflies.ai, Fathom" → Competitor names

### Pass Criteria
- [ ] Correctly classifies as "Competitor Analysis"
- [ ] Extracts target: "AI meeting assistant"
- [ ] Extracts competitors: ["Otter.ai", "Fireflies.ai", "Fathom"]
- [ ] Does NOT ask clarifying question (clear intent)

---

## Test Case 3: Domain News (Clear)

### User Request
```
What are the latest developments in AI regulation in China?
I need news from the past month.
```

### Expected Classification
- **Mode:** Domain News
- **Topic:** AI regulation in China
- **Time range:** Past month
- **Output format:** News digest with timeline

### Classification Keywords Matched
- "latest developments" → Domain News
- "news" → Domain News
- "past month" → Time-sensitive

### Pass Criteria
- [ ] Correctly classifies as "Domain News"
- [ ] Extracts topic: "AI regulation in China"
- [ ] Extracts time range: "past month"
- [ ] Does NOT ask clarifying question (clear intent)

---

## Test Case 4: Market Trends (Clear)

### User Request
```
Analyze the market trends of AI agents in 2026.
What are the emerging opportunities and risks?
```

### Expected Classification
- **Mode:** Market Trends
- **Domain:** AI agents
- **Time range:** 2026
- **User intent:** Identify opportunities and risks

### Classification Keywords Matched
- "market trends" → Market Trends
- "emerging opportunities" → Market Trends
- "risks" → Market Trends

### Pass Criteria
- [ ] Correctly classifies as "Market Trends"
- [ ] Extracts domain: "AI agents"
- [ ] Extracts time range: "2026"
- [ ] Does NOT ask clarifying question (clear intent)

---

## Test Case 5: Events and Conferences (Clear)

### User Request
```
Find AI events in Shanghai next month.
I'm looking for conferences, hackathons, and meetups.
```

### Expected Classification
- **Mode:** Events and Conferences
- **Topic:** AI events
- **City:** Shanghai
- **Time range:** Next month

### Classification Keywords Matched
- "events" → Events and Conferences
- "conferences" → Events and Conferences
- "hackathons" → Events and Conferences
- "meetups" → Events and Conferences

### Pass Criteria
- [ ] Correctly classifies as "Events and Conferences"
- [ ] Extracts topic: "AI events"
- [ ] Extracts city: "Shanghai"
- [ ] Extracts time range: "next month"
- [ ] Does NOT ask clarifying question (clear intent)

---

## Test Case 6: Policy and Regulation (Clear)

### User Request
```
Help me track changes in AI regulation in the EU.
I need to understand the compliance requirements for AI companies.
```

### Expected Classification
- **Mode:** Policy and Regulation
- **Topic:** AI regulation in EU
- **Region:** EU
- **User intent:** Compliance requirements

### Classification Keywords Matched
- "regulation" → Policy and Regulation
- "compliance" → Policy and Regulation
- "AI regulation" → Policy and Regulation

### Pass Criteria
- [ ] Correctly classifies as "Policy and Regulation"
- [ ] Extracts topic: "AI regulation in EU"
- [ ] Extracts region: "EU"
- [ ] Does NOT ask clarifying question (clear intent)

---

## Test Case 7: Company or Organization Intelligence (Clear)

### User Request
```
Track recent developments of OpenAI.
I need information about funding, partnerships, and hiring trends.
```

### Expected Classification
- **Mode:** Company or Organization Intelligence
- **Company:** OpenAI
- **Focus areas:** Funding, partnerships, hiring trends

### Classification Keywords Matched
- "OpenAI" (company name) → Company or Organization Intelligence
- "funding" → Company or Organization Intelligence
- "partnerships" → Company or Organization Intelligence
- "hiring trends" → Company or Organization Intelligence

### Pass Criteria
- [ ] Correctly classifies as "Company or Organization Intelligence"
- [ ] Extracts company: "OpenAI"
- [ ] Extracts focus areas: ["funding", "partnerships", "hiring trends"]
- [ ] Does NOT ask clarifying question (clear intent)

---

## Test Case 8: Ambiguous Request (Should Ask Clarifying Question)

### User Request
```
Tell me about AI agents.
```

### Expected Classification
- **Mode:** Ambiguous (could be Academic Research, Domain News, Market Trends, or Company Intelligence)
- **Should ask:** Clarifying question

### Possible Clarifying Questions
- "Do you want academic papers, recent news, market trends, or company information about AI agents?"
- "Are you looking for research papers, latest news, market analysis, or company updates about AI agents?"

### Pass Criteria
- [ ] Does NOT classify immediately (ambiguous)
- [ ] Asks clarifying question
- [ ] Offers specific options (academic papers, news, market trends, company info)

---

## Test Case 9: Ambiguous but Inferable (Should Infer)

### User Request
```
Find recent papers about AI agent frameworks.
```

### Expected Classification
- **Mode:** Academic Research (inferred from "papers")
- **Topic:** AI agent frameworks
- **Time range:** Recent (unspecified, use default)

### Classification Keywords Matched
- "papers" → Academic Research
- "recent" → Time-sensitive

### Pass Criteria
- [ ] Correctly classifies as "Academic Research" (inferred)
- [ ] Does NOT ask clarifying question (can infer from "papers")
- [ ] Extracts topic: "AI agent frameworks"

---

## Test Case 10: Mixed Keywords (Should Prioritize)

### User Request
```
I need to compare AI meeting assistant products and also find recent news about them.
```

### Expected Classification
- **Mode:** Competitor Analysis (prioritize "compare" over "news")
- **Topic:** AI meeting assistant products
- **Secondary intent:** Domain News (recent news)

### Classification Keywords Matched
- "compare" → Competitor Analysis (priority)
- "AI meeting assistant products" → Competitor Analysis
- "recent news" → Domain News (secondary)

### Pass Criteria
- [ ] Correctly classifies as "Competitor Analysis" (primary)
- [ ] Notes secondary intent: "Domain News (recent news)"
- [ ] Does NOT ask clarifying question (can handle both)

---

## Test Results Summary

| Test Case | Expected Mode | Actual Mode | Pass/Fail | Notes |
|-----------|----------------|-------------|-----------|-------|
| 1 | Academic Research | | | |
| 2 | Competitor Analysis | | | |
| 3 | Domain News | | | |
| 4 | Market Trends | | | |
| 5 | Events and Conferences | | | |
| 6 | Policy and Regulation | | | |
| 7 | Company Intelligence | | | |
| 8 | Ambiguous (ask question) | | | |
| 9 | Academic Research (inferred) | | | |
| 10 | Competitor Analysis (prioritized) | | | |

---

## Notes

- Update this file as new test cases are added
- Mark each test as Pass/Fail after running
- Add notes on why a test failed (misclassification, missing extraction, etc.)
- Use these test cases to improve the task taxonomy (`references/task_taxonomy.md`)
