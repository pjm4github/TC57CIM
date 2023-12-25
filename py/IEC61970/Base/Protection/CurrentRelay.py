# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Seconds import Seconds
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Protection.ProtectionEquipment import ProtectionEquipment


class CurrentRelay(ProtectionEquipment):
    def __init__(self):
        super().__init__()
        self.current_limit1 = CurrentFlow()  # * Current limit number one 1 for inverse time pickup.
        self.current_limit2 = CurrentFlow()  # * Current limit number 2 for inverse time pickup.
        self.current_limit3 = CurrentFlow()  # * Current limit number 3 for inverse time pickup.
        self.inverse_time_flag = False  # * Set true if the current relay has inverse time characteristic.
        self.time_delay1 = Seconds()  # * Inverse time delay number 1 for current limit number 1.
        self.time_delay2 = Seconds()  # * Inverse time delay number 2 for current limit number 2.
        self.time_delay3 = Seconds()  # * Inverse time delay number 3 for current limit number 3.

