# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:35:24 2023
from typing import Any

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Reactance import Reactance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Resistance import Resistance


# Impedance description for the fault.
# @author kdemaree
# @version 1.0
# @created 15-Dec-2023 4:38:27 PM
class FaultImpedance:

    def __init__(self) -> None:
        # The resistance of the fault between phases and ground.
        self.r_ground: Resistance = Resistance()

        # The resistance of the fault between phases.
        self.r_line_to_line: Resistance = Resistance()

        # The reactance of the fault between phases and ground.
        self.x_ground: Reactance = Reactance()

        # The reactance of the fault between phases.
        self.x_line_to_line: Reactance = Reactance()

