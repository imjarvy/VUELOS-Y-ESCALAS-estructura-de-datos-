from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, List, Optional

@dataclass
class ApplyResult:
    updated_state: Any
    next_proposals: Optional[Any] = None
    events: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
