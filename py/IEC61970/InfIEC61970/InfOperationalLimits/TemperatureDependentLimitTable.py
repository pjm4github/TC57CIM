# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 22:25:18 2024
from IEC61970.InfIEC61970.InfOperationalLimits.EnvironmentalDependentLimit import EnvironmentalDependentLimit
from IEC61970.InfIEC61970.InfOperationalLimits.TemperatureDependentLimitPoint import TemperatureDependentLimitPoint


class TemperatureDependentLimitTable(EnvironmentalDependentLimit):
    """
    Represents a table lookup that provides limit values corresponding to a temperature input.
    """
    def __init__(self):
        super().__init__()
        self.temperature_limit_table_point = TemperatureDependentLimitPoint()

# end TemperatureDependentLimitTable
