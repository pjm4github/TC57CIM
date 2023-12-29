from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class PlannedMarketEvent(IdentifiedObject):
    def __init__(self):
        # Planned event type.
        super().__init__()
        self.event_type = ""

        # This is relative time so that this attribute can be used by more than one planned market.
        # For example the bid submission is 10am everyday.
        self.planned_time = 0