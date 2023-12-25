from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.BaseReading import BaseReading


class IntervalReading(BaseReading):
    #  * Data captured at regular intervals of time. Interval data could be captured as
    #  * incremental data, absolute data, or relative data. The source for the data is
    #  * usually a tariff quantity or an engineering quantity. Data is typically
    #  * captured in time-tagged, uniform, fixed-length intervals of 5 min, 10 min, 15
    #  * min, 30 min, or 60 min.
    #  * Note: Interval Data is sometimes also called "Interval Data Readings" (IDR).
    #  * @created 20-Dec-2023 6:25:30 PM
    def __init__(self):
        super().__init__()

