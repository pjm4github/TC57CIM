# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:35:24 2023
from typing import Any, Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Terminal import Terminal
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Faults.Fault import Fault


class EquipmentFault(Fault):
    """
    A fault applied at the terminal, external to the equipment. This class is not
    used to specify faults internal to the equipment.
    @author kdemaree
    @version 1.0
    @created 15-Dec-2023 4:38:27 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.terminal: Optional[Terminal] = Terminal()
