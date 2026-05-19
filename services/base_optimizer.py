"""Abstract base class for all route optimizers.

Dependency Inversion in practice:
    planner_panel.js calls POST /api/plan/basic.
    r2_routes.py receives a BaseOptimizer instance (injected in app.py).
    The endpoint calls optimizer.optimize(...) without knowing whether
    it's running Dijkstra by cost, time, or distance.
    The UI depends on the abstraction, not the concrete implementation.
"""

from abc import ABC, abstractmethod
from typing import Any, List, Optional

from core.graph import Graph
from models.itinerary import Itinerary


class BaseOptimizer(ABC):
    """
    Abstract base class for all route optimizers.

    Subclasses:
        - CostOptimizer      → Dijkstra by cost (USD)
        - TimeOptimizer      → Dijkstra by flight time (min)
        - DistanceOptimizer  → Dijkstra by distance (km)

    All share the same optimize() method so r2_routes.py
    can use them interchangeably.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Optimizer name returned in API response.
        Examples: 'cost', 'time', 'distance'.
        Used by frontend to label itineraries.
        """

    @abstractmethod
    def optimize(
        self,
        graph: Graph,
        origin: str,
        dest: str,
        transport_types: Optional[List[str]] = None,
        include_secondary: bool = True,
        **params: Any,
    ) -> Optional[Itinerary]:
        """
        Find the best route between origin and dest.

        Args:
            graph: Loaded Graph from airports.json.
            origin: Departure airport code (e.g. 'BOG').
            dest: Arrival airport code (e.g. 'LIM').
            transport_types: Allowed aircraft types.
            include_secondary: Exclude non-hub airports if False.
            **params: Extra options (e.g. max_stops=2).

        Returns:
            Itinerary with optimal path, or None if not found.
        """

    def validate_endpoints(self, graph: Graph, origin: str, dest: str) -> None:
        """
        Check that origin and dest exist in graph and are different.

        Raises:
            ValueError if airports are missing or identical.
        """
        if origin not in graph:
            raise ValueError(f"Origin {origin!r} not found in graph.")
        if dest not in graph:
            raise ValueError(f"Destination {dest!r} not found in graph.")
        if origin == dest:
            raise ValueError(f"Origin and destination are the same: {origin!r}.")
