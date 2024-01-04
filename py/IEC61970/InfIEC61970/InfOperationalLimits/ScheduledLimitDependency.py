# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 22:25:18 2024
from IEC61970.InfIEC61970.InfOperationalLimits.LimitDependency import LimitDependency
from IEC61970.InfIEC61970.InfOperationalLimits.ScheduledLimitValue import ScheduledLimitValue


class ScheduledLimitDependency(LimitDependency):
    """
    Represents a limit dependency with scheduled limit values.
    """
    def __init__(self):
        super().__init__()
        self.scheduled_limit_values = ScheduledLimitValue()

# end ScheduledLimitDependency
