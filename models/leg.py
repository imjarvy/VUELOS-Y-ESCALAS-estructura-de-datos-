from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Leg:
    origin: str
    destination: str
    aircraft: str
    distance_km: float
    time_min: int
    cost_usd: float
