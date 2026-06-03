#!/usr/bin/env python3
"""
Deduplicate results by title, URL, date, or entity name.
Usage: python dedupe_results.py input.json output.json [--threshold 0.8]
"""

import json
import argparse
from difflib import SequenceMatcher

def similarity(a, b):
    """Calculate string similarity ratio."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def dedupe_by_title(results, threshold=0.8):
    """Deduplicate by title similarity."""
    seen = []
    unique = []
    
    for item in results:
        title = item.get("title", "")
        is_duplicate = False
        
        for seen_item in seen:
            seen_title = seen_item.get("title", "")
            if similarity(title, seen_title) >= threshold:
                is_duplicate = True
                # Keep the one with higher reliability score
                if item.get("reliability_score", 0) > seen_item.get("reliability_score", 0):
                    seen[seen.index(seen_item)] = item
                break
        
        if not is_duplicate:
            seen.append(item)
            unique.append(item)
    
    return unique

def dedupe_by_url(results):
    """Deduplicate by URL (exact match)."""
    seen_urls = set()
    unique = []
    
    for item in results:
        url = item.get("source_url", "")
        if url and url not in seen_urls:
            seen_urls.add(url)
            unique.append(item)
        elif not url:
            unique.append(item)  # Keep items without URL
    
    return unique

def dedupe_by_date_and_title(results, date_threshold_days=1):
    """Deduplicate by date and title similarity."""
    seen = []
    unique = []
    
    for item in results:
        title = item.get("title", "")
        date = item.get("published_or_event_date", "")
        
        is_duplicate = False
        for seen_item in seen:
            seen_title = seen_item.get("title", "")
            seen_date = seen_item.get("published_or_event_date", "")
            
            # Check title similarity
            if similarity(title, seen_title) >= 0.7:
                # Check date proximity (if both have dates)
                if date and seen_date and date == seen_date:
                    is_duplicate = True
                    # Keep the one with higher reliability
                    if item.get("reliability_score", 0) > seen_item.get("reliability_score", 0):
                        seen[seen.index(seen_item)] = item
                    break
        
        if not is_duplicate:
            seen.append(item)
            unique.append(item)
    
    return unique

def dedupe_by_entity(results, entity_field="entity_name"):
    """Deduplicate by entity name (for company/organization intelligence)."""
    seen_entities = {}
    unique = []
    
    for item in results:
        entity = item.get(entity_field, "")
        if entity:
            if entity in seen_entities:
                # Keep the more recent or higher reliability one
                seen_item = seen_entities[entity]
                if item.get("reliability_score", 0) > seen_item.get("reliability_score", 0):
                    seen_entities[entity] = item
                    # Replace in unique list
                    idx = next(i for i, x in enumerate(unique) if x.get(entity_field, "") == entity)
                    unique[idx] = item
            else:
                seen_entities[entity] = item
                unique.append(item)
        else:
            unique.append(item)  # Keep items without entity name
    
    return unique

def main():
    parser = argparse.ArgumentParser(description="Deduplicate search results.")
    parser.add_argument("input", help="Input JSON file")
    parser.add_argument("output", help="Output JSON file")
    parser.add_argument("--threshold", type=float, default=0.8, help="Title similarity threshold (0.0-1.0)")
    parser.add_argument("--method", choices=["title", "url", "date_title", "entity"], 
                        default="title", help="Deduplication method")
    
    args = parser.parse_args()
    
    # Read input
    with open(args.input, "r", encoding="utf-8") as f:
        results = json.load(f)
    
    print(f"Loaded {len(results)} results from {args.input}")
    
    # Deduplicate
    if args.method == "title":
        unique = dedupe_by_title(results, args.threshold)
    elif args.method == "url":
        unique = dedupe_by_url(results)
    elif args.method == "date_title":
        unique = dedupe_by_date_and_title(results)
    elif args.method == "entity":
        unique = dedupe_by_entity(results)
    else:
        unique = dedupe_by_title(results, args.threshold)
    
    print(f"After deduplication: {len(unique)} unique results")
    print(f"Removed {len(results) - len(unique)} duplicates")
    
    # Write output
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(unique, f, indent=2, ensure_ascii=False)
    
    print(f"Saved to {args.output}")

if __name__ == "__main__":
    main()
