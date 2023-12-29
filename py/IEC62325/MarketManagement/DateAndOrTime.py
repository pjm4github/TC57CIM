# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local imports
from IEC61970.Base.Domain.Date import Date
from IEC61970.Base.Domain.Time import Time
from IEC62325.MarketManagement.MarketDocument import MarketDocument


class DateAndOrTime:

    """
    The date and/or the time.
    @author mspivbe2
    @version 1.0
    @created 25-dec-2023 9:21:22 PM
    """

    def __init__(self):

        # Date as "yyyy-mm-dd", which conforms with ISO 8601
        self.date = Date()

        # Time as "hh:mm:ss.sssZ", which conforms with ISO 8601.
        self.time = Time()
        self.market_document = MarketDocument()

