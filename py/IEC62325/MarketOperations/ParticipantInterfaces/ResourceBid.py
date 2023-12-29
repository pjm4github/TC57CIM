# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from typing import Optional

from IEC62325.MarketOperations.ParticipantInterfaces.Bid import Bid
from IEC62325.MarketOperations.ParticipantInterfaces.BidError import BidError


class ResourceBid(Bid):
    def __init__(self) -> None:
        super().__init__()
        self.aggregation_flag: Optional[int] = 0

        self.bid_status: Optional[str] = ""
        self.commodity_type: Optional[str] = ""
        self.contingency_avail_flag: Optional[str] = ""
        self.created_iso: Optional[str] = ""
        self.energy_max_day: Optional[float] = 0.0

        self.energy_min_day: Optional[float] = 0.0

        self.market_sep_flag: Optional[str] = ""
        self.min_dispatch_time: Optional[int] = 0

        self.resource_loading_type: Optional[int] = 0

        self.shutdowns_max_day: Optional[int] = 0

        self.shutdowns_max_week: Optional[int] = 0

        self.startups_max_day: Optional[int] = 0

        self.startups_max_week: Optional[int] = 0

        self.virtual: Optional[bool] = False
        self.bid_error: Optional[BidError] = BidError()
