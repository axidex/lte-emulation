

class HSS:
    """Home Subscriber Server"""

    def __init__(self, clients: list[int] = []):
        """"""

        self.clients: list[int] = clients

    def add_client(self, client_id: int):
        """Add new client"""

        self.clients.append(client_id)

    def auth(self, client_id: int) -> bool:
        """Auth client"""
        
        return True if client_id in self.clients else False
        