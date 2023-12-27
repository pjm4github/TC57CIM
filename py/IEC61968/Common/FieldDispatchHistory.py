# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Common.Crew import Crew
from IEC61968.Common.FieldDispatchStep import FieldDispatchStep
from IEC61968.Operations.PlannedOutage import PlannedOutage
from IEC61968.Operations.UnplannedOutage import UnplannedOutage

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class FieldDispatchHistory(IdentifiedObject):
    
    def __init__(self):
        super().__init__()
        self.unplanned_outage = UnplannedOutage()
        self.planned_outage = PlannedOutage()
        self.crew = Crew()
        self.field_dispatch_step = FieldDispatchStep()
