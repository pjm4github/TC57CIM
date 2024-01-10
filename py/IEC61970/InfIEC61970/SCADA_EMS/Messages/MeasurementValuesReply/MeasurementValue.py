# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Mon Jan  8 09:07:27 2024
# public class MeasurementValue extends IdentifiedObject {
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Meas.MeasurementValueQuality import MeasurementValueQuality
from IEC61970.InfIEC61970.SCADA_EMS.Meas.MeasValueSet import MeasValueSet


class MeasurementValue(IdentifiedObject):
    # The time when the value was last updated
    # public DateTime timeStamp;
    def __init__(self):
        super().__init__()
        self.time_stamp = DateTime()  # initializing with typical value
        self.meas_value_set = MeasValueSet()  # initializing with typical value
        self.measurement_value_quality = MeasurementValueQuality()  # initializing with typical value
