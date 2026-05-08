
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class DecisionRecord:
    timestamp_min: int
    kind: str  # 'transport' | 'activity' | 'job' | 'skip'
    details: Dict[str, Any] = field(default_factory=dict)
