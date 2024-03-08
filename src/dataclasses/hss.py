from dataclasses import dataclass

@dataclass
class HSS:
    """Home Subscriber Server"""

    clients_ids: list[int]