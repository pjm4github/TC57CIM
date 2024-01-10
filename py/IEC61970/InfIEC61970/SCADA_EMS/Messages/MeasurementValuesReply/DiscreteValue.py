# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Mon Jan  8 09:07:27 2024
from IEC61970.Base.Meas.MeasurementValue import MeasurementValue


# The value to supervise.
class DiscreteValue(MeasurementValue):
    """
    @author selaost1
    @version 1.0
    @created 25-Dec-2023 8:31:56 PM
    """
    def __init__(self):
        super().__init__()
        self.value = 0  # The value to supervise.
