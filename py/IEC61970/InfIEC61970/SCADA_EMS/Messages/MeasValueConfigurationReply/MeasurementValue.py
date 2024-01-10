# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Mon Jan  8 09:18:27 2024
# Class representing a MeasurementValue
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Meas.MeasurementValueQuality import MeasurementValueQuality
from IEC61970.InfIEC61970.SCADA_EMS.Meas.MeasValueSet import MeasValueSet
from IEC61970.InfIEC61970.SCADA_EMS.Meas.MeasurementValueExt import MeasurementValueExt


class MeasurementValue(IdentifiedObject, MeasurementValueExt):
    
    # Constructor
    def __init__(self):
        super().__init__()
        self.m_meas_value_set = MeasValueSet()  # Instance of MeasValueSet class
        self.m_measurement_value_quality = MeasurementValueQuality()  # Instance of MeasurementValueQuality class
