# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Assets.AssetInfo import AssetInfo
from IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from IEC61970.Base.Domain.Frequency import Frequency
from IEC61970.Base.Domain.Pressure import Pressure
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Base.Domain.Voltage import Voltage
from IEC61970.Base.Domain.Volume import Volume


class SwitchInfo(AssetInfo):

    def __init__(self):
        super().__init__()
        self.breaking_capacity = CurrentFlow()
        self.gas_weight_per_tank = Volume()
        self.is_single_phase = True
        self.is_unganged = True
        self.low_pressure_alarm = Pressure()
        self.low_pressure_lockout = Pressure()
        self.oil_volume_per_tank = Volume()
        self.rated_current = CurrentFlow()
        self.rated_frequency = Frequency()
        self.rated_impulse_withstand_voltage = Voltage()
        self.rated_interrupting_time = Seconds()
        self.rated_voltage = Voltage()
