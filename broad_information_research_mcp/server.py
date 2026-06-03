"""Broad Information Research MCP Server."""

import json
import asyncio
from typing import Any

from mcp.server.lowlevel.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, CallToolResult

from broad_information_research import (
    TaskClassifier,
    SourceSelector,
    QueryGenerator,
    Deduplicator,
    Scorer,
    OutputRenderer,
    MediaCrawlerClient,
)
from broad_information_research.output_renderer import ResearchResult


# Initialize MCP server
server = Server("broad-information-research")

# Initialize core components
classifier = TaskClassifier()
source_selector = SourceSelector()
query_generator = QueryGenerator()
deduplicator = Deduplicator()
scorer = Scorer()
renderer = OutputRenderer()
mediacrawler = MediaCrawlerClient()


# ─── Tool Definitions ────────────────────────────────────────────────────────

TOOLS: list[Tool] = [
    Tool(
        name="classify_research_task",
        description="Classify a research query into one of 7 research modes: academic_research, competitive_analysis, market_research, technology_tracking, event_monitoring, opinion_analysis, custom_research.",
        inputSchema={
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The user's research query or topic",
                }
            },
            "required": ["query"],
        },
    ),
    Tool(
        name="get_sources_for_task",
        description="Get recommended information sources for a specific research mode.",
        inputSchema={
            "type": "object",
            "properties": {
                "mode": {
                    "type": "string",
                    "description": "Research mode (e.g., 'academic_research', 'competitive_analysis', 'technology_tracking', 'market_research', 'event_monitoring', 'opinion_analysis', 'custom_research')",
                }
            },
            "required": ["mode"],
        },
    ),
    Tool(
        name="generate_search_queries",
        description="Generate optimized search queries for a topic and source type.",
        inputSchema={
            "type": "object",
            "properties": {
                "topic": {"type": "string", "description": "Research topic"},
                "source_type": {
                    "type": "string",
                    "description": "Source type: academic, general, news, social",
                    "default": "general",
                },
                "max_queries": {
                    "type": "integer",
                    "description": "Maximum number of queries to generate",
                    "default": 5,
                },
            },
            "required": ["topic"],
        },
    ),
    Tool(
        name="deduplicate_results",
        description="Remove duplicate results from a list of research results.",
        inputSchema={
            "type": "object",
            "properties": {
                "results": {
                    "type": "array",
                    "description": "List of result dictionaries with 'title', 'url', 'content' fields",
                },
                "similarity_threshold": {
                    "type": "number",
                    "description": "Threshold for considering duplicates (0.0-1.0)",
                    "default": 0.85,
                },
            },
            "required": ["results"],
        },
    ),
    Tool(
        name="score_results",
        description="Score research results by credibility, freshness, and relevance.",
        inputSchema={
            "type": "object",
            "properties": {
                "results": {
                    "type": "array",
                    "description": "List of result dictionaries with 'title', 'url', 'content', 'source' fields",
                },
                "query": {"type": "string", "description": "Original query for relevance scoring"},
            },
            "required": ["results", "query"],
        },
    ),
    Tool(
        name="render_output",
        description="Render research results in specified format (markdown, html, json, text).",
        inputSchema={
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Research query"},
                "mode": {"type": "string", "description": "Research mode"},
                "results": {"type": "array", "description": "List of result dictionaries"},
                "scores": {
                    "type": "array",
                    "description": "List of score objects from score_results tool",
                },
                "format": {
                    "type": "string",
                    "description": "Output format: markdown, html, json, text",
                    "default": "markdown",
                },
            },
            "required": ["query", "mode", "results", "scores"],
        },
    ),
    Tool(
        name="crawl_social_media",
        description="Crawl social media platforms (XiaoHongShu, Weibo, Bilibili, Douyin, etc.) using MediaCrawler. Returns normalized results.",
        inputSchema={
            "type": "object",
            "properties": {
                "platform": {
                    "type": "string",
                    "description": "Platform: xhs (小红书), weibo, bilibili, douyin, kuaishou, zhihu, baidu",
                },
                "keywords": {"type": "string", "description": "Search keywords"},
                "max_notes": {
                    "type": "integer",
                    "description": "Maximum number of posts to crawl",
                    "default": 20,
                },
            },
            "required": ["platform", "keywords"],
        },
    ),
    Tool(
        name="mediacrawler_status",
        description="Check if MediaCrawler is available and configured.",
        inputSchema={
            "type": "object",
            "properties": {},
        },
    ),
]


# ─── Handler Registration ───────────────────────────────────────────────────

