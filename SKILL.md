---
name: broad-information-research
description: Use this skill to collect, screen, verify, and summarize information for academic research, competitor analysis, domain news, market trends, events, policy research, and company intelligence. This skill also provides 8 MCP tools for workflow automation.
---

# Broad Information Research Skill

> **MCP Tools Available:** This skill exposes 8 MCP tools (`classify_research_task`, `get_sources_for_task`, `generate_search_queries`, `deduplicate_results`, `score_results`, `render_output`, `crawl_social_media`, `mediacrawler_status`). Install the MCP server to use them directly.

## Purpose

This skill helps users collect and evaluate information from different source types according to the user's selected research mode.

## Supported Modes

1. **Academic research** - papers, literature review, research gaps, evidence synthesis
2. **Competitor analysis** - product/company comparison, features, pricing, positioning
3. **Domain news** - recent news, weekly updates, latest developments
4. **Market trends** - market direction, industry momentum, investment signals
5. **Events and conferences** - conferences, meetups, summits, hackathons
6. **Policy and regulation** - laws, compliance, government policy, regulatory change
7. **Company or organization intelligence** - company info, funding, partnerships, hiring

## Workflow

**Interactive Guide Mode (Default)**:

1. User request
2. Task classification
3. Channel selection
4. Keyword generation
5. Information retrieval
6. **🛑 Deduplication (MANDATORY)** ← Required checkpoint!
7. Verification
8. Credibility scoring
9. Structured output
10. **Ask user: Save to file?**

## Interactive Guide Flow (Required on Skill Invocation)

**When this skill is invoked, automatically start the interactive guide flow:**

### Step 1: Ask User to Choose Information Type

Present these 5 options + "Other":

```
Please select the type of information you want to find:

1. Academic Research (Academic Research) - Papers, literature review, research gaps
2. Competitor Analysis (Competitor Analysis) - Product comparison, features, pricing, positioning
3. Domain News (Domain News) - Recent news, latest developments, event timeline
4. Market Trends (Market Trends) - Market direction, industry momentum, investment signals
5. Events & Conferences (Events & Conferences) - Conferences, meetups, summits, hackathons

6. Other (Other) - 政策/监管、公司情报、或Other自定义需求

Please enter option number (1-6) or describe your request directly:
```

### Step 2: Guide User to Input Specific Request

Based on the user's choice, ask targeted follow-up questions:

**If Academic Research (1):**
```
Please provide the following information (as detailed as possible):
- Research topic or question:
- Time range (e.g., 2020-2026):
- Literature type (e.g., peer-reviewed papers, preprints, reviews):
- Specific focus (e.g., methodology, key findings, limitations):

Example request:"查找 GLP-1 受体激动剂与肾移植结局的近期论文，时间范围 2020-2026"
```

**If Competitor Analysis (2):**
```
Please provide the following information (as detailed as possible):
- Your product/company name (optional):
- Competitors to analyze (e.g., Otter.ai, Fireflies.ai):
- Focus dimensions (e.g., features, pricing, user reviews, market positioning):
- Target user group (e.g., enterprise, individual, developers):

Example request:"分析 AI 会议助手产品的竞品，对比 Otter.ai、Fireflies.ai 和 Fathom 的功能、定价和用户评价"
```

**If Domain News (3):**
```
Please provide the following information (as detailed as possible):
- Domain or topic of interest:
- Region (e.g., China, US, Global):
- Time range (e.g., past week, this month, last 30 days):
- Specific event types (e.g., product launches, policy changes, funding news):

Example request:"搜集中国 AI 监管政策的最新新闻，时间范围过去一个月"
```

**If Market Trends (4):**
```
Please provide the following information (as detailed as possible):
- Industry or domain of interest:
- Region (e.g., China, US, Global):
- Time range (e.g., 2026, past year):
- Focus signals (e.g., market size, growth rate, funding activities, M&A):

Example request:"分析 2026 年 AI Agent 的Market Trends，关注投资机会和新兴市场"
```

**If Events & Conferences (5):**
```
Please provide the following information (as detailed as possible):
- Event type (e.g., conference, hackathon, meetup, workshop):
- City or region (e.g., Shanghai, Beijing, Global):
- Time range (e.g., next month, July 2026):
- Focus topic (e.g., AI, blockchain, Web3):

Example request:"查找上海下个月的 AI 相关活动，包括会议、黑客松和开发者聚会"
```

**If Other (6):**
```
Please describe your request:
- Information type (e.g., policy/regulation, company intelligence, custom):
- Specific content:
- Time range (if applicable):
- Region (if applicable):
- Other要求：

Example request:"追踪欧盟 AI 法规的最新变化，关注对 AI 公司的合规要求"
```

### Step 3: Confirm and Start Research

After collecting the user's input:

1. **Summarize the request** to confirm understanding:
```
Based on your input, I will conduct [mode name] research:
- Topic: [extracted topic]
- Time range: [extracted time range]
- Region: [extracted region]
- Focus: [extracted focus]

Confirm to start research? (yes/no)
```

2. **If user confirms (yes)**: Proceed to task classification and normal workflow
3. **If user wants to modify (no)**: Go back to Step 2 and ask for modifications

---

## Task Classification (Automatic after Guide Flow)

After the interactive guide flow, automatically determine:
- **mode** - Which of the 7 supported modes (already determined in guide flow)
- **topic** - What is the main subject (extracted from user input)
- **region** - Geographic scope if relevant (extracted from user input)
- **time range** - Date range for the information (extracted from user input)
- **depth** - How detailed should the research be (ask if not specified)
- **output format** - Raw links, structured tables, synthesis, or strategic recommendations (ask if not specified)

If the mode is ambiguous even after guide flow, infer the most likely mode from the user's wording. Ask a clarifying question only when the missing choice would materially change the search strategy.

