"""Example plugin for AetherRecon"""

from typing import Any, Dict
from core.plugin import PluginBase


class HelloPlugin(PluginBase):
    name = "hello"
    description = "Example plugin that greets the target"
    version = "1.0.0"
    author = "AetherRecon"
    requires_auth = False
    category = "example"

    def run(self, **kwargs) -> Dict[str, Any]:
        target = kwargs.get("target", "world")
        return {
            "message": f"Hello, {target}! This is an example AetherRecon plugin.",
            "status": "success",
        }
