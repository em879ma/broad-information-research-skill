# Output Quality Tests

This file contains test cases for output quality to verify the skill generates well-structured, accurate, and useful outputs.

## Test Case 1: Academic Research Output Quality

### User Request
```
Help me find papers on GLP-1 and kidney transplant outcomes.
Time range: 2020-2026
```

### Expected Output Structure (using `academic_research_template.md`)
1. **Search Scope** section with:
   - Research question clearly stated
   - Field specified
   - Time range specified
   - Inclusion/exclusion criteria listed

2. **Literature Matrix** with:
   - At least 5 papers
   - All required columns filled (Paper, Year, Venue, Data/Method, Main Finding, Relevance, Limitation, Confidence)
   - Relevance scores 1-5
   - Confidence labels (High/Medium/Low)

3. **Thematic Synthesis** with:
   - At least 3 themes
   - Papers listed under each theme
   - Key findings synthesized
   - Evidence strength stated

4. **Research Gaps** with:
   - At least 3 gaps identified
   - Evidence for each gap
   - Potential impact stated

5. **Suggested Next Searches** with:
   - At least 3 suggested searches
   - Rationale for each
   - Expected outcome

### Pass Criteria
- [ ] Literature Matrix has ≥5 papers
- [ ] All papers have Relevance score (1-5)
- [ ] All papers have Confidence label (High/Medium/Low)
- [ ] At least 3 themes in Thematic Synthesis
- [ ] At least 3 Research Gaps identified
- [ ] At least 3 Next Searches suggested
- [ ] Output uses academic_research_template.md structure
- [ ] No hallucinated papers (all papers can be verified from sources)

---

## Test Case 2: Competitor Analysis Output Quality

### User Request
```
Analyze the competitors of my AI meeting assistant.
Compare features, pricing, and user reviews.
Competitors: Otter.ai, Fireflies.ai, Fathom
```

### Expected Output Structure (using `competitor_analysis_template.md`)
1. **Competitor Map** with:
   - All 3 competitors listed
   - Type (Direct/Indirect/Emerging)
   - Positioning statement
   - Target users
   - Key features (top 5)
   - Pricing model and amount
   - Evidence source
   - Confidence label

2. **Detailed Comparison** with:
   - At least 3 dimensions (e.g., Core Features, Pricing, User Experience)
   - Comparison table for each dimension
   - User product included in comparison

3. **Strategic Takeaways** with:
   - At least 3 takeaways
   - Observation, Evidence, Implication for each

4. **Gaps and Opportunities** with:
   - At least 2 gaps identified
   - At least 2 opportunities identified
   - Evidence and recommended action for each

### Pass Criteria
- [ ] Competitor Map has all 3 competitors
- [ ] All competitors have Confidence label
- [ ] At least 3 comparison dimensions
- [ ] User product included in comparison
- [ ] At least 3 Strategic Takeaways
- [ ] At least 2 Gaps and 2 Opportunities
- [ ] Output uses competitor_analysis_template.md structure
- [ ] No hallucinated features (all can be verified from sources)

---

## Test Case 3: Domain News Output Quality

### User Request
```
What are the latest developments in AI regulation in China?
I need news from the past month.
```

### Expected Output Structure (using `news_digest_template.md`)
1. **Key News** with:
   - At least 5 news items
   - All required columns (Date, Event, Source, What happened, Why it matters, Confidence)
   - Sorted by date (newest first) or importance

2. **Timeline** with:
   - News items arranged chronologically
   - Source and "Why it matters" for each

3. **Implications** with:
   - At least 3 implications
   - Observation, Evidence, Potential impact for each

4. **Unverified / Low-Confidence Items** with:
   - Items that are potentially relevant but low confidence
   - Reason for low confidence stated

### Pass Criteria
- [ ] Key News has ≥5 items
- [ ] All items have Confidence label
- [ ] Timeline is chronological
- [ ] At least 3 Implications
- [ ] Unverified Items section present (even if empty)
- [ ] Output uses news_digest_template.md structure
- [ ] No hallucinated news (all can be verified from sources)

---

