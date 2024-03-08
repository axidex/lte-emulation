from abc import ABC, abstractmethod

from src.session.session import Session

class Connector(ABC):
    """Establish Connection"""

    @abstractmethod
    def get_session() -> Session:
        """"""