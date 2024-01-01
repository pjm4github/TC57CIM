# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from datetime import datetime
from typing import Optional, Union

from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketCommon.RegisteredResource import RegisteredResource


class DotInstruction:

    def __init__(self) -> None:
        self.actual_ramp_rateOptional[float] = 0.0
        self.compliant_indicator: str = ""
        self.dotOptional[float] = 0.0
        self.economic_max_overrideOptional[float] = 0.0
        self.expected_energyOptional[float] = 0.0
        self.generator_performance_degreeOptional[float] = 0.0
        self.hour_ahead_sched_energyOptional[float] = 0.0
        self.hourly_scheduleOptional[float] = 0.0
        self.instruction_time: DateTime = DateTime()
        self.maximum_emergency_ind: bool
        self.meter_load_followingOptional[float] = 0.0
        self.non_ramp_restricted_mwOptional[float] = 0.0
        self.non_spin_reserveOptional[float] = 0.0
        self.previous_dot_time_stamp: DateTime = DateTime()
        self.ramp_rate_limitOptional[float] = 0.0
        self.regulation_status: str = ""
        self.spin_reserveOptional[float] = 0.0
        self.standard_ramp_energyOptional[float] = 0.0
        self.supplemental_energyOptional[float] = 0.0
        self.unit_statusOptional[int] = int()
        self.registered_resourceOptional[RegisteredResource] = RegisteredResource()
