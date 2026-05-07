from __future__ import annotations

from typing import Any, Dict, List, TYPE_CHECKING
import uuid

from models.planner_models import (
    TripConfig,
    TripState,
    StepProposalResult,
    ApplyResult,
    TripReport,
)

if TYPE_CHECKING:
    from services.advanced_planner import AdvancedPlanner


class TripSession:
    """Represents a step-by-step interactive session.

    The UI should call ``step_proposals()`` and then ``apply_choice()``
    according to the traveler decision. Every decision is stored in
    ``state.decisions``.
    """

    def __init__(self, config: TripConfig, initial_state: TripState, planner: "AdvancedPlanner") -> None:
        self.config = config
        self.state = initial_state
        self.planner = planner
        self.session_id = str(uuid.uuid4())

    def step_proposals(self) -> StepProposalResult:
        """Compute and return current alternatives.

        It should include:
        - candidate routes from ``state.current_airport``
        - transport options per route
        - available activities and jobs
        - markers for mandatory actions (lodging/meals)
        """
        raise NotImplementedError()

    def apply_choice(self, choice: Dict[str, Any]) -> ApplyResult:
        """Apply a user decision and update ``TripState``.

        ``choice`` is a dict carrying the decision
        (transport/activity/job/skip).
        Returns ``ApplyResult`` with the updated state and next proposals.
        """
        raise NotImplementedError()

    def serialize(self) -> Dict[str, Any]:
        """Serialize session state for persistence (save/restore)."""
        raise NotImplementedError()

    @staticmethod
    def deserialize(data: Dict[str, Any], planner: "AdvancedPlanner") -> "TripSession":
        """Restore a ``TripSession`` from serialized data."""
        raise NotImplementedError()

    def force_recalculate_after_network_change(self, changed_edges: List[Any]) -> Dict[str, Any]:
        """Recompute proposals when network state changes (R4 integration).

        Should return metadata about recalculation and the new state.
        """
        raise NotImplementedError()

    def finalize_and_report(self) -> TripReport:
        """Generate the final ``TripReport`` with totals and records.

        This method returns the report structure required by R5.
        """
        raise NotImplementedError()


__all__ = ["TripSession"]
