"""Output Renderer - Render research results in different formats."""

from typing import Dict, List, Any
from dataclasses import dataclass
import json
from datetime import datetime


@dataclass
class ResearchResult:
    """Container for research results."""
    query: str
    mode: str
    results: List[Dict[str, Any]]
    scores: List[Any]  # List of SourceScore
    metadata: Dict[str, Any]


class OutputRenderer:
    """Render research results in various formats."""
    
    def __init__(self):
        pass  # No pre-configured templates needed
    
    def render(self, result: ResearchResult, format: str = "markdown") -> str:
        """
        Render research result in specified format.
        
        Args:
            result: ResearchResult object
            format: Output format ("markdown", "html", "json", "text")
            
        Returns:
            Rendered string
        """
        if format == "markdown":
            return self._render_markdown(result)
        elif format == "html":
            return self._render_html(result)
        elif format == "json":
            return self._render_json(result)
        elif format == "text":
            return self._render_text(result)
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    def _render_markdown(self, result: ResearchResult) -> str:
        """Render as Markdown."""
        md = f"# 研究报告: {result.query}\n\n"
        md += f"**研究模式**: {result.mode}\n"
        md += f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        md += f"**结果数量**: {len(result.results)}\n\n"
        
        md += "---\n\n"
        
        # Render results
        for i, (item, score) in enumerate(zip(result.results, result.scores), 1):
            md += f"## {i}. {item.get('title', '无标题')}\n\n"
            md += f"- **来源**: {item.get('source', '未知')}\n"
            md += f"- **URL**: {item.get('url', '无')}\n"
            md += f"- **可信度评分**: {score.credibility_score:.2f}\n"
            md += f"- **新鲜度评分**: {score.freshness_score:.2f}\n"
            md += f"- **相关性评分**: {score.relevance_score:.2f}\n"
            md += f"- **总评分**: {score.total_score:.2f}\n\n"
            
            if item.get('content'):
                content = item['content'][:500]  # First 500 chars
                md += f"**摘要**:\n{content}...\n\n"
            
            if score.reasons:
                md += f"**评分理由**: {', '.join(score.reasons)}\n"
            
            md += "\n---\n\n"
        
        # Metadata
        if result.metadata:
            md += "\n## 元数据\n\n"
            md += "```json\n"
            md += json.dumps(result.metadata, ensure_ascii=False, indent=2)
            md += "\n```\n"
        
        return md
    
    def _render_html(self, result: ResearchResult) -> str:
        """Render as HTML."""
        html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>研究报告</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1 { color: #333; }
        h2 { color: #555; margin-top: 30px; }
        .meta { color: #666; font-size: 0.9em; }
        .score { background: #f0f0f0; padding: 10px; border-radius: 5px; margin: 10px 0; }
        .reason { color: #666; font-size: 0.9em; }
        hr { border: none; border-top: 1px solid #ddd; }
    </style>
</head>
<body>
"""
        
        html += f"<h1>研究报告: {result.query}</h1>\n"
        html += f'<p class="meta">研究模式: {result.mode} | 生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | 结果数量: {len(result.results)}</p>\n'
        
        # Render results
        for i, (item, score) in enumerate(zip(result.results, result.scores), 1):
            html += f"<h2>{i}. {item.get('title', '无标题')}</h2>\n"
            html += '<div class="score">\n'
            html += f'<p><strong>来源</strong>: {item.get("source", "未知")}</p>\n'
            html += f'<p><strong>URL</strong>: <a href="{item.get("url", "#")}">{item.get("url", "无")}</a></p>\n'
            html += f'<p><strong>可信度评分</strong>: {score.credibility_score:.2f}</p>\n'
            html += f'<p><strong>新鲜度评分</strong>: {score.freshness_score:.2f}</p>\n'
            html += f'<p><strong>相关性评分</strong>: {score.relevance_score:.2f}</p>\n'
            html += f'<p><strong>总评分</strong>: {score.total_score:.2f}</p>\n'
            html += '</div>\n'
            
            if item.get('content'):
                content = item['content'][:500]
                html += f"<p><strong>摘要</strong>:<br>{content}...</p>\n"
            
            if score.reasons:
                html += f'<p class="reason">评分理由: {", ".join(score.reasons)}</p>\n'
            
            html += "<hr>\n"
        
        html += "</body>\n</html>"
        return html
    
    def _render_json(self, result: ResearchResult) -> str:
        """Render as JSON."""
        output = {
            "query": result.query,
            "mode": result.mode,
            "generated_at": datetime.now().isoformat(),
            "result_count": len(result.results),
            "results": []
        }
        
        for item, score in zip(result.results, result.scores):
            result_dict = {
                "title": item.get('title'),
                "source": item.get('source'),
                "url": item.get('url'),
                "content": item.get('content', '')[:500],
                "scores": {
                    "credibility": score.credibility_score,
                    "freshness": score.freshness_score,
                    "relevance": score.relevance_score,
                    "total": score.total_score,
                },
                "reasons": score.reasons,
            }
            output["results"].append(result_dict)
        
        output["metadata"] = result.metadata
        
        return json.dumps(output, ensure_ascii=False, indent=2)
    
    def _render_text(self, result: ResearchResult) -> str:
        """Render as plain text."""
        text = f"研究报告: {result.query}\n"
        text += "=" * 50 + "\n\n"
        text += f"研究模式: {result.mode}\n"
        text += f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        text += f"结果数量: {len(result.results)}\n\n"
        text += "-" * 50 + "\n\n"
        
        for i, (item, score) in enumerate(zip(result.results, result.scores), 1):
            text += f"{i}. {item.get('title', '无标题')}\n"
            text += f"   来源: {item.get('source', '未知')}\n"
            text += f"   URL: {item.get('url', '无')}\n"
            text += f"   可信度: {score.credibility_score:.2f} | 新鲜度: {score.freshness_score:.2f} | 相关性: {score.relevance_score:.2f} | 总分: {score.total_score:.2f}\n"
            
            if item.get('content'):
                content = item['content'][:200]
                text += f"   摘要: {content}...\n"
            
            if score.reasons:
                text += f"   评分理由: {', '.join(score.reasons)}\n"
            
            text += "\n"
        
        return text
    
    def save_to_file(self, result: ResearchResult, filepath: str, format: str = "markdown") -> None:
        """
        Save rendered output to file.
        
        Args:
            result: ResearchResult object
            filepath: Output file path
            format: Output format
        """
        rendered = self.render(result, format)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(rendered)
