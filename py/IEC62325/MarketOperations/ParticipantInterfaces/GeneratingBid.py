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
        self.combined_cycle_unit_offerOptional[str] = ""
        self.down_time_maxOptional[float] = 0.0
        self.installed_capacityOptional[float] = 0.0
        self.lower_ramp_rateOptional[ActivePowerChangeRate] = ActivePowerChangeRate()
        self.max_emergency_mwOptional[ActivePower] = ActivePower()
        self.maximum_economic_mwOptional[float] = 0.0
        self.min_emergency_mwOptional[ActivePower] = ActivePower()
        self.minimum_economic_mwOptional[float] = 0.0
        self.no_load_costOptional[float] = 0.0
        self.notification_timeOptional[float] = 0.0
        self.operating_modeOptional[str] = ""
        self.raise_ramp_rateOptional[ActivePowerChangeRate] = ActivePowerChangeRate()
        self.ramp_curve_typeOptional[int] = 0
        self.startup_costOptional[float] = 0.0
        self.start_up_ramp_rateOptional[ActivePowerChangeRate] = ActivePowerChangeRate()
        self.start_up_typeOptional[int] = 0
        self.up_time_maxOptional[float] = 0.0
        self.notification_time_curveOptional[NotificationTimeCurve] = NotificationTimeCurve()
        self.ramp_rate_curveOptional[RampRateCurve] = RampRateCurve()
        self.security_constraintsOptional[SecurityConstraints] = SecurityConstraints()
