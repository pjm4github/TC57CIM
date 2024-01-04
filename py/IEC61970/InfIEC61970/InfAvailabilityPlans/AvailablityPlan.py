from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval


class AvailablityPlan(IdentifiedObject):
    """
    The collection of all the availability schedules for a given time range. Only
    one availability plan shall be valid for the same period.
    @author 222206
    @version 1.0
    @created 25-Dec-2023 8:31:54 PM
    """
    def __init__(self):
        super().__init__()
        self.valid_period = DateTimeInterval()  # The period of time for which the plan is valid.

# end AvailablityPlan
