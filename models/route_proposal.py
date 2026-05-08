from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Any

@dataclass
class RouteProposal:
    id: str
    destination: str
    distance_km: float
    transport_options: List[Any] = field(default_factory=list)
    est_arrival_min: int = 0
