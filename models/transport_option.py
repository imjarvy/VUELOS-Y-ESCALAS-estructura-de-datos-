from __future__ import annotations
from dataclasses import dataclass

@dataclass
class TransportOption:
    aircraft: str
    cost_usd: float
    time_min: int
    is_subsidized: bool = False
