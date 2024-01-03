from IEC61970.Base.Meas.AccumulatorValue import AccumulatorValue
from IEC61970.Base.Meas.Measurement import Measurement
from IEC61970.Base.Meas.AccumulatorLimitSet import AccumulatorLimitSet


class Accumulator(Measurement):
    """
    Accumulator represents an accumulated (counted) Measurement, e.g. an energy
    value.
    @created 03-Jan-2024 4:14:57 PM
    """
    def __init__(self):
        super().__init__()
        self.max_value = 0  # Normal value range maximum for any of the MeasurementValue.values
        self.accumulator_values = AccumulatorValue()  # The values connected to this measurement
        self.limit_sets = AccumulatorLimitSet()  # A measurement may have zero or more limit ranges defined for it
