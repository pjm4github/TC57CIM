# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Frequency import Frequency
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.RegulatingCondEq import RegulatingCondEq


class FrequencyConverter(RegulatingCondEq):

    def __init__(self):
        super().__init__()
        self.frequency: Frequency = Frequency()
        self.max_p: ActivePower = ActivePower()
        self.max_u: Voltage = Voltage()
        self.min_p: ActivePower = ActivePower()
        self.min_u: Voltage = Voltage()

    def get_frequency(self) -> Frequency:
        return self.frequency

    def get_max_p(self) -> ActivePower:
        return self.max_p

    def get_max_u(self) -> Voltage:
        return self.max_u

    def get_min_p(self) -> ActivePower:
        return self.min_p

    def get_min_u(self) -> Voltage:
        return self.min_u

    def set_frequency(self, new_val: Frequency) -> None:
        self.frequency = new_val

    def set_max_p(self, new_val: ActivePower) -> None:
        self.max_p = new_val

    def set_max_u(self, new_val: Voltage) -> None:
        self.max_u = new_val

    def set_min_p(self, new_val: ActivePower) -> None:
        self.min_p = new_val

    def set_min_u(self, new_val: Voltage) -> None:
        self.min_u = new_val
