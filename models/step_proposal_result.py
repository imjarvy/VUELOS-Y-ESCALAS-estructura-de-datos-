from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Any, Dict

@dataclass
class StepProposalResult:
    routes: List[Any] = field(default_factory=list)
    activities: List[Any] = field(default_factory=list)
    jobs: List[Any] = field(default_factory=list)
    mandatory_actions: List[str] = field(default_factory=list)
    meta: Dict[str, Any] = field(default_factory=dict)
