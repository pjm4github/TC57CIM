# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Common.Document import Document
from IEC61968.Operations.OutageOrder import OutageOrder
from IEC61968.Operations.PlannedOutage import PlannedOutage
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval


class OutagePlan(Document):
    
    def __init__(self):
        super().__init__()
        self.approved_date_time = DateTime()
        self.cancelled_date_time = DateTime()
        self.planned_period = DateTimeInterval()
        self.purpose =""
        self.outage_order = OutageOrder()
        self.planned_outage = PlannedOutage()
