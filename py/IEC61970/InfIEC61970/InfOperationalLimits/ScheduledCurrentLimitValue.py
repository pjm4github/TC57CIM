# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 22:25:18 2024
from IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from IEC61970.InfIEC61970.InfOperationalLimits.ScheduledLimitDependency import ScheduledLimitValue


class ScheduledCurrentLimitValue(ScheduledLimitValue):
    """
    Represents a current limit that is scheduled.
    """
    def __init__(self):
        super().__init__()
        self.value = CurrentFlow()

# end ScheduledCurrentLimitValue
