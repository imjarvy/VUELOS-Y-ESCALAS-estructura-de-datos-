from __future__ import annotations
from dataclasses import dataclass
from typing import Any

@dataclass
class JobRecord:
    job: Any
    hours_worked: int
    income_usd: float
