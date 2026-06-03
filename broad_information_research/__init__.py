"""Broad Information Research Core - Core logic extracted from QClaw skill."""

__version__ = "0.1.0"

from .task_classifier import TaskClassifier
from .source_selector import SourceSelector
from .query_generator import QueryGenerator
from .deduplicator import Deduplicator
from .scorer import Scorer
from .output_renderer import OutputRenderer
from .mediacrawler_client import MediaCrawlerClient

__all__ = [
    "TaskClassifier",
    "SourceSelector", 
    "QueryGenerator",
    "DedupLicator",
    "Scorer",
    "OutputRenderer",
    "MediaCrawlerClient",
]
