# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:22:57 2023
from typing import Any

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Equipment import Equipment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.DC.DCTerminal import DCTerminal
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage


class DCConductingEquipment(Equipment):
    """
    The parts of the DC power system that are designed to carry current or that are
    conductively connected through DC terminals.
    """

    def __init__(self) -> None:
        super().__init__()
        self.rated_udc: Voltage = Voltage()
        self.dc_terminals: DCTerminal = DCTerminal()
