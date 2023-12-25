# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ApparentPower import ApparentPower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Conductance import Conductance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Reactance import Reactance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Resistance import Resistance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Susceptance import Susceptance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.TransformerEnd import TransformerEnd
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.WindingConnection import WindingConnection


class PowerTransformerEnd(TransformerEnd):

    def __init__(self):
        super().__init__()
        self.b: Optional[Susceptance] = Susceptance()  # Magnetizing branch susceptance (B mag)
        self.b0: Optional[Susceptance] = Susceptance()  # Zero sequence magnetizing branch susceptance
        self.connection_kind: Optional[WindingConnection] = WindingConnection.D  # Kind of connection
        self.g: Optional[Conductance] = Conductance()  # Magnetizing branch conductance
        self.g0: Optional[Conductance] = Conductance()  # Zero sequence magnetizing branch conductance (star-model)
        self.phase_angle_clock: int = 0  # Terminal voltage phase angle displacement
        self.r: Optional[Resistance] = Resistance()  # Resistance (star-model) of the transformer end
        self.r0: Optional[Resistance] = Resistance()  # Zero sequence series resistance (star-model) of the transformer end
        self.rated_s: Optional[ApparentPower] = ApparentPower()  # Normal apparent power rating
        self.rated_u: Optional[Voltage] = Voltage()  # Rated voltage
        self.x: Optional[Reactance] = Reactance()  # Positive sequence series reactance (star-model) of the transformer end
        self.x0: Optional[Reactance] = Reactance()  # Zero sequence series reactance of the transformer end

    def set_b(self, new_val: Susceptance) -> None:
        self.b = new_val

    def set_b0(self, new_val: Susceptance) -> None:
        self.b0 = new_val

    def set_connection_kind(self, new_val: WindingConnection) -> None:
        self.connection_kind = new_val

    def set_g(self, new_val: Conductance) -> None:
        self.g = new_val

    def set_g0(self, new_val: Conductance) -> None:
        self.g0 = new_val

    def set_phase_angle_clock(self, new_val: int) -> None:
        self.phase_angle_clock = new_val

    def set_r(self, new_val: Resistance) -> None:
        self.r = new_val

    def set_r0(self, new_val: Resistance) -> None:
        self.r0 = new_val

    def set_rated_s(self, new_val: ApparentPower) -> None:
        self.rated_s = new_val

    def set_rated_u(self, new_val: Voltage) -> None:
        self.rated_u = new_val

    def set_x(self, new_val: Reactance) -> None:
        self.x = new_val

    def set_x0(self, new_val: Reactance) -> None:
        self.x0 = new_val

    def get_b(self) -> Optional[Susceptance]:
        return self.b

    def get_b0(self) -> Optional[Susceptance]:
        return self.b0

    def get_connection_kind(self) -> Optional[WindingConnection]:
        return self.connection_kind

    def get_g(self) -> Optional[Conductance]:
        return self.g

    def get_g0(self) -> Optional[Conductance]:
        return self.g0

    def get_phase_angle_clock(self) -> int:
        return self.phase_angle_clock

    def get_r(self) -> Optional[Resistance]:
        return self.r

    def get_r0(self) -> Optional[Resistance]:
        return self.r0

    def get_rated_s(self) -> Optional[ApparentPower]:
        return self.rated_s

    def get_rated_u(self) -> Optional[Voltage]:
        return self.rated_u

    def get_x(self) -> Optional[Reactance]:
        return self.x

    def get_x0(self) -> Optional[Reactance]:
        return self.x0
