# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ApparentPower import ApparentPower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Reactance import Reactance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ReactivePower import ReactivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Resistance import Resistance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Generation.Production.PowerElectronicsUnit import PowerElectronicsUnit
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.RegulatingCondEq import RegulatingCondEq


class PowerElectronicsConnection(RegulatingCondEq):

    def __init__(self) -> None:
        """A connection to the AC network for energy production or consumption
        that uses power electronics rather than rotating machines.
        """
        super().__init__()
        self.max_q: Optional[ReactivePower] = ReactivePower()  # Maximum reactive power limit
        self.min_q: Optional[ReactivePower] = ReactivePower()  # Minimum reactive power limit
        self.p: Optional[ActivePower] = None  # Active power injection
        self.q: Optional[ReactivePower] = ReactivePower()  # Reactive power injection
        self.r: Optional[Resistance] = Resistance()  # Equivalent resistance of generator
        self.r0: Optional[Resistance] = Resistance()  # Zero sequence resistance of the synchronous machine
        self.rated_s: Optional[ApparentPower] = None  # Nameplate apparent power rating for the unit
        self.rated_u: Optional[Voltage] = None  # Rated voltage
        self.rn: Optional[Resistance] = Resistance()  # Negative sequence Thevenin resistance
        self.x: Optional[Reactance] = Reactance()  # Positive sequence Thevenin reactance
        self.x0: Optional[Reactance] = Reactance()  # Zero sequence Thevenin reactance
        self.xn: Optional[Reactance] = Reactance()  # Negative sequence Thevenin reactance
        self.power_electronics_unit = PowerElectronicsUnit()

    def get_max_q(self) -> Optional[ReactivePower]:
        return self.max_q

    def get_min_q(self) -> Optional[ReactivePower]:
        return self.min_q

    def get_p(self) -> Optional[ActivePower]:
        return self.p

    def get_power_electronics_unit(self) -> Optional[
        PowerElectronicsUnit]:  # Assuming PowerElectronicsUnit is an existing class
        return self.power_electronics_unit

    def get_q(self) -> Optional[ReactivePower]:
        return self.q

    def get_r(self) -> Optional[Resistance]:
        return self.r

    def get_r0(self) -> Optional[Resistance]:
        return self.r0

    def get_rated_s(self) -> Optional[ApparentPower]:
        return self.rated_s

    def get_rated_u(self) -> Optional[Voltage]:
        return self.rated_u

    def get_rn(self) -> Optional[Resistance]:
        return self.rn

    def get_x(self) -> Optional[Reactance]:
        return self.x

    def get_x0(self) -> Optional[Reactance]:
        return self.x0

    def get_xn(self) -> Optional[Reactance]:
        return self.xn

    def set_max_q(self, new_val: ReactivePower) -> None:
        self.max_q = new_val

    def set_min_q(self, new_val: ReactivePower) -> None:
        self.min_q = new_val

    def set_p(self, new_val: ActivePower) -> None:
        self.p = new_val

    def set_power_electronics_unit(self,
                                   new_val: PowerElectronicsUnit) -> None:  # Assuming PowerElectronicsUnit is an existing class
        self.power_electronics_unit = new_val

    def set_q(self, new_val: ReactivePower) -> None:
        self.q = new_val

    def set_r(self, new_val: Resistance) -> None:
        self.r = new_val

    def set_r0(self, new_val: Resistance) -> None:
        self.r0 = new_val

    def set_rated_s(self, new_val: ApparentPower) -> None:
        self.rated_s = new_val

    def set_rated_u(self, new_val: Voltage) -> None:
        self.rated_u = new_val

    def set_rn(self, new_val: Resistance) -> None:
        self.rn = new_val

    def set_x(self, new_val: Reactance) -> None:
        self.x = new_val

    def set_x0(self, new_val: Reactance) -> None:
        self.x0 = new_val

    def set_xn(self, new_val: Reactance) -> None:
        self.xn = new_val
