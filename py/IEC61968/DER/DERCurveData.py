# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.DER.DERMonitorableParameter import DERMonitorableParameter
from CIM_STD_PYTHON.TC57CIM.IEC61968.DER.DispatchSchedule import DispatchSchedule
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime


class DerCurveData:
    def __init__(self):
        self.interval_number = 0
        self.max_y_value = 0.0
        self.min_y_value = 0.0
        self.nominal_y_value = 0.0
        self.time_stamp = DateTime()
        self.dispatch_schedule = DispatchSchedule()
        self.der_monitorable_parameter = DERMonitorableParameter()
