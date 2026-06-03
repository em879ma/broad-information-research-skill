# Source Selection Tests

This file contains test cases for source selection to verify the skill correctly selects appropriate sources based on the research mode.

## Test Case 1: Academic Research Source Selection

### User Request
```
Help me find papers on GLP-1 and kidney transplant outcomes.
Time range: 2020-2026
```

### Expected Sources (from `references/source_registry.md`)
**Primary:**
- Google Scholar
- Semantic Scholar
- PubMed
- arXiv (for preprints, marked as lower confidence)

**Secondary:**
- Nature, Science, JAMA, NEJM (for verification)
- IEEE Xplore, ACM Digital Library (if engineering aspect)

### Pass Criteria
- [ ] Selects Google Scholar, PubMed, Semantic Scholar
- [ ] Does NOT select Reuters, Bloomberg (wrong mode)
- [ ] Does NOT select Crunchbase (wrong mode)
- [ ] Marks arXiv as "medium confidence" (preprint, not peer-reviewed)

---

## Test Case 2: Competitor Analysis Source Selection

### User Request
```
Analyze the competitors of my AI meeting assistant.
Compare features, pricing, and user reviews.
```

### Expected Sources (from `references/source_registry.md`)
**Primary:**
- Official websites (Otter.ai, Fireflies.ai, Fathom)
- Product pages, pricing pages, documentation

**Secondary:**
- App Store, Chrome Web Store, Product Hunt, G2 (user reviews)
- TechCrunch, 36Kr (media coverage)

### Pass Criteria
- [ ] Selects official websites first
- [ ] Selects G2, Product Hunt (review platforms)
- [ ] Does NOT select Google Scholar (wrong mode)
- [ ] Does NOT select government websites (unless company is gov-owned)

---

## Test Case 3: Domain News Source Selection

### User Request
```
What are the latest developments in AI regulation in China?
I need news from the past week.
```

### Expected Sources (from `references/source_registry.md`)
**Primary:**
- Company blogs, government websites (for official announcements)
- Reuters, AP, Bloomberg, Financial Times, The Verge (authoritative media)

**Secondary:**
- X (Twitter), Reddit, Hacker News, Zhihu (social/community, labeled as "early signals")

### Pass Criteria
- [ ] Selects Reuters, Bloomberg (authoritative media)
- [ ] Selects government websites (for regulation)
- [ ] Does NOT select Google Scholar (wrong mode)
- [ ] Labels social media as "early signals" or "low confidence"

---

## Test Case 4: Market Trends Source Selection

### User Request
```
Analyze the market trends of AI agents in 2026.
I need market size, growth rate, and investment signals.
```

### Expected Sources (from `references/source_registry.md`)
**Primary:**
- Gartner, IDC, CB Insights, PitchBook, McKinsey, Deloitte (market reports)
- Crunchbase, QiChaCha, ITJuzi (funding/M&A)

**Secondary:**
- Company websites, hiring pages, press releases (product/hiring signals)

### Pass Criteria
- [ ] Selects Gartner, IDC, CB Insights (market research)
- [ ] Selects Crunchbase, PitchBook (funding data)
- [ ] Does NOT select Google Scholar (wrong mode, unless academic market research)
- [ ] Does NOT select social media as primary source

---

## Test Case 5: Events and Conferences Source Selection

### User Request
```
Find AI events in Shanghai next month.
I need conferences, hackathons, and meetups.
```

### Expected Sources (from `references/source_registry_ai_events.md`)
**S-Level (prioritize):**
- aitop100.cn/activity/
- aitop100.cn/aicreation/

**A-Level (supplementary):**
- Luma, Juejin Events, Huodongjia, SenseTime Developer Events

**B-Level (manual verification):**
- Huodongxing, Hudongba, CSDN Events, Open Source China

**Company event pages:**
- Huawei, Alibaba Cloud, Tencent Cloud, Baidu AI

### Pass Criteria
- [ ] Prioritizes S-Level sources (aitop100.cn)
- [ ] Checks A-Level sources (Luma, Juejin)
- [ ] Checks B-Level sources (Huodongxing, CSDN)
- [ ] Checks company event pages (Huawei, Alibaba, etc.)
- [ ] Does NOT select Google Scholar (wrong mode)

---

## Test Case 6: Policy and Regulation Source Selection

