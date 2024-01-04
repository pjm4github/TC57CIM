# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 22:25:18 2024
from IEC61970.Base.Domain.ApparentPower import ApparentPower
from IEC61970.InfIEC61970.InfOperationalLimits.ScheduledLimitDependency import ScheduledLimitValue


class ScheduledApparentPowerLimitValue(ScheduledLimitValue):
    """
    Represents a time scheduled value for apparent power limit.
    """
    def __init__(self):
        super().__init__()
        self.value = ApparentPower()

# end ScheduledApparentPowerLimitValue
