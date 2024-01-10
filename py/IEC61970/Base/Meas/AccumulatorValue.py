from IEC61970.Base.Meas.MeasurementValue import MeasurementValue


class AccumulatorValue(MeasurementValue):
    # The value to supervise. The value is positive
    def __init__(self):
        super().__init__()
        self.value = 0
