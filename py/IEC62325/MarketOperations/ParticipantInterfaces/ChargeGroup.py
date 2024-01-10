# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from typing import Optional

from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MarketOpCommon.MktUserAttribute import MktUserAttribute


class ChargeGroup:
    """
    Charge Group is the grouping of Charge Types for settlement invoicing purpose.
    Examples such as Ancillary Services, Interests, etc.
    @created 28-Dec-2023 5:20:24 PM
    """

    def __init__(self) -> None:
        self.effective_date: Optional[DateTime] = DateTime()
        self.market_code: Optional[str] = ""
        self.termination_date: Optional[DateTime] = DateTime()
        # A ChargeGroup instance can have relationships with other ChargeGroup instances.
        self.charge_group_parent: Optional[ChargeGroup] = ChargeGroup()
        self.mkt_user_attribute: Optional[MktUserAttribute] = MktUserAttribute()
