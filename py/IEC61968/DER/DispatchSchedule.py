# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
import IEC61970.Base.Domain.per_cent
import IEC61970.Base.Core.curve_style
import IEC61970.Base.Domain.integer
import IEC61970.Base.Domain.date_time

from IEC61968.DER.DERMonitorableParameter import DERMonitorableParameter
from IEC61968.DER.TimeIntervalKind import TimeIntervalKind
from IEC61970.Base.Core.CurveStyle import CurveStyle
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.PerCent import PerCent


class DispatchSchedule:
    def __init__(self):
        self.confidence = PerCent()
        self.curve_style_kind = CurveStyle.STRAIGHT_LINE_Y_VALUES
        self.number_of_intervals = 0
        self.start_time = DateTime()
        self.time_interval_duration = 0
        self.time_interval_unit = TimeIntervalKind
        self.der_monitorable_parameter = DERMonitorableParameter()

