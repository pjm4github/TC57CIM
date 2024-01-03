from IEC61970.Base.Meas.Limit import Limit


class AccumulatorLimit(Limit):
    """
    Limit values for Accumulator measurements.
    @created 03-Jan-2024 4:15:23 PM
    """

    def __init__(self):
        super().__init__()
        self.value = 0  # The value to supervise against. The value is positive
