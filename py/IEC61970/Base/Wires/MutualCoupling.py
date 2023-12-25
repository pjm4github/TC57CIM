# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Any

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Length import Length
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Reactance import Reactance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Resistance import Resistance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Susceptance import Susceptance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.NonlinearShuntCompensatorPhasePoint import Conductance


class MutualCoupling:

    """
    This class represents the zero sequence line mutual coupling.
    @author pmora
    @updated 15-Dec-2023 1:39:41 PM
    """

    def __init__(self) -> None:
        """
        Zero sequence mutual coupling shunt (charging) susceptance,
        uniformly distributed, of the entire line section.
        """
        self.b0ch: Susceptance = Susceptance()

        """
        Distance to the start of the coupled region from the first line's terminal
        having sequence number equal to 1.
        """
        self.distance11: Length = Length()

        """
        Distance to the end of the coupled region from the first line's terminal with
        sequence number equal to 1.
        """
        self.distance12: Length = Length()

        """
        Distance to the start of coupled region from the second line's terminal with
        sequence number equal to 1.
        """
        self.distance21: Length = Length()

        """
        Distance to the end of coupled region from the second line's terminal with
        sequence number equal to 1.
        """
        self.distance22: Length = Length()

        """
        Zero sequence mutual coupling shunt (charging) conductance,
        uniformly distributed, of the entire line section.
        """
        self.g0ch: Conductance = Conductance()

        """
        Zero sequence branch-to-branch mutual impedance coupling, resistance.
        """
        self.r0: Resistance = Resistance()

        """
        Zero sequence branch-to-branch mutual impedance coupling, reactance.
        """
        self.x0: Reactance = Reactance()

    def get_b0ch(self) -> Susceptance:
        return self.b0ch

    def get_distance11(self) -> Length:
        return self.distance11

    def get_distance12(self) -> Length:
        return self.distance12

    def get_distance21(self) -> Length:
        return self.distance21

    def get_distance22(self) -> Length:
        return self.distance22

    def get_g0ch(self) -> Conductance:
        return self.g0ch

    def get_r0(self) -> Resistance:
        return self.r0

    def get_x0(self) -> Reactance:
        return self.x0

    def set_b0ch(self, new_val: Susceptance) -> None:
        self.b0ch = new_val

    def set_distance11(self, new_val: Length) -> None:
        self.distance11 = new_val

    def set_distance12(self, new_val: Length) -> None:
        self.distance12 = new_val

    def set_distance21(self, new_val: Length) -> None:
        self.distance21 = new_val

    def set_distance22(self, new_val: Length) -> None:
        self.distance22 = new_val

    def set_g0ch(self, new_val: Conductance) -> None:
        self.g0ch = new_val

    def set_r0(self, new_val: Resistance) -> None:
        self.r0 = new_val

    def set_x0(self, new_val: Reactance) -> None:
        self.x0 = new_val
