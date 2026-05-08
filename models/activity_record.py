from __future__ import annotations
from dataclasses import dataclass
from typing import Any

@dataclass
class ActivityRecord:
    activity: Any
    performed_at_min: int
