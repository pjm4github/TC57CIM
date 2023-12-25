# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.BaseVoltage import BaseVoltage
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Terminal import Terminal
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Reactance import Reactance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Resistance import Resistance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.PhaseTapChanger import PhaseTapChanger
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.RatioTapChanger import RatioTapChanger
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.TransformerStarImpedance import TransformerStarImpedance


class TransformerEnd:
    """
    A conducting connection point of a power transformer. It corresponds to a physical transformer winding terminal.
    In earlier CIM versions, the TransformerWinding class served a similar purpose, but this class is more flexible because
    it associates to terminal but is not a specialization of ConductingEquipment.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:42 PM
    """

    def __init__(self) -> None:
        self.bmag_sat: Optional[BaseVoltage] = BaseVoltage()  # Core shunt magnetizing susceptance in the saturation region
        self.end_number: Optional[int] = 0  # Number for this transformer end, corresponding to the end's order in the power transformer vector group or phase angle clock number.
        # Highest voltage winding should be 1. Each end within a power transformer should have a unique subsequent end number.
        # Note the transformer end number need not match the terminal sequence number.
        self.grounded: Optional[bool] = False  # (for Yn and Zn connections) True if the neutral is solidly grounded
        self.mag_base_u: Optional[float] = 0.0  # The reference voltage at which the magnetizing saturation measurements were made
        self.mag_sat_flux: Optional[float] = 0.0  # Core magnetizing saturation curve knee flux level
        self.r_ground: Optional[Resistance] = Resistance() # (for Yn and Zn connections) Resistance part of neutral impedance where 'grounded' is true
        self.x_ground: Optional[Reactance] = Reactance()  # (for Yn and Zn connections) Reactive part of neutral impedance where 'grounded' is true
        self.phase_tap_changer: Optional[PhaseTapChanger] = PhaseTapChanger()  # Phase tap changer associated with this transformer end
        self.ratio_tap_changer: Optional[RatioTapChanger] = RatioTapChanger()  # Ratio tap changer associated with this transformer end
        self.star_impedance: Optional[TransformerStarImpedance] = TransformerStarImpedance()  # (accurate for 2- or 3-winding transformers only) Pi-model impedances of this transformer end.
        # By convention, for a two winding transformer, the full values of the transformer should be entered on the high voltage end (endNumber=1).
        self.terminal: Optional[Terminal] = Terminal()  # The terminal associated with the transformer end

    def get_base_voltage(self) -> Optional[BaseVoltage]:
        return self.bmag_sat

    def get_bmag_sat(self) -> Optional[float]:
        return self.bmag_sat

    def get_end_number(self) -> Optional[int]:
        return self.end_number

    def get_grounded(self) -> Optional[bool]:
        return self.grounded

    def get_mag_base_u(self) -> Optional[float]:
        return self.mag_base_u

    def get_mag_sat_flux(self) -> Optional[float]:
        return self.mag_sat_flux

    def get_phase_tap_changer(self) -> Optional[PhaseTapChanger]:
        return self.phase_tap_changer

    def get_ratio_tap_changer(self) -> Optional[RatioTapChanger]:
        return self.ratio_tap_changer

    def get_r_ground(self) -> Optional[float]:
        return self.r_ground

    def get_star_impedance(self) -> Optional[object]:
        return self.star_impedance

    def get_terminal(self) -> Optional[object]:
        return self.terminal

    def get_x_ground(self) -> Optional[float]:
        return self.x_ground

    def set_base_voltage(self, new_val: BaseVoltage) -> None:
        self.bmag_sat = new_val

    def set_bmag_sat(self, new_val: float) -> None:
        self.bmag_sat = new_val

    def set_end_number(self, new_val: int) -> None:
        self.end_number = new_val

    def set_grounded(self, new_val: bool) -> None:
        self.grounded = new_val

    def set_mag_base_u(self, new_val: float) -> None:
        self.mag_base_u = new_val

    def set_mag_sat_flux(self, new_val: float) -> None:
        self.mag_sat_flux = new_val

    def set_phase_tap_changer(self, new_val: PhaseTapChanger) -> None:
        self.phase_tap_changer = new_val

    def set_ratio_tap_changer(self, new_val: RatioTapChanger) -> None:
        self.ratio_tap_changer = new_val

    def set_r_ground(self, new_val: float) -> None:
        self.r_ground = new_val

    def set_star_impedance(self, new_val: TransformerStarImpedance) -> None:
        self.star_impedance = new_val

    def set_terminal(self, new_val: Terminal) -> None:
        self.terminal = new_val

    def set_x_ground(self, new_val: float) -> None:
        self.x_ground = new_val
