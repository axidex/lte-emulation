from src.dataclasses.client import Client
from src.dataclasses.hss import HSS
from src.dataclasses.mme import MME
from src.dataclasses.ta import TrackingArea
from src.dataclasses.pcrf import PCRF
from src.dataclasses.pgw import PGW
from src.dataclasses.sgw import SGW
from src.dataclasses.recipient import Recipient

from src.protocols.pdcp import PDCP
from src.protocols.plcp import PLCP


class Recipients:

    recipient = Recipient(ip="192.168.0.1")

class PCRFs:
    """"""

    pcrf1 = PCRF()


class PGWs:
    """"""

    pgw1 = PGW(pgw_id=1)


class SGWs:
    """"""

    sgw1 = SGW(
        sgw_id=1,
        pgw=PGWs.pgw1,
        pcrf=PCRFs.pcrf1,
        protocols=[PDCP()]
    )

    sgw2 = SGW(
        sgw_id=2,
        pgw=PGWs.pgw1,
        pcrf=PCRFs.pcrf1,
        protocols=[PLCP()]
    )


class HSSs:
    """"""

    hss1 =  HSS(clients_ids=[1, 2])


class MMEs:
    """"""

    mme1 = MME(
        mme_id=1, 
        hss=HSSs.hss1,
        sgw=[SGWs.sgw1, SGWs.sgw2]
    )


class TAs:
    """"""

    ta1 = TrackingArea(
                    ta_id=1, 
                    mme=[MMEs.mme1]
                )

class Clients:
    """Custom client Storage"""

    client1 = Client(
                client_id=1, 
                protocols=[PDCP()],
                available_ta=TAs.ta1
            )

    client2 = Client(
                client_id=2,
                protocols=[PDCP()],
                available_ta=TAs.ta1
            )



