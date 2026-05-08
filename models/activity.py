from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Activity:
    id: str
    name: str
    type: str  # 'mandatory' | 'optional'
    duration_min: int
    cost_usd: float
