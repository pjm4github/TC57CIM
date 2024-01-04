# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 22:25:18 2024
from IEC61970.InfIEC61970.InfOperationalLimits.EnvironmentalDependentLimit import EnvironmentalDependentLimit


class TemperaturePolynomialLimit(EnvironmentalDependentLimit):
    """
    Represents the coefficients of a polynomial function that has temperature as input and calculates limit values as output.
    """
    def __init__(self):
        super().__init__()
        self.coefficient0 = 0.0  # The polynomial coefficient of power 0.
        self.coefficient1 = 0.0  # The polynomial coefficient of power 1.
        self.coefficient2 = 0.0  # The polynomial coefficient of power 2.
        self.coefficient3 = 0.0  # The polynomial coefficient of power 3.
        self.coefficient4 = 0.0  # The polynomial coefficient of power 4.


