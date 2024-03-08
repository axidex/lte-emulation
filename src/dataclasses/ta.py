from dataclasses import dataclass

from src.dataclasses.mme import MME

@dataclass(frozen=True)
class TrackingArea:
    """Tracking Area"""

    ta_id: int
    mme: list[MME]
