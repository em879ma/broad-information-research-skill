"""Scorer - Score credibility of information sources."""

from typing import Dict, Any, List
from dataclasses import dataclass
import re


@dataclass
class SourceScore:
    """Score for a source."""
    source_name: str
    credibility_score: float  # 0.0-1.0
    freshness_score: float     # 0.0-1.0
    relevance_score: float     # 0.0-1.0
    total_score: float         # 0.0-1.0
    reasons: List[str]


class Scorer:
    """Score information sources based on credibility, freshness, relevance."""
    
    # Credibility tiers
    CREDIBILITY_TIERS = {
        "high": 0.9,
        "medium": 0.6,
        "low": 0.3,
    }
    
    # Source type credibility modifiers
    SOURCE_TYPE_MODIFIERS = {
        "academic": 0.95,      # Academic sources are most credible
        "official": 0.9,        # Official sources are very credible
        "report": 0.85,         # Industry reports are credible
        "data": 0.85,           # Data sources are credible
        "review": 0.7,          # Reviews are moderately credible
        "news": 0.65,           # News is moderately credible
        "forum": 0.5,           # Forums are less credible
        "social": 0.4,           # Social media is least credible
        "general": 0.5,          # General web is less credible
    }
    
    def __init__(self):
        self.credibility_tiers = self.CREDIBILITY_TIERS
        self.source_type_modifiers = self.SOURCE_TYPE_MODIFIERS
    
    def score_source(self, result: Dict[str, Any], 
                     query: str, 
                     publication_date: str = None) -> SourceScore:
        """
        Score a single information source.
        
        Args:
            result: Result dictionary with 'title', 'url', 'content', 'source', etc.
            query: Original query for relevance calculation
            publication_date: Optional publication date string
            
        Returns:
            SourceScore object
        """
        source_name = result.get('source', 'Unknown')
        title = result.get('title', '')
        content = result.get('content', '')
        url = result.get('url', '')
        
        # Calculate credibility score
        credibility_score = self._calculate_credibility(source_name, url)
        
        # Calculate freshness score
        freshness_score = self._calculate_freshness(publication_date)
        
        # Calculate relevance score
        relevance_score = self._calculate_relevance(title, content, query)
        
        # Calculate total score (weighted average)
        total_score = (
            credibility_score * 0.4 +
            freshness_score * 0.3 +
            relevance_score * 0.3
        )
        
        # Generate reasons
        reasons = self._generate_reasons(
            source_name, url, title, content, 
            credibility_score, freshness_score, relevance_score
        )
        
        return SourceScore(
            source_name=source_name,
            credibility_score=credibility_score,
            freshness_score=freshness_score,
            relevance_score=relevance_score,
            total_score=total_score,
            reasons=reasons
        )
    
    def _calculate_credibility(self, source_name: str, url: str) -> float:
        """Calculate credibility score based on source name and URL."""
        # Check if source is in a known credibility tier
        source_lower = source_name.lower()
        
        # Academic sources
        if any(term in source_lower for term in ['scholar', 'pubmed', 'arxiv', 'ieee', 'acm']):
            return self.CREDIBILITY_TIERS['high']
        
        # Official sources
        if any(term in source_lower for term in ['official', 'gov', 'edu', 'org']):
            return self.CREDIBILITY_TIERS['high']
        
        # Review sites
        if any(term in source_lower for term in ['g2', 'capterra', 'trustpilot']):
            return self.CREDIBILITY_TIERS['medium']
        
        # News sites
        if any(term in source_lower for term in ['news', 'bbc', 'cnn', 'reuters']):
            return self.CREDIBILITY_TIERS['medium']
        
        # Social media
        if any(term in source_lower for term in ['weibo', 'xiaohongshu', 'douyin', 'bilibili']):
            return self.CREDIBILITY_TIERS['low']
        
        # Default: medium
        return self.CREDIBILITY_TIERS['medium']
    
    def _calculate_freshness(self, publication_date: str = None) -> float:
        """Calculate freshness score based on publication date."""
        if not publication_date:
            return 0.5  # Unknown date, neutral score
        
        # Simple heuristic: newer is better
        # In practice, would parse date and compare to current date
        try:
            # Assume format like "2024-01-01" or "2024"
            if isinstance(publication_date, str):
                if len(publication_date) >= 4:
                    year = int(publication_date[:4])
                    current_year = 2026  # Would use actual current year
                    age = current_year - year
                    
                    if age <= 1:
                        return 0.9
                    elif age <= 3:
                        return 0.7
                    elif age <= 5:
                        return 0.5
                    else:
                        return 0.3
        except (ValueError, IndexError):
            pass
        
        return 0.5  # Default neutral score
    
    def _calculate_relevance(self, title: str, content: str, query: str) -> float:
        """Calculate relevance score based on keyword matching."""
        if not query:
            return 0.5
        
        # Normalize
        query_lower = query.lower()
        title_lower = title.lower()
        content_lower = content.lower()
        
        # Extract keywords from query (simple split by space)
        keywords = set(query_lower.split())
        
        if not keywords:
            return 0.5
        
        # Count keyword matches in title and content
        title_matches = sum(1 for kw in keywords if kw in title_lower)
        content_matches = sum(1 for kw in keywords if kw in content_lower)
        
        # Weight title matches more heavily
        score = (title_matches * 2 + content_matches) / (len(keywords) * 3)
        
        return min(score, 1.0)
    
    def _generate_reasons(self, source_name: str, url: str, title: str, 
                         content: str, credibility: float, freshness: float, 
                         relevance: float) -> List[str]:
        """Generate human-readable reasons for the score."""
        reasons = []
        
        if credibility >= 0.8:
            reasons.append(f"高可信度来源: {source_name}")
        elif credibility >= 0.5:
            reasons.append(f"中等可信度来源: {source_name}")
        else:
            reasons.append(f"低可信度来源: {source_name}")
        
        if freshness >= 0.8:
            reasons.append("内容较新")
        elif freshness <= 0.3:
            reasons.append("内容较旧")
        
        if relevance >= 0.8:
            reasons.append("与查询高度相关")
        elif relevance >= 0.5:
            reasons.append("与查询相关")
        else:
            reasons.append("与查询相关性较低")
        
        return reasons
    
    def score_all(self, results: List[Dict[str, Any]], 
                  query: str) -> List[SourceScore]:
        """
        Score all results.
        
        Args:
            results: List of result dictionaries
            query: Original query
            
        Returns:
            List of SourceScore objects
        """
        scores = []
        for result in results:
            score = self.score_source(result, query)
            scores.append(score)
        
        return scores
    
    def filter_by_score(self, results: List[Dict[str, Any]], 
                       scores: List[SourceScore], 
                       min_score: float = 0.5) -> List[Dict[str, Any]]:
        """
        Filter results by minimum score.
        
        Args:
            results: List of result dictionaries
            scores: List of SourceScore objects
            min_score: Minimum total score to keep
            
        Returns:
            Filtered list of results
        """
        filtered = []
        for result, score in zip(results, scores):
            if score.total_score >= min_score:
                filtered.append(result)
        
        return filtered
