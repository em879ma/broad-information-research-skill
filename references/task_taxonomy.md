# Task Taxonomy

This file defines the task classification rules for routing user requests to the correct research mode.

## 1. Academic Research (学术研究)

### Trigger Keywords
- Papers (论文)
- Literature review (文献综述)
- Research gaps (研究空白)
- Evidence synthesis (证据综合)
- Academic background (学术背景)
- Theory (理论)
- Citation (引用)
- Peer-reviewed (同行评审)
- Meta-analysis (元分析)
- Systematic review (系统综述)

### Example User Requests
- "Help me find papers on GLP-1 and kidney transplant outcomes"
- "Conduct a literature review on AI agent frameworks"
- "What are the research gaps in diabetes treatment for transplant patients?"
- "Summarize the evidence on COVID-19 vaccine efficacy"

### Classification Rules
- If the user mentions "paper", "literature", "research", "academic", "citation", "study" → Classify as Academic Research
- If the user asks for "evidence synthesis", "meta-analysis", "systematic review" → Classify as Academic Research
- If the user asks about "theory", "theoretical framework", "academic background" → Classify as Academic Research

### Search Sources
- Google Scholar, Semantic Scholar, PubMed, arXiv, SSRN
- IEEE Xplore, ACM Digital Library
- Nature, Science, JAMA, NEJM
- University repositories

### Output Template
Use `assets/output_templates/academic_research_template.md`

## 2. Competitor Analysis (竞品分析)

### Trigger Keywords
- Compare (比较)
- Competitor (竞品, 竞争对手)
- Product (产品)
- Company (公司)
- Features (功能)
- Pricing (定价)
- Positioning (定位)
- Users (用户)
- Business model (商业模式)
- Alternative (替代品)
- Vs (对比)

### Example User Requests
- "Help me analyze the competitors of an AI meeting assistant product"
- "Compare the features and pricing of Otter.ai, Fireflies.ai, and Fathom"
- "What are the competitive advantages of Tesla in the EV market?"
- "Find alternatives to Adobe Photoshop"

### Classification Rules
- If the user mentions "competitor", "compare", "vs", "alternative" → Classify as Competitor Analysis
- If the user asks about "features", "pricing", "positioning", "business model" → Classify as Competitor Analysis
- If the user asks to compare products or companies → Classify as Competitor Analysis

### Search Sources
- Official websites, product pages, pricing pages
- App Store, Chrome Web Store, Product Hunt, G2
- TechCrunch, The Information, 36Kr, QbitAI
- Company annual reports, investor presentations

### Output Template
Use `assets/output_templates/competitor_analysis_template.md`

## 3. Domain News (领域新闻)

### Trigger Keywords
- Recent news (最近新闻)
- Latest developments (最新进展)
- Weekly updates (本周更新)
- Event timeline (事件时间线)
- Breaking news (突发新闻)
- News digest (新闻摘要)
- Latest updates (最新动态)
- What's happening (发生了什么)
- Current events (当前事件)

### Example User Requests
- "Help me collect recent news about AI regulation in China"
- "What are the latest developments in the AI agent market?"
- "Summarize this week's news in the EV industry"
- "Track news about OpenAI's GPT model releases"

### Classification Rules
- If the user mentions "news", "latest", "recent", "update", "developments" → Classify as Domain News
- If the user asks for "weekly digest", "news summary", "timeline" → Classify as Domain News
- If the user asks "what's happening", "what's new", "current events" → Classify as Domain News

### Search Sources
- Company blogs, government websites, organization announcements
- Reuters, AP, Bloomberg, Financial Times, The Verge
- X (Twitter), Reddit, Hacker News, Zhihu, WeChat
- Industry-specific news sites

### Output Template
Use `assets/output_templates/news_digest_template.md`

## 4. Market Trends (市场动向)

### Trigger Keywords
- Market direction (市场方向)
- Industry momentum (行业势头)
- Investment signals (投资信号)
- Emerging opportunities (新兴机会)
- Risks (风险)
- Market size (市场规模)
- Growth rate (增长率)
- Market share (市场份额)
- Trend (趋势)
- Outlook (展望)
- Forecast (预测)

### Example User Requests
- "Analyze the market trends of AI agents in 2026"
- "What are the emerging opportunities in the Chinese EV market?"
- "Track investment signals in the AI startup ecosystem"
- "What is the market size and growth rate of the cloud computing industry?"

### Classification Rules
- If the user mentions "market trend", "market direction", "industry momentum" → Classify as Market Trends
- If the user asks about "investment signals", "emerging opportunities", "risks" → Classify as Market Trends
- If the user asks about "market size", "growth rate", "market share", "forecast" → Classify as Market Trends

### Search Sources
- Gartner, IDC, CB Insights, PitchBook, McKinsey, Deloitte
- Crunchbase, QiChaCha, ITJuzi
- Company websites, hiring pages, press releases
- Industry reports, white papers

### Output Template
Use `assets/output_templates/market_trend_template.md`

## 5. Events and Conferences (活动/会议搜集)

