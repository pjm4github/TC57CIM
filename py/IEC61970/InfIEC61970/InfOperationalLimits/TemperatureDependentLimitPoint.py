# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 22:25:18 2024
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.Domain.Temperature import Temperature


class TemperatureDependentLimitPoint:
    """
    Represents a point on a table of limit versus temperature.
    """
    def __init__(self):
        self.limit_percent = PerCent()  # The scaling of the operational limit in percent.
        self.temperature = Temperature()  # The temperature of the table point.

# end TemperatureDependentLimitPoint
