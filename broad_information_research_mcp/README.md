# Broad Information Research MCP Service

A Model Context Protocol (MCP) service that provides structured tools for broad information research across academic, competitive, market, technology, event, and opinion research modes.

## Architecture

```
broad-information-research-skill (QClaw)
          ↓ extract core logic
broad-information-research-core (Python package)
          ↓ wrap as MCP tools
broad-information-research-mcp (MCP service)
          ↓ connect
Any MCP-compatible agent (Claude Code, Cursor, etc.)
```

## Installation

### 1. Install the core package (editable mode)

```bash
cd /path/to/broad-information-research-core
pip install -e .
```

### 2. Install the MCP service

```bash
cd /path/to/broad-information-research-mcp
pip install -e .
```

### 3. Configure the MCP client

Add to your MCP client configuration (e.g., Claude Code's `~/.claude/...` or Cursor's settings):

```json
{
  "mcpServers": {
    "broad-information-research": {
      "command": "broad-information-research-mcp",
      "args": []
    }
  }
}
```

Or run directly:

```bash
uv run python -m broad_information_research_mcp.server
```

## Available Tools

| Tool | Description |
|------|-------------|
| `classify_research_task` | Classify a query into one of 7 research modes |
| `get_sources_for_task` | Get recommended information sources for a mode |
| `generate_search_queries` | Generate optimized search queries |
| `deduplicate_results` | Remove duplicate results from search output |
| `score_results` | Score results by credibility, freshness, relevance |
| `render_output` | Render results in markdown/html/json/text format |
| `crawl_social_media` | Crawl social platforms via MediaCrawler |
| `mediacrawler_status` | Check MediaCrawler availability |

## Research Modes

| Mode | Description |
|------|-------------|
| `academic_research` | Academic papers, literature review, systematic review |
| `competitive_analysis` | Competitor comparison, market positioning |
| `market_research` | Market size, trends, consumer insights |
| `technology_tracking` | Framework updates, tool releases, GitHub stars |
| `event_monitoring` | Real-time news, breaking updates |
| `opinion_analysis` | Social media sentiment, reviews, feedback |
| `custom_research` | Fallback for undefined topics |

## Usage Example

```python
# Classify a research query
result = await mcp.call_tool("classify_research_task", {
    "query": "What are the latest developments in Rust async programming?"
})
# Returns: { "mode": "technology_tracking", "confidence": 0.85, ... }

# Get sources for the identified mode
sources = await mcp.call_tool("get_sources_for_task", {
    "mode": "technology_tracking"
})
# Returns: [{ "name": "GitHub", "type": "code", ... }, ...]

# Generate search queries
queries = await mcp.call_tool("generate_search_queries", {
    "topic": "Rust async",
    "source_type": "general",
    "max_queries": 5
})
# Returns: ["Rust async", "Rust async guide", "Rust async examples", ...]

# Deduplicate search results
deduped = await mcp.call_tool("deduplicate_results", {
    "results": [...],
    "similarity_threshold": 0.85
})

# Score results
scored = await mcp.call_tool("score_results", {
    "results": [...],
    "query": "Rust async programming"
})

# Render output
output = await mcp.call_tool("render_output", {
    "query": "Rust async",
    "mode": "technology_tracking",
    "results": [...],
    "scores": [...],
    "format": "markdown"
})
```

## MediaCrawler Integration

For social media research (Xiaohongshu, Weibo, Bilibili, Douyin, etc.), install MediaCrawler:

```bash
git clone https://github.com/NanmiCoder/MediaCrawler.git ~/MediaCrawler
cd ~/MediaCrawler
uv sync
uv run playwright install chromium
```

Then use the `crawl_social_media` tool:

```python
result = await mcp.call_tool("crawl_social_media", {
    "platform": "xhs",
    "keywords": "AI products",
    "max_notes": 20
})
```

## Dependencies

- `broad-information-research-core` >= 0.1.0
- `mcp` >= 1.0.0
- Python >= 3.10

## License

MIT