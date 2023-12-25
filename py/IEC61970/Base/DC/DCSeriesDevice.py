# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:22:57 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.DC.DCConductingEquipment import DCConductingEquipment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Inductance import Inductance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Resistance import Resistance


class DCSeriesDevice(DCConductingEquipment):

    def __init__(self) -> None:
        super().__init__()
        self.inductance: Inductance = Inductance()
        self.resistance: Resistance = Resistance()
