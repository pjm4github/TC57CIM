# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106

from IEC61970.Base.Meas.AnalogLimitSet import AnalogLimitSet


class MktAnalogLimitSet(AnalogLimitSet):
    """
    Subclass of IEC 61970:Meas:AnalogLimitSet.
    @author: mspivbe2
    @version: 1.0
    @created: 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        super().__init__()
        """
        Default constructor
        """
        self.rating_set = 0
