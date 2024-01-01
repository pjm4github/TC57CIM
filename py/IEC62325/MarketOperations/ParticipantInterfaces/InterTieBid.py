# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023

from typing import Optional

from IEC62325.MarketOperations.ParticipantInterfaces.RampRateCurve import RampRateCurve
from IEC62325.MarketOperations.ParticipantInterfaces.ResourceBid import ResourceBid
from IEC62325.MarketOperations.ReferenceData.RegisteredInterTie import RegisteredInterTie


class InterTieBid(ResourceBid):
    """
    This class represents the inter tie bid.
    @created 28-Dec-2023 5:21:28 PM
    """
    def __init__(self) -> None:
        """
        Constructor for InterTieBid
        """
        super().__init__()
        self.min_hourly_blockOptional[int] = 0

        self.registered_inter_tieOptional[RegisteredInterTie] = RegisteredInterTie()
        self.ramp_rate_curveOptional[RampRateCurve] = RampRateCurve()
