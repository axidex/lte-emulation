from dataclasses import dataclass, field

from src.protocols.protocol import Protocol
from src.dataclasses.ta import TrackingArea

@dataclass(eq=True)
class Client:
    """Cellular network client"""

    client_id: int

    protocols: list[Protocol] = field(compare=False)
    available_ta: TrackingArea = field(compare=False)