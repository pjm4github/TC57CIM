
class IrregularTimePoint:
    def __init__(self):
        self.time = 0       # The time is relative to the schedule starting time.
        self.value1 = 0.0   # The first value at the time. The meaning of the value is defined by the derived type of the associated schedule.
        self.value2 = 0.0   # The second value at the time. The meaning of the value is defined by the derived type of the associated schedule.