Use `references/task_taxonomy.md` for detailed task classification rules.

## Source Selection Rules

Use `references/source_registry.md` to select sources by mode.

For AI events, use `references/source_registry_ai_events.md`.

**微信公众号信息源（wechat-query skill）**

大量国内行业信息（活动通知、行业新闻、公司动态）只在微信公众号发布，是其他平台无法覆盖的重要信息源。

**集成方式：** wechat-query-skill 已通过符号链接安装到 `~/.qclaw/skills/wechat-query`

**使用前提：**
1. wechat-download-api 服务已部署并运行（需要 Docker）
2. 已使用公众号管理员微信扫码登录（登录有效期约 4 天）
3. 已订阅相关领域的公众号

#### 微信公众号账号库（Pre-defined Accounts Registry）

**目的：** 减少账号探索时间，直接使用预定义的高质量公众号 fakeid

**账号库文件：** `references/wechat_accounts_registry.md`

**支持领域：**
1. 文娱/娱乐 (Entertainment & Music)
2. 财经/金融 (Finance & Economy) - ✅ 已填充 8 个账号
3. 体育 (Sports)
4. 医疗/健康 (Healthcare & Medical)
5. 教育 (Education)
6. 科技/AI (Technology & AI)
7. 游戏 (Gaming)
8. 汽车出行 (Automotive)
9. 房产/地产 (Real Estate)
10. 消费/零售 (Consumer & Retail)
11. 法律/政策 (Law & Policy)
12. 其他垂直领域 (Other Verticals)

**使用逻辑：**

**场景 1：账号库中有所需领域的公众号**
```
User: "搜索音乐行业最新动态"

Agent:
1. 检查 wechat_accounts_registry.md 的文娱/音乐板块
2. 找到预定义账号：摇滚客、音乐财经、网易云音乐
3. 直接使用 fakeid 获取文章：/api/public/articles?fakeid=MzIwNzQxMjM0NQ==
4. 无需账号探索，直接返回结果 ✅
```

**场景 2：账号库中无所需公众号**
```
User: "搜索某个小众音乐公众号的文章"

Agent:
1. 检查 wechat_accounts_registry.md
2. 未找到该公众号
3. 询问用户：
   "未找到该公众号的预设账号。请选择：
   a) 搜索并添加到账号库（推荐，方便后续使用）
   b) 仅本次搜索，不保存
   c) 使用其他信息源"
4. 根据用户选择执行
```

**场景 3：Agent 自动探索并更新账号库**
```
User: "查找AI行业的最新新闻"

Agent:
1. 检查 wechat_accounts_registry.md 的科技/AI 板块
2. 找到预定义账号：36氪、量子位、机器之心
3. 获取这些账号的文章
4. 同时搜索更多 AI 相关公众号："AI 新闻"、"人工智能 资讯"
5. 将新发现的高质量账号添加到账号库
6. 返回综合结果
```

**更新账号库的方法：**

详见 README.md 的「Managing WeChat Official Account Registry」章节，或运行：
```bash
cd /Users/zhuoyuwei/broad-information-research-skill
python3 scripts/query_wechat_fakeids.py
```

---

**在子代理中查询微信公众号文章时，使用以下 API：**

| API | 用途 | 示例 |
|-----|------|------|
| `GET /api/public/searchbiz?query=xxx` | 搜索公众号 | 搜索「量子位」「机器之心」等 AI 媒体 |
| `POST /api/rss/subscribe` (body: `{"fakeid":"xxx"}`) | 订阅公众号 | 先搜索获取 fakeid |
| `GET /api/rss/subscriptions` | 查看已订阅列表 | 确认已有订阅 |
| `GET /api/public/articles?fakeid=xxx` | 获取公众号文章列表 | 拉取最新文章 |
| `GET /api/public/articles/search?fakeid=xxx&query=xxx` | 按关键词搜索文章 | 在公众号内搜索特定主题 |
| `POST /api/article/fetch` (body: `{"url":"xxx"}`) | 抓取单篇文章全文 | 用户发来链接时 |
| `POST /api/rss/poll` | 手动触发一次轮询 | 立即拉取所有订阅号的最新文章 |
| `GET /api/health` | 健康检查 | 先确认服务可用 |
| `GET /api/admin/status` | 登录状态检查 | 确认登录有效 |

**默认服务地址：** `http://localhost:18080`（请确认实际部署端口，当前实际端口为 5000）

**查询流程：**
1. 先 `GET /api/health` 确认服务可用
2. 再 `GET /api/admin/status` 确认登录有效
3. 查询已订阅公众号的文章列表
4. 按关键词筛选相关文章
5. 提取文章标题、链接、发布时间、内容摘要

**如果在子代理中使用，子代理的 task 应包含：**
```
使用 wechat-query skill 查询微信公众号文章。服务地址 http://localhost:5000。
先检查 /api/health 和 /api/admin/status。
然后查询已订阅公众号的文章列表，按关键词「xxx」筛选。
提取相关文章的标题、链接、发布时间和内容摘要。
```

**⚠️ 如果 wechat-download-api 服务不可用（health 检查失败）：**

**必须询问用户，不要默认跳过微信公众号渠道！** 大量国内行业信息只在公众号发布。

向用户展示以下提示：
```
⚠️ 微信公众号信息源不可用

检测到 wechat-download-api 服务未运行。微信公众号是重要的信息来源，
大量国内行业信息（活动通知、新闻、公司动态）只在公众号发布。

是否需要现在部署？
- 回复「部署」→ 我来帮你一键安装（需要 Docker，约 3-5 分钟）
- 回复「跳过」→ 本次搜索跳过微信公众号渠道，继续使用Other来源

部署需要：
- Docker（如未安装会自动通过 Homebrew 安装）
- 一个微信公众号（订阅号或服务号均可）
- 微信扫码登录（公众号管理员微信）
```

