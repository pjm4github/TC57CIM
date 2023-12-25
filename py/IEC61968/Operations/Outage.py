# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Crew import Crew
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.CrewStatusKind import CrewStatusKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Document import Document
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.UsagePoint import UsagePoint
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.OutageStatusKind import OutageStatusKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.ServicePointOutageSummary import ServicePointOutageSummary
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.SwitchAction import SwitchAction
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Equipment import Equipment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Faults.Fault import Fault
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.Switch import Switch


class Outage(Document):
    
    def __init__(self):
        super().__init__()
        self.actual_period = DateTimeInterval()
        self.community_descriptor = ""
        self.customers_restored = 0
        self.estimated_period = DateTimeInterval()
        self.meters_affected = 0
        self.original_customers_served = 0
        self.original_meters_affected = 0
        self.outage_kind = OutageStatusKind.CONFIRMED
        self.status_kind = CrewStatusKind.AWAITING_CREW_ASSIGNMENT
        self.summary = ServicePointOutageSummary()
        self.utility_disclaimer = ""
        self.faults = Fault()
        self.de_energized_usage_point = UsagePoint()
        self.opened_switches = Switch()
        self.equipments = Equipment()
        self.energized_usage_point = UsagePoint()
        self.planned_switch_actions = SwitchAction()
        self.crew = Crew()
