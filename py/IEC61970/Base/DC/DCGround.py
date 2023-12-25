from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.DC import DCConductingEquipment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Inductance import Inductance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Resistance import Resistance


class DCGround(DCConductingEquipment):
    """
    A ground within a DC system.

    @author: selaost1
    @version: 1.0
    @created: 15-Dec-2023 4:38:27 PM
    """
    def __init__(self) -> None:
        """
        Default constructor
        """

        self.inductance: Inductance = Inductance()  # Inductance to ground
        self.r: Resistance = Resistance()  # Resistance to ground

