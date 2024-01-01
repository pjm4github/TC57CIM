# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 12:50:20 2023

from typing import Optional

from IEC61970.Base.Core.BasicIntervalSchedule import BasicIntervalSchedule
from IEC62325.MarketOperations.MarketOpCommon.MktMeasurement import MktMeasurement
from IEC62325.MarketOperations.ReferenceData.SubControlArea import SubControlArea


class DynamicSchedule(BasicIntervalSchedule):

    def __init__(self) -> None:
        super().__init__()
        self.dyn_sched_sign_revOptional[bool] = False  # Dynamic schedule sign reversal required (true/false)
        self.dyn_sched_statusOptional[str] = ""  # The "active" or "inactive" status of the dynamic schedule
        self.send_sub_control_areaOptional[SubControlArea] = SubControlArea()  # A control area can send dynamic schedules to other control areas
        self.receive_sub_control_areaOptional[SubControlArea] = SubControlArea()  # A control area can receive dynamic schedules from other control areas
        self.mkt_measurementOptional[MktMeasurement] = MktMeasurement()
