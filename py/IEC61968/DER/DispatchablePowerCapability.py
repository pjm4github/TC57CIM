# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ApparentPower import ApparentPower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ReactivePower import ReactivePower


class DispatchablePowerCapability:
    
    def __init__(self):
        self.current_active_power = ActivePower()
        self.current_apparent_power = ApparentPower()
        self.current_reactive_power = ReactivePower()
        self.max_active_power = ActivePower()
        self.max_apparent_power = ApparentPower()
        self.max_reactive_power = ReactivePower()
        self.min_active_power = ActivePower()
        self.min_apparent_power = ApparentPower()
        self.min_reactive_power = ReactivePower()
