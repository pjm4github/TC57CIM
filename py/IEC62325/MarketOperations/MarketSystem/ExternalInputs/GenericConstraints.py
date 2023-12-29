# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime

from IEC62325.MarketOperations.ReferenceData.Flowgate import Flowgate

from IEC62325.MarketOperations.MarketSystem.ExternalInputs.TransmissionCapacity import TransmissionCapacity


class GenericConstraints(IdentifiedObject):
    """
    Generic constraints can represent secure areas, voltage profile, transient
    stability and voltage collapse limits.
    
    The generic constraints can be one of the following forms:
    a) Thermal MW limit constraints type
    b) Group line flow constraint type
    """
    
    def __init__(self):
        super().__init__()
        """
        Constructor
        """
        self.interval_end_time = DateTime()  # 	 * Interval End Time
        self.interval_start_time = DateTime()  #  * Interval Start Time
        self.max_limit = 0.0  # Maximum Limit (MW)
        self.min_limit = 0.0  # Minimum Limit (MW)
        self.flowgate = Flowgate()
        self.transmission_capacity = TransmissionCapacity()  # assuming TransmissionCapacity is another class
