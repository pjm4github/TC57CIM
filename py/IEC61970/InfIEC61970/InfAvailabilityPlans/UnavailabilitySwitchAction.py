from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Wires.Switch import Switch
from IEC61970.InfIEC61970.InfAvailabilityPlans.EquipmentUnavailabilitySchedule import EquipmentUnavailabilitySchedule


class UnavailabilitySwitchAction(IdentifiedObject):
    """
    Relevant switching action for supporting the availability (or unavailability) plans.
    This could open or close a switch that is not directly connected to the unavailable equipment.
    """
    def __init__(self):
        super().__init__()
        self.open = True  # The switch is to be open during the scheduled period.
        self.equipment_unavailability_schedule = EquipmentUnavailabilitySchedule()
        self.switch = Switch()

