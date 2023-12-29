# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.PerCent import PerCent


class ResourceStartupCost:
    """
    To model the startup costs of a generation resource.
    @author USRAKHA
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """

    def __init__(self):

        # Verifiable Cold Start Up Fuel (MMBtu per start)
        self.fuel_cold_startup = 0.0

        # Verifiable Hot Start Up Fuel (MMBtu per start)
        self.fuel_hot_startup = 0.0

        # Verifiable Intermediate Start Up Fuel (MMBtu per start)
        self.fuel_intermediate_startup = 0.0

        # Minimum-Energy fuel, MMBtu/MWh
        self.fuel_low_sustained_limit = 0.0

        # Percentage of Fuel Index Price (gas) for cold startup
        self.gas_percent_cold_startup = PerCent()

        # Percentage of Fuel Index Price (gas) for hot startup
        self.gas_percent_hot_startup = PerCent()

        # Percentage of Fuel Index Price (gas) for intermediate startup
        self.gas_percent_intermediate_startup = PerCent()

        # Percentage of FIP (gas) for operating at LSL
        self.gas_percent_low_sustained_limit = PerCent()

        # Percentage of Fuel Oil Price (FOP) for cold startup
        self.oil_percent_cold_startup = PerCent()

        # Percentage of Fuel Oil Price (FOP) for hot startup
        self.oil_percent_hot_startup = PerCent()

        # Percentage of Fuel Oil Price (FOP) for intermediate startup
        self.oil_percent_intermediate_startup = PerCent()

        # Percentage of FOP (oil) for operating at LSL
        self.oil_percent_low_sustained_limit = PerCent()

        # Percentage of Solid Fuel for cold startup
        self.solid_fuel_percent_cold_startup = PerCent()

        # Percentage of Solid Fuel for hot startup
        self.solid_fuel_percent_hot_startup = PerCent()

        # Percentage of Solid Fuel for intermedite startup
        self.solid_fuel_percent_intermediate_startup = PerCent()

        # Percentage of Solid Fuel for operating at LSL
        self.solid_fuel_percent_low_sustained_limit = PerCent()
