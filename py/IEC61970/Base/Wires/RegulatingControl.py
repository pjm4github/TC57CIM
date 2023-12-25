# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import Enum
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.PhaseCode import PhaseCode
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.RegulatingControlModeKind import RegulatingControlModeKind


class RegulatingControl:
    """
    Specifies a set of equipment that works together to control a power system
    quantity such as voltage or flow.
    Remote bus voltage control is possible by specifying the controlled terminal
    located at some place remote from the controlling equipment.
    In case multiple equipment, possibly of different types, control same terminal
    there must be only one RegulatingControl at that terminal. The most specific
    subtype of RegulatingControl shall be used in case such equipment participate
    in the control, e.g. TapChangerControl for tap changers.
    For flow control  load sign convention is used, i.e. positive sign means flow
    out from a TopologicalNode (bus) into the conducting equipment.
    """

    def __init__(self):
        self.discrete: bool = False  # The regulation is performed in a discrete mode.
        self.enabled: bool = False  # The flag tells if regulation is enabled.
        self.mode: RegulatingControlModeKind = RegulatingControlModeKind.VOLTAGE
        # The regulating control mode presently available.  This specification allows for
        # determining the kind of regulation without need for obtaining the units from a schedule.
        self.monitored_phase: Optional[PhaseCode] = PhaseCode.A
        # Phase voltage controlling this regulator, measured at regulator location.
        self.target_deadband: float = 0.0
        # This is a deadband used with discrete control to avoid excessive update of
        # controls like tap changers and shunt compensator banks while regulating.
        # The units of those appropriate for the mode.
        self.target_value: float = 0.0
        # The target value specified for case input.  This value can be used for the
        # target value without the use of schedules. The value has the units appropriate
        # to the mode attribute.
        self.target_value_unit_multiplier: Optional[UnitMultiplier] = UnitMultiplier.none
        # Specify the multiplier for used for the targetValue.

    def get_discrete(self) -> bool:
        return self.discrete

    def get_enabled(self) -> bool:
        return self.enabled

    def get_mode(self) -> Optional[RegulatingControlModeKind]:
        return self.mode

    def get_monitored_phase(self) -> Optional[PhaseCode]:
        return self.monitored_phase

    def get_target_deadband(self) -> float:
        return self.target_deadband

    def get_target_value(self) -> float:
        return self.target_value

    def get_target_value_unit_multiplier(self) -> Optional[UnitMultiplier]:
        return self.target_value_unit_multiplier

    def set_discrete(self, new_val: bool):
        self.discrete = new_val

    def set_enabled(self, new_val: bool):
        self.enabled = new_val

    def set_mode(self, new_val: RegulatingControlModeKind):
        self.mode = new_val

    def set_monitored_phase(self, new_val: Optional[PhaseCode]):
        self.monitored_phase = new_val

    def set_target_deadband(self, new_val: float):
        self.target_deadband = new_val

    def set_target_value(self, new_val: float):
        self.target_value = new_val

    def set_target_value_unit_multiplier(self, new_val: Optional[UnitMultiplier]):
        self.target_value_unit_multiplier = new_val
