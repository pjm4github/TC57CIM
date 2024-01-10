# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Mon Jan  8 09:15:59 2024
# public class MeasValueConfiguration extends IdentifiedObject {
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.Seconds import Seconds


class MeasValueConfiguration(IdentifiedObject):
    """A class representing the configuration of measurement values"""

    def __init__(self):
        super().__init__()
        # public Seconds keepAliveTime;
        self.keep_alive_time = Seconds()  # // attribute initialized to the class type as a method call
        # public Boolean readAllValues;
        self.read_all_values = True  # // attribute initialized to the class type as a method call
        # public DateTime sampleTime;
        self.sample_time = DateTime()  # // attribute initialized to the class type as a method call
        # public Seconds sampleTimeDeviation;
        self.sample_time_deviation = Seconds()  # // attribute initialized to the class type as a method call

