# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.Date import Date
from IEC62325.MarketManagement.TimeSeries import TimeSeries


class Series(TimeSeries):
    """
    A set of similar physical or conceptual objects defined for the same period or
    point of time.
    @author ENTSO-E
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """

    def __init__(self):
        super().__init__()

        # The date of the last update related to this market object.
        self.last_update_date = Date()

        # Type of method used in the business process related to this Series, e.g.
        # metering method.
        self.method_type = ""

        # For a market object, the date of registration of a contract, e.g. the date of
        # change of supplier for a customer.
        self.registration_date = Date()
        self.self_series = Series()