### User Request
```
Track changes in AI regulation in the EU.
I need compliance requirements for AI companies.
```

### Expected Sources (from `references/source_registry.md`)
**Primary:**
- Government websites (eu.europa.eu, gov.uk, etc.)
- Regulatory agency websites

**Secondary:**
- Legal databases (PKULaw, Law.com.cn)
- Industry association websites, white papers

### Pass Criteria
- [ ] Selects government websites (EU, national)
- [ ] Selects regulatory agency websites
- [ ] Does NOT select social media as primary source
- [ ] Does NOT select company blogs (unless company is regulating itself)

---

## Test Case 7: Company or Organization Intelligence Source Selection

### User Request
```
Track recent developments of OpenAI.
I need information about funding, partnerships, and hiring trends.
```

### Expected Sources (from `references/source_registry.md`)
**Primary:**
- Company website, investor relations page, press releases, annual reports
- Crunchbase, LinkedIn, QiChaCha, TianYanCha (business databases)

**Secondary:**
- Business media, industry publications, CEO interviews
- Company social media accounts, executive LinkedIn/Twitter

### Pass Criteria
- [ ] Selects company website, investor relations page
- [ ] Selects Crunchbase, LinkedIn (business databases)
- [ ] Selects business media (TechCrunch, Bloomberg)
- [ ] Does NOT select Google Scholar (wrong mode)
- [ ] Does NOT select event platforms (unless company hosts events)

---

## Test Case 8: Mixed Mode Source Selection (Competitor + News)

### User Request
```
Compare Otter.ai and Fireflies.ai, and also find recent news about them.
```

### Expected Sources
**Competitor Analysis sources:**
- Official websites (Otter.ai, Fireflies.ai)
- G2, Product Hunt (reviews)

**Domain News sources:**
- TechCrunch, The Verge (recent news)
- Company blogs (for announcements)

### Pass Criteria
- [ ] Selects both competitor analysis sources AND news sources
- [ ] Does NOT confuse the two modes
- [ ] Correctly identifies which sources are for competitor analysis vs. news

---

## Test Case 9: Source Reliability Scoring

### User Request
```
Find information about OpenAI's GPT-5 release.
```

### Expected Reliability Scores
- **OpenAI official blog (https://openai.com/blog/...)**: Reliability = 5 (official source)
- **TechCrunch article (https://techcrunch.com/...)**: Reliability = 4 (authoritative media)
- **Individual tweet (https://twitter.com/user/status/...)**: Reliability = 2 (user-generated, weak source)

### Pass Criteria
- [ ] Assigns Reliability = 5 to OpenAI official blog
- [ ] Assigns Reliability = 4 to TechCrunch article
- [ ] Assigns Reliability = 2 to individual tweet
- [ ] Does NOT assign Reliability = 5 to tweet (common mistake)

---

## Test Case 10: Cross-Verification Requirement

### User Request
```
Find the release date of GPT-5.
```

### Expected Behavior
- Searches multiple sources (OpenAI blog, TechCrunch, The Verge)
- Cross-verifies the release date
- If sources conflict, reports conflict explicitly

### Pass Criteria
- [ ] Searches at least 2-3 sources
- [ ] If sources agree → reports date with "High confidence"
- [ ] If sources disagree → reports conflict explicitly
- [ ] Does NOT silently merge conflicting information

---

## Test Results Summary

| Test Case | Expected Sources | Actual Sources | Pass/Fail | Notes |
|-----------|-----------------|-----------------|-----------|-------|
| 1 (Academic) | Google Scholar, PubMed | | | |
| 2 (Competitor) | Official websites, G2 | | | |
| 3 (News) | Reuters, Bloomberg, govt websites | | | |
| 4 (Market) | Gartner, CB Insights, Crunchbase | | | |
| 5 (Events) | aitop100.cn, Luma, company pages | | | |
| 6 (Policy) | Government websites, regulatory agencies | | | |
| 7 (Company) | Company website, Crunchbase, media | | | |
| 8 (Mixed) | Both competitor + news sources | | | |
| 9 (Scoring) | Correct reliability scores | | | |
| 10 (Cross-verify) | Cross-verification performed | | | |

---

## Notes

- Update this file as new test cases are added
- Mark each test as Pass/Fail after running
- Add notes on why a test failed (wrong source selected, missing source, etc.)
- Use these test cases to improve `references/source_registry.md`