**一键部署命令（用户确认后执行）：**
```bash
# 安装 Docker（如果未安装）
brew install --cask docker

# 启动 Docker
open -a Docker

# 等待 Docker 启动完成后，启动 wechat-download-api
cd /Users/zhuoyuwei/wechat-query-skill/services/wechat-download-api
cp env.example .env
docker compose up -d --build

# 健康检查
curl -s http://localhost:5000/api/health
```

**部署成功后的扫码登录引导：**
1. 发起登录会话：`POST /api/login/relogin/start`
2. 获取二维码：`GET /api/login/relogin/{request_id}/qrcode`
3. 下载二维码图片并通过 MEDIA: 发送给用户
4. 提醒用户使用**公众号管理员微信**扫码
5. 轮询登录状态直到成功
6. 引导用户订阅相关领域的公众号

**如果用户选择「跳过」：**
- 在报告中注明「微信公众号信息源未启用（用户选择跳过）」
- 继续使用Other信息源完成搜集

**⚠️ 如果 MediaCrawler 不可用（未安装或未配置）：**

**必须询问用户，不要默认跳过国内社交媒体渠道！** 小红书、知乎等平台有大量独家内容和用户真实反馈。

向用户展示以下提示：
```
⚠️ MediaCrawler（多平台爬虫）不可用

检测到 MediaCrawler 未安装或未配置。它可以爬取小红书、知乎、微博、B站等平台的内容，
是获取国内社交媒体信息和用户真实反馈的重要工具。

是否需要现在安装？
- 回复「安装」→ 我来帮你一键安装（需要 Python >=3.10、uv、Chrome 浏览器）
- 回复「跳过」→ 本次搜索跳过国内社交媒体渠道，继续使用Other来源

安装需要：
- Python >= 3.10
- uv（Python 包管理器，会自动安装）
- Chrome 浏览器（推荐）或 Playwright
- 各平台账号（用于登录爬取，登录态会缓存）
```

**一键安装命令（用户确认后执行）：**

```bash
# 1. 安装 uv（如果未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. 克隆 MediaCrawler 仓库
cd /Users/zhuoyuwei
git clone https://github.com/NanmiCoder/MediaCrawler.git

# 3. 安装依赖
cd MediaCrawler
uv sync

# 4. 安装 Playwright 浏览器
uv run playwright install chromium

# 5. 配置使用 Playwright 模式（禁用 CDP 模式）
# 编辑 MediaCrawler/config/base_config.py
# 将 ENABLE_CDP_MODE: bool = True 改为 ENABLE_CDP_MODE: bool = False

sed -i '' 's/ENABLE_CDP_MODE: bool = True/ENABLE_CDP_MODE: bool = False/' MediaCrawler/config/base_config.py

# 6. 测试运行（会弹出二维码，需要扫码登录）
cd MediaCrawler
uv run python main.py --platform xhs --lt qrcode --type search --keywords "测试" --crawler_max_notes_count 5
```

**⚠️ 重要配置说明：**
- MediaCrawler 的 API 服务器目前有问题（启动后立即退出），请使用 **CLI 模式**
- 必须设置 `ENABLE_CDP_MODE: False`（使用 Playwright 直接启动浏览器，而非连接 Chrome CDP）
- 首次运行各平台时需要扫码登录，登录态会保存在 `cookies/` 目录

**登录各平台（首次使用时）：**

MediaCrawler 支持两种登录方式：

1. **二维码登录（推荐）**：运行爬虫时会弹出二维码，用对应平台的 App 扫码登录
2. **Cookie 登录**：手动配置 `config/base_config.py` 中的 Cookie

**支持的平台和爬取内容：**

| 平台 | 可爬取内容 | 登录方式 |
|------|-------------|----------|
| 小红书 (xhs) | 笔记、评论、用户主页 | 二维码 |
| 知乎 (zhihu) | 问答、回答、评论 | 二维码 |
| 微博 (weibo) | 微博、评论、用户主页 | 二维码 |
| B站 (bilibili) | 视频、评论、UP主主页 | 二维码 |
| 抖音 (dy) | 视频、评论、用户主页 | 二维码 |
| 快手 (ks) | 视频、评论、用户主页 | 二维码 |
| 贴吧 (tieba) | 帖子、评论、用户主页 | 二维码 |

**在子代理中使用 MediaCrawler（CLI 模式）：**

由于 MediaCrawler 的 API 服务器当前不可用，请使用 **CLI 模式** 直接运行命令。

**方式一：直接使用 CLI（推荐）**

```
使用 MediaCrawler CLI 爬取内容。

任务：爬取小红书上关于「xxx」的笔记
1. 切换到 MediaCrawler 目录：cd /Users/zhuoyuwei/MediaCrawler
2. 运行 CLI 命令：
   uv run python main.py --platform xhs --lt qrcode --type search --keywords "xxx" --crawler_max_notes_count 20
3. 扫码登录（首次运行时）
4. 爬取完成后，读取输出文件：
   - 笔记内容：data/xhs/jsonl/search_contents_*.jsonl
   - 评论内容：data/xhs/jsonl/search_comments_*.jsonl
5. 提取笔记标题、内容、点赞数、评论数、发布时间
```

**方式二：使用封装脚本（更简单）**

Skill 提供了封装脚本 `scripts/mediacrawler_wrapper.py`：

```bash
# 检查 MediaCrawler 状态
python scripts/mediacrawler_wrapper.py --check

# 列出支持的平台
python scripts/mediacrawler_wrapper.py --list-platforms

# 爬取小红书内容
python scripts/mediacrawler_wrapper.py --platform xhs --keywords "AI" --max-notes 20

# 爬取微博内容
python scripts/mediacrawler_wrapper.py --platform weibo --keywords "AI" --max-notes 20
```

**在子代理中的调用示例：**

