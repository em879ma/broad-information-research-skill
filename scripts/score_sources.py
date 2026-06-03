#!/usr/bin/env python3
"""
Score results by reliability, relevance, and freshness.
Usage: python score_sources.py input.json output.json [--user-time-range DAYS]
"""

import json
import argparse
from datetime import datetime, timedelta
import re

def calculate_reliability_score(source_url, source_name):
    """Calculate reliability score (1-5) based on source."""
    
    # S-Level sources (5)
    s_level_domains = [
        "gov", "gov.cn", "who.int", "nih.gov", "nature.com", 
        "science.org", "nejm.org", "jama.jamanetwork.com",
        "ieee.org", "acm.org", "springer.com", "elsevier.com"
    ]
    
    # A-Level sources (4)
    a_level_domains = [
        "reuters.com", "ap.org", "bloomberg.com", "ft.com",
        "techcrunch.com", "theverge.com", "36kr.com", "caixin.com",
        "scholar.google.com", "pubmed.ncbi.nlm.nih.gov", "arxiv.org",
        "crunchbase.com", "pitchbook.com", "gartner.com", "cbinsights.com"
    ]
    
    # Check URL or source name
    url_to_check = source_url.lower() if source_url else ""
    name_to_check = source_name.lower() if source_name else ""
    
    # Check S-Level (5)
    for domain in s_level_domains:
        if domain in url_to_check or domain in name_to_check:
            return 5
    
    # Check A-Level (4)
    for domain in a_level_domains:
        if domain in url_to_check or domain in name_to_check:
            return 4
    
    # B-Level sources (3) - professional blogs, conference pages
    b_level_patterns = [
        "blog", "medium.com", "github.io", "wordpress.com",
        "conference", "summit", "event"
    ]
    for pattern in b_level_patterns:
        if pattern in url_to_check or pattern in name_to_check:
            return 3
    
    # Check if it's a company official website (5)
    if source_url and ("official" in source_name.lower() or 
                      "官网" in source_name or 
                      "announcement" in source_name.lower()):
        return 5
    
    # Default scores based on URL patterns
    if not source_url or not source_name:
        return 1  # Unsourced claim
    
    # Check for user-generated content (2)
    user_generated_patterns = [
        "twitter.com", "x.com", "reddit.com", "zhihu.com", 
        "xiaohongshu.com", "weibo.com"
    ]
    for pattern in user_generated_patterns:
        if pattern in url_to_check:
            return 2
    
    # Default: 3 (medium reliability)
    return 3

def calculate_relevance_score(item, user_query):
    """Calculate relevance score (1-5) based on user query."""
    title = item.get("title", "").lower()
    summary = item.get("summary", "").lower()
    query_lower = user_query.lower()
    
    # Extract keywords from query
    query_keywords = set(re.findall(r'\w+', query_lower))
    
    # Count matches in title and summary
    title_matches = sum(1 for kw in query_keywords if kw in title)
    summary_matches = sum(1 for kw in query_keywords if kw in summary)
    
    # Calculate score
    total_keywords = len(query_keywords)
    if total_keywords == 0:
        return 3  # No query, neutral score
    
    match_ratio = (title_matches * 2 + summary_matches) / (total_keywords * 3)  # Title matches weighted more
    
    if match_ratio >= 0.8:
        return 5  # Directly answers the question
    elif match_ratio >= 0.6:
        return 4  # Strongly related
    elif match_ratio >= 0.4:
        return 3  # Useful context
    elif match_ratio >= 0.2:
        return 2  # Weakly related
    else:
        return 1  # Irrelevant

def calculate_freshness_score(published_date, user_time_range_days=30):
    """Calculate freshness score (1-5) based on date."""
    if not published_date:
        return 3  # Unknown date, neutral score
    
    try:
        # Try to parse date (support multiple formats)
        date_formats = [
            "%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%d/%m/%Y",
            "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%SZ"
        ]
        
        parsed_date = None
        for fmt in date_formats:
            try:
                parsed_date = datetime.strptime(published_date, fmt)
                break
            except ValueError:
                continue
        
        if not parsed_date:
            return 3  # Can't parse date
        
        # Calculate days since publication
        now = datetime.now()
        days_since = (now - parsed_date).days
        
        if days_since <= user_time_range_days:
            return 5  # Within user-specified time range
        elif days_since <= user_time_range_days * 2:
            return 4  # Recent and still valid
        elif days_since <= 365:
            return 3  # Somewhat old but useful
        elif days_since <= 730:
            return 2  # Outdated for current decisions
        else:
            return 1  # Stale or superseded
    
    except Exception:
        return 3  # Error parsing, neutral score

def calculate_confidence_label(reliability, relevance, freshness, cross_verified=False):
    """Calculate confidence label (High/Medium/Low)."""
    
    # High confidence: reliable + relevant + fresh + (cross-verified or reliability=5)
    if (reliability >= 4 and relevance >= 4 and freshness >= 4 and 
        (cross_verified or reliability == 5)):
        return "High"
    
    # Medium confidence: mostly reliable but incomplete/old/one strong source
    if ((reliability >= 3 and relevance >= 3 and freshness >= 3) or 
        (reliability >= 4 and relevance >= 3) or 
        (reliability >= 3 and relevance >= 4)):
        return "Medium"
    
    # Low confidence: weak source/conflict/unclear date/limited evidence
    return "Low"

def score_results(results, user_query="", user_time_range_days=30):
    """Score all results and add scores to each item."""
    scored = []
    
    for item in results:
        # Calculate scores
        reliability = calculate_reliability_score(
            item.get("source_url", ""),
            item.get("source_name", "")
        )
        
        relevance = calculate_relevance_score(item, user_query)
        
        freshness = calculate_freshness_score(
            item.get("published_or_event_date", ""),
            user_time_range_days
        )
        
        # Determine confidence
        # Check if cross-verified (this would need external logic)
        cross_verified = item.get("cross_verified", False)
        confidence = calculate_confidence_label(reliability, relevance, freshness, cross_verified)
        
        # Add scores to item
        item["reliability_score"] = reliability
        item["relevance_score"] = relevance
        item["freshness_score"] = freshness
        item["confidence"] = confidence
        
        scored.append(item)
    
    return scored

def main():
    parser = argparse.ArgumentParser(description="Score search results by reliability, relevance, and freshness.")
    parser.add_argument("input", help="Input JSON file")
    parser.add_argument("output", help="Output JSON file")
    parser.add_argument("--user-query", default="", help="User's original query (for relevance scoring)")
    parser.add_argument("--user-time-range", type=int, default=30, 
                        help="User's time range in days (for freshness scoring)")
    
    args = parser.parse_args()
    
    # Read input
    with open(args.input, "r", encoding="utf-8") as f:
        results = json.load(f)
    
    print(f"Loaded {len(results)} results from {args.input}")
    
    # Score results
    scored = score_results(results, args.user_query, args.user_time_range)
    
    # Summary
    high = sum(1 for r in scored if r["confidence"] == "High")
    medium = sum(1 for r in scored if r["confidence"] == "Medium")
    low = sum(1 for r in scored if r["confidence"] == "Low")
    
    print(f"Scoring results:")
    print(f"  High confidence: {high}")
    print(f"  Medium confidence: {medium}")
    print(f"  Low confidence: {low}")
    
    # Write output
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(scored, f, indent=2, ensure_ascii=False)
    
    print(f"Saved to {args.output}")

if __name__ == "__main__":
    main()
