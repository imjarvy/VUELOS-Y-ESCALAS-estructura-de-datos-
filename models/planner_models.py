"""Dataclass models used by the advanced planner (R3).

This file groups pure data structures to avoid mixing logic and models
inside the same module.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any


@dataclass
class TripConfig:
    budget_initial: float
    time_available_h: float
    preferred_aircraft: List[str]
    allow_secondary_airports: bool = True
    budget_threshold_pct: float = 35.0
    global_overrides: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Leg:
    origin: str
    destination: str
    aircraft: str
    distance_km: float
    time_min: int
    cost_usd: float


@dataclass
class TransportOption:
    aircraft: str
    cost_usd: float
    time_min: int
    is_subsidized: bool = False


@dataclass
class Activity:
    id: str
    name: str
    type: str  # 'mandatory' | 'optional'
    duration_min: int
    cost_usd: float


@dataclass
class ActivityRecord:
    activity: Activity
    performed_at_min: int


@dataclass
class JobOffer:
    id: str
    name: str
    hourly_rate: float
    max_hours: int


@dataclass
class JobRecord:
    job: JobOffer
    hours_worked: int
    income_usd: float


@dataclass
class DecisionRecord:
    timestamp_min: int
    kind: str  # 'transport' | 'activity' | 'job' | 'skip'
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TripState:
    current_airport: str
    budget_remaining: float
    time_elapsed_min: int
    time_remaining_min: int
    itinerary: List[Leg] = field(default_factory=list)
    activities_done: List[ActivityRecord] = field(default_factory=list)
    jobs_done: List[JobRecord] = field(default_factory=list)
    last_accommodation_at_min: Optional[int] = None
    last_meal_at_min: Optional[int] = None
    decisions: List[DecisionRecord] = field(default_factory=list)


@dataclass
class RouteProposal:
    id: str
    destination: str
    distance_km: float
    transport_options: List[TransportOption]
    est_arrival_min: int


@dataclass
class StepProposalResult:
    routes: List[RouteProposal]
    activities: List[Activity]
    jobs: List[JobOffer]
    mandatory_actions: List[str]
    meta: Dict[str, Any]


@dataclass
class ApplyResult:
    updated_state: TripState
    next_proposals: Optional[StepProposalResult]
    events: List[str]
    errors: List[str]


@dataclass
class TripReport:
    visited: List[Dict[str, Any]]
    legs: List[Leg]
    activities: List[ActivityRecord]
    jobs: List[JobRecord]
    totals: Dict[str, Any]


__all__ = [
    "TripConfig",
    "TripState",
    "Leg",
    "TransportOption",
    "Activity",
    "ActivityRecord",
    "JobOffer",
    "JobRecord",
    "DecisionRecord",
    "RouteProposal",
    "StepProposalResult",
    "ApplyResult",
    "TripReport",
]
