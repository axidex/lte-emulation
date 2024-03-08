from src.dataclasses.client import Client
from src.dataclasses.sgw import SGW
from src.dataclasses.recipient import Recipient

from src.session.fourth_generation_session import FourthGenerationSession

class Controller:
    """"""

    def __init__(self, client: Client):
        """"""

        self.client = client

    def _auth(self) -> list[SGW]:
        """4G authentication"""

        ta = self.client.available_ta

        for mme in ta.mme:
            if self.client.client_id in mme.hss.clients_ids:
                sgw = [sgw for sgw in mme.sgw if self.__is_sgw_available(sgw)]
                print(f"After AUTH | found MME id - {mme.mme_id} | SGW - {[(sgw.sgw_id) for sgw in sgw]}")

                return sgw
            
    def __is_sgw_available(self, sgw: SGW) -> bool:
        """"""

        for protocol in self.client.protocols:
            if protocol.name in [protocol.name for protocol in sgw.protocols]:
                return True
            
        return False
    
    def _get_session(self, sgw: SGW) -> FourthGenerationSession:
        """"""

        return FourthGenerationSession(
                                    sgw=sgw,
                                    quality=sgw.pcrf.get_quality()
                                )

    def __choose_sgw(self, sgw_list: list[SGW]) -> SGW:
        """"""
        
        return sgw_list[0] if sgw_list else None

    def send_message(self, recipient: Recipient, message: str) -> bool:
        """"""

        sgw_list = self._auth()
        if not sgw_list:
            print("Message was not sent because of your device hasn't needed protocols")
            return False
        sgw = self.__choose_sgw(sgw_list=sgw_list)
        
        with self._get_session(sgw) as session:
            session.send_message(recipient=recipient, message=message)
        
        
                                
        