# discrete.py
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Meas.DiscreteValue import DiscreteValue
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Meas.Measurement import Measurement


class Discrete(Measurement):
    def __init__(self):
        super().__init__()
        self.max_value = 10
        self.min_value = 0
        self.normal_value = 2
        self.discrete_values = DiscreteValue()
