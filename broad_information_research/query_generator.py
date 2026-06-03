"""Query Generator - Generate search queries based on research topic."""

from typing import List, Dict, Any
import re


class QueryGenerator:
    """Generate optimized search queries for different sources."""
    
    def __init__(self):
        self.query_templates = {
            "academic": [
                '"{topic}"',
                '"{topic}" review',
                '"{topic}" meta-analysis',
                '"{topic}" systematic review',
            ],
            "general": [
                '{topic}',
                '{topic} guide',
                '{topic} tutorial',
                '{topic} examples',
            ],
            "news": [
                '{topic} news',
                '{topic} latest',
                '{topic} update',
                '{topic} 2024',
            ],
            "social": [
                '{topic}',
                '{topic} 推荐',
                '{topic} 分享',
                '{topic} 体验',
            ],
        }
    
    def generate(self, topic: str, source_type: str, max_queries: int = 5) -> List[str]:
        """
        Generate search queries for a topic and source type.
        
        Args:
            topic: Research topic
            source_type: Type of source (academic, general, news, social)
            max_queries: Maximum number of queries to generate
            
        Returns:
            List of search queries
        """
        templates = self.query_templates.get(source_type, self.query_templates["general"])
        
        queries = []
        for template in templates:
            query = template.format(topic=topic)
            queries.append(query)
            
            if len(queries) >= max_queries:
                break
        
        return queries
    
    def generate_for_sources(self, topic: str, sources: List[Dict[str, Any]]) -> Dict[str, List[str]]:
        """
        Generate queries for multiple sources.
        
        Args:
            topic: Research topic
            sources: List of source dictionaries
            
        Returns:
            Dictionary mapping source names to query lists
        """
        result = {}
        for source in sources:
            source_name = source["name"]
            source_type = source["type"]
            
            # Map source type to query type
            query_type_map = {
                "academic": "academic",
                "official": "general",
                "review": "general",
                "report": "general",
                "data": "general",
                "code": "general",
                "forum": "general",
                "news": "news",
                "social": "social",
                "general": "general",
            }
            
            query_type = query_type_map.get(source_type, "general")
            queries = self.generate(topic, query_type)
            result[source_name] = queries
        
        return result
    
    def optimize_query(self, query: str, source: Dict[str, Any]) -> str:
        """
        Optimize a query for a specific source.
        
        Args:
            query: Original query
            source: Source dictionary
            
        Returns:
            Optimized query
        """
        source_name = source["name"].lower()
        
        # Google Scholar optimizations
        if "scholar" in source_name:
            # Remove quotes, add filetype:pdf for papers
            query = query.replace('"', '')
            query += ' filetype:pdf'
            
        # PubMed optimizations
        elif "pubmed" in source_name:
            pass  # Keep as is, PubMed handles natural language
            
        # General web search optimizations
        elif "google" in source_name or "bing" in source_name:
            # Add quotes for exact phrases
            if ' ' in query and '"' not in query:
                query = f'"{query}"'
        
        return query
    
    def expand_query(self, query: str, max_variants: int = 3) -> List[str]:
        """
        Expand a query into variants.
        
        Args:
            query: Original query
            max_variants: Maximum number of variants
            
        Returns:
            List of query variants
        """
        variants = [query]
        
        # Add "what is" variant
        if not query.lower().startswith("what"):
            variants.append(f"what is {query}")
        
        # Add "how to" variant
        if not query.lower().startswith("how"):
            variants.append(f"how to {query}")
        
        # Add "best" variant
        if "best" not in query.lower():
            variants.append(f"best {query}")
        
        return variants[:max_variants]
