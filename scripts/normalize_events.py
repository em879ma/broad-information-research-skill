#!/usr/bin/env python3
"""
Normalize event fields to unified schema.
Usage: python normalize_events.py input.json output.json [--source-type TYPE]
"""

import json
import argparse
from datetime import datetime
import re

# Unified event schema
EVENT_SCHEMA = {
    "title": "",
    "type": "event",  # academic/news/event/company/market/competitor
    "event_type": "",  # Conference/Hackathon/Meetup/Seminar/Webinar
    "source_name": "",
    "source_url": "",
    "published_or_event_date": "",
    "event_start_date": "",
    "event_end_date": "",
    "city": "",
    "venue": "",
    "organizer": "",
    "registration_status": "unknown",  # open/closed/not_yet_open/unknown
    "registration_url": "",
    "registration_deadline": "",
    "registration_fee": "",
    "capacity": "",
    "speakers": [],
    "description": "",
    "summary": "",
    "evidence": "",
    "relevance_score": 0,
    "reliability_score": 0,
    "freshness_score": 0,
    "confidence": "low",  # high/medium/low
    "verified": False,
    "cross_verified": False,
    "notes": ""
}

def normalize_date(date_str):
    """Try to parse and normalize date to YYYY-MM-DD format."""
    if not date_str:
        return ""
    
    date_formats = [
        "%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%d/%m/%Y",
        "%B %d, %Y", "%b %d, %Y", "%d %B %Y", "%d %b %Y",
        "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%SZ"
    ]
    
    # Try parsing with known formats
    for fmt in date_formats:
        try:
            parsed = datetime.strptime(date_str.strip(), fmt)
            return parsed.strftime("%Y-%m-%d")
        except ValueError:
            continue
    
    # Try extracting YYYY-MM-DD pattern
    match = re.search(r'\d{4}-\d{2}-\d{2}', date_str)
    if match:
        return match.group(0)
    
    # Try extracting YYYY/MM/DD pattern
    match = re.search(r'\d{4}/\d{2}/\d{2}', date_str)
    if match:
        return match.group(0).replace("/", "-")
    
    return date_str  # Return as-is if can't parse

def normalize_city(city_str):
    """Normalize city name."""
    if not city_str:
        return ""
    
    city_lower = city_str.lower()
    
    # Common city name variations
    city_map = {
        "shanghai": "Shanghai",
        "beijing": "Beijing",
        "shenzhen": "Shenzhen",
        "guangzhou": "Guangzhou",
        "hangzhou": "Hangzhou",
        "sh": "Shanghai",
        "bj": "Beijing",
        "sz": "Shenzhen",
        "gz": "Guangzhou"
    }
    
    return city_map.get(city_lower, city_str.strip())

def normalize_event_type(type_str):
    """Normalize event type."""
    if not type_str:
        return "Unknown"
    
    type_lower = type_str.lower()
    
    if "hackathon" in type_lower:
        return "Hackathon"
    elif "conference" in type_lower or "conf" in type_lower:
        return "Conference"
    elif "summit" in type_lower:
        return "Summit"
    elif "meetup" in type_lower:
        return "Meetup"
    elif "seminar" in type_lower:
        return "Seminar"
    elif "webinar" in type_lower:
        return "Webinar"
    elif "workshop" in type_lower:
        return "Workshop"
    elif "training" in type_lower:
        return "Training"
    else:
        return type_str.strip()

def normalize_registration_status(status_str):
    """Normalize registration status."""
    if not status_str:
        return "unknown"
    
    status_lower = status_str.lower()
    
    if "open" in status_lower or "accepting" in status_lower:
        return "open"
    elif "close" in status_lower or "full" in status_lower:
        return "closed"
    elif "not yet" in status_lower or "coming soon" in status_lower:
        return "not_yet_open"
    else:
        return "unknown"

def extract_speakers(text):
    """Extract speaker names from text."""
    if not text:
        return []
    
    # Common patterns: "Speakers: Name1, Name2" or "Key Speakers: ..."
    speakers = []
    
    # Try to find "Speakers:" pattern
    match = re.search(r'Speakers?:\s*(.+?)(?:\n|$)', text, re.IGNORECASE)
    if match:
        speaker_str = match.group(1)
        # Split by comma or "and"
        names = re.split(r',\s*|\s+and\s+', speaker_str)
        speakers = [name.strip() for name in names if name.strip()]
    
    return speakers

