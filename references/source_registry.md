# Source Registry

This file defines the recommended information sources for each research mode.

## 1. Academic Research (学术研究)

| Source Type | Recommended Channels | Usage Rules |
|------------|---------------------|--------------|
| Academic Databases | Google Scholar, Semantic Scholar, PubMed, arXiv, SSRN, IEEE Xplore, ACM Digital Library | Prioritize review articles, meta-analyses, papers from last 5 years, classic highly-cited papers |
| Institutional/Journal Websites | Nature, Science, JAMA, NEJM, ACM, IEEE, Elsevier, Springer | Used to confirm paper information, journal, year, and DOI |
| Preprints | arXiv, medRxiv, SSRN | Can be used as latest research signals, 
**Search Strategy:**
- Start with broad keyword search in Google Scholar
- Filter by year (last 5 years preferred)
- Look for review papers and meta-analyses
- Check citation counts for importance
- Verify with journal websites for final publication details

## 2. Competitor Analysis (竞品分析)

| Source Type | Recommended Channels | Usage Rules |
|------------|---------------------|--------------|
| Primary Sources | Official website, product pages, pricing pages, documentation, announcement pages | Use first, avoid relying on outdated secondary summaries |
| User Feedback | App Store, Chrome Web Store, Product Hunt, G2, Reddit, Zhihu, Xiaohongshu, Weibo | **MediaCrawler** 可爬取国内社交媒体的真实用户评价 |
| Media/Industry Analysis | TechCrunch, The Information, 36Kr, QbitAI, JiQiZhiXin, JiaZiGuangNian | Used to supplement funding, strategy, market positioning |
| **Social Media Crawling** | **MediaCrawler** — 爬取 **小红书、知乎、微博、B站** 等平台 | **重要信息源！** 大量用户讨论和真实反馈只在社交媒体平台。使用 `MediaCrawler API (http://localhost:8080)` |

**Search Strategy:**
- Start with official website and product documentation
- Check pricing pages and feature lists
- Search for user reviews on app stores and review platforms
- **Use MediaCrawler to crawl 小红书、知乎、微博 for real user feedback**
- Look for media coverage of funding and strategy
- Compare features using comparison tables from reputable sources

## 3. Domain News (领域新闻)

| Source Type | Recommended Channels | Usage Rules |
|------------|---------------------|--------------|
| Official Announcements | Company blogs, government websites, institution announcements | Prioritize confirming facts themselves |
| Authoritative Media | Reuters, AP, Bloomberg, Financial Times, The Verge, 36Kr, Caixin | Used to supplement background and impact |
| **WeChat Public Accounts** (微信公众号) | **wechat-query skill** — 依赖 wechat-download-api 服务 | **重要信息源！** 大量国内行业信息只在公众号发布。需要先部署服务并扫码登录。详见 `SKILL.md` 中「微信公众号信息源集成」章节。**垂直领域公众号库见 `wechat_accounts_registry.md`** |
| **Social Media Crawling** | **MediaCrawler** — 爬取 **小红书、知乎、微博、B站** 等平台 | **重要信息源！** 大量实时讨论和用户反馈只在社交媒体平台。使用 `MediaCrawler API (http://localhost:8080)` |
| Social/Community | X (Twitter), Reddit, Hacker News, Zhihu | Only as early signals or opinion sources |

**Search Strategy:**
- Start with official sources for fact verification
- Use authoritative media for context and analysis
- **Use MediaCrawler to crawl 小红书、知乎、微博 for real-time discussions**
- Check social media for early signals and community reactions
- Verify dates and timelines carefully
- Cross-reference multiple sources for important claims

## 4. Market Trends (市场动向)

