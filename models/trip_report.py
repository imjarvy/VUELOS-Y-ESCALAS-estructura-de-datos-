from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class TripReport:
    visited: List[Dict[str, Any]]
    legs: List[Any]
    activities: List[Any]
    jobs: List[Any]
    totals: Dict[str, Any]
