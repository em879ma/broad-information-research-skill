# Reliability Scoring

This file defines the scoring rules for evaluating information reliability, relevance, and freshness.

## Reliability Score (信息源可信度评分)

### Score 5 - Highest Reliability
- **Official sources**: Government websites, company websites, official announcements
- **Peer-reviewed papers**: Published in reputable journals with peer review
- **Government/organization pages**: Official government or organization webpages
- **Company announcements**: Official company press releases, investor relations pages

**Examples:**
- `https://www.gov.cn/` (Chinese government website)
- `https://www.nature.com/articles/...` (Nature paper)
- `https://investor.openai.com/` (OpenAI investor relations)
- `https://www.who.int/news/item/` (WHO official announcement)

### Score 4 - High Reliability
- **Reputable media**: Well-known news media with editorial standards
- **Respected databases**: Established academic or business databases
- **Well-known industry platforms**: Recognized industry websites or platforms

**Examples:**
- `https://www.reuters.com/...` (Reuters news)
- `https://www.bloomberg.com/...` (Bloomberg news)
- `https://scholar.google.com/...` (Google Scholar)
- `https://www.crunchbase.com/...` (Crunchbase database)

### Score 3 - Medium Reliability
- **Professional blogs**: Blogs written by industry professionals or experts
- **Conference pages**: Official conference or event websites
- **Community platforms**: Established community websites with moderation

**Examples:**
- `https://openai.com/blog/...` (OpenAI official blog - professional but not peer-reviewed)
- `https://neurips.cc/...` (NeurIPS conference page)
- `https://www.reddit.com/r/MachineLearning/` (Reddit ML community - moderated)

### Score 2 - Low Reliability
- **User-generated posts**: Social media posts, forum posts
- **Reposts**: Content that is reposted without original analysis
- **Unclear sources**: Content where the source is not clearly identified

**Examples:**
- `https://twitter.com/user/status/...` (Individual tweet)
- `https://www.zhihu.com/question/...` (Zhihu answer - user-generated)
- `https://www.xiaohongshu.com/...` (Xiaohongshu post - user-generated)

### Score 1 - Lowest Reliability
- **Unsourced claims**: Content that makes claims without citing sources
- **Marketing content**: Pure marketing or promotional content
- **Broken/expired pages**: Web pages that are no longer accessible

**Examples:**
- Marketing landing pages with unsubstantiated claims
- Expired event pages (404 errors)
- Content that cannot be verified from original source

## Relevance Score (相关性评分)

### Score 5 - Directly Answers the Question
- The content directly addresses the user's research question
- All key aspects of the question are covered
- The information is complete and actionable

**Example:**
User asks: "What are the side effects of GLP-1 receptor agonists?"
Paper: "Comprehensive review of GLP-1 receptor agonist side effects: nausea (30%), vomiting (10%), diarrhea (15%)..." → Score 5

### Score 4 - Strongly Related but Not Complete
- The content is strongly related to the question
- Most key aspects are covered, but some are missing
- The information is useful but may need supplementation

**Example:**
User asks: "What are the side effects of GLP-1 receptor agonists?"
Paper: "GLP-1 receptor agonists cause gastrointestinal side effects including nausea and vomiting..." (missing other side effects) → Score 4

### Score 3 - Useful Context Only
- The content provides useful background or context
- It does not directly answer the question but helps understanding
- The information is supplementary

**Example:**
User asks: "What are the side effects of GLP-1 receptor agonists?"
Paper: "GLP-1 receptor agonists work by mimicking incretin hormones..." (mechanism but not side effects) → Score 3

### Score 2 - Weakly Related
- The content is weakly related to the question
- It may mention related topics but is not directly relevant
- The information has limited value for the research question

**Example:**
User asks: "What are the side effects of GLP-1 receptor agonists?"
Paper: "Diabetes prevalence is increasing worldwide..." (general diabetes info, not about GLP-1 side effects) → Score 2

### Score 1 - Irrelevant or Off-Topic
- The content is not related to the research question
- It does not provide any useful information for the query
- The information is irrelevant

**Example:**
User asks: "What are the side effects of GLP-1 receptor agonists?"
Paper: "Artificial intelligence in healthcare..." (completely unrelated topic) → Score 1

## Freshness Score (时效性评分)

### Score 5 - Within User-Specified Time Range or Latest Available
- The content is published within the user's specified time range
- If no time range is specified, it is the latest available information
- The information is current and up-to-date

**Example:**
User asks: "Latest AI developments in 2026"
Article published: June 2026 → Score 5

### Score 4 - Recent and Still Valid
- The content is recent but may be slightly outside the ideal time range
- The information is still valid and applicable
- No major changes have occurred since publication

**Example:**
User asks: "AI developments in 2026"
Article published: December 2025 → Score 4 (recent and likely still valid)

