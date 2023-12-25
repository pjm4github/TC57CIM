# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Work.Work import Work
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval


class Appointment(IdentifiedObject):
    def __init__(self):
        super().__init__()
        self.call_ahead = False
        self.meeting_interval = DateTimeInterval()
        self.works = Work()

