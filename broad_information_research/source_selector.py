"""Source Selector - Select information sources based on research mode."""

from typing import Dict, List, Any


class SourceSelector:
    """Select appropriate information sources based on task type."""
    
    # Source registry: mode -> list of sources
    SOURCE_REGISTRY = {
        "academic_research": [
            {
                "name": "Google Scholar",
                "type": "academic",
                "url": "https://scholar.google.com",
                "reliability": "high",
                "access_method": "web_search",
            },
            {
                "name": "PubMed",
                "type": "academic",
                "url": "https://pubmed.ncbi.nlm.nih.gov",
                "reliability": "high",
                "access_method": "web_search",
            },
            {
                "name": "arXiv",
                "type": "academic",
                "url": "https://arxiv.org",
                "reliability": "high",
                "access_method": "web_search",
            },
        ],
        "competitive_analysis": [
            {
                "name": "Company Websites",
                "type": "official",
                "url": "",
                "reliability": "high",
                "access_method": "web_search",
            },
            {
                "name": "Product Hunt",
                "type": "review",
                "url": "https://www.producthunt.com",
                "reliability": "medium",
                "access_method": "web_search",
            },
            {
                "name": "G2",
                "type": "review",
                "url": "https://www.g2.com",
                "reliability": "medium",
                "access_method": "web_search",
            },
        ],
        "market_research": [
            {
                "name": "Industry Reports",
                "type": "report",
                "url": "",
                "reliability": "high",
                "access_method": "web_search",
            },
            {
                "name": "Statista",
                "type": "data",
                "url": "https://www.statista.com",
                "reliability": "high",
                "access_method": "web_search",
            },
            {
                "name": "Government Statistics",
                "type": "official",
                "url": "",
                "reliability": "high",
                "access_method": "web_search",
            },
        ],
        "technology_tracking": [
            {
                "name": "GitHub",
                "type": "code",
                "url": "https://github.com",
                "reliability": "high",
                "access_method": "web_search",
            },
            {
                "name": "Stack Overflow",
                "type": "forum",
                "url": "https://stackoverflow.com",
                "reliability": "medium",
                "access_method": "web_search",
            },
            {
                "name": "Official Documentation",
                "type": "official",
                "url": "",
                "reliability": "high",
                "access_method": "web_search",
            },
        ],
        "event_monitoring": [
            {
                "name": "News APIs",
                "type": "news",
                "url": "",
                "reliability": "medium",
                "access_method": "web_search",
            },
            {
                "name": "Social Media",
                "type": "social",
                "url": "",
                "reliability": "low",
                "access_method": "mediacrawler",
            },
        ],
        "opinion_analysis": [
            {
                "name": "Social Media (XiaoHongShu)",
                "type": "social",
                "url": "",
                "reliability": "medium",
                "access_method": "mediacrawler",
            },
            {
                "name": "Social Media (Weibo)",
                "type": "social",
                "url": "",
                "reliability": "medium",
                "access_method": "mediacrawler",
            },
            {
                "name": "Social Media (Douyin)",
                "type": "social",
                "url": "",
                "reliability": "medium",
                "access_method": "mediacrawler",
            },
        ],
        "custom_research": [
            {
                "name": "Web Search",
                "type": "general",
                "url": "",
                "reliability": "medium",
                "access_method": "web_search",
            },
        ],
    }
    
    def __init__(self):
        self.registry = self.SOURCE_REGISTRY
        
    def get_sources_for_mode(self, mode: str) -> List[Dict[str, Any]]:
        """
        Get list of information sources for a research mode.
        
        Args:
            mode: Research mode (e.g., "academic_research")
            
        Returns:
            List of source dictionaries
        """
        return self.registry.get(mode, self.registry["custom_research"])
    
    def get_source_by_name(self, name: str) -> Dict[str, Any]:
        """
        Get a specific source by name.
        
        Args:
            name: Source name
            
        Returns:
            Source dictionary or empty dict if not found
        """
        for mode, sources in self.registry.items():
            for source in sources:
                if source["name"] == name:
                    return source
        return {}
    
    def add_custom_source(self, mode: str, source: Dict[str, Any]) -> None:
        """
        Add a custom source to a mode.
        
        Args:
            mode: Research mode
            source: Source dictionary
        """
        if mode not in self.registry:
            self.registry[mode] = []
        self.registry[mode].append(source)
    
    def get_all_modes(self) -> List[str]:
        """Get all available modes."""
        return list(self.registry.keys())
