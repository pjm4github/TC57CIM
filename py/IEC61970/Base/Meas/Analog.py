# Analog.py
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Meas.AnalogLimitSet import AnalogLimitSet
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Meas.AnalogValue import AnalogValue
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Meas.Measurement import Measurement


class Analog(Measurement):
    def __init__(self):
        super().__init__()
        self.max_value = 0.0  # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
        self.min_value = 0.0  # Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
        self.normal_value = 0.0  # Normal measurement value, e.g., used for percentage calculations.
        self.positive_flow_in = True  # If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource.
        self.analog_values = AnalogValue()  # The values connected to this measurement.
        self.limit_sets = AnalogLimitSet()  # A measurement may have zero or more limit ranges defined for it.
