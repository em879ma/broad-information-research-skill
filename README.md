# 🔍 Broad Information Research Skill

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT" />
  <img src="https://img.shields.io/badge/version-0.3--beta-orange.svg" alt="Version: 0.3 Beta" />
  <img src="https://img.shields.io/badge/MCP-Server-green.svg" alt="MCP Server" />
  <img src="https://img.shields.io/badge/MCP-Server-blue.svg" alt="MCP Server" />
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg" alt="Platform: macOS | Linux | Windows" />
</p>

<p align="center">
  <strong>A general-purpose MCP server for collecting, screening, verifying, and summarizing information across multiple domains — works with QClaw, Claude Code, Cursor, and any MCP client.</strong>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-features">Features</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-examples">Examples</a> •
  <a href="#-media-crawler-integration">MediaCrawler Integration</a> •
  <a href="#-troubleshooting">Troubleshooting</a>
</p>

---

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [What It Does](#-what-it-does)
- [Key Features](#-key-features)
- [Supported Research Modes](#-supported-research-modes)
- [Installation](#-installation)
- [MCP Server Configuration](#-mcp-server-configuration)
- [Usage](#-usage)
- [MediaCrawler Integration](#-mediacrawler-integration)
- [WeChat Official Account Integration](#-wechat-official-account-integration)
- [Examples](#-examples)
- [File Structure](#-file-structure)
- [Scripts](#-scripts)
- [Development Roadmap](#-development-roadmap)
- [Troubleshooting](#-troubleshooting)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [License](#-license)
- [Support](#-support)
- [Acknowledgments](#-acknowledgments)

---

## 🚀 Quick Start

```bash
# Option 1: Install via SkillHub (Recommended)
skillhub install broad-information-research

# Option 2: Manual Installation
git clone https://github.com/em879ma/broad-information-research-skill.git
cp -r broad-information-research-skill ~/.qclaw/skills/
```

The MCP server is now active and ready to use.

---

## 🎯 What It Does

This skill helps you **collect, screen, verify, and summarize information** across 7 research modes:

- 📚 **Academic Research** - Papers, literature review, research gaps
- 🏢 **Competitor Analysis** - Product/company comparison, features, pricing
- 📰 **Domain News** - Recent news, weekly updates, latest developments
- 📈 **Market Trends** - Market direction, industry momentum, investment signals
- 🎪 **Events & Conferences** - Conferences, meetups, summits, hackathons
- ⚖️ **Policy & Regulation** - Laws, compliance, government policy
- 🏢 **Company Intelligence** - Company info, funding, partnerships, hiring

**Core Workflow:**
```
User Request → Task Classification → Channel Selection → 
Keyword Generation → Information Retrieval → Deduplication & Verification → 
Credibility Scoring → Structured Output
```

---

## ✨ Key Features

✅ **Interactive Guide Flow** - Step-by-step guidance for optimal results  
✅ **Multi-Source Integration** - Academic databases, news media, social platforms  
✅ **MediaCrawler Integration** - Crawl Xiaohongshu, Bilibili, Weibo, Zhihu, etc.  
✅ **WeChat Official Account Integration** - Search WeChat official account articles  
✅ **Intelligent Deduplication** - Remove duplicate results automatically  
✅ **Credibility Scoring** - Score results by relevance, reliability, freshness  
✅ **Structured Output** - Mode-specific output templates (Markdown/JSON/CSV)  
✅ **Export Capabilities** - Export to file, Tencent Docs, PDF  
✅ **Multi-Turn Conversation** - Support follow-up questions and refinement  

---

## 🔧 Supported Research Modes

### 1. Academic Research
**Use for:** Literature review, research gaps, evidence synthesis, theoretical frameworks

**Information Sources:**
- Google Scholar, PubMed, IEEE Xplore, ACM Digital Library
- arXiv, Scopus, Web of Science

**Output:** Literature matrix, thematic synthesis, research gaps

---

### 2. Competitor Analysis
**Use for:** Product/company comparison, features, pricing, positioning, business models

**Information Sources:**
- Official websites, product pages
- G2, Capterra, TrustRadius (user reviews)
- Crunchbase, PitchBook (funding data)
- News articles, industry reports

**Output:** Competitor map, comparison table, strategic takeaways

---

### 3. Domain News
**Use for:** Recent news, weekly updates, latest developments, event timelines

**Information Sources:**
- Reuters, Bloomberg, AP News
- TechCrunch, The Verge, Hacker News
- WeChat official accounts (via wechat-download-api)
- Industry-specific news sites

**Output:** Key news table, timeline, implications

---

### 4. Market Trends
**Use for:** Market direction, industry momentum, investment signals, emerging opportunities

**Information Sources:**
- Industry reports (Gartner, IDC, Forrester)
- Market research firms
- Financial news, SEC filings
- Social media trends (via MediaCrawler)

**Output:** Trend table, signals to monitor, uncertainties

---

### 5. Events & Conferences
**Use for:** Conferences, meetups, summits, hackathons, competitions, trainings

**Information Sources:**
- Eventbrite, Meetup.com, Cvent
- Conference websites, LinkedIn Events
- Industry association websites
- Social media event posts (via MediaCrawler)

**Output:** Verified events table, excluded events, notes

---

### 6. Policy & Regulation
**Use for:** Laws, compliance, official rules, government policy, regulatory change

**Information Sources:**
- Government websites (.gov)
- Legal databases
- Official gazettes
- Policy analysis think tanks

**Output:** Policy table, compliance checklist, impact analysis

---

### 7. Company or Organization Intelligence
**Use for:** Company info, funding, partnerships, hiring, roadmap

**Information Sources:**
- Company website, Crunchbase, PitchBook
- LinkedIn, Glassdoor
- News articles, press releases
- Job postings, patent filings

**Output:** Company profile, SWOT analysis, partnership map

---

## 📦 Installation

### Prerequisites

- **Python >= 3.10** (3.11 recommended)
- **uv** (Python package manager) — will be installed automatically if needed
- **Git** for cloning

### Option 1: Install via SkillHub (QClaw users)

```bash
skillhub install broad-information-research
```

### Option 2: Manual Installation

**Step 1: Clone the repository**
```bash
git clone https://github.com/em879ma/broad-information-research-skill.git
cd broad-information-research-skill
```

**Step 2: Set up Python environment**
```bash
uv venv .venv --python 3.11
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate    # Windows
uv pip install mcp pydantic>=2 -e .
```

**Step 3: Configure in your MCP client**

See [MCP Server Configuration](#-mcp-server-configuration) section below for QClaw, Claude Code, and Cursor setup.
### Optional Dependencies

**MediaCrawler** (for social media crawling): https://github.com/NanmiCoder/MediaCrawler

**WeChat Query Skill** (for WeChat official account articles): https://github.com/adennng/wechat-query-skill

When searching these channels, the skill will automatically ask if you want to install them.

---

## 📖 Usage

### Basic Usage

After installation, invoke the skill in QClaw:

```
> Use this skill to [your request]
```

The skill will start an **interactive guide flow**:

**Step 1: Choose information type**
```
请选择您想查找的信息类型：

1. 学术研究 (Academic Research)
2. 竞品分析 (Competitor Analysis)
3. 领域新闻 (Domain News)
4. 市场动向 (Market Trends)
5. 活动/会议搜集 (Events & Conferences)
6. 其他 (Other)

请输入选项编号 (1-6) 或直接描述您的需求：
```

**Step 2: Input specific request**
Based on your choice, the skill will ask targeted follow-up questions.

**Step 3: Information retrieval**
The skill will search multiple sources, deduplicate results, verify credibility, and generate structured output.

**Step 4: Review and refine**
You can ask follow-up questions or request modifications.

### Advanced Usage

#### Use MediaCrawler for social media crawling

If your research involves Xiaohongshu, Bilibili, Weibo, Zhihu, etc., the skill will:
1. Check if MediaCrawler is installed
2. If not, ask if you want to install it
3. If yes, provide installation instructions
4. If installed, run MediaCrawler CLI to crawl data

#### Use WeChat Download API for official account articles

If your research involves Chinese-language sources, the skill can:
1. Check if wechat-download-api is running
2. If not, ask if you want to start it
3. If yes, search WeChat official accounts and articles

#### Export results

After generating results, you can:
```
> Export to Tencent Docs
> Save to file
> Export as PDF
```

---

### v0.3: MCP Server Integration (Recommended)

The core logic has been extracted to a standalone **MCP server** that can be used with QClaw, Claude Code, Cursor, and any MCP-compatible client.


**Installation:**
```bash
# Clone repositories
git clone https://github.com/em879ma/broad-information-research-skill.git
cd broad-information-research-skill

# Create venv
uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install mcp pydantic>=2 -e .

# Configure in QClaw (add to openclaw.json)
# {
#   "mcp": {
#     "servers": {
#       "broad-information-research": {
#         "command": "path/to/.venv/bin/python",
#         "args": ["-m", "broad_information_research_mcp.server"],
#         "cwd": "/path/to/broad-information-research-skill"
#       }
#     }
#   }
# }
```

**Available Tools (8 total):**

| Tool | Description |
|------|------------|
| `classify_research_task` | Classify query into 7 research modes |
| `get_sources_for_task` | Get recommended info sources by mode |
| `generate_search_queries` | Generate optimized search queries |
| `deduplicate_results` | Remove duplicate results (Jaccard similarity) |
| `score_results` | Score by credibility/freshness/relevance |
| `render_output` | Render results in MD/HTML/JSON/Text |
| `crawl_social_media` | Crawl platforms via MediaCrawler |
| `mediacrawler_status` | Check MediaCrawler availability |


This repo contains both the core Python library (`broad_information_research/`) and the MCP server (`broad_information_research_mcp/`).

---

## 🕷️ MediaCrawler Integration

This skill uses **MediaCrawler** for social media crawling: https://github.com/NanmiCoder/MediaCrawler

When your research involves Xiaohongshu, Bilibili, Weibo, Zhihu, Douyin, Kuaishou, or Tieba, the skill will automatically ask if you want to install it.

---

## 📱 WeChat Official Account Integration

This skill uses **WeChat Query Skill** to search WeChat official account articles: https://github.com/adennng/wechat-query-skill

When searching Chinese-language sources, the skill will automatically ask if you want to install it.

---

## 📝 Examples

### Example 1: Academic Research

**Request:**
```
> Use this skill to find recent academic papers about GLP-1 and kidney transplant outcomes
```

**Skill response:**
```
✅ Task classified as: Academic Research

Generating search queries...
- "GLP-1 receptor agonists kidney transplant"
- "semaglutide transplant outcomes"
- "GLP-1 CKD transplant patients"

Searching Google Scholar...
Found 12 papers.

Deduplicating results...
Removed 3 duplicates.

Scoring results...
- "Semaglutide and Kidney Transplant Outcomes" (2025, NEJM) - Relevance: 5, Reliability: 5, Freshness: 5, Confidence: HIGH
- "GLP-1 Agonists in Transplant Medicine" (2024, Transplantation) - Relevance: 4, Reliability: 5, Freshness: 4, Confidence: HIGH
...

Generating structured output...
Saved to: outputs/academic_research_glp1_kidney_transplant_20260602.md
```

---

### Example 2: Competitor Analysis

**Request:**
```
> Use this skill to compare competitors of an AI meeting assistant product
```

**Skill response:**
```
✅ Task classified as: Competitor Analysis

Identifying competitors...
- Otter.ai
- Fireflies.ai
- Rev.com
- Descript
- Grain

Searching product information...
- Features
- Pricing
- User reviews
- Funding

Generating comparison table...
Saved to: outputs/competitor_analysis_ai_meeting_assistant_20260602.md
```

---

### Example 3: Events & Conferences (with MediaCrawler)

**Request:**
```
> Use this skill to find AI events in Shanghai next month
```

**Skill response:**
```
✅ Task classified as: Events & Conferences

Do you want to search social media (Xiaohongshu, Bilibili, Weibo) for event information?

1. Yes, use MediaCrawler to crawl social media
2. No, use only official sources

> 1

[Checks MediaCrawler status...]
[MediaCrawler not installed. Asking user...]
Do you want to install MediaCrawler?

1. Yes, install MediaCrawler
2. No, skip social media sources

> 1

[Providing installation instructions...]
After installation, the skill will run MediaCrawler to crawl event information from social media.

Searching official sources...
- Eventbrite
- Meetup.com
- Conference websites

Searching social media (after MediaCrawler installation)...
- Xiaohongshu posts about "上海 AI 活动"
- Bilibili videos about "上海 AI 大会"
- Weibo posts about "上海 人工智能 会议"

Generating verified events table...
Saved to: outputs/event_collection_shanghai_ai_20260603.md
```

---

### Example 4: Domain News (with WeChat Official Accounts)

**Request:**
```
> Use this skill to track recent news about OpenAI's GPT model releases
```

**Skill response:**
```
✅ Task classified as: Domain News

Do you want to search WeChat official accounts for Chinese-language news?

1. Yes, use wechat-download-api
2. No, use only international sources

> 1

[Checks wechat-download-api status...]
[wechat-download-api not running. Asking user...]
Do you want to start wechat-download-api?

1. Yes, start wechat-download-api
2. No, skip WeChat sources

> 1

[Providing docker-compose instructions...]
After starting, you need to login by scanning QR code.

Searching international sources...
- Reuters
- Bloomberg
- TechCrunch

Searching WeChat official accounts (after login)...
- "机器之心" articles about "GPT-5"
- "量子位" articles about "OpenAI 发布"

Generating news digest...
Saved to: outputs/news_digest_openai_gpt_20260603.md
```

---

## 📂 File Structure

```
broad-information-research-skill/
├── SKILL.md                    # QClaw skill instructions (interactive guide)
├── README.md                   # This file
├── LICENSE                     # MIT License
├── pyproject.toml              # Root project config (declares both packages)
├── references/                 # Reference data and rules
│   ├── source_registry.md      # Source channels by mode
│   ├── source_registry_ai_events.md  # AI event sources
│   ├── search_query_patterns.md      # Query generation patterns
│   ├── reliability_scoring.md        # Scoring rules
│   └── task_taxonomy.md             # Task classification rules
├── assets/                    # Output templates
│   └── output_templates/
│       ├── academic_research_template.md
│       ├── competitor_analysis_template.md
│       ├── news_digest_template.md
│       ├── market_trend_template.md
│       └── event_collection_template.md
├── scripts/                    # Helper scripts
│   ├── dedupe_results.py      # Deduplicate results
│   ├── score_sources.py       # Score results by reliability/relevance/freshness
│   ├── normalize_events.py    # Normalize event fields
│   ├── save_to_file.py        # Save results to file
│   ├── export_report.py       # Export results (Tencent Docs, PDF)
│   └── mediacrawler_wrapper.py  # Wrapper for MediaCrawler CLI
├── examples/                   # Example requests and outputs
│   ├── academic_research_example.md
│   ├── competitor_analysis_example.md
│   ├── market_trend_example.md
│   └── ai_events_example.md
├── outputs/                    # Generated outputs (gitignored)
│   ├── academic_research_glp1_kidney_transplant_20260602.md
│   ├── competitor_analysis_ai_meeting_assistant_20260602.md
│   └── ...
├── tests/                      # Test cases
│   ├── routing_tests.md        # Task classification tests
│   ├── source_selection_tests.md   # Source selection tests
│   └── output_quality_tests.md     # Output quality tests
├── broad_information_research/   # Core Python library
│   ├── __init__.py
│   ├── task_classifier.py       # 7-mode task classifier
│   ├── source_selector.py       # Source registry by mode
│   ├── query_generator.py       # Query generation for 4+ source types
│   ├── deduplicator.py          # Jaccard similarity dedup
│   ├── scorer.py                # 3-dimension scoring
│   ├── output_renderer.py       # MD/HTML/JSON/Text output
│   └── mediacrawler_client.py   # MediaCrawler CLI wrapper
└── broad_information_research_mcp/  # MCP server package
    ├── __init__.py
    ├── server.py                 # 8 MCP tools
    ├── pyproject.toml           # MCP package config
    └── README.md                 # MCP server docs
```

---

## 🛠️ Scripts

The `scripts/` directory contains optional Python helper scripts:

### Core Scripts

- **`dedupe_results.py`** - Deduplicate results by title, URL, date, or entity name
- **`score_sources.py`** - Score results by reliability, relevance, and freshness
- **`normalize_events.py`** - Normalize event fields to unified schema

### Extended Scripts

- **`save_to_file.py`** - Save results to Markdown/JSON/CSV file
- **`export_report.py`** - Export results to Tencent Docs or PDF
- **`mediacrawler_wrapper.py`** - Wrapper script for MediaCrawler CLI

### Usage

```bash
# Deduplicate results
python scripts/dedupe_results.py --input outputs/raw_results.json --output outputs/deduped_results.json

# Score results
python scripts/score_sources.py --input outputs/deduped_results.json --output outputs/scored_results.json

# Save to file
python scripts/save_to_file.py --input outputs/scored_results.json --output outputs/final_report.md --format markdown

# Export to Tencent Docs
python scripts/export_report.py --input outputs/scored_results.json --format tencent-docs --title "My Research Report"
```

---

## 🗺️ Development Roadmap

### ✅ v0.1 MVP (Completed)
- [x] Task classification (7 modes)
- [x] Universal scoring system
- [x] 5 output templates
- [x] Source registry
- [x] Search query patterns
- [x] Basic scripts (dedupe, score, normalize)

### ✅ v0.2 MediaCrawler Integration (Completed)
- [x] Integrate MediaCrawler for social media crawling
- [x] Support 7 platforms (Xiaohongshu, Zhihu, Weibo, Bilibili, Douyin, Kuaishou, Tieba)
- [x] CLI mode wrapper script
- [x] Interactive installation prompt

### ✅ v0.3 MCP Server & Core Library (Completed)
- [x] Extract core logic to standalone Python package `broad-information-research-core`
- [x] Build MCP service `broad-information-research-mcp` with 8 tools
- [x] Compatible with QClaw, Claude Code, Cursor, and any MCP client
- [x] Verified all 8 tools working (classify, sources, queries, dedupe, score, render, crawl, status)
- [x] Independent venv with MCP 1.27.2 + pydantic 2.x

### ✅ v0.2 MediaCrawler Integration (Completed)
- [x] Integrate MediaCrawler CLI for 7 platforms (XHS, Weibo, Bilibili, Douyin, Kuaishou, Zhihu, Tieba)
- [x] QR code login support for all platforms
- [x] Auto-degradation when MediaCrawler unavailable
- [x] Platform status check tool

### 🔄 v0.4 Enhanced Output (In Progress)
- [ ] Export to Tencent Docs
- [ ] Export to PDF
- [ ] Multi-turn conversation support

### 🚀 v1.0 Stable Release (Planned)
- [ ] Complete test cases
- [ ] Add CI/CD pipeline
- [ ] Add CHANGELOG.md
- [ ] Publish to SkillHub
- [ ] Write comprehensive documentation

---

## 🔧 Troubleshooting

### Issue: MediaCrawler fails to start

**Symptoms:**
```
MediaCrawler API server starts then exits immediately
```

**Solution:**
Use CLI mode instead of API mode:
1. Edit `MediaCrawler/config/base_config.py`
2. Change `ENABLE_CDP_MODE: bool = True` to `ENABLE_CDP_MODE: bool = False`
3. Run MediaCrawler via CLI: `uv run python main.py --platform xhs --lt qrcode --type search --keywords "test"`

---

### Issue: WeChat Download API fails to start

**Symptoms:**
```
docker-compose up -d fails with permission error
```

**Solution:**
Use `sudo` or adjust Docker permissions:
```bash
sudo docker-compose up -d
```

Or add your user to the `docker` group:
```bash
sudo usermod -aG docker $USER
# Logout and login again
```

---

### Issue: Skill not found after installation

**Symptoms:**
```
> Use this skill to...
Error: Skill not found: broad-information-research
```

**Solution:**
1. Check if the skill is in the correct directory:
   ```bash
   ls ~/.qclaw/skills/broad-information-research-skill/
   ```
2. If not, copy the skill to the correct directory:
   ```bash
   cp -r broad-information-research-skill ~/.qclaw/skills/
   ```
3. Restart QClaw gateway:
   ```bash
   openclaw gateway restart
   ```

---

### Issue: MediaCrawler login fails

**Symptoms:**
```
QR code scan fails or times out
```

**Solution:**
1. Make sure you're using the correct app to scan the QR code:
   - Xiaohongshu → Xiaohongshu app
   - Weibo → Weibo app
   - Bilibili → Bilibili app
2. Make sure your phone and computer are on the same network
3. Try again with a fresh QR code

---

## ❓ FAQ

### Q1: Does this skill require an internet connection?

**A:** Yes, most features require internet to search online sources. However, you can use locally downloaded data (e.g., from MediaCrawler) offline.

---

### Q2: Is MediaCrawler required?

**A:** No, MediaCrawler is optional. If you don't need to crawl Xiaohongshu, Bilibili, etc., you can skip MediaCrawler installation. The skill will use other sources (Google Scholar, news media, etc.).

---

### Q3: Is wechat-download-api required?

**A:** No, wechat-download-api is optional. If you don't need WeChat official account articles, you can skip it. The skill will use other sources.

---

### Q4: Can I use this skill without QClaw?

**A:** Yes! This is now primarily an **MCP server** that works with any MCP-compatible client (QClaw, Claude Code, Cursor, etc.). You can also use the core Python library (`broad_information_research/`) directly in your own projects.

---

### Q5: How do I contribute?

**A:** See the [Contributing](#-contributing) section below. Pull requests are welcome!

---

### Q6: How do I report bugs or request features?

**A:** Please open an issue on the [GitHub repository](https://github.com/em879ma/broad-information-research-skill/issues).

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Guidelines

- Follow the existing code style
- Add tests for new features
- Update documentation as needed
- Make sure all tests pass

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💬 Support

If you encounter any issues or have suggestions for improvement, please:

- Open an issue on the [GitHub repository](https://github.com/em879ma/broad-information-research-skill/issues)
- Join our community (link TBD)
- Contact the maintainer (email TBD)

---

## 🙏 Acknowledgments

- **QClaw (OpenClaw)** - For the amazing AI assistant framework
- **MediaCrawler** - For the multi-platform social media crawler
- **wechat-download-api** - For the WeChat official account API
- **All contributors** - For improving this skill

---

## 📧 Contact

Maintainer: em879ma  
GitHub: [@em879ma](https://github.com/em879ma)  
Repository: [broad-information-research-skill](https://github.com/em879ma/broad-information-research-skill)

---

<p align="center">
  ⭐ Star this repository if you find it useful! ⭐
</p>

<p align="center">
  Made with ❤️ for researchers, analysts, and professionals who need to collect and evaluate information across multiple domains.
</p>
