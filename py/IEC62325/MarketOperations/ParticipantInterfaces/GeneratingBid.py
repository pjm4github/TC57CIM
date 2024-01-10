# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from typing import Optional

from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.ActivePowerChangeRate import ActivePowerChangeRate
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.SecurityConstraints import SecurityConstraints
from IEC62325.MarketOperations.ParticipantInterfaces.NotificationTimeCurve import NotificationTimeCurve
from IEC62325.MarketOperations.ParticipantInterfaces.RampRateCurve import RampRateCurve
from IEC62325.MarketOperations.ParticipantInterfaces.ResourceBid import ResourceBid


class GeneratingBid(ResourceBid):
    def __init__(self) -> None:
        super().__init__()
        self.combined_cycle_unit_offer: Optional[str] = ""
        self.down_time_max: float = 0.0
        self.installed_capacity: float = 0.0
        self.lower_ramp_rate: Optional[ActivePowerChangeRate] = ActivePowerChangeRate()
        self.max_emergency_mw: Optional[ActivePower] = ActivePower()
        self.maximum_economic_mw: float = 0.0
        self.min_emergency_mw: Optional[ActivePower] = ActivePower()
        self.minimum_economic_mw: float = 0.0
        self.no_load_cost: float = 0.0
        self.notification_timefloat = 0.0
        self.operating_mode: Optional[str] = ""
        self.raise_ramp_rate: Optional[ActivePowerChangeRate] = ActivePowerChangeRate()
        self.ramp_curve_type: Optional[int] = 0
        self.startup_costfloat = 0.0
        self.start_up_ramp_rate: Optional[ActivePowerChangeRate] = ActivePowerChangeRate()
        self.start_up_type: Optional[int] = 0
        self.up_time_maxfloat = 0.0
        self.notification_time_curve: Optional[NotificationTimeCurve] = NotificationTimeCurve()
        self.ramp_rate_curve: Optional[RampRateCurve] = RampRateCurve()
        self.security_constraints: Optional[SecurityConstraints] = SecurityConstraints()
