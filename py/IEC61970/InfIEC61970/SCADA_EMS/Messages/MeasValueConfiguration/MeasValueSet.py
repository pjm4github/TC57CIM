# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Mon Jan  8 09:08:40 2024
# Class for measurement value set
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.Meas.MeasurementValue import MeasurementValue


class MeasValueSet(IdentifiedObject):
    """
    @author selaost1
    @version 1.0
    @created 25-Dec-2023 8:32:00 PM
    """

    def __init__(self):
        super().__init__()
        self.analog_value_deadband = PerCent()  # Percentage
        self.report_discrete_on_change = True  # Boolean
        self.measurement_value = MeasurementValue()  # Measurement value
