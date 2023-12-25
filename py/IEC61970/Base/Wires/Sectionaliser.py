# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# Automatic switch that will lock open to isolate a faulted section. It may, or
# may not, have load breaking capability. Its primary purpose is to provide fault
# sectionalising at locations where the fault current is either too high, or too
# low, for proper coordination of fuses.
# @author pmora
# @version 1.0
# @updated 15-Dec-2023 1:39:42 PM
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.Switch import Switch


class Sectionaliser(Switch):

    def __init__(self) -> None:
        super().__init__()