def normalize_event(event_data, source_type="unknown"):
    """Normalize a single event to unified schema."""
    normalized = EVENT_SCHEMA.copy()
    
    # Map fields based on source type
    if source_type == "aitop100":
        normalized["title"] = event_data.get("activity_name", "")
        normalized["event_type"] = normalize_event_type(event_data.get("activity_type", ""))
        normalized["event_start_date"] = normalize_date(event_data.get("start_date", ""))
        normalized["event_end_date"] = normalize_date(event_data.get("end_date", ""))
        normalized["city"] = normalize_city(event_data.get("city", ""))
        normalized["venue"] = event_data.get("location", "")
        normalized["organizer"] = event_data.get("organizer", "")
        normalized["registration_status"] = normalize_registration_status(event_data.get("registration", ""))
        normalized["registration_url"] = event_data.get("registration_link", "")
        normalized["source_url"] = event_data.get("source_url", "")
        normalized["source_name"] = "aitop100.cn"
        normalized["reliability_score"] = 5  # S-Level source
        
    elif source_type == "luma":
        normalized["title"] = event_data.get("name", "")
        normalized["event_type"] = normalize_event_type(event_data.get("type", ""))
        normalized["event_start_date"] = normalize_date(event_data.get("start_at", ""))
        normalized["event_end_date"] = normalize_date(event_data.get("end_at", ""))
        normalized["city"] = normalize_city(event_data.get("location_city", ""))
        normalized["venue"] = event_data.get("location_address", "")
        normalized["organizer"] = event_data.get("host", "")
        normalized["registration_url"] = event_data.get("url", "")
        normalized["source_url"] = event_data.get("url", "")
        normalized["source_name"] = "Luma"
        normalized["reliability_score"] = 4  # A-Level source
        
    elif source_type == "huodongxing":
        normalized["title"] = event_data.get("title", "")
        normalized["event_type"] = normalize_event_type(event_data.get("category", ""))
        normalized["event_start_date"] = normalize_date(event_data.get("start_time", ""))
        normalized["event_end_date"] = normalize_date(event_data.get("end_time", ""))
        normalized["city"] = normalize_city(event_data.get("city", ""))
        normalized["venue"] = event_data.get("address", "")
        normalized["organizer"] = event_data.get("organizer", "")
        normalized["registration_status"] = normalize_registration_status(event_data.get("status", ""))
        normalized["registration_url"] = event_data.get("url", "")
        normalized["source_url"] = event_data.get("url", "")
        normalized["source_name"] = "Huodongxing"
        normalized["reliability_score"] = 3  # B-Level source
        
    else:  # Generic/unknown source
        normalized["title"] = event_data.get("title", "") or event_data.get("name", "")
        normalized["event_type"] = normalize_event_type(event_data.get("event_type", "") or event_data.get("type", ""))
        normalized["event_start_date"] = normalize_date(event_data.get("start_date", "") or event_data.get("date", ""))
        normalized["event_end_date"] = normalize_date(event_data.get("end_date", ""))
        normalized["city"] = normalize_city(event_data.get("city", "") or event_data.get("location", ""))
        normalized["venue"] = event_data.get("venue", "") or event_data.get("address", "")
        normalized["organizer"] = event_data.get("organizer", "") or event_data.get("host", "")
        normalized["registration_url"] = event_data.get("registration_url", "") or event_data.get("url", "")
        normalized["source_url"] = event_data.get("source_url", "") or event_data.get("url", "")
        normalized["source_name"] = event_data.get("source_name", "unknown")
        normalized["reliability_score"] = 3  # Default to medium reliability
    
    # Common processing
    normalized["type"] = "event"
    normalized["published_or_event_date"] = normalized["event_start_date"]
    normalized["description"] = event_data.get("description", "") or event_data.get("summary", "")
    normalized["summary"] = normalized["description"][:500]  # Truncate to 500 chars
    normalized["speakers"] = extract_speakers(normalized["description"])
    
    # Determine confidence based on reliability and verification
    reliability = normalized["reliability_score"]
    if reliability >= 4 and normalized["verified"]:
        normalized["confidence"] = "high"
    elif reliability >= 3:
        normalized["confidence"] = "medium"
    else:
        normalized["confidence"] = "low"
    
    # Copy notes if present
    normalized["notes"] = event_data.get("notes", "")
    
    return normalized

def main():
    parser = argparse.ArgumentParser(description="Normalize event fields to unified schema.")
    parser.add_argument("input", help="Input JSON file (list of events)")
    parser.add_argument("output", help="Output JSON file (normalized events)")
    parser.add_argument("--source-type", 
                        choices=["aitop100", "luma", "huodongxing", "generic"],
                        default="generic",
                        help="Source type for field mapping")
    
    args = parser.parse_args()
    
    # Read input
    with open(args.input, "r", encoding="utf-8") as f:
        events = json.load(f)
    
    print(f"Loaded {len(events)} events from {args.input}")
    print(f"Source type: {args.source_type}")
    
    # Normalize each event
    normalized_events = []
    for event in events:
        normalized = normalize_event(event, args.source_type)
        normalized_events.append(normalized)
    
    print(f"Normalized {len(normalized_events)} events")
    
    # Write output
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(normalized_events, f, indent=2, ensure_ascii=False)
    
    print(f"Saved to {args.output}")
    
    # Summary
    high = sum(1 for e in normalized_events if e["confidence"] == "high")
    medium = sum(1 for e in normalized_events if e["confidence"] == "medium")
    low = sum(1 for e in normalized_events if e["confidence"] == "low")
    
    print(f"\nConfidence distribution:")
    print(f"  High: {high}")
    print(f"  Medium: {medium}")
    print(f"  Low: {low}")

if __name__ == "__main__":
    main()
