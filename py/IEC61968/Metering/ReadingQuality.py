from IEC61970.Base.Domain.DateTime import DateTime
from IEC61968.Metering.BaseReading import BaseReading
from IEC61968.Metering.ReadingQualityType import ReadingQualityType


class ReadingQuality:
    def __init__(self):
        self.comment = ""  # Elaboration on the quality code1.
        self.source = ""  # System acting as the source of the quality code1.
        self.time_stamp = DateTime()  # Date and time at which the quality code1 was assigned or ascertained.
        self.reading = BaseReading()  # Reading value to which this quality applies.
        self.reading_quality_type = ReadingQualityType()  # Type of this reading quality.
