# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from typing import Optional

from IEC62325.MarketOperations.ParticipantInterfaces.Bid import Bid
from IEC62325.MarketOperations.ParticipantInterfaces.LoadBid import LoadBid


class AreaLoadBid(Bid):
    """
    AreaLoadBid is not submitted by a market participant into the Markets. Instead,
    it is simply an aggregation of all LoadBids contained wtihin a specific
    SubControlArea. This entity should inherit from Bid for representation of the
    timeframe (startTime, stopTime) and the market type.
    @created 28-Dec-2023 5:17:54 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.demand_bid_mw: float = 0.0  # The Demand Bid Megawatt for the area case. Attribute Usage: This is
        # Scheduled demand MW in Day Ahead
        self.load_bid: Optional[LoadBid] = LoadBid()
