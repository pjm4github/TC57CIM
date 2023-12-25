from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.BaseReading import BaseReading
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.ReadingReasonKind import ReadingReasonKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.ReadingType import ReadingType
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.MeterReading import MeterReading


class Reading(BaseReading):
    def __init__(self):
        super().__init__()
        self.reason = ReadingReasonKind()  # Reason for this reading being taken.
        self.reading_type = ReadingType()  # Type information for this reading value.
        self.meter_readings = MeterReading()  # All meter readings (sets of values) containing this reading value.
