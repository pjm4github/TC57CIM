# package IEC62325.MarketOperations.MarketPlan;
#
# import IEC61970.Base.Domain.String;
# import IEC61970.Base.Domain.DateTime;
# import IEC62325.MarketOperations.MktDomain.MarketEventStatusKind;
# import IEC61970.Base.Core.IdentifiedObject;

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MktDomain.MarketEventStatusKind import MarketEventStatusKind


class MarketActualEvent(IdentifiedObject):
    def __init__(self):
        super().__init__()
        self.event_comments = ""  # Free format comments for the event, for any purpose needed.
        self.event_end_time = DateTime()  # End time of the event.
        self.event_start_time = DateTime()  # Start time of the event.
        self.event_status = MarketEventStatusKind.planned  # Event status, e.g. active, canceled, expired, etc.
        self.event_type = ""  # Actual event type.
        self.market_run = MarketRun()  # Market run triggered by this actual event. For example, the DA market run is triggered by the actual open bid submission event and terminated by the actual execution and completion of the DA market run captured by the runState of the MarketRun.
        self.planned_market_event = PlannedMarketEvent()  # Planned event executed by this actual event.