# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Assets.InspectionDataSet import InspectionDataSet
from IEC61968.Common.ScheduledEvent import ScheduledEvent
from IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval


# Schedule parameters for an activity that is to occur, is occurring, or has completed.
# @created 20-Dec-2023 5:28:58 PM
class ScheduledEventData:

    # Estimated date and time for activity execution (with earliest possibility of activity initiation and latest possibility of activity completion).
    def __init__(self):
        self.estimated_window = DateTimeInterval()
        # Requested date and time interval for activity execution.
        self.requested_window = DateTimeInterval()
        self.status = ''
        self.inspection_data_set = InspectionDataSet()
        # All scheduled events with this specification.
        self.scheduled_events = ScheduledEvent()

