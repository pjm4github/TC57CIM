# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:03:56 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.EquipmentContainer import EquipmentContainer
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Substation import Substation
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Terminal import Terminal


class Feeder(EquipmentContainer):
    """
    A collection of equipment for organizational purposes, used for grouping
    distribution resources. The organization a feeder does not necessarily
    reflect connectivity or current operation state.
    """

    def __init__(self) -> None:
        super().__init__()
        self.naming_secondary_substation = Substation()  # The secondary substations that are normally energized from the feeder. Used for naming purposes.
        self.normal_head_terminal = Terminal()  # The normal head terminal or terminals of the feeder.
        self.normal_energized_substation = Substation()  # The substations that are normally energized by the feeder.



