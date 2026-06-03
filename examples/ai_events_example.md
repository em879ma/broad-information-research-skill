# AI Events Example

## User Request

```
I need to find AI-related events in Shanghai next month (July 2026).
Please collect:
1. Conferences and summits
2. Hackathons and competitions
3. Meetups and workshops
4. Webinars (if online events are included)

For each event, I need:
- Event name and date
- Venue and organizer
- Registration status and link
- Confidence level (High/Medium/Low)

Please verify the information from multiple sources.
```

## Agent Response (Summary)

The agent classified this as **Events and Conferences** mode and performed the following steps:

### 1. Task Classification
- **Mode:** Events and Conferences
- **Topic:** AI events
- **City:** Shanghai
- **Time range:** July 2026
- **Event types:** Conferences, hackathons, meetups, webinars

### 2. Source Selection
Used `references/source_registry_ai_events.md` to select:
- **S-Level (prioritize):** aitop100.cn/activity/, aitop100.cn/aicreation/
- **A-Level (supplementary):** Luma, Juejin Events, Huodongjia, SenseTime Developer Events
- **B-Level (manual verification):** Huodongxing, Hudongba, CSDN Events, Open Source China
- **Company event pages:** Huawei, Alibaba Cloud, Tencent Cloud, Baidu AI
- **Annual fixed events:** WAIC (usually July), QCon (may have Shanghai edition)

### 3. Search Queries Generated
```
1. "AI 活动 上海 2026年7月 报名"
2. "AIGC 峰会 上海 2026"
3. "AI 黑客松 报名 上海 7月"
4. "开发者大会 AI 上海 2026"
5. "AI conference Shanghai July 2026"
6. "WAIC 2026 Shanghai"
7. "AI hackathon Shanghai register"
```

### 4. Verified Events

| Event | Date | City | Venue | Organizer | Type | Registration status | Link | Reliability |
|-------|------|------|-------|------------|------|---------------------|------|-------------|
| **WAIC 2026 (World AI Conference)** | 2026-07-08 to 2026-07-10 | Shanghai | Shanghai World Expo Exhibition & Convention Center | Ministry of Industry and Information Technology + Shanghai Municipal Government | Conference / Summit | Open (until 2026-07-05) | https://www.worldaic.com.cn/ | S (Official website) |
| **AI Hackathon Shanghai 2026** | 2026-07-15 to 2026-07-16 | Shanghai | Zhangjiang Hi-Tech Park | Shanghai AI Industry Association + AITOP100 | Hackathon | Open (until 2026-07-10) | https://aitop100.cn/activity/hackathon-sh-2026 | S (Structured data) |
| **Baidu AI Developer Salon (Shanghai)** | 2026-07-22 | Shanghai | Baidu Shanghai Office (Pudong) | Baidu AI Cloud | Meetup / Workshop | Open (until 2026-07-20) | https://cloud.baidu.com/salon/shanghai-2026-07 | A (Company website) |
| **AIGC Summit Shanghai** | 2026-07-28 | Shanghai | Shanghai International Convention Center | AITOP100 + Juejin Community | Summit | Not yet open (opens 2026-07-10) | https://aitop100.cn/aicreation/summit-2026-07 | S (Structured data) |
| **AI Meetup: LLM Applications** | 2026-07-05 | Shanghai | Xuhui District Co-working Space | Shanghai AI Developers Community (volunteer) | Meetup | Open (until full) | https://www.huodongxing.com/event/12345678 | B (Community event, needs verification) |

### 5. Event Details

#### WAIC 2026 (World AI Conference)
**Basic Information:**
- **Date:** 2026-07-08 to 2026-07-10
- **Time:** 09:00 - 18:00 (all days)
- **City:** Shanghai
- **Venue:** Shanghai World Expo Exhibition & Convention Center
- **Organizer:** Ministry of Industry and Information Technology + Shanghai Municipal Government
- **Event type:** Conference / Summit

**Registration:**
- **Status:** Open (until 2026-07-05)
- **Registration link:** https://www.worldaic.com.cn/register
- **Registration fee:** ¥2,800 (standard), ¥1,500 (student)
- **Capacity:** 50,000 attendees

**Description:**
- **Theme:** "Intelligent Connectivity, Infinite Possibilities"
- **Target audience:** AI researchers, industry leaders, policymakers, developers
- **Agenda:** https://www.worldaic.com.cn/agenda-2026
- **Speakers:** 200+ speakers (incl. Yann LeCun, Andrew Ng, Pony Ma)
- **Language:** Primarily Chinese, with English translation for keynotes

