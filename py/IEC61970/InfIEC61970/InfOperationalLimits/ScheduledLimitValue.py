# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 22:25:18 2024
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.LoadModel.Season import Season


class ScheduledLimitValue(IdentifiedObject):
    """
    Represents a limit that is applicable during a scheduled time period.
    """
    def __init__(self):
        super().__init__()
        self.season = Season()  # The season for which the scheduled limits applies. If not specified, then applicable to any season.

# end ScheduledLimitValue
