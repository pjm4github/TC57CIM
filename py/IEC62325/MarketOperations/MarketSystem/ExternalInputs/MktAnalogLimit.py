# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Meas.AnalogLimit import AnalogLimit
from IEC62325.MarketOperations.MktDomain.AnalogLimitType import AnalogLimitType

class MktAnalogLimit(AnalogLimit):
    """
    Subclass of IEC 61970:Meas:AnalogLimit.
    @author: mspivbe2
    @version: 1.0
    @created: 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        super().__init__()
        """
        Constructor
        """
        # 	 * The type of limit the value represents
        # 	 * Branch Limit Types:
        # 	 * Short Term
        # 	 * Medium Term
        # 	 * Long Term
        # 	 * Voltage Limits:
        # 	 * High
        # 	 * Low
        self.exceeded_limit = False
        self.limit_type = AnalogLimitType