### Score 3 - Somewhat Old but Useful Background
- The content is somewhat old but provides useful background information
- The core information may still be valid, but some details may be outdated
- Useful for understanding historical context or foundational concepts

**Example:**
User asks: "Recent AI developments"
Article published: 2023 → Score 3 (useful background but not recent developments)

### Score 2 - Outdated for Current Decisions
- The content is outdated for making current decisions
- The information may have been valid at the time but is no longer applicable
- Should be used with caution or supplemented with more recent information

**Example:**
User asks: "Current AI market size"
Report published: 2020 → Score 2 (outdated for current market decisions)

### Score 1 - Stale or Superseded
- The content is stale or has been superseded by newer information
- The information is no longer valid or has been disproven
- Should not be used for current research

**Example:**
User asks: "Current treatment guidelines for diabetes"
Guidelines published: 2010 → Score 1 (superseded by newer guidelines)

## Confidence Label (置信度标签)

### High Confidence
- **Reliable source** (reliability score 4-5)
- **Directly relevant** (relevance score 4-5)
- **Fresh** (freshness score 4-5)
- **Preferably cross-verified** (confirmed by multiple sources)

**Use case:** Can be presented as a definitive finding

**Example:**
- Source: Nature paper (reliability 5)
- Relevance: Directly answers the question (relevance 5)
- Freshness: Published in 2026 (freshness 5)
- Cross-verified: Confirmed by 3 other studies
→ **High confidence**

### Medium Confidence
- **Mostly reliable** but incomplete, old, or only one strong source
- Reliability score 3-4, OR
- Relevance score 3-4, OR
- Freshness score 3-4, OR
- Only one strong source (not cross-verified)

**Use case:** Present as likely finding but note limitations

**Example:**
- Source: TechCrunch article (reliability 4)
- Relevance: Strongly related but not complete (relevance 4)
- Freshness: Published 6 months ago (freshness 4)
- Only one source (not cross-verified)
→ **Medium confidence**

### Low Confidence
- **Weak source** (reliability score 1-2)
- **Conflict** between sources
- **Unclear date** or timing
- **Limited evidence** (only one weak source)

**Use case:** Present as preliminary or uncertain, clearly label as low confidence

**Example:**
- Source: Individual tweet (reliability 2)
- Relevance: Weakly related (relevance 2)
- Freshness: Date unclear (freshness ?)
- Only one source, weak
→ **Low confidence**

## Deduplication and Conflict Rules

### Deduplication Rules
- **If multiple sources report the same event**, keep the most official or original source
- **If the same information appears in multiple formats** (e.g., press release and news article), prefer the original source
- **Remove duplicates** from the results list

### Conflict Rules
- **If sources conflict**, do not merge silently; report the conflict explicitly
- **Present both sides** of the conflict with their respective sources
- **Let the user decide** which source to trust, or provide guidance on evaluating the sources
- **Label conflicting information** as "conflicting" or "disputed"

**Example:**
Source A (company website): "Product X will launch in Q2 2026"
Source B (tech media): "Product X launch delayed to Q4 2026"

→ Report conflict: "There is a conflict between sources. The company website states Q2 2026 launch, while tech media reports Q4 2026 delay. Further verification needed."

### Expiration Rules
- **If an event/news item is expired**, exclude it unless the user asks for historical results
- **Clearly label expired information** if included for historical context
- **Check dates carefully** to avoid presenting expired information as current

### Weak Source Rules
- **If only weak sources support an item**, mark it as low confidence
- **Do not present weak-source information as fact**
- **Label clearly** as "low confidence" or "unverified"

## Scoring Workflow

1. **For each information item**, assign:
   - Reliability score (1-5)
   - Relevance score (1-5)
   - Freshness score (1-5)

2. **Calculate confidence label**:
   - High: reliability 4-5 AND relevance 4-5 AND freshness 4-5 AND (cross-verified OR reliability=5)
   - Medium: (reliability 3-4 OR relevance 3-4 OR freshness 3-4) OR (only one strong source)
   - Low: reliability 1-2 OR conflict OR unclear date OR limited evidence

3. **Apply deduplication and conflict rules**

4. **Output with scores and confidence labels**

## Example Scoring

**Information Item:** "OpenAI released GPT-5 in June 2026"

**Source:** OpenAI official blog (reliability 5)
**Relevance:** Directly answers the question "When was GPT-5 released?" (relevance 5)
**Freshness:** June 2026, user asks for 2026 information (freshness 5)
**Cross-verified:** Confirmed by TechCrunch and The Verge (cross-verified)

→ **High confidence**

**Source:** Individual tweet (reliability 2)
**Relevance:** Mentions GPT-5 release (relevance 3)
**Freshness:** Date unclear (freshness ?)
**Cross-verified:** No, only one source

→ **Low confidence**
