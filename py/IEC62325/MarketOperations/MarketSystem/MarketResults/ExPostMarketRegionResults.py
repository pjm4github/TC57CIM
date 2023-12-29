# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from typing import Optional

from IEC62325.MarketOperations.MarketSystem.MarketResults.ExPostMarketRegion import ExPostMarketRegion
from IEC62325.MarketOperations.ReferenceData.MarketRegion import MarketRegion


class ExPostMarketRegionResults:
    def __init__(self) -> None:
        self.ex_post_cleared_price: float = 0.0
        self.market_region: Optional[MarketRegion] = MarketRegion()
        self.ex_post_market_region: Optional[ExPostMarketRegion] = ExPostMarketRegion()
