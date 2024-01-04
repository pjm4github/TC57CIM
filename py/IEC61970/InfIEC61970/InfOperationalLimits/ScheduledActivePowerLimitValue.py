# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 22:25:18 2024
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.InfIEC61970.InfOperationalLimits.ScheduledApparentPowerLimitValue import ScheduledLimitValue


class ScheduledActivePowerLimitValue(ScheduledLimitValue):
    """
    Represents a scheduled limit value for active power.
    """
    def __init__(self):
        super().__init__()
        self.value = ActivePower()

# end ScheduledActivePowerLimitValue