### Trigger Keywords
- Conference (会议)
- Meetup (聚会)
- Summit (峰会)
- Hackathon (黑客松)
- Competition (竞赛)
- Training (培训)
- Workshop (工作坊)
- Seminar (研讨会)
- Webinar (网络研讨会)
- Registration (报名)
- Event (活动)
- Upcoming events (即将举行的活动)
- Calendar (日历)

### Example User Requests
- "Find AI events in Shanghai next month"
- "What are the upcoming AI conferences in China in 2026?"
- "Help me find hackathons related to AI agents"
- "Collect a list of AI summits with registration links"

### Classification Rules
- If the user mentions "event", "conference", "meetup", "summit", "hackathon" → Classify as Events and Conferences
- If the user asks about "registration", "upcoming events", "event calendar" → Classify as Events and Conferences
- If the user specifies city and time range for events → Classify as Events and Conferences

### Search Sources
- aitop100.cn/activity/, Luma, Juejin Events, Huodongjia
- Huodongxing, Hudongba, CSDN Events, Open Source China
- Company event pages (Huawei, Alibaba Cloud, Tencent Cloud, Baidu AI)
- Annual fixed events (GAITC, WAIC, HDC, Baidu Create, QCon, NeurIPS)

### Output Template
Use `assets/output_templates/event_collection_template.md`

## 6. Policy and Regulation (政策/监管)

### Trigger Keywords
- Law (法律)
- Compliance (合规)
- Official rules (官方规定)
- Government policy (政府政策)
- Regulatory change (监管变化)
- Industry standards (行业标准)
- Regulation (法规)
- Policy (政策)
- Legal (法律)
- Compliance requirement (合规要求)
- Government announcement (政府公告)

### Example User Requests
- "Help me track changes in AI regulation in China"
- "What are the compliance requirements for AI companies in the EU?"
- "Find recent government policies on data privacy"
- "Analyze the impact of new AI regulations on startups"

### Classification Rules
- If the user mentions "policy", "regulation", "law", "compliance", "legal" → Classify as Policy and Regulation
- If the user asks about "government policy", "regulatory change", "industry standards" → Classify as Policy and Regulation
- If the user asks about "compliance requirements", "government announcement" → Classify as Policy and Regulation

### Search Sources
- Government websites (gov.cn, eu.europa.eu, whitehouse.gov)
- Regulatory agency websites
- Legal databases (PKULaw, Law.com.cn)
- Industry association websites, white papers

### Output Template
Use `assets/output_templates/policy_regulation_template.md` (to be created)

## 7. Company or Organization Intelligence (公司/机构情报)

### Trigger Keywords
- Company (公司)
- Lab (实验室)
- Institution (机构)
- Product team (产品团队)
- Founder (创始人)
- Funding (融资)
- Partnerships (合作伙伴)
- Hiring (招聘)
- Roadmap (路线图)
- Leadership (领导层)
- Revenue (收入)
- Strategy (战略)
- Acquisition (收购)
- IPO (上市)

### Example User Requests
- "Track recent developments of OpenAI"
- "What are the recent funding rounds and partnerships of Anthropic?"
- "Analyze the hiring trends and strategic direction of DeepSeek"
- "Find information about the founders and leadership of Mistral AI"

### Classification Rules
- If the user asks about a specific company or organization → Classify as Company or Organization Intelligence
- If the user mentions "funding", "partnerships", "hiring", "roadmap", "strategy" → Classify as Company or Organization Intelligence
- If the user asks about "founders", "leadership", "revenue", "acquisition" → Classify as Company or Organization Intelligence

### Search Sources
- Company website, investor relations page, press releases, annual reports
- Crunchbase, LinkedIn, QiChaCha, TianYanCha
- Business media, industry publications, CEO interviews
- Company social media accounts, executive LinkedIn/Twitter

### Output Template
Use `assets/output_templates/company_intelligence_template.md` (to be created)

## Ambiguous Requests

If the user's request could fit multiple modes:

1. **Infer the most likely mode** from the user's wording
2. **Ask a clarifying question** only when the missing choice would materially change the search strategy
3. **Prioritize** based on keyword strength

### Examples

**Ambiguous:** "Tell me about AI agents"
- Could be: Academic Research, Domain News, Market Trends, Company Intelligence
- Infer from context: If no context, ask "Do you want academic papers, recent news, market trends, or company information about AI agents?"

**Clear:** "Find recent papers about AI agent frameworks"
- Clearly Academic Research → No need to ask

**Clear:** "What are the latest news about AI agents?"
- Clearly Domain News → No need to ask

## Classification Workflow

1. **Extract keywords** from the user's request
2. **Match keywords** against the trigger keywords for each mode
3. **Count matches** for each mode
4. **Select the mode** with the most matches
5. **If tie or ambiguous**, infer from context or ask clarifying question
6. **Confirm the mode** with the user if uncertain

## Notes

- This taxonomy is not exhaustive; add new keywords as needed
- Consider cultural context (Chinese vs. English keywords)
- Update this file as new patterns emerge
- When in doubt, ask the user to clarify
