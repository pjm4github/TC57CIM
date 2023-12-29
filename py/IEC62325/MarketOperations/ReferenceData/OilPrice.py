# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC62325.MarketOperations.ReferenceData.FuelRegion import FuelRegion


class OilPrice:
    """
    Price of oil in monetary units.
    @author USRAKHA
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """

    def __init__(self):
        """
        The average oil price at a defined fuel region.
        """
        self.oil_price_index = 0.0
        self.fuel_region = FuelRegion()
