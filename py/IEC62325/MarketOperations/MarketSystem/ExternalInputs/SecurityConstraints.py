# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from datetime import datetime
from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC62325.MarketOperations.Participant.RTO import RTO


class SecurityConstraints(IdentifiedObject):
    """
    Typical for regional transmission operators (RTOs), these constraints include
    transmission as well as generation group constraints identified in both base
    case and critical contingency cases.
    """

    def __init__(self) -> None:
        super().__init__()
        self.actual_mw: Optional[ActivePower] = ActivePower()  # Actual branch or group of branches MW flow (only for transmission constraints)
        self.max_mw: Optional[ActivePower] = ActivePower()  # Maximum MW limit
        self.min_mw: Optional[ActivePower] = ActivePower()  # Minimum MW limit (only for transmission constraints)
        self.rto: Optional[RTO] = RTO()
