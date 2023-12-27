# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.AngleRadians import AngleRadians
from IEC61970.Base.Domain.Frequency import Frequency
from IEC61970.Base.Domain.Voltage import Voltage
from IEC61970.Base.Protection.ProtectionEquipment import ProtectionEquipment


class SynchrocheckRelay(ProtectionEquipment):

    def __init__(self):
        super().__init__()
        self.max_angle_diff = AngleRadians()
        self.max_freq_diff = Frequency()
        self.max_volt_diff = Voltage()
