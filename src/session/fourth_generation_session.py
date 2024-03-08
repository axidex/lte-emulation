from src.session.session import Session
from src.dataclasses.sgw import SGW
from src.dataclasses.quality import Quality
from src.dataclasses.recipient import Recipient

from datetime import datetime

class FourthGenerationSession(Session):
    """"""

    def __init__(self, sgw: SGW, quality: Quality):
        """"""

        self.sgw = sgw
        self.quality = quality

        print(f"Session will be using sgw: {self.sgw.sgw_id}")
        print(f"Quality will be {self.quality}")      
        
    
    def send_message(self, recipient: Recipient, message: str):
        """"""
        
        print(f"Message was sent to {recipient.ip} | message: {message}")

    def __enter__(self):
        print(f"Session Started | {datetime.utcnow()}")
        return self
    
    def __exit__(self, type, value, traceback):
        print(f"Session Ended | {datetime.utcnow()}")