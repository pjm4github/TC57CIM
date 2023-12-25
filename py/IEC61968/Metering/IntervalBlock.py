from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.IntervalReading import IntervalReading
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.MeterReading import MeterReading
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.PendingCalculation import PendingCalculation
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.ReadingType import ReadingType


class IntervalBlock:
    def __init__(self):
        self.pending_calculation = PendingCalculation()  # Pending calculation to apply to interval reading values contained by this block (after which the resulting reading type is different than the original because it reflects the conversion result).
        self.interval_readings = IntervalReading()  # Interval reading contained in this block.
        self.reading_type = ReadingType()  # Type information for interval reading values contained in this block.
        self.meter_reading = MeterReading()  # Meter reading containing this interval block.