**Verification:**
- **Source:** Official website (worldaic.com.cn)
- **Cross-verified:** Yes (36Kr, Caixin, Reuters reported)
- **Last verified:** 2026-06-02
- **Confidence:** High

**Notes:**
- Visa support available (contact organizer)
- Airport pickup available for international speakers
- Accommodation discount at partner hotels

#### AI Hackathon Shanghai 2026
[Similar detailed structure as above]

#### Baidu AI Developer Salon (Shanghai)
[Similar detailed structure as above]

#### AIGC Summit Shanghai
[Similar detailed structure as above]

#### AI Meetup: LLM Applications
[Similar detailed structure as above]

### 6. Excluded / Low-Confidence Events

| Event | Reason excluded | Source |
|-------|-----------------|--------|
| "AI Finance Summit Shanghai" (claimed July 15) | Conflicting dates (source A says July 15, source B says August 15) | WeChat public account (unverified) |
| "AI Education Workshop" (claimed July 20) | Expired (already passed, user asked for July events) | Zhihu article |
| "Shanghai AI Job Fair" (claimed July 25) | Low reliability source (individual tweet, no official announcement) | Twitter/X post |

### 7. Event Statistics

- **Total events found:** 12
- **Verified events:** 5
- **Excluded events:** 7
- **High confidence events:** 4
- **Medium confidence events:** 1
- **Low confidence events:** 0

### 8. Source Summary

| Source | Events found | Verified | Reliability |
|--------|--------------|----------|------------|
| aitop100.cn/activity/ | 5 | 3 | S |
| aitop100.cn/aicreation/ | 3 | 2 | S |
| WAIC official website | 1 | 1 | S |
| Baidu AI Cloud website | 1 | 1 | A |
| Huodongxing.com | 2 | 1 | B |
| WeChat public accounts | 4 | 0 | Low (excluded) |

### 9. Confidence Assessment

- **High confidence events:**
  - WAIC 2026 (official website + cross-verified by media)
  - AI Hackathon Shanghai 2026 (structured data from aitop100.cn)
  - Baidu AI Developer Salon (company website)
  - AIGC Summit Shanghai (structured data from aitop100.cn)

- **Medium confidence events:**
  - AI Meetup: LLM Applications (community event, needs on-site verification)

- **Low confidence events:** None included in verified list

- **Conflicts between sources:**
  - "AI Finance Summit Shanghai": Date conflict (July 15 vs. August 15) → Excluded
  - "AI Education Workshop": Already expired → Excluded

### 10. Recommended Next Steps

1. **[Step 1]:** Register for WAIC 2026 before deadline (2026-07-05)
   - **Timeline:** Within 3 days (deadline approaching)
   - **Priority:** High

2. **[Step 2]:** Register for AI Hackathon Shanghai 2026 (if interested)
   - **Timeline:** Before 2026-07-10
   - **Priority:** Medium

3. **[Step 3]:** Monitor AIGC Summit Shanghai registration (opens 2026-07-10)
   - **Timeline:** Check on 2026-07-10
   - **Priority:** Medium

## Output File

The agent generated a full **Event Collection Report** using `assets/output_templates/event_collection_template.md` and saved it to:
`/Users/zhuoyuwei/search_skill/outputs/AI_events_Shanghai_July2026.md`

## Key Takeaways for Skill Testing

1. **Task classification worked:** Correctly identified as Events and Conferences
2. **Source selection worked:** Prioritized S-level sources (aitop100.cn), then A-level (company websites), then B-level (community events)
3. **Query generation worked:** Generated 7 query variations (Chinese + English, with time/location qualifiers)
4. **Verification worked:** Cross-verified WAIC 2026 with official website + media reports
5. **Output template worked:** Used event_collection_template.md correctly
6. **Exclusion worked:** Excluded events with conflicting dates or low-reliability sources
7. **Confidence scoring worked:** Assigned High/Medium/Low based on source reliability + cross-verification

## User Feedback (Simulated)

```
This is exactly what I needed! The verified events table gives me a quick overview, and the detailed event information helps me decide which ones to attend.

The "Excluded Events" section is helpful - I can see why some events didn't make the cut.

One suggestion: Could you add a "Travel Tips" section for events in different cities? (e.g., visa, accommodation, transportation)

Agent response: Great suggestion! I'll add that to the template in the next version.
```

## Notes for Skill Improvement

1. **Add travel tips section:** For events in different cities, include visa, accommodation, transportation info
2. **Add calendar integration:** Allow exporting events to .ics calendar format
3. **Add notification system:** Alert user when registration opens for "not yet open" events
4. **Improve conflict resolution:** When sources conflict, show both sides and let user decide
