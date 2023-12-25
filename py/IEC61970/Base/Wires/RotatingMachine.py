# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ApparentPower import ApparentPower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ReactivePower import ReactivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Generation.Production.HydroPump import HydroPump
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.RegulatingCondEq import RegulatingCondEq


class RotatingMachine(RegulatingCondEq):
    """
    A rotating machine which may be used as a generator or motor.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:42 PM
    """

    def __init__(self) -> None:
        """
        Constructor for RotatingMachine class.
        """
        super().__init__()
        self.p: ActivePower = ActivePower()
        self.q: ReactivePower = ReactivePower()
        self.rated_power_factor: float = 1.0
        self.rated_s: ApparentPower = ApparentPower()
        self.rated_u: Voltage = Voltage()
        self.hydro_pump: HydroPump = HydroPump()

    def get_hydro_pump(self) -> HydroPump:
        return self.hydro_pump

    def get_p(self) -> ActivePower:
        return self.p

    def get_q(self) -> ReactivePower:
        return self.q

    def get_rated_power_factor(self) -> float:
        return self.rated_power_factor

    def get_rated_s(self) -> ApparentPower:
        return self.rated_s

    def get_rated_u(self) -> Voltage:
        return self.rated_u

    def set_hydro_pump(self, new_val: HydroPump) -> None:
        self.hydro_pump = new_val

    def set_p(self, new_val: ActivePower) -> None:
        self.p = new_val

    def set_q(self, new_val: ReactivePower) -> None:
        self.q = new_val

    def set_rated_power_factor(self, new_val: float) -> None:
        self.rated_power_factor = new_val

    def set_rated_s(self, new_val: ApparentPower) -> None:
        self.rated_s = new_val

    def set_rated_u(self, new_val: Voltage) -> None:
        self.rated_u = new_val
