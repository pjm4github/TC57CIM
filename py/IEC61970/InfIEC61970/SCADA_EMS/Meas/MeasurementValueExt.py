# measurement_value_ext.py
from IEC61970.InfIEC61970.SCADA_EMS.Meas.TimeAccuracy import TimeAccuracy


class MeasurementValueExt:
    def __init__(self):
        super().__init__()
        self.time_accuracy = TimeAccuracy.T1SEC

