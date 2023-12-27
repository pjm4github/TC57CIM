# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local import
from IEC62325.Environmental.EnvDomain.GeosphericAnalogKind import GeosphericAnalogKind
from IEC62325.Environmental.EnvironmentalAnalog import EnvironmentalAnalog


# Analog (float) measuring a geospheric condition.
# @author ppbr003
# @version 1.0
# @created 25-Dec-2023 9:21:22 PM
class GeosphericAnalog(EnvironmentalAnalog):

    # Kind of geospheric analog.
    def __init__(self):
        super().__init__()
        self.kind = GeosphericAnalogKind.SNOW_PACK_DEPTH
