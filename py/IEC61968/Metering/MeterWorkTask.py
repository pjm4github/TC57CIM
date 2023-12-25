from CIM_STD_PYTHON.TC57CIM.IEC61968.Work.WorkTask import WorkTask
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.UsagePoint import UsagePoint
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.Meter import Meter


class MeterWorkTask(WorkTask):
    def __init__(self):
        super().__init__()
        self.usage_point = UsagePoint()  # Usage point to which this meter service work task applies.
        self.meter = Meter()  # Meter on which this non-replacement work task is performed.
        self.old_meter = Meter()  # Old meter replaced by this work task.

