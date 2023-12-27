# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC62325.MarketManagement.Domain import Domain
from IEC62325.MarketManagement.Point import Point
from IEC62325.MarketManagement.TimeSeries import TimeSeries


# Description of quantities needed in the data exchange.
# The type of the quantity is described either by the role of the association or the type attribute.
# The quality attribute provides the information about the quality of the quantity (measured, estimated, etc.)
# @author ENTSO-E
# @version 1.0
# @created 25-Dec-2023 9:21:23 PM

class Quantity:
    # The quality of the information being provided. This quality may be estimated, not available, as provided, etc.
    def __init__(self):
        self.quality = 0
        self.type = ""
        # Public attributes
        self.time_series = TimeSeries()
        self.point = Point()
        self.domain = Domain()


    # The quantity value. The association role provides the information about what is expressed.
    def set_quantity(self, val):
        self.quantity = val

    # The description of the type of the quantity.
    def set_type(self, type_str):
        self.type = type_str

