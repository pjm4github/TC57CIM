from IEC61970.Base.Core.Bay import Bay
from IEC61970.Base.Core.Terminal import Terminal
from IEC61970.Base.Wires.Line import Line


class Circuit(Line):
    """
    @author selaost1
    @version 1.0
    @created 02-Jan-2024 9:13:40 PM
    """
    def __init__(self):
        super().__init__()
        self.end_bay = Bay()  # End bay of the circuit.
        self.end_terminal = Terminal()  # End terminal of the circuit.

