from IEC61968.Common.ActivityRecord import ActivityRecord
from IEC61968.Operations.PSREventKind import PSREventKind
from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource


class PSREvent(ActivityRecord):
    """
    Event recording the change in operational status of a power system resource;
    may be for an event that has already occurred or for a planned activity.
    @created 29-Dec-2023 5:19:26 PM
    """
    def __init__(self):
        super().__init__()
        self.kind = PSREventKind.OTHER  # Kind of event.
        self.power_system_resource = PowerSystemResource()  # Power system resource that generated this event.
