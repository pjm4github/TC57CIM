

# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:22:57 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.DC import DCConductingEquipment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Capacitance import Capacitance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Resistance import Resistance


class DcShunt(DCConductingEquipment):
    """
    /**
     * A shunt device within the DC system, typically used for filtering. Needed for
     * transient and short circuit studies.
     *
     * @author selaost1
     * @version 1.0
     * @created 15-Dec-2023 4:38:27 PM
     */
    """
    def __init__(self) -> None:
        super().__init__()
        self.capacitance: Capacitance = Capacitance()
        self.resistance: Resistance = Resistance()

