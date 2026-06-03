"""MediaCrawler Client - Interface to MediaCrawler for social media crawling."""

import subprocess
import json
import os
from typing import Dict, List, Any, Optional
from pathlib import Path


class MediaCrawlerClient:
    """Client for MediaCrawler CLI."""
    
    # Supported platforms
    PLATFORMS = ["xhs", "weibo", "douyin", "bilibili", "tiktok", "kuaishou", "zhihu", "baidu"]
    
    def __init__(self, mediacrawler_path: str = None):
        """
        Initialize MediaCrawler client.
        
        Args:
            mediacrawler_path: Path to MediaCrawler directory.
                             If None, assumes it's in PATH or current directory.
        """
        self.mediacrawler_path = mediacrawler_path or self._find_mediacrawler()
        self.data_dir = None  # Will be set after running crawler
        
    def _find_mediacrawler(self) -> Optional[str]:
        """Find MediaCrawler installation."""
        # Check common locations
        possible_paths = [
            os.path.expanduser("~/MediaCrawler"),
            os.path.expanduser("~/mediacrawler"),
            "./MediaCrawler",
            "./mediacrawler",
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                return path
        
        return None
    
    def is_available(self) -> bool:
        """Check if MediaCrawler is available."""
        if not self.mediacrawler_path:
            return False
        
        # Check if uv is available
        try:
            subprocess.run(["uv", "--version"], capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def crawl(self, 
              platform: str, 
              keywords: str, 
              max_notes: int = 20,
              lt: str = "qrcode") -> Dict[str, Any]:
        """
        Crawl a platform for keywords.
        
        Args:
            platform: Platform name (xhs, weibo, douyin, etc.)
            keywords: Search keywords
            max_notes: Maximum number of notes/posts to crawl
            lt: Login type (qrcode, phone, etc.)
            
        Returns:
            Dictionary with 'success', 'data_file', 'error' keys
        """
        if platform not in self.PLATFORMS:
            return {
                "success": False,
                "error": f"Unsupported platform: {platform}. Supported: {', '.join(self.PLATFORMS)}"
            }
        
        if not self.mediacrawler_path:
            return {
                "success": False,
                "error": "MediaCrawler not found. Please install it first."
            }
        
        # Build command
        cmd = [
            "uv", "run", "python", "main.py",
            "--platform", platform,
            "--lt", lt,
            "--type", "search",
            "--keywords", keywords,
            "--crawler_max_notes_count", str(max_notes)
        ]
        
        try:
            # Run MediaCrawler
            result = subprocess.run(
                cmd,
                cwd=self.mediacrawler_path,
                capture_output=True,
                text=True,
                timeout=300  # 5 minutes timeout
            )
            
            if result.returncode != 0:
                return {
                    "success": False,
                    "error": result.stderr or "Unknown error",
                    "stdout": result.stdout
                }
            
            # Find data file
            data_file = self._find_latest_data(platform)
            
            return {
                "success": True,
                "data_file": data_file,
                "stdout": result.stdout,
                "stderr": result.stderr
            }
            
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "error": "Crawling timeout (5 minutes)"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def _find_latest_data(self, platform: str) -> Optional[str]:
        """Find the latest crawled data file."""
        if not self.mediacrawler_path:
            return None
        
        # Look for JSONL files in data directory
        data_dir = os.path.join(self.mediacrawler_path, "data", platform, "jsonl")
        
        if not os.path.exists(data_dir):
            return None
        
        # Find the latest file
        files = list(Path(data_dir).glob("*.jsonl"))
        if not files:
            return None
        
        latest_file = max(files, key=os.path.getmtime)
        return str(latest_file)
    
    def parse_data(self, data_file: str) -> List[Dict[str, Any]]:
        """
        Parse crawled data from JSONL file.
        
        Args:
            data_file: Path to JSONL file
            
        Returns:
            List of parsed items
        """
        items = []
        
        try:
            with open(data_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        try:
                            item = json.loads(line)
                            items.append(item)
                        except json.JSONDecodeError:
                            continue
        except Exception as e:
            print(f"Error parsing {data_file}: {e}")
        
        return items
    
    def crawl_and_parse(self, 
                       platform: str, 
                       keywords: str, 
                       max_notes: int = 20) -> Dict[str, Any]:
        """
        Crawl and parse in one step.
        
        Args:
            platform: Platform name
            keywords: Search keywords
            max_notes: Maximum number of notes/posts
            
        Returns:
            Dictionary with 'success', 'items', 'error' keys
        """
        # Crawl
        result = self.crawl(platform, keywords, max_notes)
        
        if not result['success']:
            return result
        
        # Parse
        data_file = result.get('data_file')
        if not data_file:
            return {
                "success": False,
                "error": "No data file found"
            }
        
        items = self.parse_data(data_file)
        
        return {
            "success": True,
            "items": items,
            "data_file": data_file,
            "count": len(items)
        }
    
    def normalize_to_standard_format(self, items: List[Dict[str, Any]], 
                                    platform: str) -> List[Dict[str, Any]]:
        """
        Normalize crawled items to standard format.
        
        Args:
            items: Raw items from MediaCrawler
            platform: Platform name
            
        Returns:
            List of normalized items with 'title', 'content', 'url', 'source', etc.
        """
        normalized = []
        
        for item in items:
            # Extract common fields (platform-specific)
            if platform == "xhs":
                normalized_item = {
                    "title": item.get("note_title", ""),
                    "content": item.get("note_desc", ""),
                    "url": item.get("note_url", ""),
                    "source": "XiaoHongShu",
                    "platform": platform,
                    "author": item.get("nickname", ""),
                    "publish_time": item.get("create_time", ""),
                    "stats": {
                        "likes": item.get("liked_count", 0),
                        "comments": item.get("comment_count", 0),
                        "shares": item.get("share_count", 0),
                    },
                    "raw": item
                }
            elif platform == "weibo":
                normalized_item = {
                    "title": item.get("note_title", "") or item.get("content", "")[:50],
                    "content": item.get("content", "") or item.get("note_desc", ""),
                    "url": item.get("note_url", "") or item.get("url", ""),
                    "source": "Weibo",
                    "platform": platform,
                    "author": item.get("nickname", ""),
                    "publish_time": item.get("create_time", ""),
                    "stats": {
                        "likes": item.get("attitudes_count", 0),
                        "comments": item.get("comments_count", 0),
                        "shares": item.get("reposts_count", 0),
                    },
                    "raw": item
                }
            else:
                # Generic normalization
                normalized_item = {
                    "title": item.get("title", "") or item.get("note_title", ""),
                    "content": item.get("content", "") or item.get("note_desc", ""),
                    "url": item.get("url", "") or item.get("note_url", ""),
                    "source": platform,
                    "platform": platform,
                    "author": item.get("author", "") or item.get("nickname", ""),
                    "publish_time": item.get("create_time", "") or item.get("publish_time", ""),
                    "stats": {},
                    "raw": item
                }
            
            normalized.append(normalized_item)
        
        return normalized