## Test Case 4: Market Trend Output Quality

### User Request
```
Analyze the market trends of AI agents in 2026.
What are the emerging opportunities and risks?
```

### Expected Output Structure (using `market_trend_template.md`)
1. **Executive Summary** with:
   - At least 3 key findings
   - Overall trend direction (Upward/Downward/Stable/Volatile)
   - Confidence label

2. **Key Trends** with:
   - At least 3 trends
   - All required columns (Trend, Evidence, Representative players, Market signal, Opportunity, Risk, Confidence)

3. **Signals Worth Monitoring** with:
   - At least 3 signals
   - Why it matters and suggested monitoring source for each

4. **Detailed Analysis** for each trend with:
   - Overview, Evidence, Market Signals
   - Opportunities and Risks
   - Representative Players
   - Confidence Assessment

5. **Uncertainties** with:
   - At least 3 uncertainties
   - Impact if resolved, How to resolve, Timeline for each

### Pass Criteria
- [ ] Executive Summary has ≥3 key findings
- [ ] At least 3 Key Trends
- [ ] All trends have Confidence label
- [ ] At least 3 Signals Worth Monitoring
- [ ] Detailed Analysis for each trend
- [ ] At least 3 Uncertainties
- [ ] Output uses market_trend_template.md structure
- [ ] No hallucinated trends (all supported by evidence)

---

## Test Case 5: Event Collection Output Quality

### User Request
```
Find AI events in Shanghai next month.
I'm looking for conferences, hackathons, and meetups.
```

### Expected Output Structure (using `event_collection_template.md`)
1. **Verified Events** with:
   - At least 3 events (if available)
   - All required columns (Event, Date, City, Venue, Organizer, Type, Registration status, Link, Reliability)
   - Sorted by date or reliability

2. **Event Details** for each verified event with:
   - Basic Information (Date, Time, City, Venue, Organizer, Event type)
   - Registration (Status, Link, Deadline, Fee, Capacity)
   - Description (Theme, Target audience, Agenda, Speakers, Language)
   - Verification (Source, Cross-verified, Last verified, Confidence)

3. **Excluded / Low-Confidence Events** with:
   - Events excluded and reason
   - Source for each

4. **Event Statistics** with:
   - Total events found, Verified events, Excluded events
   - High/Medium/Low confidence counts

### Pass Criteria
- [ ] Verified Events has ≥3 events (if available)
- [ ] All events have Reliability score (S/A/B)
- [ ] All events have Confidence label
- [ ] Event Details complete for each verified event
- [ ] Excluded Events section present
- [ ] Event Statistics present
- [ ] Output uses event_collection_template.md structure
- [ ] No hallucinated events (all can be verified from sources)

---

## Test Case 6: Confidence Scoring Accuracy

### User Request
```
Find information about OpenAI's GPT-5 release.
```

### Expected Confidence Scoring
1. **High Confidence:**
   - Source: OpenAI official blog (Reliability=5)
   - Relevance: Directly answers the question (Relevance=5)
   - Freshness: Within time range (Freshness=5)
   - Cross-verified: Confirmed by TechCrunch and The Verge
   → **High confidence**

2. **Medium Confidence:**
   - Source: TechCrunch article (Reliability=4)
   - Relevance: Strongly related but not complete (Relevance=4)
   - Freshness: 6 months ago (Freshness=4)
   - Only one strong source (not cross-verified)
   → **Medium confidence**

3. **Low Confidence:**
   - Source: Individual tweet (Reliability=2)
   - Relevance: Weakly related (Relevance=2)
   - Freshness: Date unclear (Freshness=?)
   - Only one weak source
   → **Low confidence**

### Pass Criteria
- [ ] High confidence items have Reliability 4-5 AND Relevance 4-5 AND Freshness 4-5
- [ ] Medium confidence items have some limitation (Reliability 3-4 OR Relevance 3-4 OR Freshness 3-4 OR only one source)
- [ ] Low confidence items have Reliability 1-2 OR conflict OR unclear date OR limited evidence
- [ ] Confidence labels match the scoring rules in `references/reliability_scoring.md`

