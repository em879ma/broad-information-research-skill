#!/usr/bin/env python3
"""
save_to_file.py - Auto-save research results to files with format options.

Supports:
- Markdown (.md)
- JSON (.json)
- CSV (.csv)
- Plain text (.txt)

Usage:
    python save_to_file.py --mode academic_research --topic "donor_obesity_kidney_transplant" --format md --content "..."

Or import as module:
    from save_to_file import save_research_report
    save_research_report(mode, topic, content, format='md')
"""

import argparse
import json
import csv
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Union
import re


def sanitize_filename(name: str) -> str:
    """Sanitize string for filename."""
    # Replace special chars with underscores
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[-\s]+', '_', name)
    return name.strip('_')


def get_timestamp() -> str:
    """Get current timestamp in YYYYMMDD_HHMMSS format."""
    return datetime.now().strftime('%Y%m%d_%H%M%S')


def save_markdown(content: str, filepath: str) -> str:
    """Save content as Markdown file."""
    filepath = str(filepath)
    if not filepath.endswith('.md'):
        filepath += '.md'
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filepath


def save_json(data: Dict, filepath: str, indent: int = 2) -> str:
    """Save data as JSON file."""
    filepath = str(filepath)
    if not filepath.endswith('.json'):
        filepath += '.json'
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)
    
    return filepath


def save_csv(data: List[Dict], filepath: str, fieldnames: Optional[List[str]] = None) -> str:
    """Save data as CSV file."""
    filepath = str(filepath)
    if not filepath.endswith('.csv'):
        filepath += '.csv'
    
    if not data:
        # Empty CSV
        Path(filepath).touch()
        return filepath
    
    # Determine fieldnames from first dict if not provided
    if fieldnames is None:
        fieldnames = list(data[0].keys())
    
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    return filepath


def save_txt(content: str, filepath: str) -> str:
    """Save content as plain text file."""
    filepath = str(filepath)
    if not filepath.endswith('.txt'):
        filepath += '.txt'
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filepath


def parse_academic_research_content(content: str) -> Dict[str, Any]:
    """
    Parse academic research content into structured data.
    
    Expected sections:
    - 文献检索 (Literature Search)
    - 检索结果 (Search Results)
    - 主要发现 (Key Findings)
    - 研究空白与建议 (Research Gaps & Recommendations)
    
    Returns:
        Dict with 'papers', 'findings', 'gaps', 'metadata'
    """
    result = {
        'papers': [],
        'findings': [],
        'gaps': [],
        'metadata': {}
    }
    
    # Simple parsing - look for lines starting with numbers or bullets
    lines = content.split('\n')
    current_section = None
    
    for line in lines:
        line = line.strip()
        
        # Detect section headers
        if any(kw in line for kw in ['文���检索', '检索结果', '主要发现', '研究空白']):
            if '检索结果' in line or '文献' in line:
                current_section = 'papers'
            elif '主要发现' in line:
                current_section = 'findings'
            elif '研究空白' in line:
                current_section = 'gaps'
            continue
        
        # Skip empty lines
        if not line or line.startswith('#'):
            continue
        
        # Parse bullet points
        if line.startswith(('- ', '• ', '* ', '1. ', '2. ', '3. ', '4. ', '5. ')):
            item = line.lstrip('- • *1234567890. ')
            
            if current_section == 'papers' and item:
                # Try to extract metadata
                paper = {'title': item}
                
                # Extract year if present
                year_match = re.search(r'\((\d{4})\)', item)
                if year_match:
                    paper['year'] = year_match.group(1)
                
                # Extract DOI if present
                doi_match = re.search(r'(doi:?\s*[\w./]+)', item, re.IGNORECASE)
                if doi_match:
                    paper['doi'] = doi_match.group(1)
                
                result['papers'].append(paper)
            
            elif current_section == 'findings' and item:
                result['findings'].append(item)
            
            elif current_section == 'gaps' and item:
                result['gaps'].append(item)
    
    return result