| Source Type | Recommended Channels | Usage Rules |
|------------|---------------------|--------------|
| Market Reports | Gartner, IDC, CB Insights, PitchBook, McKinsey, Deloitte, iResearch, QuestMobile | Used for scale, trends, market structure |
| Funding/M&A | Crunchbase, PitchBook, QiChaCha, ITJuzi, media funding reports | Used to judge capital flow |
| Product/Hiring Signals | Company websites, hiring pages, press releases, developer documentation | Used to judge strategic direction and real investment |
| **Social Trends** | **小红书热门**, **抖音热门**, **B站热门** | **MediaCrawler** 可爬取国内社交媒体平台的热门话题和趋势 |

**Search Strategy:**
- Start with market research reports from reputable firms
- Check funding databases for investment trends
- Monitor company hiring pages for strategic direction
- **Use MediaCrawler to crawl 小红书、B站 hot topics for trend signals**
- Look for product launch announcements
- Analyze developer documentation for technical trends

## 5. Events and Conferences (活动/会议搜集)

See `source_registry_ai_events.md` for detailed AI event sources.

**General Event Sources:**
- Event platforms: Eventbrite, Luma, Huodongxing, Huodongxia
- **WeChat Public Accounts** (微信公众号) — **大量活动信息只在公众号发布！** 使用 wechat-query skill 查询已订阅公众号的活动通知
- **Social Media Crawling** — **大量活动宣传在社交媒体平台！** 使用 **MediaCrawler** 爬取 **小红书、微博、知乎** 上的活动宣传帖子
- Tech community: CSDN, Juejin, Open Source China
- University websites: For academic conferences
- Company websites: For developer conferences and product launches

**Search Strategy:**
- Clarify city, time range, event type
- Check multiple event platforms
- **Use MediaCrawler to crawl 小红书、微博 for event promotions**
- Verify with official websites
- Cross-check dates, locations, registration status

## 6. Policy and Regulation (政策/监管)

| Source Type | Recommended Channels | Usage Rules |
|------------|---------------------|--------------|
| Government Websites | Official government portals, regulatory agency websites | Primary source, most authoritative |
| Legal Databases | Official legal databases, legal news websites | For detailed legal text and interpretation |
| Industry Associations | Industry association websites, white papers | For industry-specific regulations and standards |

**Search Strategy:**
- Start with official government websites
- Check regulatory agency announcements
- Look for legal interpretations in legal databases
- Check industry association websites for industry-specific regulations
- Verify effective dates and expiration dates

## 7. Company or Organization Intelligence (公司/机构情报)

| Source Type | Recommended Channels | Usage Rules |
|------------|---------------------|--------------|
| Official Sources | Company website, investor relations page, press releases, annual reports | Most reliable for financial and strategic information |
| Business Databases | Crunchbase, LinkedIn, QiChaCha, TianYanCha | For funding, leadership, business scope |
| News and Media | Business media, industry publications, CEO interviews | For strategy, partnerships, market positioning |
| **Social Media Crawling** | **MediaCrawler** — 爬取 **小红书、知乎、微博、B站** 上的用户评价和舆情 | **重要信息源！** 用户对公司的真实反馈和口碑 |
| **WeChat Public Accounts** (微信公众号) — 公司官方公众号发布的第一手信息 | 使用 wechat-query skill 查询 |
| Social Media | Company social media accounts, executive LinkedIn/Twitter | For real-time updates and culture |

**Search Strategy:**
- Start with official website and investor relations page
- Check business databases for funding and leadership
- Look for recent news and media coverage
- **Use MediaCrawler to crawl 小红书、知乎、微博 for user sentiment**
- Monitor social media for real-time updates
- Check job postings for strategic direction

## Source Reliability Guidelines

When selecting sources, prioritize in this order:

1. **Official sources** - Government websites, company websites, official announcements
2. **Primary databases** - Academic databases, business databases, legal databases
3. **Reputable media or industry platforms** - Well-known news media, industry publications
4. **Community/user-generated sources** - Only as secondary signals, must be labeled as subjective

## Cross-Verification Rules

- **At least 2 sources** for important claims
- **Official source preferred** when available
- **Report conflicts** when sources disagree
- **Label uncertainty** when evidence is weak
- **Check dates** to ensure information is current
