from abc import ABC, abstractmethod

class Session(ABC):
    """Handling Messages"""

    @abstractmethod
    def send_message(client_id: int):
        """"""