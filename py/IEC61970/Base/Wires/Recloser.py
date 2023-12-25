# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# Pole-mounted fault interrupter with built-in phase and ground relays, current
# transformer (CT), and supplemental controls.
# @author pmora
# @version 1.0
# @updated 15-Dec-2023 1:39:42 PM
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.ProtectedSwitch import ProtectedSwitch


class Recloser(ProtectedSwitch):

    def __init__(self) -> None:
        super().__init__()
