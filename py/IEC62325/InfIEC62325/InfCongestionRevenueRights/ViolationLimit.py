from IEC61970.Base.Meas.Limit import Limit  # Importing Limit class from IEC61970.Base.Meas module
from IEC62325.MarketOperations.ReferenceData.Flowgate import Flowgate  # Importing Flowgate class from IEC62325.MarketOperations.ReferenceData module
from IEC62325.MarketOperations.MarketOpCommon.MktMeasurement import MktMeasurement  # Importing MktMeasurement class from IEC62325.MarketOperations.MarketOpCommon module

class ViolationLimit(Limit):
    """
    A type of limit that indicates if it is enforced and, through association, the
    organisation responsible for setting the limit.
    @created 28-Dec-2023 7:42:29 PM
    """

    def __init__(self):
        super().__init__()  # Calling the __init__() method of the superclass
        self.enforced = False  # Creating an instance of Boolean class and assigning it to the 'enforced' attribute
        self.flowgate = Flowgate()  # Creating an instance of Flowgate class and assigning it to the 'flowgate' attribute
        self.mkt_measurement = MktMeasurement()  # Creating an instance of MktMeasurement class and assigning it to the 'mkt_measurement' attribute
