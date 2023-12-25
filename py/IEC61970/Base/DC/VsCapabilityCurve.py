# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:22:57 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Curve import Curve
from typing import Any

class VsCapabilityCurve(Curve):
    """
    The P-Q capability curve for a voltage source converter, with P on x-axis and
    Qmin and Qmax on y1-axis and y2-axis.
    @author T. Kostic
    @version 1.0
    @created 15-Dec-2023 4:38:30 PM
    """
    def __init__(self) -> None:
        super().__init__()
