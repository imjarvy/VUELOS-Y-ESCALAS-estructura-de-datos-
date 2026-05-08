from __future__ import annotations
from dataclasses import dataclass

@dataclass
class JobOffer:
    id: str
    name: str
    hourly_rate: float
    max_hours: int
