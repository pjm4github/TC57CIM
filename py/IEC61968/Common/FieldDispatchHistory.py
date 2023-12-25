# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Crew import Crew
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.FieldDispatchStep import FieldDispatchStep
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.PlannedOutage import PlannedOutage
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.UnplannedOutage import UnplannedOutage

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class FieldDispatchHistory(IdentifiedObject):
    
    def __init__(self):
        super().__init__()
        self.unplanned_outage = UnplannedOutage()
        self.planned_outage = PlannedOutage()
        self.crew = Crew()
        self.field_dispatch_step = FieldDispatchStep()
