"""Task Classifier - Classify user intent into research modes."""

from typing import Dict, List, Tuple
import re


class TaskClassifier:
    """Classify user research intent into one of 7 modes."""
    
    # 7 research modes
    MODES = [
        "academic_research",      # 学术研究
        "competitive_analysis",    # 竞品分析
        "market_research",         # 市场调研
        "technology_tracking",     # 技术追踪
        "event_monitoring",       # 事件监测
        "opinion_analysis",       # 舆情分析
        "custom_research",        # 自定义研究
    ]
    
    # Keywords for each mode
    KEYWORDS = {
        "academic_research": [
            "研究", "论文", "文献", "学术", "期刊", "pubmed", "scholar",
            "doi", "citation", "引用", "meta分析", "系统综述",
        ],
        "competitive_analysis": [
            "竞品", "竞争对手", "对比", "分析", "比较", "vs", " versus",
            "市场份额", "产品对比", "功能对比",
        ],
        "market_research": [
            "市场", "调研", "市场规模", "趋势", "消费者", "用户画像",
            "需求分析", "市场机会", "赛道",
        ],
        "technology_tracking": [
            "技术", "框架", "库", "工具", "github", "star", "更新",
            "版本", "发布", "新特性", "roadmap",
        ],
        "event_monitoring": [
            "事件", "监测", "监控", "实时", "动态", "新闻", "快讯",
            "breaking", "最新", "更新",
        ],
        "opinion_analysis": [
            "舆情", "口碑", "评论", "反馈", "评价", "社交媒体",
            "小红书", "微博", "抖音", "态度", "情绪",
        ],
        "custom_research": [],  # Default fallback
    }
    
    def __init__(self):
        self.mode_keywords = self.KEYWORDS
        
    def classify(self, user_input: str) -> Tuple[str, float]:
        """
        Classify user input into a research mode.
        
        Args:
            user_input: User's research query
            
        Returns:
            Tuple of (mode, confidence_score)
        """
        input_lower = user_input.lower()
        
        # Count keyword matches for each mode
        scores = {}
        for mode, keywords in self.mode_keywords.items():
            if mode == "custom_research":
                continue
            score = 0
            for keyword in keywords:
                if keyword in input_lower:
                    score += 1
            scores[mode] = score
        
        # Find best match
        if not scores:
            return "custom_research", 1.0
            
        best_mode = max(scores, key=scores.get)
        best_score = scores[best_mode]
        
        if best_score == 0:
            return "custom_research", 1.0
        
        # Calculate confidence (normalized)
        total_keywords = len(self.mode_keywords[best_mode])
        confidence = min(best_score / max(total_keywords * 0.3, 1), 1.0)
        
        return best_mode, confidence
    
    def get_mode_description(self, mode: str) -> str:
        """Get Chinese description for a mode."""
        descriptions = {
            "academic_research": "学术研究",
            "competitive_analysis": "竞品分析",
            "market_research": "市场调研",
            "technology_tracking": "技术追踪",
            "event_monitoring": "事件监测",
            "opinion_analysis": "舆情分析",
            "custom_research": "自定义研究",
        }
        return descriptions.get(mode, "未知模式")
    
    def get_available_modes(self) -> List[str]:
        """Get list of all available modes."""
        return self.MODES
