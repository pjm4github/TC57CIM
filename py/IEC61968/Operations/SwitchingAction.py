# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Crew import Crew
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Operator import Operator
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime


class SwitchingAction(IdentifiedObject):
    
    def __init__(self):
        super().__init__()
        self.description = ""
        self.executed_date_time = DateTime()
        self.is_free_sequence = True
        self.issued_date_time = DateTime()
        self.planned_date_time = DateTime()
        self.crew = Crew()
        self.operator = Operator()