@server.list_tools()
async def list_tools():
    """List all available MCP tools."""
    return TOOLS


@server.call_tool()
async def call_tool(tool_name: str, arguments: dict) -> dict | list[TextContent]:
    """Handle tool calls."""
    args = arguments or {}

    if tool_name == "classify_research_task":
        query = args["query"]
        mode, confidence = classifier.classify(query)
        return {
            "mode": mode,
            "mode_description": classifier.get_mode_description(mode),
            "confidence": round(confidence, 3),
            "available_modes": classifier.get_available_modes(),
        }

    elif tool_name == "get_sources_for_task":
        mode = args["mode"]
        sources = source_selector.get_sources_for_mode(mode)
        return {"mode": mode, "sources": sources, "count": len(sources)}

    elif tool_name == "generate_search_queries":
        topic = args["topic"]
        source_type = args.get("source_type", "general")
        max_queries = args.get("max_queries", 5)
        queries = query_generator.generate(topic, source_type, max_queries)
        return {"topic": topic, "source_type": source_type, "queries": queries}

    elif tool_name == "deduplicate_results":
        results = args["results"]
        threshold = args.get("similarity_threshold", 0.85)
        deduplicator.similarity_threshold = threshold
        deduped = deduplicator.deduplicate(results)
        return {
            "original_count": len(results),
            "deduplicated_count": len(deduped),
            "removed": len(results) - len(deduped),
            "results": deduped,
        }

    elif tool_name == "score_results":
        results = args["results"]
        query = args["query"]
        scores = scorer.score_all(results, query)
        return {
            "count": len(scores),
            "scores": [
                {
                    "source": s.source_name,
                    "credibility": round(s.credibility_score, 3),
                    "freshness": round(s.freshness_score, 3),
                    "relevance": round(s.relevance_score, 3),
                    "total": round(s.total_score, 3),
                    "reasons": s.reasons,
                }
                for s in scores
            ],
        }

    elif tool_name == "render_output":
        query = args["query"]
        mode = args["mode"]
        results = args["results"]
        scores_data = args["scores"]
        output_format = args.get("format", "markdown")

        # Reconstruct SourceScore objects
        from broad_information_research.scorer import SourceScore

        scores = [
            SourceScore(
                source_name=r.get("source", "Unknown"),
                credibility_score=s["credibility"],
                freshness_score=s["freshness"],
                relevance_score=s["relevance"],
                total_score=s["total"],
                reasons=s["reasons"],
            )
            for r, s in zip(results, scores_data)
        ]

        result_obj = ResearchResult(
            query=query, mode=mode, results=results, scores=scores, metadata={}
        )
        rendered = renderer.render(result_obj, output_format)
        return {"format": output_format, "output": rendered}

    elif tool_name == "crawl_social_media":
        platform = args["platform"]
        keywords = args["keywords"]
        max_notes = args.get("max_notes", 20)

        # Check availability first
        if not mediacrawler.is_available():
            return {
                "success": False,
                "error": "MediaCrawler not available. Please install: git clone https://github.com/NanmiCoder/MediaCrawler.git ~/MediaCrawler && cd ~/MediaCrawler && uv sync && uv run playwright install chromium",
                "hint": "Then set mediacrawler_path in MediaCrawlerClient to the MediaCrawler directory",
            }

        # Crawl
        result = mediacrawler.crawl_and_parse(platform, keywords, max_notes)

        if result["success"]:
            items = result.get("items", [])
            normalized = mediacrawler.normalize_to_standard_format(items, platform)
            return {
                "success": True,
                "platform": platform,
                "keywords": keywords,
                "total_found": result["count"],
                "preview_count": len(normalized[:10]),
                "results": normalized[:10],
            }
        else:
            return result

    elif tool_name == "mediacrawler_status":
        available = mediacrawler.is_available()
        data_file = None
        if available:
            # Check for recent data in common platforms
            for plat in ["xhs", "weibo", "bilibili"]:
                data_file = mediacrawler._find_latest_data(plat)
                if data_file:
                    break

        return {
            "available": available,
            "mediacrawler_path": mediacrawler.mediacrawler_path,
            "supported_platforms": mediacrawler.PLATFORMS,
            "latest_data_file": data_file,
        }

    else:
        return {"error": f"Unknown tool: {tool_name}"}


# ─── Main Entry Point ────────────────────────────────────────────────────────

async def main():
    """Main entry point."""
    async with stdio_server() as streams:
        await server.run(streams[0], streams[1], server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
