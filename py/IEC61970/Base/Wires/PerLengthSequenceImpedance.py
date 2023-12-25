# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ConductancePerLength import ConductancePerLength
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ReactancePerLength import ReactancePerLength
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ResistancePerLength import ResistancePerLength
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.SusceptancePerLength import SusceptancePerLength
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.PerLengthImpedance import PerLengthImpedance


class PerLengthSequenceImpedance(PerLengthImpedance):
    """
    Sequence impedance and admittance parameters per unit length, for transposed
    lines of 1, 2, or 3 phases. For 1-phase lines, define x=x0=xself. For 2-phase
    lines, define x=xs-xm and x0=xs+xm.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:41 PM
    """

    def __init__(self):
        super().__init__()
        self.b0ch: SusceptancePerLength = SusceptancePerLength()
        self.bch: SusceptancePerLength = SusceptancePerLength()
        self.g0ch: ConductancePerLength = ConductancePerLength()
        self.gch: ConductancePerLength = ConductancePerLength()
        self.r: ResistancePerLength = ResistancePerLength()
        self.r0: ResistancePerLength = ResistancePerLength()
        self.x: ReactancePerLength = ReactancePerLength()
        self.x0: ReactancePerLength = ReactancePerLength()

    def get_b0ch(self) -> SusceptancePerLength:
        return self.b0ch

    def get_bch(self) -> SusceptancePerLength:
        return self.bch

    def get_g0ch(self) -> ConductancePerLength:
        return self.g0ch

    def get_gch(self) -> ConductancePerLength:
        return self.gch

    def get_r(self) -> ResistancePerLength:
        return self.r

    def get_r0(self) -> ResistancePerLength:
        return self.r0

    def get_x(self) -> ReactancePerLength:
        return self.x

    def get_x0(self) -> ReactancePerLength:
        return self.x0

    def set_b0ch(self, new_val: SusceptancePerLength) -> None:
        self.b0ch = new_val

    def set_bch(self, new_val: SusceptancePerLength) -> None:
        self.bch = new_val

    def set_g0ch(self, new_val: ConductancePerLength) -> None:
        self.g0ch = new_val

    def set_gch(self, new_val: ConductancePerLength) -> None:
        self.gch = new_val

    def set_r(self, new_val: ResistancePerLength) -> None:
        self.r = new_val

    def set_r0(self, new_val: ResistancePerLength) -> None:
        self.r0 = new_val

    def set_x(self, new_val: ReactancePerLength) -> None:
        self.x = new_val

    def set_x0(self, new_val: ReactancePerLength) -> None:
        self.x0 = new_val
