from dataclasses import dataclass

from src.dataclasses.hss import HSS
from src.dataclasses.sgw import SGW

@dataclass(frozen=True)
class MME:
    """Mobile Management Entity"""

    mme_id: int
    hss: HSS
    sgw: list[SGW]
