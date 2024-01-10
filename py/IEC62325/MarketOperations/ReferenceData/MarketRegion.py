# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.ReserveDemandCurve import ReserveDemandCurve
from IEC62325.MarketOperations.MarketSystem.MarketResults.MarketRegionResults import MarketRegionResults
from IEC62325.MarketOperations.ReferenceData.AggregateNode import AggregateNode


class MarketRegion(AggregateNode):
    """
    A specialized class of AggregatedNdeo type. Defines the MarketRegions. Regions
    could be system Market Regions, Energy Regions or Ancillary Service Regions.
    @created 28-Dec-2023 12:17:33 PM
    """
    def __init__(self) -> None:
        super().__init__()
        self.market_region_results: MarketRegionResults = MarketRegionResults()
        self.reserve_demand_curve: ReserveDemandCurve = ReserveDemandCurve()

