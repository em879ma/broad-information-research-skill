# Source Registry: AI Events (AI 活动渠道清单)

This file defines the information sources for collecting AI-related events and conferences.

## AI Events Collection Workflow

1. Clarify city, time range, event type
2. Prioritize S-level structured sources
3. Check A-level event platforms and company event pages
4. Supplement with keyword search
5. Cross-verify time, location, registration status
6. Output structured event list

## Source Rankings

### S-Level (最高优先级 - 结构化数据，可自动采集)

| Source | Data Type / Description |
|--------|------------------------|
| aitop100.cn/activity/ | Structured data, crawlable, frequently updated; suitable for automated collection layer |
| aitop100.cn/aicreation/ | AI creation events, structured data |
| Sogou WeChat Search | WeChat official account events, searchable |

**Characteristics:**
- Structured data available
- Regularly updated
- Suitable for automated crawlers
- High reliability

### A-Level (高优先级 - 需要 JS 渲染或特殊工具)

| Source | Data Type / Description |
|--------|------------------------|
| Luma | Event management platform, requires JS rendering |
| Juejin Events (掘金活动) | Developer community events |
| Huodongjia (活动家) | Professional event platform |
| SenseTime Developer Events (商汤开发者活动) | AI company events |

**Characteristics:**
- Good data quality
- Requires special access methods
- Suitable as supplementary layer

### B-Level (中优先级 - 需人工/半自动采集，需交叉验证)

| Source | Data Type / Description |
|--------|------------------------|
| Huodongxing (活动行) | Event platform, requires manual/semi-automated collection |
| Hudongba (互动吧) | Local events, requires verification |
| CSDN Events (CSDN活动) | Developer community events |
| Open Source China (开源中国) | Open source community events |

**Characteristics:**
- Has events but requires manual collection
- Needs cross-verification
- Good for comprehensive coverage

### Company Event Pages (大厂活动页 - 长期稳定，可监控)

| Company | Event Page URL | Description |
|---------|---------------|-------------|
| Huawei | Huawei Developer Conference page | Annual developer conference |
| Alibaba Cloud | Alibaba Cloud Events page | Cloud computing events |
| Tencent Cloud | Tencent Cloud Events page | Cloud and AI events |
| Baidu AI | Baidu AI Developer page | AI platform events |
| Microsoft | Microsoft Events page | Global events |
| Google | Google Developer Events page | Developer conferences |

**Characteristics:**
- Long-term stable
- Can be monitored for annual events
- High reliability

### Annual Fixed Events (年度固定活动 - 可预排，适合提前加入候选池)

| Event | Type | Typical Time | Description |
|-------|------|--------------|-------------|
| GAITC | AI Conference | Usually mid-year | Global Artificial Intelligence Technology Conference |
| WAIC | AI Expo | Usually July | World Artificial Intelligence Conference (Shanghai) |
| HDC | Developer Conference | Usually April | Huawei Developer Conference |
| Baidu Create | AI Conference | Usually Q2-Q3 | Baidu AI Developer Conference |
| Yunqi Conference (云栖大会) | Cloud Computing | Usually September | Alibaba Cloud Computing Conference |
| QCon | Tech Conference | Multiple times/year | Software development conference |
| NeurIPS | Academic Conference | Usually December | Neural Information Processing Systems |
| ICML | Academic Conference | Usually July | International Conference on Machine Learning |
| CVPR | Academic Conference | Usually June | Conference on Computer Vision and Pattern Recognition |

**Characteristics:**
- Fixed annual schedule
- Can be pre-scheduled
- Suitable for advance planning

## Search Keywords for AI Events

### Chinese Keywords
- AI 活动 (AI events)
- AIGC 峰会 (AIGC summit)
- AI 黑客松 (AI hackathon)
- 开发者大会 (Developer conference)
- 人工智能 会议 (AI conference)
- 机器学习 研讨会 (ML workshop)

### English Keywords
- AI conference
- AI summit
- AI hackathon
- Developer conference AI
- Machine learning meetup
- AI workshop

## Event Verification Checklist

For each event found, verify:
- [ ] Event name
- [ ] Date and time
- [ ] City and venue
- [ ] Organizer
- [ ] Registration status (open/closed)
- [ ] Registration link
- [ ] Event description
- [ ] Speakers (if available)
- [ ] Registration fee (if applicable)
- [ ] Source reliability

## Cross-Verification Rules

1. **Time verification**: Check multiple sources for event date
2. **Location verification**: Verify venue address
3. **Registration status**: Check if registration is still open
4. **Organizer verification**: Verify organizer identity
5. **Event existence**: Confirm the event is not cancelled

## Output Format

See `assets/output_templates/event_collection_template.md` for the standard output format.

## Notes

- S-level sources should be checked first for comprehensive coverage
- A-level sources provide high-quality events but may require special access
- B-level sources need manual verification
- Company event pages are reliable but may not list all events
- Annual fixed events can be pre-added to the candidate pool
- Always cross-verify important event details
