from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.BasicIntervalSchedule import BasicIntervalSchedule
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IrregularTimePoint import IrregularTimePoint


class IrregularIntervalSchedule(BasicIntervalSchedule):
    def __init__(self):
        super().__init__()
        self.time_points = IrregularTimePoint()  # The point data values that define a curve.
