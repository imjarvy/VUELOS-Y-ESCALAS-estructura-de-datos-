from __future__ import annotations
from typing import Optional, Any, Dict
from models.planner_models import (
    TripConfig,
)
from services.trip_session import TripSession


class AdvancedPlanner:
    """
    Session manager for advanced planning.
    Receives a graph instance and exposes methods to start step-by-step sessions.
    """
    def __init__(self, graph: Any, defaults: Optional[Dict[str, Any]] = None) -> None:
        self.graph = graph
        self.defaults = defaults or {}

    def start_session(self, origin: str, budget: float, time_h: float, preferences: Optional[TripConfig] = None) -> "TripSession":
        """Create and return a new ``TripSession``.

        This method only initializes session state.
        """
        raise NotImplementedError()


__all__ = [
    "AdvancedPlanner",
    "TripSession",
]
