from random import randint

from src.dataclasses.quality import Quality

class PCRF:
    """Policy and Charging Rules Function"""

    def get_quality(self) -> Quality:
        """"""

        return Quality(randint(1,3))
