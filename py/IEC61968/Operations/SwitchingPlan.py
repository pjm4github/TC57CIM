# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Document import Document
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.Outage import Outage
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.OutagePlan import OutagePlan
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval


class SwitchingPlan(Document):
    def __init__(self):
        super().__init__()
        self.approved_date_time = DateTime()  # The date and time the switching plan was approved
        self.cancelled_date_time = DateTime()  # Date and Time the switching plan was cancelled
        self.planned_period = DateTimeInterval()  # the planned start and end times for the switching plan
        self.purpose = ""  # Purpose of this plan
        self.rank = 0  # Ranking in comparison to other switching plans
        self.outage = Outage()  # Outage that will be activated or eliminated when this switching plan gets executed
        self.switching_step_groups = None  # All groups of switching steps within this switching plan
        self.safety_documents = []  # All safety documents applicable to this switching plan
        self.outage_plan = OutagePlan()  # The outage plan for which the switching plan is defined
        self.work_tasks = None  # All work tasks to execute this switching plan
