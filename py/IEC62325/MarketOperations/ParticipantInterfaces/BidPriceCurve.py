# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from typing import Any

from IEC61970.Base.Core.Curve import Curve
from IEC62325.MarketOperations.ParticipantInterfaces.BidPriceSchedule import BidPriceSchedule


class BidPriceCurve(Curve):
    """
    * Relationship between unit operating price in $/hour (Y-axis) and unit output in
    * MW (X-axis).
    * @created 28-Dec-2023 5:19:23 PM
    """
    def __init__(self) -> None:
        super().__init__()
        self.bid_schedule: Any = BidPriceSchedule()