---

## Test Case 7: Deduplication and Conflict Reporting

### User Request
```
Find news about AI regulation in China.
```

### Scenario: Multiple Sources Report Same Event
- **Source A (Reuters):** "China releases AI regulation draft on June 1, 2026"
- **Source B (Bloomberg):** "China releases AI regulation draft on June 1, 2026"
- **Source C (Individual blog):** "China releases AI regulation on May 30, 2026"

### Expected Behavior
- **Deduplication:** Keep Source A (most official) and discard Source C (weak source, conflicting date)
- **Cross-verification:** Source A and Source B agree → High confidence
- **Conflict reporting:** If sources disagree, report conflict explicitly (don't merge silently)

### Pass Criteria
- [ ] Keeps most official source when multiple sources report same event
- [ ] Discards duplicates
- [ ] Reports conflict explicitly when sources disagree
- [ ] Does NOT merge conflicting information silently
- [ ] Labels conflicting information as "conflicting" or "disputed"

---

## Test Case 8: Output Template Adherence

### User Request (any mode)
```
[Any valid request for any of the 7 modes]
```

### Expected Behavior
- **Mode 1 (Academic Research):** Uses `academic_research_template.md`
- **Mode 2 (Competitor Analysis):** Uses `competitor_analysis_template.md`
- **Mode 3 (Domain News):** Uses `news_digest_template.md`
- **Mode 4 (Market Trends):** Uses `market_trend_template.md`
- **Mode 5 (Events and Conferences):** Uses `event_collection_template.md`
- **Mode 6 (Policy and Regulation):** Uses `policy_regulation_template.md` (if available)
- **Mode 7 (Company Intelligence):** Uses `company_intelligence_template.md` (if available)

### Pass Criteria
- [ ] Output matches the correct template for the mode
- [ ] All required sections from template are present
- [ ] Output structure follows template structure
- [ ] No missing sections from template

---

## Test Case 9: Source Citation and Transparency

### User Request (any mode)
```
[Any valid request]
```

### Expected Behavior
- **All claims backed by sources:** Every claim in output has a source citation
- **Source URLs included:** Where possible, source URLs are included
- **Confidence labeled:** Each item has confidence label
- **Limitations noted:** If information is incomplete or uncertain, this is noted

### Pass Criteria
- [ ] All claims have source citations
- [ ] Source URLs included where available
- [ ] Confidence labels present for all items
- [ ] Limitations and uncertainties noted
- [ ] No unsupported claims ("hallucinations")

---

## Test Case 10: Time Range Adherence

### User Request
```
Find papers on GLP-1 and kidney transplant from 2020-2026.
```

### Expected Behavior
- **Time filter applied:** Only papers from 2020-2026 included
- **Expired items excluded:** Items outside time range excluded (unless user asks for historical)
- **Time range stated:** Search Scope section states time range

### Pass Criteria
- [ ] Only papers from 2020-2026 included
- [ ] Papers outside time range excluded
- [ ] Time range stated in Search Scope
- [ ] If user asks for "latest" or "recent," most recent items prioritized

---

## Test Results Summary

| Test Case | Expected Quality | Actual Quality | Pass/Fail | Notes |
|-----------|-----------------|----------------|-----------|-------|
| 1 (Academic Output) | Structured, complete | | | |
| 2 (Competitor Output) | Structured, complete | | | |
| 3 (News Output) | Structured, complete | | | |
| 4 (Market Output) | Structured, complete | | | |
| 5 (Event Output) | Structured, complete | | | |
| 6 (Confidence Scoring) | Accurate scoring | | | |
| 7 (Deduplication/Conflict) | Correct handling | | | |
| 8 (Template Adherence) | Correct template used | | | |
| 9 (Source Citation) | Transparent, cited | | | |
| 10 (Time Range) | Time filter applied | | | |

---

## Notes

- Update this file as new test cases are added
- Mark each test as Pass/Fail after running
- Add notes on why a test failed (missing sections, hallucinated content, etc.)
- Use these test cases to improve output templates (`assets/output_templates/`)
