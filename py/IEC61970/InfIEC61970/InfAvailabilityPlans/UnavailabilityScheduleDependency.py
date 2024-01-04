from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.InfIEC61970.InfAvailabilityPlans.UnavailablitySchedule import UnavailablitySchedule


class UnavailabilityScheduleDependency(IdentifiedObject):
    """
    A dependency between two unavailability schedules, where one schedule impacts the other.
    The impacted schedule depends on the other schedule.
    """
    def __init__(self):
        super().__init__()
        self.unavailability_schedule_impacts = UnavailablitySchedule()  # Unavailability schedule that is impacted.
        self.unavailability_schedule_depends_on = UnavailablitySchedule()  # Unavailability schedule that is depended on.