```
使用 MediaCrawler 爬取社交媒体内容。

执行命令：
cd /Users/zhuoyuwei/MediaCrawler && uv run python main.py --platform xhs --lt qrcode --type search --keywords "AI" --crawler_max_notes_count 20

等待命令执行完成（约 2-5 分钟），然后读取结果文件：
- data/xhs/jsonl/search_contents_*.jsonl
- data/xhs/jsonl/search_comments_*.jsonl

提取关键信息：标题、描述、点赞数、评论数、链接。
```

**支持的平台代码：**
- `xhs` - 小红书
- `zhihu` - 知乎
- `wb` - 微博
- `bili` - B站（哔哩哔哩）
- `dy` - 抖音
- `ks` - 快手
- `tieba` - 贴吧

**如果用户选择「跳过」：**
- 在报告中注明「国内社交媒体信息源未启用（用户选择跳过）」
- 继续使用Other信息源完成搜集

**⚠️ 常见问题：**
1. **API 服务器启动后立即退出** → 不使用 API 模式，改用 CLI 模式（本文档已更新）
2. **Firefox 下载失败** → 只需 Chromium 即可，运行 `uv run playwright install chromium`
3. **登录二维码不弹出** → 确保 `ENABLE_CDP_MODE: False`，使用 Playwright 模式
4. **爬取结果为空** → 检查是否需要重新登录（cookies 可能过期）

## Search Strategy

For each task, generate:
1. **Broad keywords** - General topic terms
2. **Narrow keywords** - Specific subtopics, regions, time ranges
3. **Official-source queries** - Site-specific or official terms
4. **Alternative synonyms** - Abbreviations, Chinese/English variants
5. **Time-sensitive queries** - "latest", "2026", "this month", "last 30 days"

Use `references/search_query_patterns.md` for query generation patterns by mode.

Record for each search:
- Source
- Date
- Claim
- Confidence level

## Verification Rules

- **Do not treat a claim as confirmed** unless it is supported by a reliable source
- **For news and market trends**: Prefer recent sources
- **For academic research**: Distinguish peer-reviewed papers from preprints
- **For events**: Verify date, city, venue, organizer, and registration status
- **When sources conflict**: Explicitly report the conflict

## Scoring

For each item, assign:

### Relevance Score (1-5)
- 5 = directly answers the user's question
- 4 = strongly related but not complete
- 3 = useful context only
- 2 = weakly related
- 1 = irrelevant or off-topic

### Source Reliability Score (1-5)
- 5 = official source, peer-reviewed paper, government/organization page, company announcement
- 4 = reputable media, respected database, well-known industry platform
- 3 = professional blog, conference page, community platform
- 2 = user-generated post, repost, unclear source
- 1 = unsourced claim, marketing content, broken/expired page

### Freshness Score (1-5)
- 5 = within user-specified time range or latest available
- 4 = recent and still valid
- 3 = somewhat old but useful background
- 2 = outdated for current decisions
- 1 = stale or superseded

### Confidence Label
- **High** = reliable source + directly relevant + fresh + preferably cross-verified
- **Medium** = mostly reliable but incomplete, old, or only one strong source
- **Low** = weak source, conflict, unclear date, or limited evidence

Use `references/reliability_scoring.md` for detailed scoring rules.

## Deduplication and Conflict Rules (MANDATORY)

**🛑 This is a REQUIRED step - do NOT skip deduplication!**

### Step 1: Collect All Results
After searching multiple sources, you will have a list of results from different platforms. **Must deduplicate before scoring and output.**

### Step 2: Run Deduplication

**Option A: Use dedupe_results.py script (Recommended)**

```bash
python scripts/dedupe_results.py --input raw_results.json --output deduped_results.json --similarity-threshold 0.85
```

**Option B: Manual Deduplication**

If script is not available, manually deduplicate by:
1. **Title matching** - Remove items with identical or near-identical titles (Jaccard similarity > 0.85)
2. **URL matching** - Remove items with identical URLs
3. **Entity matching** - For events/companies, remove duplicates by name + date + location
4. **DOI matching** - For academic papers, remove duplicates by DOI

### Step 3: Deduplication Rules

- **If multiple sources report the same event**: Keep the most official or original source
- **If sources conflict**: Do NOT merge silently; report the conflict explicitly
- **If an event/news item is expired**: Exclude it unless the user asks for historical results
- **If only weak sources support an item**: Mark it as low confidence
- **Cross-verify claims**: Prefer items confirmed by multiple independent sources

### Step 4: Document Deduplication

**Must include in final output:**
```
### Deduplication Summary
- Total results collected: [N]
- Duplicates removed: [M]
- Unique results after deduplication: [N-M]
- Conflicts detected: [list conflicts, if any]
```

### Example Deduplication Output

```json
{
  "total_results": 45,
  "duplicates_removed": 12,
  "unique_results": 33,
  "conflicts": [
    {
      "item": "AI Conference Shanghai 2026",
      "conflict": "Date differs: Source A says June 15, Source B says June 22",
      "resolution": "Verified official website - correct date is June 15"
    }
  ]
}
```

**⚠️ Do NOT proceed to Scoring and Output until deduplication is complete!**

## Output

Choose the output template based on the mode:

- **Academic research** → `assets/output_templates/academic_research_template.md`
- **Competitor analysis** → `assets/output_templates/competitor_analysis_template.md`
- **Domain news** → `assets/output_templates/news_digest_template.md`
- **Market trends** → `assets/output_templates/market_trend_template.md`
- **Events and conferences** → `assets/output_templates/event_collection_template.md`

Always include:
- Search scope
- Sources used
- Selected results
- Excluded or uncertain items when important
- Synthesis or recommendation when requested

## Output Integrity (Critical)

**🛑 CRITICAL REMINDER: Do NOT stop generating until the ENTIRE output is complete.**

