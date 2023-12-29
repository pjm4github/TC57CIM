# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from IEC62325.InfIEC62325.InfMarketResults.MarketCaseClearing import MarketCaseClearing
from IEC62325.MarketOperations.MarketPlan.MarketFactors import MarketFactors
from IEC62325.MarketOperations.MarketSystem.MarketResults.MarketRegionResults import MarketRegionResults


class AncillaryServiceClearing(MarketFactors):
    """
    Model of results of market clearing with respect to Ancillary Service products.
    """
    def __init__(self) -> None:
        super().__init__()
        self.market_region_results: MarketRegionResults = MarketRegionResults()
        self.market_case_clearing: MarketCaseClearing = MarketCaseClearing()
