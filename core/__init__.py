"""AetherRecon Core Engine"""

from .engine import AetherEngine
from .auth import AuthorizationGuard
from .config import Settings
from .plugin import PluginLoader, PluginBase
from .reporter import EvidenceReporter

__all__ = [
    "AetherEngine",
    "AuthorizationGuard",
    "Settings",
    "PluginLoader",
    "PluginBase",
    "EvidenceReporter",
]

__version__ = "1.0.0"
__author__ = "Sayan the researcher"
