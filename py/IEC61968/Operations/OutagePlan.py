# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Document import Document
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.OutageOrder import OutageOrder
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.PlannedOutage import PlannedOutage
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval


class OutagePlan(Document):
    
    def __init__(self):
        super().__init__()
        self.approved_date_time = DateTime()
        self.cancelled_date_time = DateTime()
        self.planned_period = DateTimeInterval()
        self.purpose =""
        self.outage_order = OutageOrder()
        self.planned_outage = PlannedOutage()
