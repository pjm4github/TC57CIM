# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import List

from gov_pnnl_goss.cimhub.dto.Switch import Switch


class CompositeSwitch:
    """
    A model of a set of individual Switches normally enclosed within the same
    cabinet and possibly with interlocks that restrict the combination of switch
    positions. These are typically found in medium voltage distribution networks.
    A CompositeSwitch could represent a Ring-Main-Unit (RMU), or pad-mounted
    switchgear, with primitive internal devices such as an internal bus-bar plus 3
    or 4 internal switches each of which may individually be open or closed. A
    CompositeSwitch and a set of contained Switches can also be used to represent a
    multi-position switch e.g. a switch that can connect a circuit to Ground, Open
    or Busbar.
    """

    def __init__(self) -> None:
        self.composite_switch_type: str = ""
        self.switches: List[Switch] = [Switch()]

    def get_composite_switch_type(self) -> str:
        return self.composite_switch_type

    def get_switches(self) -> List[Switch]:
        return self.switches

    def set_composite_switch_type(self, new_val: str) -> None:
        self.composite_switch_type = new_val

    def set_switches(self, new_val: Switch) -> None:
        self.switches = new_val
