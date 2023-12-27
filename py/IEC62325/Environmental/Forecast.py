# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval
from IEC62325.Environmental.EnvironmentalInformation import EnvironmentalInformation


class Forecast(EnvironmentalInformation):
    """
    A forecast group of value sets and/or phenomena characteristics.
    @author mcmorran
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        super().__init__()

        #  The interval for which the forecast is valid.  For example, a forecast issued
        #  now for tomorrow might be valid for the next 2 hours.
        self.valid_for = DateTimeInterval()