When generating long outputs (literature reviews, competitor analyses, market reports):

1. **Complete ALL template sections** - Do NOT leave any section unfinished
2. **Do NOT truncate** - If the output is very long, continue to the next section. NEVER stop mid-template.
3. **Check token usage** - If you're approaching the token limit, explicitly state "⚠️ OUTPUT TRUNCATED" and provide a summary of what was completed and what remains
4. **Use the full template** - Ensure all required fields in the template are filled
5. **If interrupted, resume** - If the output was truncated, the user may send "continue" or "接着". When you see this, resume from where you left off.

### Continuation Protocol

If the output was truncated (due to token limits or other reasons):

1. **User may send "continue" or "接着"** - Resume from where you left off
2. **Check completed sections** - First, check which sections of the template are already completed
3. **Continue with next incomplete section** - Resume generating from the next incomplete section
4. **State where you're continuing from** - Explicitly tell the user which section you're continuing from

Example:
```
（继续输出...）

## 研究空白与研究机会

[Continuing from previous output - Research Gaps section]

1. ...
```

### Long Output Strategy

For very long outputs (50+ items, 10+ pages):

1. **Use streaming output** - Output section by section, do NOT wait until everything is complete
2. **Show progress** - Use progress indicators like "正在生成第 3/5 部分..."
3. **Break into chunks** - If the output exceeds 5000 tokens, consider breaking it into multiple responses
4. **Save to file** - For extremely long outputs, save to a file and provide the file path

---

## Auto-Save to File

当输出非常长时，自动保存到文件而不是在聊天中返回。这可以避免截断。

### 何时自动保存

满足以下任一条件时自动保存：
- 输出超过 4000 tokens
- 输出包含 50+ 个项目
- 用户明确要求保存到文件
- 检测到输出完整性风险时（token 不足）

### 如何保存

1. **使用 `save_to_file.py` 脚本**：
```python
import sys
sys.path.append('./scripts')
from save_to_file import save_research_report

# 保存为 Markdown
filepath = save_research_report(
    mode='academic_research',
    topic='donor_obesity_kidney_transplant',
    content=report_content,
    format='md',
    output_dir='./outputs'
)
```

2. **使用 `write` 工具直接保存**：
```json
{
  "tool": "write",
  "parameters": {
    "path": "./outputs/academic_research_[topic]_[timestamp].md",
    "content": "报告内容..."
  }
}
```

### 保存格式

支持以下格式：
- **Markdown (.md)** - 默认格式，易于阅读和编辑
- **JSON (.json)** - 适合程序处理和数据交换
- **CSV (.csv)** - 适合 Excel 分析
- **纯文本 (.txt)** - 最简单的纯文本格式

### 保存路径惯例

```
output_dir/
├── mode_topic_timestamp.md    # 例如：academic_research_donor_obesity_20250603.md
├── mode_topic_timestamp.json  # JSON 格式
└── mode_topic_timestamp.csv   # CSV 格式
```

### 显示进度指示

在保存输出时，显示进度：
- ✅ 正在保存到文件... 
- ✅ 已保存到：outputs/academic_research_xxx.md
- 📎 查看完整报告：[文件名]

---

## Multi-Round Dialogue Support

允许用户在研究过程中修改请求、补充信息或请求澄清。

### 支持的场景

1. **用户想修改请求**
   - 用户：这不是我想要的，换成 XXX
   - 操作：暂停当前任务，确认新请求，必要时重新开始

2. **用户想补充信息**
   - 用户：再加一个条件，比如 XXX
   - 操作：在当前搜索中添加新条件

3. **用户想请求澄清**
   - 用户：这个结果是什么意思？
   - 操作：解释结果，询问是否需要更多信息

4. **用户想看更多细节**
   - 用户：能展开讲讲这个点吗？
   - 操作：找到相关部分，生成更详细的解释

5. **用户想终止任务**
   - 用户：够了/不用了/停止
   - 操作：保存当前进度，提供最终摘要，礼貌结束

### 触发关键词

检测以下关键词来触发多轮对话：

| 关键词 | 含义 |
|--------|------|
| 改变/换成/改成 | 修改请求 |
| 另外/还有/加上 | 补充信息 |
| 展开/详细点/展开讲讲 | 请求详细说明 |
| 这个/那是什么 | 请求澄清 |
| 继续/接着 | 从中断处继续 |
| 停止/够了/不用了 | 终止任务 |
| 保存 | 保存当前进度 |

### 处理流程

```
用户输入
    ↓
检测多轮关键词
    ↓
┌─────────┴─────────┐
↓                     ↓
用户想修改         用户想补充
    ↓                     ↓
确认修改内容      添加新条件
    ↓                     ↓
暂停当前任务     更新搜索参数
    ↓                     ↓
┌─────────┴─────────┐
↓                     ↓
继续执行          继续执行
```


### 示例对话框

**场景 1：用户想修改请求**
```
用户：我想换成搜索竞争对手YYY
→ 确认：是，您想搜索 **[YYY]** 而不是 **[XXX]**，���吗？
→ 用户：是的
→ 执行：保存当前进度 → 开始新搜索
```


**场景 2：用户想补充条件**
```
用户：再加一个条件，要上海的
→ 执行：从“在北上广深”中添加“上海”
→ 继续：更新搜索条件 → 返回更新后的结果
```

**场景 3：用户想要详细说明**
```
用户：能展开讲讲第二个研究发现吗？
→ 执行：定位到第二个研究发现 → 生成详细说明
→ 显示：✓ 已展开说明
```

**场景 4：用户想保存当前进度**
```
用户：保存一下
→ 执行：将当前结果保存到文件
→ 显示：✅ 已保存到：outputs/xxx.md
```

### 实现

1. 在每次研究步骤后（关键词生成后、搜索后、去重后、评分后）检测用户输入
2. 如果检测到多轮关键词，解析用户意图
3. 根据意图采取相应行动
4. 处理完成后继续原任务

