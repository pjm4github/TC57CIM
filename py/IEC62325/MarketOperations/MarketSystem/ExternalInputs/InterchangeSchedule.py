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
        self.check_out_typeOptional[CheckOutType] = CheckOutType  # To indicate a check out type such as adjusted capacity or dispatch capacity
        self.direction_typeOptional[InterTieDirection] = InterTieDirection()  # Import or export
        self.energy_typeOptional[MarketProductType] = MarketProductType # Energy product type
        self.interval_lengthOptional[int] = 0  # Interval length
        self.market_typeOptional[MarketType] = MarketType  # Market type
        self.operating_dateOptional[DateTime] = DateTime()  # Operating date, hour
        self.out_of_market_typebool = False  # To indicate an out-of-market (OOM) schedule
        self.schedule_typeOptional[EnergyProductType] = EnergyProductType  # Schedule type
        self.wcr_idOptional[str] = ""  # Wheeling Counter-Resource ID (required when Schedule Type=Wheel)
        self.intertieOptional[SchedulingPoint] = SchedulingPoint()
        self.registered_intertieOptional[RegisteredInterTie] = RegisteredInterTie()
        self.interchange_etc_dataOptional[InterchangeETCData] = InterchangeETCData()
