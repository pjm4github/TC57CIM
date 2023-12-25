# measurement_value_ext.py
from CIM_STD_PYTHON.TC57CIM.IEC61970.InfIEC61970.SCADA_EMS.Meas.TimeAccuracy import TimeAccuracy


class MeasurementValueExt:
    def __init__(self):
        self.time_accuracy = TimeAccuracy.T1SEC

