# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Core.PSRType import PSRType
from IEC62325.MarketManagement.TimeSeries import TimeSeries


class MktPsrType(PSRType):

    """
    The type of a power system resource.
    @author: mspivbe2
    @version: 1.0
    @created: 25-Dec-2023 9:21:23 PM
    """

    def __init__(self):
        super().__init__()
        # The coded type of a power system resource.
        self.psr_type = ""
        self.time_series = TimeSeries()
