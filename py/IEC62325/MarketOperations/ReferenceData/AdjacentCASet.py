# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 13:18:10 2023
from typing import Optional

from IEC62325.MarketOperations.ParticipantInterfaces.BidSelfSched import BidSelfSched
from IEC62325.MarketOperations.ReferenceData.SubControlArea import SubControlArea


class AdjacentCASet:
    """
    Groups Adjacent Control Areas.
    """
    def __init__(self) -> None:
        self.loss_percentage: float = 0.0
        self.sub_control_area: Optional[SubControlArea] = SubControlArea()
        self.bid_self_sched: Optional[BidSelfSched] = BidSelfSched()
