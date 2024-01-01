# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from typing import Optional

from IEC62325.MarketOperations.ParticipantInterfaces.Bid import Bid
from IEC62325.MarketOperations.ParticipantInterfaces.BidError import BidError


class ResourceBid(Bid):
    def __init__(self) -> None:
        super().__init__()
        self.aggregation_flagOptional[int] = 0

        self.bid_statusOptional[str] = ""
        self.commodity_typeOptional[str] = ""
        self.contingency_avail_flagOptional[str] = ""
        self.created_isoOptional[str] = ""
        self.energy_max_dayOptional[float] = 0.0

        self.energy_min_dayOptional[float] = 0.0

        self.market_sep_flagOptional[str] = ""
        self.min_dispatch_timeOptional[int] = 0

        self.resource_loading_typeOptional[int] = 0

        self.shutdowns_max_dayOptional[int] = 0

        self.shutdowns_max_weekOptional[int] = 0

        self.startups_max_dayOptional[int] = 0

        self.startups_max_weekOptional[int] = 0

        self.virtualOptional[bool] = False
        self.bid_errorOptional[BidError] = BidError()
