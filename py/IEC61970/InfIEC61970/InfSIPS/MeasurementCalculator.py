# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Mon Jan  8 09:17:12 2024
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.InfIEC61970.InfSIPS.CalculationKind import CalculationKind
from IEC61970.InfIEC61970.InfSIPS.MeasurementCalculatorInput import MeasurementCalculatorInput
from IEC61970.InfIEC61970.InfSIPS.PinMeasurement import PinMeasurement


class MeasurementCalculator(IdentifiedObject):
    """
    Result of a calculation of one or more measurement.
    @author sveinols
    @version 1.0
    @created 25-Dec-2023 8:32:00 PM
    """

    def __init__(self):
        super().__init__()
        # Calculation operation executed on the operands.
        self.kind = CalculationKind.SUM  # Typical value
        self.pin_measurement = PinMeasurement()  # Typical value
        self.measurement_calculator_input = MeasurementCalculatorInput()  # Typical value
