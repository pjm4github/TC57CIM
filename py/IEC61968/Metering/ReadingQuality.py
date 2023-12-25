from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.BaseReading import BaseReading
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.ReadingQualityType import ReadingQualityType


class ReadingQuality:
    def __init__(self):
        self.comment = ""  # Elaboration on the quality code.
        self.source = ""  # System acting as the source of the quality code.
        self.time_stamp = DateTime()  # Date and time at which the quality code was assigned or ascertained.
        self.reading = BaseReading()  # Reading value to which this quality applies.
        self.reading_quality_type = ReadingQualityType()  # Type of this reading quality.
