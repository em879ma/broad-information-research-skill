"""Deduplicator - Remove duplicate results from multiple sources."""

from typing import List, Dict, Any, Set
import hashlib
import re


class Deduplicator:
    """Remove duplicate results based on content similarity."""
    
    def __init__(self, similarity_threshold: float = 0.85):
        """
        Initialize deduplicator.
        
        Args:
            similarity_threshold: Threshold for considering results as duplicates (0.0-1.0)
        """
        self.similarity_threshold = similarity_threshold
    
    def deduplicate(self, results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Remove duplicates from results list.
        
        Args:
            results: List of result dictionaries (each should have 'title', 'url', 'content' fields)
            
        Returns:
            Deduplicated list of results
        """
        if not results:
            return []
        
        unique_results = []
        seen_titles: Set[str] = set()
        seen_urls: Set[str] = set()
        seen_content_hashes: Set[str] = set()
        
        for result in results:
            title = result.get('title', '').strip().lower()
            url = result.get('url', '').strip().lower()
            content = result.get('content', '').strip()
            
            # Check for duplicates
            if self._is_duplicate(title, url, content, seen_titles, seen_urls, seen_content_hashes):
                continue
            
            # Add to seen sets
            if title:
                seen_titles.add(title)
            if url:
                seen_urls.add(url)
            if content:
                content_hash = self._hash_content(content)
                seen_content_hashes.add(content_hash)
            
            unique_results.append(result)
        
        return unique_results
    
    def _is_duplicate(self, title: str, url: str, content: str,
                     seen_titles: Set[str], seen_urls: Set[str], 
                     seen_content_hashes: Set[str]) -> bool:
        """Check if a result is a duplicate."""
        
        # Check URL exact match
        if url and url in seen_urls:
            return True
        
        # Check title exact match
        if title and title in seen_titles:
            return True
        
        # Check content hash
        if content:
            content_hash = self._hash_content(content)
            if content_hash in seen_content_hashes:
                return True
        
        # Check title similarity
        if title:
            for seen_title in seen_titles:
                if self._calculate_similarity(title, seen_title) >= self.similarity_threshold:
                    return True
        
        return False
    
    def _hash_content(self, content: str) -> str:
        """Generate hash for content."""
        # Normalize content: remove whitespace, convert to lowercase
        normalized = re.sub(r'\s+', ' ', content.lower()).strip()
        return hashlib.md5(normalized.encode('utf-8')).hexdigest()
    
    def _calculate_similarity(self, str1: str, str2: str) -> float:
        """
        Calculate similarity between two strings using Jaccard similarity.
        
        Returns:
            Similarity score (0.0-1.0)
        """
        # Tokenize
        tokens1 = set(str1.split())
        tokens2 = set(str2.split())
        
        if not tokens1 or not tokens2:
            return 0.0
        
        # Jaccard similarity
        intersection = tokens1 & tokens2
        union = tokens1 | tokens2
        
        if not union:
            return 0.0
        
        return len(intersection) / len(union)
    
    def deduplicate_by_field(self, results: List[Dict[str, Any]], 
                           field: str) -> List[Dict[str, Any]]:
        """
        Deduplicate results by a specific field.
        
        Args:
            results: List of result dictionaries
            field: Field name to check for duplicates
            
        Returns:
            Deduplicated list of results
        """
        if not results:
            return []
        
        unique_results = []
        seen_values: Set[Any] = set()
        
        for result in results:
            value = result.get(field)
            
            if value is None:
                unique_results.append(result)
                continue
            
            if value not in seen_values:
                seen_values.add(value)
                unique_results.append(result)
        
        return unique_results
    
    def remove_near_duplicates(self, results: List[Dict[str, Any]], 
                              threshold: float = 0.9) -> List[Dict[str, Any]]:
        """
        Remove near-duplicates based on content similarity.
        
        Args:
            results: List of result dictionaries
            threshold: Similarity threshold (0.0-1.0)
            
        Returns:
            Filtered list of results
        """
        if not results:
            return []
        
        filtered = []
        contents = [r.get('content', '') for r in results]
        
        for i, result in enumerate(results):
            is_near_duplicate = False
            
            for j in range(i):
                if self._calculate_similarity(contents[i], contents[j]) >= threshold:
                    is_near_duplicate = True
                    break
            
            if not is_near_duplicate:
                filtered.append(result)
        
        return filtered