---

## Result Export Function

允许用户将结果导出为不同格式。

### 支持的导出格式

| 格式 | 扩展名 | 说明 |
|------|--------|------|
| Markdown | .md | 默认格式，易于阅读 |
| JSON | .json | 适合程序处理 |
| CSV | .csv | 适合 Excel 分析 |
| Word | .docx | 适合正式文档 |
| PDF | .pdf | 适合打印和分享 |
| HTML | .html | 适合网页展示 |

### 导出方式

#### 1. 使用 `save_to_file.py` 

```python
import sys
sys.path.append('./scripts')
from save_to_file import save_research_report

# 导出为指定格式
save_research_report(
    mode='academic_research',
    topic='donor_obesity',
    content=report_content,
    format='json',  # md, json, csv, txt
    output_dir='./exports'
)
```

#### 2. 使用 `export_report.py` 命令行工具

```bash
# 导出为 Word
python scripts/export_report.py --input outputs/result.md --format docx

# 导出为 PDF
python scripts/export_report.py --input outputs/result.md --format pdf

# 导出为 HTML
python scripts/export_report.py --input outputs/result.md --format html

# 列出可用格式
python scripts/export_report.py --list-formats
```


#### 3. 使用 QClaw 工具

在研究完成后询问用户：
```
请问您希望如何保存结果？
1. Markdown (.md) - 直接查看
2. JSON (.json) - 程序处理
3. CSV (.csv) - Excel 分析
4. Word (.docx) - 正式文档
5. PDF (.pdf) - 打印/分享
请选择：
```

### 自动导出

也可以在完成研究后自动导出为多种格式：
```python
# 同时导出为多种格式
for fmt in ['md', 'json', 'csv']:
    save_research_report(
        mode=mode,
        topic=topic,
        content=content,
        format=fmt,
        output_dir='./exports'
    )
```

### 导出设置

可以在 `SKILL.md` 中设置默认导出格式：
```yaml
default_export_format: md  # 默认格式
export_formats:
  - md
  - json
  - csv
auto_export: false  # 是否自动导出
```

---

## MCP Client Compatibility Notes

This skill works with multiple MCP clients, but some features are client-specific:

### QClaw (OpenClaw)
- ✅ Full support for all features
- ✅ Sub-agent workflow with `sessions_spawn`
- ✅ File output and export
- ✅ Multi-round dialogue

### Claude Code
- ✅ Core research workflow (interactive guide, search, scoring, output)
- ⚠️ **No sub-agent support** - Claude Code does not have `sessions_spawn` tool
- ✅ Use **WebSearch tool directly in main conversation** instead of spawning agents
- ✅ File output via `write` tool
- ⚠️ Background Agent mode has permission approval issues

**Claude Code Adaptation:**

In Claude Code environment, **do NOT use sub-agents**. Instead:

1. **Use WebSearch directly in main conversation** - Search each source sequentially
2. **No parallel processing** - Process sources one by one
3. **Simpler workflow** - Skip sub-agent spawning, directly call WebSearch

Example Claude Code workflow:
```
User: Find recent papers on GLP-1 and kidney transplant

[In Claude Code, directly use WebSearch tool]
1. WebSearch: "GLP-1 kidney transplant PubMed 2024-2026"
2. WebSearch: "GLP-1 receptor agonist transplant outcomes Google Scholar"
3. Process and deduplicate results
4. Score and format output
5. Ask user: Save to file? (Markdown/JSON/CSV)
```

### Cursor
- ✅ Core research workflow
- ⚠️ Sub-agent support depends on Cursor version
- ✅ File output and export

---

## Sub-Agent Workflow (Optional)

对于复杂的、多部分的研究任务，使用子代理（sub-agents）将工作分解为更小、更细致的块。

### 何时使用子代理

在以下情况下使用子代理：
- 任务有多个不同的组成部分（例如：Academic Research需要搜索多个数据库）
- 输出会非常长（50+ 项，10+ 页）
- 需要并行处理（同时搜索多个来源）
- 希望提高输出质量（每个子代理专注于一个部分）

### 如何生成子代理

使用 `sessions_spawn` 工具，设置 `runtime="subagent"`：

```json
{
  "tool": "sessions_spawn",
  "parameters": {
    "runtime": "subagent",
    "task": "在 PubMed 上搜索关于供体肥胖和肾移植存活率的论文，关注 BMI cutoff 值和 DGF 发生率",
    "mode": "run",
    "cleanup": "delete",
    "runTimeoutSeconds": 300
  }
}
```

**参数说明：**
- `runtime`: `"subagent"` (OpenClaw 子代理) 或 `"acp"` (ACP 协议)
- `task`: 子代理的任务描述（详细、具体）
- `mode`: `"run"` (一次性) 或 `"session"` (持久会话)
- `cleanup`: `"delete"` (完成后自动删除) 或 `"keep"` (保留会话)
- `runTimeoutSeconds`: 超时时间（秒），默认 0 = 无超时
- `lightContext`: `true` (使用轻量级上下文，减少 token 消耗)

**⚠️ Claude Code Note:** Claude Code does not support `sessions_spawn`. Use WebSearch tool directly in main conversation instead.

### 按模式划分的子代理工作流

#### 1. Academic Research（Academic Research）

为每个数据库生成独立的子代理：

```json
[
  {"task": "在 PubMed 上搜索 [主题]，时间范围 [起始年份]-[结束年份]，关注 [关注点]"},
  {"task": "在 Google Scholar 上搜索 [主题]，按年份过滤 [起始年份]-[结束年份]"},
  {"task": "在 Semantic Scholar 上搜索 [主题]，按引用次数排序"}
]
```

