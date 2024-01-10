# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# Import locally due to unavailable package information
from IEC62325.Environmental.EnvDomain.AtmosphericAnalogKind import AtmosphericAnalogKind
from IEC62325.Environmental.EnvironmentalAnalog import EnvironmentalAnalog


class AtmosphericAnalog(EnvironmentalAnalog):
    #  * Analog (float) measuring an atmospheric condition.
    #  * @author ppbr003
    #  * @version 1.0
    #  * @created 25-Dec-2023 9:21:22 PM

    def __init__(self):
        super().__init__()
        self.kind = AtmosphericAnalogKind.ATMOSPHERIC_PRESSURE  # Kind of atmospheric analog
