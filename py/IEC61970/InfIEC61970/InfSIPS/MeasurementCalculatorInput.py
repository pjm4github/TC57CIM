# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Mon Jan  8 09:17:12 2024
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Meas.Measurement import Measurement


class MeasurementCalculatorInput(IdentifiedObject):
    """
    Input to measurement calculation. Support Analog, Discrete and Accumulator.
    @author sveinols
    @version 1.0
    @created 25-Dec-2023 8:32:00 PM
    """

    def __init__(self):
        super().__init__()
        # If true, use the absolute value for the calculation.
        self.absolute_value = True
        # Positive number that defines the order of the operant in the calculation. 0 = default.
        self.order = 0  # The order is not relevant (e.g. summation).
        self.measurement = Measurement()
