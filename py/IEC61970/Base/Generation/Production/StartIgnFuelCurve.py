# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from IEC61970.Base.Core.Curve import Curve
from IEC61970.Base.Generation.Production.FuelType import FuelType


class StartIgnFuelCurve(Curve):
    """
    The quantity of ignition fuel (Y-axis) used to restart and repay the auxiliary
    power consumed versus the number of hours (X-axis) the unit was off line.
    @created 02-Jan-2024 10:57:59 PM
    """

    def __init__(self):
        super().__init__()
        # Type of ignition fuel.
        self.ignition_fuel_type = FuelType.GAS  # assuming Fuel_type class has a typical value method
        # end StartIgnFuelCurve
