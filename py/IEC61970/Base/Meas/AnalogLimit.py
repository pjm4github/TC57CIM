# /**
#  * Limit values for Analog measurements.
#  * @created 06-Jan-2024 11:46:51 PM
#  */
from IEC61970.Base.Meas.Limit import Limit


class AnalogLimit(Limit):

    # /**
    #  * The value to supervise against.
    #  */
    def __init__(self):
        super().__init__()
        self.value = 0.0

