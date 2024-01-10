# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from IEC61970.Base.Core.Curve import Curve
from IEC61970.Base.Generation.Production.FuelType import FuelType


class StartMainFuelCurve(Curve):
    """
    The quantity of main fuel (Y-axis) used to restart and repay the auxiliary
    power consumed versus the number of hours (X-axis) the unit was off line.
    @created 02-Jan-2024 10:58:13 PM
    """

    def __init__(self):
        super().__init__()
        self.main_fuel_type = FuelType.GASOLINE  # Type of main fuel.