**聚合结果：**
1. 等待所有子代理完成
2. 使用 `scripts/dedupe_results.py` 去重
3. 使用 `scripts/score_sources.py` 评分
4. 生成最终报告（使用 `academic_research_template.md`）

#### 2. Competitor Analysis（Competitor Analysis）

为每个竞品生成独立的子代理：

```json
[
  {"task": "分析 Otter.ai：功能、定价、用户评价、市场定位"},
  {"task": "分析 Fireflies.ai：功能、定价、用户评价、市场定位"},
  {"task": "分析 Fathom：功能、定价、用户评价、市场定位"}
]
```

**聚合结果：**
1. 等待所有子代理完成
2. 提取每个竞品的关键信息
3. 创建对比表格
4. 生成综合对比报告（使用 `competitor_analysis_template.md`）

**🎯 竞品参考商家（必须包含）：**

在Competitor Analysis报告中，**必须附上该产品/赛道中已经做起来的商家链接或名字**，给用户一个更直观的经验参考。具体要求：

1. **标注参考商家** — 对每个竞品或行业标杆，提供：
   - 商家名称（中英文）
   - 平台/店铺链接（Amazon 店铺、Etsy 店铺、独立站 URL、阿里巴巴店铺等）
   - 为什么值得参考（例如：月销量高、好评多、定价策略好、差异化做得好）

2. **分类展示参考商家**：
   - 🏆 **头部标杆** — 该赛道中做得最好的 2-3 个商家，适合学习整体策略
   - 💡 **差异化案例** — 有独特卖点的商家，适合借鉴差异化思路
   - 🆕 **新兴黑马** — 最近崛起的商家，适合了解最新趋势

3. **格式要求**：
```
### 参考商家

| 商家名称 | 平台 | 链接 | 月销量/好评 | 参考价值 |
|----------|------|------|------------|----------|
| BrandName | Amazon | https://... | ⭐4.8 (5K+) | 定价策略、listing 优化 |
| ShopName | Etsy | https://... | ⭐4.9 (2K+) | 产品差异化、包装设计 |
```

4. **搜索参考商家时，应重点查找**：
   - Amazon Best Sellers 排行榜上的商家
   - Etsy Star Sellers 或热门店铺
   - 独立站中有影响力的品牌
   - 行业论坛/Reddit 上被推荐的商家
   - 1688/阿里巴巴上评分高的供应商

#### 3. Market Trends（Market Trends）

为每个数据源生成独立的子代理：

```json
[
  {"task": "搜索 Gartner 关于 [行业] 市场趋势的报告 [年份]"},
  {"task": "搜索 CB Insights 关于 [行业] 融资数据 [年份]"},
  {"task": "搜索 PitchBook 关于 [行业] 并购活动 [年份]"}
]
```

**聚合结果：**
1. 等待所有子代理完成
2. 提取市场规模、增长率、投资信号
3. 识别趋势和机会
4. 生成Market Trends报告（使用 `market_trend_template.md`）

#### 4. Events & Conferences（Events & Conferences）

为每个活动平台生成独立的子代理：

```json
[
  {"task": "在 Eventbrite 上搜索 [主题] 活动，地点 [城市]，时间范围 [时间范围]"},
  {"task": "在 Luma 上搜索 [主题] 活动，地点 [城市]，时间范围 [时间范围]"},
  {"task": "在活动行上搜索 [主题] 活动，地点 [城市]，时间范围 [时间范围]"}
]
```

**聚合结果：**
1. 等待所有子代理完成
2. 去重（同一活动可能出现在多个平台）
3. 验证活动详情（日期、地点、报名状态）
4. 生成活动清单（使用 `event_collection_template.md`）

### 聚合结果

所有子代理完成后：

1. **收集结果** - 使用 `subagents` 工具，`action="list"` 检查状态
2. **获取输出** - 使用 `sessions_history` 获取子代理的输出
3. **去重** - 使用 `scripts/dedupe_results.py` 或手动去重
4. **评分** - 使用 `scripts/score_sources.py` 或手动评分
5. **合成** - 使用模板生成最终输出

### 错误处理

如果子代理失败：
- 使用 `subagents` 工具，`action="list"` 检查错误状态
- 使用修改后的参数重试任务
- 如果重试失败，在最终输出中注明失败原因
- 继续处理Other子代理的结果

### 超时处理

如果子代理超时：
- 增加 `runTimeoutSeconds` 参数
- 将任务分解为更小的子任务
- 使用 `mode="session"` 创建持久会话（允许多次交互）

### 🛡️ 超时保护策略（重要）

**核心原则：不要因为一个信息源超时就丢弃所有已收集的数据！**

#### 子代理级别的超时保护：

1. **设置合理超时时间** — 根据信息源特性设置不同超时：
   - Eventbrite / 活动行 / Luma：90-120 秒（页面相对简单）
   - Google 搜索 / Google Scholar：120-150 秒（反爬严格）
   - Alibaba / Amazon / Etsy：120-180 秒（反爬严格）
   - PubMed / Semantic Scholar API：90-120 秒（API 响应快）

2. **子代理内部执行策略** — 搜索多个 URL 时，**不要串行执行所有搜索**：
   - 先执行 1-2 个最重要的搜索
   - 如果成功获取到结果，**立即提取并格式化数据**
   - 再尝试额外搜索
   - 如果检测到时间不足（已用超过 60% 的超时时间），**立即停止新搜索**，优先处理已获取的数据
   - **绝不等到最后一秒才输出结果**

3. **超时子代理的结果处理**：
   - 超时子代理可能已经有部分数据（检查中间输出）
   - **即使是超时状态，也要提取已获取的信息**
   - 在报告中注明该信息源「部分结果（搜索超时）」
   - 不要标记为「搜索失败」，而是「部分完成」

