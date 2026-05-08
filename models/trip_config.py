from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class TripConfig:
    budget_initial: float
    time_available_h: float
    preferred_aircraft: List[str]
    allow_secondary_airports: bool = True
    budget_threshold_pct: float = 35.0
    global_overrides: Dict[str, Any] = field(default_factory=dict)
