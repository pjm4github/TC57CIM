# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from datetime import datetime
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.ConductingEquipment import ConductingEquipment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.SwitchPhase import SwitchPhase
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.SwitchSchedule import SwitchSchedule


class Switch(ConductingEquipment):
    """
    A generic device designed to close, or open, or both, one or more electric
    circuits.  All switches are two terminal devices including grounding switches.
    @author pmora
    @updated 15-Dec-2023 1:39:42 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.normal_open: bool = False  # The attribute is used in cases when no Measurement for the status value is present...
        self.open: bool = False  # The attribute tells if the switch is considered open when used as input to topology processing.
        self.rated_current: Optional[CurrentFlow] = CurrentFlow()  # The maximum continuous current carrying capacity in amps governed by the device material and construction.
        self.retained: bool = False  # Branch is retained in a bus branch model...
        self.switch_on_count: int = 0  # The switch on count since the switch was last reset or initialized.
        self.switch_on_date: Optional[datetime] = datetime.now()  # The date and time when the switch was last switched on.
        self.switch_phase: Optional[SwitchPhase] = SwitchPhase()  # The individual switch phases for the switch.
        self.switch_schedules: Optional[SwitchSchedule] = SwitchSchedule()  # A Switch can be associated with SwitchSchedules.

    def get_normal_open(self) -> bool:
        return self.normal_open

    def get_open(self) -> bool:
        return self.open

    def get_rated_current(self) -> Optional[CurrentFlow]:
        return self.rated_current

    def get_retained(self) -> bool:
        return self.retained

    def get_switch_on_count(self) -> int:
        return self.switch_on_count

    def get_switch_on_date(self) -> Optional[datetime]:
        return self.switch_on_date

    def get_switch_phase(self) -> Optional[SwitchPhase]:
        return self.switch_phase

    def get_switch_schedules(self) -> Optional[SwitchSchedule]:
        return self.switch_schedules

    def set_normal_open(self, new_val: bool) -> None:
        self.normal_open = new_val

    def set_open(self, new_val: bool) -> None:
        self.open = new_val

    def set_rated_current(self, new_val: CurrentFlow) -> None:
        self.rated_current = new_val

    def set_retained(self, new_val: bool) -> None:
        self.retained = new_val

    def set_switch_on_count(self, new_val: int) -> None:
        self.switch_on_count = new_val

    def set_switch_on_date(self, new_val: datetime) -> None:
        self.switch_on_date = new_val

    def set_switch_phase(self, new_val: SwitchPhase) -> None:
        self.switch_phase = new_val

    def set_switch_schedules(self, new_val: SwitchSchedule) -> None:
        self.switch_schedules = new_val
