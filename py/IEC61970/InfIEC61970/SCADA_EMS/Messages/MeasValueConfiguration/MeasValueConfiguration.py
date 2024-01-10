# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Mon Jan  8 09:08:40 2024
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.InfIEC61970.SCADA_EMS.Meas.MeasValueSet import MeasValueSet


class MeasValueConfiguration(IdentifiedObject):
    """
    @author selaost1
    @version 1.0
    @created 25-Dec-2023 8:32:00 PM
    """
    # Constructor
    def __init__(self):
        super().__init__()
        # sample cycle of the measurement value configuration
        self.sample_cycle = Seconds()  # Typical value
        # sample time of the measurement value configuration
        self.sample_time = DateTime()  # Typical value
        # sample time deviation of the measurement value configuration
        self.sample_time_deviation = Seconds()  # Typical value
        # measurement value set of the measurement value configuration
        self.meas_value_set = MeasValueSet()  # Typical value
