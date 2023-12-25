# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Meas.MeasurementValue import MeasurementValue


class BaseReading(MeasurementValue):
    def __init__(self):
        super().__init__()
        self.reported_date_time = DateTime()
        self.source = ""
        self.time_period = DateTimeInterval()
        self.value = ""
