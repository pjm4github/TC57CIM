# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# Importing local modules
from IEC62325.MarketOperations.ReferenceData.FuelRegion import FuelRegion


class GasPrice:
    """
    Price of gas in monetary units.
    @author USRAKHA
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """
    def __init__(self):
        # The average natural gas price at a defined fuel region
        self.gas_price_index = 0.0
        self.fuel_region = FuelRegion()

