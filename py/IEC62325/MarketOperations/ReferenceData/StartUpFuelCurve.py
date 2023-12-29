# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from typing import List

from IEC61970.Base.Core.Curve import Curve


class StartUpFuelCurve(Curve):
    """
    * The fuel consumption of a Generating Resource to complete a Start-Up.(x=cooling
    * time) Form Startup Fuel Curve. xAxisData -> cooling time, y1AxisData -> MBtu.
    * @created 28-Dec-2023 12:23:50 PM
    """
    def __init__(self) -> None:
        super().__init__()

