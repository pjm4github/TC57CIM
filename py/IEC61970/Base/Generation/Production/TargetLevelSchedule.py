# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024

from IEC61970.Base.Core.Curve import Curve
from IEC61970.Base.Domain.WaterLevel import WaterLevel


class TargetLevelSchedule(Curve):
    # Reservoir water level targets from advanced studies or "rule curves". Typically
    # in one hour increments for up to 10 days.
    # @created 02-Jan-2024 10:59:19 PM
    def __init__(self):
        super().__init__()

        # High target level limit, above which the reservoir operation will be penalized.
        self.high_level_limit = WaterLevel()  # initializing the high_level_limit attribute to WaterLevel class

        # Low target level limit, below which the reservoir operation will be penalized.
        self.low_level_limit = WaterLevel()   # initializing the low_level_limit attribute to WaterLevel class
