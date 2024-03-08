from src.controller import Controller

from src.storage import Clients
from src.storage import Recipients

def main():
    """"""

    cellular_device  = Controller(client=Clients.client1)

    cellular_device.send_message(
                                recipient=Recipients.recipient,
                                message="Hello!!!"
                            )

if __name__ == "__main__":
    main()