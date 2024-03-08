from src.connectors.connector import Connector
from src.session.fourth_generation_session import FourthGenerationSession

from src.dataclasses.sgw import SGW

class FourthGenerationConnector(Connector):
    """"""

    def get_session(self, sgw: SGW) -> FourthGenerationSession:
        """"""

        return FourthGenerationSession(sgw=sgw)