4. **主代理聚合策略**：
   - **不需要等待所有子代理完成** — 只要有 2/3 以上子代理返回，即可开始生成报告
   - 如果 4 个子代理中有 3 个完成，**立即开始聚合**，超时的子代理结果后续补充
   - 在报告中标注每个信息源的完成状态：
     - ✅ 完整结果
     - ⏳ 部分结果（超时）
     - ❌ 未获取数据

5. **重试策略**：
   - 对于超时的重要信息源（如 Google 搜索），可以派发一个更小、更聚焦的子代理重试
   - 重试时减少搜索 URL 数量，聚焦 1 个最重要的查询

### 示例：完整的子代理工作流

**用户请求：**
```
查找关于供体肥胖程度（BMI）对肾移植存活率影响的近期论文，
时间范围 2020-2026，关注供体 BMI cutoff 值、延迟移植功能（DGF）发生率、以及长期移植物存活率。
```

**步骤 1：生成子代理**

```json
[
  {
    "runtime": "subagent",
    "task": "在 PubMed 上搜索 'donor obesity BMI kidney transplant survival'，时间范围 2020-2026。关注：1) 供体 BMI cutoff 值 2) DGF 发生率 3) 长期移植物存活率。返回前 10 篇相关论文，包括标题、作者、期刊、年份、摘要、DOI。",
    "mode": "run",
    "cleanup": "delete",
    "runTimeoutSeconds": 300
  },
  {
    "runtime": "subagent",
    "task": "在 Google Scholar 上搜索 'donor BMI kidney transplant outcome'，时间范围 2020-2026。按引用次数排序，返回前 10 篇相关论文，包括标题、作者、年份、引用次数、PDF 链接（如有）。",
    "mode": "run",
    "cleanup": "delete",
    "runTimeoutSeconds": 300
  },
  {
    "runtime": "subagent",
    "task": "在 Semantic Scholar 上搜索 'donor obesity renal transplant survival rate'，时间范围 2020-2026。返回前 10 篇相关论文，包括标题、作者、年份、引用次数、PDF 链接。",
    "mode": "run",
    "cleanup": "delete",
    "runTimeoutSeconds": 300
  }
]
```

**步骤 2：等待子代理完成**

使用 `subagents` 工具检查状态：
```json
{
  "tool": "subagents",
  "parameters": {
    "action": "list",
    "recentMinutes": 10
  }
}
```

**步骤 3：收集结果**

使用 `sessions_history` 获取每个子代理的输出：
```json
{
  "tool": "sessions_history",
  "parameters": {
    "sessionKey": "<sub-agent-session-key>",
    "limit": 10
  }
}
```

**步骤 4：去重与评分**

1. 合并所有论文结果
2. 使用标题和 DOI 去重
3. 使用 `references/reliability_scoring.md` 中的规则评分
4. 标记高/中/低置信度

**步骤 5：生成最终报告**

使用 `assets/output_templates/academic_research_template.md` 生成结构化报告。

---

## Scripts (Optional)

The `scripts/` directory contains optional helper scripts:

- `dedupe_results.py` - Deduplicate results by title, URL, date, or entity name
- `score_sources.py` - Score results by reliability, relevance, and freshness
- `normalize_events.py` - Normalize event fields to unified schema

These scripts are not required for MVP but can be used to automate processing.

## Examples

See `examples/` directory for sample requests and outputs:
- `academic_research_example.md`
- `competitor_analysis_example.md`
- `market_trend_example.md`
- `ai_events_example.md`

## File Structure

```
broad-information-research-skill/
├── SKILL.md                    # This file
├── README.md                   # Human-readable documentation
├── LICENSE                     # MIT License
├── references/                 # Reference data and rules
│   ├── source_registry.md
│   ├── source_registry_ai_events.md
│   ├── search_query_patterns.md
│   ├── reliability_scoring.md
│   └── task_taxonomy.md
├── assets/                    # Output templates
│   └── output_templates/
│       ├── academic_research_template.md
│       ├── competitor_analysis_template.md
│       ├── news_digest_template.md
│       ├── market_trend_template.md
│       └── event_collection_template.md
├── scripts/                    # Optional helper scripts
│   ├── dedupe_results.py
│   ├── score_sources.py
│   └── normalize_events.py
├── examples/                   # Example requests and outputs
│   ├── academic_research_example.md
│   ├── competitor_analysis_example.md
│   ├── market_trend_example.md
│   └── ai_events_example.md
└── tests/                      # Test cases
    ├── routing_tests.md
    ├── source_selection_tests.md
    └── output_quality_tests.md
```

## Version

Current version: 0.1 MVP

## License

MIT License - see LICENSE file for details.

---

## Post-Search Export Prompt (Required)

After completing the research and generating the structured output, **MUST ask the user**:

```
Research completed! How would you like to save the results?

1. Markdown (.md) - Easy to read and edit
2. JSON (.json) - For programmatic processing
3. CSV (.csv) - For Excel analysis
4. Word (.docx) - Formal document
5. PDF (.pdf) - For printing/sharing
6. Don't save - Just show in chat

Please select option (1-6):
```

**If user selects 1-5**, save the output to file using the appropriate format:

```python
# Save as Markdown
write to: outputs/{mode}_{topic}_{timestamp}.md

# Save as JSON  
write to: outputs/{mode}_{topic}_{timestamp}.json

# Save as CSV
write to: outputs/{mode}_{topic}_{timestamp}.csv
```

**File naming convention:**
- Mode: academic_research, competitor_analysis, domain_news, market_trends, events_collection
- Topic: first 3 words of the research topic (lowercase, underscores)
- Timestamp: YYYYMMDD_HHMM

**Example:** `academic_research_donor_obesity_20260603_1645.md`

**After saving, inform the user:**
```
✅ Results saved to: outputs/academic_research_donor_obesity_20260603_1645.md

You can also export to other formats later by saying:
"Export to PDF" or "Save as Word document"
```

---
