# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from IEC61968.InfIEC61968.InfCommon.Craft import Craft
from IEC61968.InfIEC61968.InfCommon.OldCrew import OldCrew
from IEC61968.InfIEC61968.InfWork.CUGroup import WorkIdentifiedObject, Status
from IEC61968.InfIEC61968.InfWork.OldWorkTask import OldWorkTask
from IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval


class Capability(WorkIdentifiedObject):

    def __init__(self) -> None:
        self.performance_factor = ''  # Capability performance factor
        self.statusO= Status()
        self.type = ''  # Classification by utility's work management standards and practices
        self.validity_interval = DateTimeInterval()  # Date and time interval for which this capability is valid (when it became effective and when it expires)
        self.work_tasks = [OldWorkTask()]
        self.crew = OldCrew()
        self.crafts = Craft()
