from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class TripState:
    current_airport: str
    budget_remaining: float
    time_elapsed_min: int
    time_remaining_min: int
    itinerary: List[Any] = field(default_factory=list)
    activities_done: List[Any] = field(default_factory=list)
    jobs_done: List[Any] = field(default_factory=list)
    last_accommodation_at_min: Optional[int] = None
    last_meal_at_min: Optional[int] = None
    decisions: List[Any] = field(default_factory=list)
