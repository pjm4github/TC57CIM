# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from typing import Optional

from IEC62325.MarketOperations.MarketPlan.MarketFactors import MarketFactors
from IEC62325.MarketOperations.MarketSystem.MarketResults.CommodityPrice import CommodityPrice
from IEC62325.MarketOperations.MarketSystem.MarketResults.PnodeResults import PnodeResults


class PnodeClearing(MarketFactors):
    def __init__(self) -> None:
        super().__init__()
        self.commodity_price: Optional[CommodityPrice] = CommodityPrice()
        self.pnode_results: Optional[PnodeResults] = PnodeResults()
