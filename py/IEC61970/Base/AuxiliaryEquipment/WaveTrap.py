# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:00:47 2023
from typing import Any
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.AuxiliaryEquipment import AuxiliaryEquipment


class WaveTrap(AuxiliaryEquipment):
    """
    Line traps are devices that impede high frequency power line carrier signals
    yet present a negligible impedance at the main power frequency.
    @author kdemaree
    @version 1.0
    @created 15-Dec-2023 4:38:30 PM
    """

    def __init__(self) -> None:
        super().__init__()
