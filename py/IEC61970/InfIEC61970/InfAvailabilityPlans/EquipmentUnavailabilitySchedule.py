from IEC61970.Base.Core.Equipment import Equipment
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.InfIEC61970.InfAvailabilityPlans.UnavailablitySchedule import UnavailablitySchedule


class EquipmentUnavailabilitySchedule(IdentifiedObject):
    """
    @author 222206
    @version 1.0
    @created 25-Dec-2023 8:31:56 PM
    """
    def __init__(self):
        super().__init__()
        self.unavailability_schedule = UnavailablitySchedule()  # Unavailability schedule for the equipment.
        self.equipment = Equipment()  # Equipment associated with the unavailability schedule.

# end EquipmentUnavailabilitySchedule
