# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from datetime import datetime
from typing import Optional

from IEC61970.Base.Core.Curve import Curve
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.InterchangeETCData import InterchangeETCData

from IEC62325.MarketOperations.MktDomain.CheckOutType import CheckOutType
from IEC62325.MarketOperations.MktDomain.InterTieDirection import InterTieDirection
from IEC62325.MarketOperations.MktDomain.MarketProductType import MarketProductType
from IEC62325.MarketOperations.MktDomain.MarketType import MarketType
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MktDomain.EnergyProductType import EnergyProductType
from IEC62325.MarketOperations.ReferenceData.SchedulingPoint import SchedulingPoint
from IEC62325.MarketOperations.ReferenceData.RegisteredInterTie import RegisteredInterTie


class InterchangeSchedule(Curve):
    def __init__(self) -> None:
        super().__init__()
        self.check_out_type: Optional[CheckOutType] = CheckOutType  # To indicate a check out type such as adjusted capacity or dispatch capacity
        self.direction_type: Optional[InterTieDirection] = InterTieDirection()  # Import or export
        self.energy_type: Optional[MarketProductType] = MarketProductType # Energy product type
        self.interval_length: Optional[int] = 0  # Interval length
        self.market_type: Optional[MarketType] = MarketType  # Market type
        self.operating_date: Optional[DateTime] = DateTime()  # Operating date, hour
        self.out_of_market_type: Optional[bool] = False  # To indicate an out-of-market (OOM) schedule
        self.schedule_type: Optional[EnergyProductType] = EnergyProductType  # Schedule type
        self.wcr_id: Optional[str] = ""  # Wheeling Counter-Resource ID (required when Schedule Type=Wheel)
        self.intertie: Optional[SchedulingPoint] = SchedulingPoint()
        self.registered_intertie: Optional[RegisteredInterTie] = RegisteredInterTie()
        self.interchange_etc_data: Optional[InterchangeETCData] = InterchangeETCData()
