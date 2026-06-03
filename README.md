# 🔍 Broad Information Research Skill

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT" />
  <img src="https://img.shields.io/badge/version-0.2-beta-orange.svg" alt="Version: 0.2 Beta" />
  <img src="https://img.shields.io/badge/QClaw-Skill-green.svg" alt="QClaw Skill" />
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg" alt="Platform: macOS | Linux | Windows" />
</p>

<p align="center">
  <strong>A reusable QClaw skill for collecting, screening, verifying, and summarizing information across multiple domains.</strong>
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

**Then in QClaw:**
```
> Use this skill to find AI events in Shanghai next month
```

The skill will guide you through an interactive flow to collect, verify, and summarize information from multiple sources.

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

- **QClaw** (OpenClaw) installed and configured
- **Python >= 3.10** (for MediaCrawler integration)
- **uv** (Python package manager) - will be installed automatically if needed
- **Chrome browser** (recommended) or Playwright

### Option 1: Install via SkillHub (Recommended)

```bash
skillhub install broad-information-research
```

### Option 2: Manual Installation

**Step 1: Clone the repository**
```bash
git clone https://github.com/em879ma/broad-information-research-skill.git
cd broad-information-research-skill
```

**Step 2: Copy to QClaw skills directory**
```bash
# Managed skills directory (recommended)
cp -r broad-information-research-skill ~/.qclaw/skills/

# OR: Personal skills directory
cp -r broad-information-research-skill ~/.agents/skills/
```

**Step 3: Verify installation**
```bash
ls ~/.qclaw/skills/broad-information-research-skill/
# Should show: SKILL.md, README.md, LICENSE, references/, assets/, scripts/, examples/, tests/
```

### Optional: Install MediaCrawler (for social media crawling)

```bash
# 1. Install uv (if not installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Clone MediaCrawler
cd ~
git clone https://github.com/NanmiCoder/MediaCrawler.git
cd MediaCrawler

# 3. Install dependencies
uv sync

# 4. Install Playwright browser
uv run playwright install chromium

# 5. Configure (disable CDP mode, use Playwright mode)
sed -i '' 's/ENABLE_CDP_MODE: bool = True/ENABLE_CDP_MODE: bool = False/' config/base_config.py

# 6. Test run (scan QR code to login)
uv run python main.py --platform xhs --lt qrcode --type search --keywords "test" --crawler_max_notes_count 5
```

### Optional: Install WeChat Download API (for WeChat official accounts)

```bash
# 1. Install Docker (if not installed)
# Download from: https://www.docker.com/products/docker-desktop

# 2. Clone wechat-download-api
cd ~
git clone https://github.com/your-repo/wechat-download-api.git
cd wechat-download-api

# 3. Start with docker-compose
docker-compose up -d

# 4. Check status
curl <INTERNAL_HOST_REMOVED>

# 5. Login by scanning QR code
# Open <INTERNAL_HOST_REMOVED> in browser, scan QR code with WeChat
```

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

## 🕷️ MediaCrawler Integration

MediaCrawler is a powerful web crawler that supports **7 platforms**:

| Platform | Command | Login Method |
|----------|---------|-------------|
| 小红书 (Xiaohongshu) | `--platform xhs` | QR code scan |
| 知乎 (Zhihu) | `--platform zhihu` | QR code scan |
| 微博 (Weibo) | `--platform weibo` | QR code scan |
| B站 (Bilibili) | `--platform bili` | QR code scan |
| 抖音 (Douyin) | `--platform dy` | QR code scan |
| 快手 (Kuaishou) | `--platform ks` | QR code scan |
| 贴吧 (Tieba) | `--platform tieba` | QR code scan |

### How it works

1. The skill detects if your request involves social media platforms
2. If MediaCrawler is not installed, the skill **automatically asks if you want to install it**
3. If you agree, the skill provides installation instructions
4. After installation, the skill runs MediaCrawler CLI to crawl data
5. Results are saved to `MediaCrawler/data/<platform>/jsonl/` directory

### Example: Crawl Xiaohongshu notes

```bash
cd ~/MediaCrawler
uv run python main.py \
  --platform xhs \
  --lt qrcode \
  --type search \
  --keywords "AI tools" \
  --crawler_max_notes_count 20
```

This will:
- Open a browser and display a QR code
- You scan the QR code with Xiaohongshu app to login
- Crawl 20 notes with keyword "AI tools"
- Save results to `MediaCrawler/data/xhs/jsonl/`

### Supported content types

- **Search** (`--type search`) - Search notes/videos by keyword
- **Creator** (`--type creator`) - Get creator's posts
- **Detail** (`--type detail`) - Get note/video details

---

## 📱 WeChat Official Account Integration

WeChat official accounts are a major source of high-quality Chinese-language content. This skill integrates with `wechat-download-api` to search and download official account articles.

### How it works

1. The skill detects if your request involves Chinese-language sources
2. If wechat-download-api is not running, the skill asks if you want to start it
3. If you agree, the skill provides docker-compose instructions
4. After starting, you need to login by scanning a QR code
5. The skill can then search official accounts and download articles

### Setup

**Step 1: Start wechat-download-api**
```bash
cd ~/wechat-download-api
docker-compose up -d
```

**Step 2: Check status**
```bash
curl <INTERNAL_HOST_REMOVED>
# Should return: {"status": "healthy", ...}
```

**Step 3: Login**
- Open `<INTERNAL_HOST_REMOVED> in browser
- Scan QR code with WeChat app
- After login, the API can access your official accounts

### Usage

After setup, the skill can:
```
> Search WeChat official accounts for "AI" 
> Get latest articles from "全球人工智能" official account
> Download articles from "机器之心" in the past month
```

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
├── SKILL.md                    # Main skill instructions (read by QClaw)
├── README.md                   # This file
├── LICENSE                     # MIT License
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
└── tests/                      # Test cases
    ├── routing_tests.md        # Task classification tests
    ├── source_selection_tests.md   # Source selection tests
    └── output_quality_tests.md     # Output quality tests
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

### 🔄 v0.3 WeChat Integration (In Progress)
- [x] Integrate wechat-download-api for WeChat official accounts
- [ ] Improve WeChat article parsing
- [ ] Add WeChat account subscription management
- [ ] Add more Chinese-language sources

### 📅 v0.4 Export & Integration (Planned)
- [ ] Export to Tencent Docs
- [ ] Export to PDF
- [ ] Integration with more QClaw skills
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

**A:** No, this is a QClaw skill and requires QClaw (OpenClaw) to run. However, you can adapt the scripts and templates for other uses.

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
