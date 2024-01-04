from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.InfIEC61970.InfAvailabilityPlans.AvailablityPlan import AvailablityPlan


class UnavailablitySchedule(IdentifiedObject):
    """
    A schedule of unavailability for one or more specified equipment that need to
    follow the same scheduling periods.
    @author 222206
    @version 1.0
    @created 25-Dec-2023 8:32:04 PM
    """
    def __init__(self):
        super().__init__()
        self.availability_plan = AvailablityPlan()  # Availability plan associated with the unavailability schedule.

# end UnavailablitySchedule
