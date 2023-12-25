from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.ConductingEquipment import ConductingEquipment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Length import Length


class Connector(ConductingEquipment):
    """A conductor, or group of conductors, with negligible impedance, that serve to
    connect other conducting equipment within a single substation and are modelled
    with a single logical terminal.
    """
    def __init__(self) -> None:
        super().__init__()
        self.length = Length()

