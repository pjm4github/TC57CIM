from IEC61970.Base.Domain.Voltage import Voltage
from IEC61970.InfIEC61970.InfOperationalLimits.ScheduledLimitValue import ScheduledLimitValue


class ScheduledVoltageLimitValue(ScheduledLimitValue):
    """
    Represents a voltage limit value for a scheduled time.
    """
    def __init__(self):
        super().__init__()
        self.value = Voltage()

# end ScheduledVoltageLimitValue
