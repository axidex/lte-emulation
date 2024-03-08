from dataclasses import dataclass

from src.dataclasses.pgw import PGW
from src.dataclasses.pcrf import PCRF
from src.protocols.protocol import Protocol

@dataclass(frozen=True)
class SGW:
    """Serving GateWay"""

    sgw_id: int
    pgw: PGW
    pcrf: PCRF
    
    protocols: list[Protocol]

    def __hash__(self):
        return hash(self.sgw_id)