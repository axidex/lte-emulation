from abc import ABC, abstractmethod

class Protocol(ABC):
    """Network protocol"""

    @abstractmethod
    def __init__(self):
        """"""
    
        self.name = "name"
        raise NotImplementedError