# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 13:18:10 2023
from typing import Optional

from IEC61970.Base.Domain.CostPerEnergyUnit import CostPerEnergyUnit
from IEC62325.MarketOperations.MktDomain.MarketType import MarketType


class BidPriceCap:
    """
    This class represent the bid price cap.
    @created 28-Dec-2023 1:01:53 PM
    """

    def __init__(self) -> None:

        # Bid Ceiling ($/MWH)
        self.bid_ceilingOptional[CostPerEnergyUnit] = CostPerEnergyUnit()

        # Bid Ceiling ($/MWH) for generic AS versus a specific market product
        self.bid_ceiling_asOptional[CostPerEnergyUnit] = CostPerEnergyUnit()

        # Bid Floor, ($/MWH)
        self.bid_floorOptional[CostPerEnergyUnit] = CostPerEnergyUnit()

        # Bid Floor ($/MWH) for generic AS versus a specific market product
        self.bid_floor_asOptional[CostPerEnergyUnit] = CostPerEnergyUnit()

        # Bid Default Price($/MWH)
        self.default_priceOptional[CostPerEnergyUnit] = CostPerEnergyUnit()

        # Market Type of the cap (DAM or RTM)
        self.market_typeOptional[MarketType] = MarketType.DAM
