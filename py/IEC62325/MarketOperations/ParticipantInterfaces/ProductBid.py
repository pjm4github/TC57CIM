# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from typing import Any

from IEC62325.MarketOperations.ParticipantInterfaces.Bid import Bid
from IEC62325.MarketOperations.ParticipantInterfaces.BidDistributionFactor import BidDistributionFactor
from IEC62325.MarketOperations.ParticipantInterfaces.BidPriceSchedule import BidPriceSchedule
from IEC62325.MarketOperations.ParticipantInterfaces.BidSelfSched import BidSelfSched


class ProductBid:

    def __init__(self) -> None:
        self.bid_schedule: BidPriceSchedule()
        self.bid: Any = Bid()
        self.bid_distribution_factor: Any = BidDistributionFactor()
        self.bid_self_sched: Any = BidSelfSched()