def parse_competitor_analysis_content(content: str) -> Dict[str, Any]:
    """
    Parse competitor analysis content.
    
    Returns:
        Dict with 'competitors', 'comparison', 'metadata'
    """
    result = {
        'competitors': [],
        'comparison': {},
        'metadata': {}
    }
    
    lines = content.split('\n')
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines and headers
        if not line or line.startswith('#'):
            continue
        
        # Parse bullet points
        if line.startswith(('- ', '• ', '* ')):
            item = line.lstrip('- • *')
            if item and ':' in item:
                # Key-value pair
                key, value = item.split(':', 1)
                result['comparison'][key.strip()] = value.strip()
    
    return result


def parse_event_collection_content(content: str) -> List[Dict[str, str]]:
    """
    Parse event collection content into list of events.
    
    Returns:
        List of event dicts
    """
    events = []
    lines = content.split('\n')
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines and headers
        if not line or line.startswith('#'):
            continue
        
        # Parse bullet points representing events
        if line.startswith(('- ', '• ', '* ')):
            item = line.lstrip('- • *')
            if item:
                event = {'name': item}
                
                # Extract date if present
                date_match = re.search(r'(\d{1,2}[/月]\d{1,2}[日]?)', item)
                if date_match:
                    event['date'] = date_match.group(1)
                
                # Extract location if present
                loc_match = re.search(r'[在@](\w+)', item)
                if loc_match:
                    event['location'] = loc_match.group(1)
                
                events.append(event)
    
    return events


def save_research_report(
    mode: str,
    topic: str,
    content: str,
    format: str = 'md',
    output_dir: str = './outputs'
) -> str:
    """
    Auto-save research report to file.
    
    Args:
        mode: Research mode (academic_research, competitor_analysis, etc.)
        topic: Research topic (sanitized for filename)
        content: Report content (Markdown string)
        format: Output format ('md', 'json', 'csv', 'txt')
        output_dir: Output directory
    
    Returns:
        Path to saved file
    """
    # Ensure output directory exists
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Generate filename
    sanitized_topic = sanitize_filename(topic)
    timestamp = get_timestamp()
    filename = f"{mode}_{sanitized_topic}_{timestamp}"
    
    # Full filepath
    filepath = output_path / filename
    
    # Save based on format
    if format == 'md':
        filepath = save_markdown(content, filepath)
    elif format == 'json':
        # Parse content into structured data
        if mode == 'academic_research':
            data = parse_academic_research_content(content)
        elif mode == 'competitor_analysis':
            data = parse_competitor_analysis_content(content)
        elif mode == 'event_collection':
            data = parse_event_collection_content(content)
        else:
            data = {'content': content, 'mode': mode, 'topic': topic}
        
        filepath = save_json(data, filepath)
    elif format == 'csv':
        # Parse content into rows
        if mode == 'academic_research':
            data = parse_academic_research_content(content).get('papers', [])
        elif mode == 'event_collection':
            data = parse_event_collection_content(content)
        else:
            data = [{'content': content}]
        
        filepath = save_csv(data, filepath)
    else:  # txt
        filepath = save_txt(content, filepath)
    
    return filepath


def main():
    parser = argparse.ArgumentParser(
        description='Save research report to file with format options.'
    )
    parser.add_argument('--mode', required=True, help='Research mode')
    parser.add_argument("--topic", required=True, help="Research topic")
    parser.add_argument("--content", required=True, help="Report content (as string)")
    parser.add_argument("--format", default="md", choices=["md", "json", "csv", "txt"],
                        help="Output format")
    parser.add_argument("--output-dir", default="./outputs", help="Output directory")
    
    args = parser.parse_args()
    
    filepath = save_research_report(
        mode=args.mode,
        topic=args.topic,
        content=args.content,
        format=args.format,
        output_dir=args.output_dir
    )
    
    print(f"Saved to: {filepath}")
    return filepath


if __name__ == '__main__':
    main()