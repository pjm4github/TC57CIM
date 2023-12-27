# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# no need for imports
from IEC62325.Environmental.EnvDomain.HydrosphericAnalogKind import HydrosphericAnalogKind
from IEC62325.Environmental.EnvironmentalAnalog import EnvironmentalAnalog


# Analog (float) measuring a hydrospheric condition.
# @author ppbr003
# @version 1.0
# @created 25-Dec-2023 9:21:22 PM
class HydrosphericAnalog(EnvironmentalAnalog):

    # Kind of hydrospheric analog.
    def __init__(self):
        super().__init__()
        self.kind = HydrosphericAnalogKind.STORM_SURGE_HEIGHT
