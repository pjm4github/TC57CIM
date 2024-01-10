# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from IEC62325.MarketOperations.MarketSystem.MarketResults.LossClearingResults import LossClearingResults
from IEC62325.MarketOperations.ReferenceData.AggregateNode import AggregateNode


class RucZone(AggregateNode):
    """
    A specialized class of type AggregatedNode type. Defines RUC Zones. A forecast
    region represents a collection of Nodes for which the Market operator has
    developed sufficient historical demand and relevant weather data to perform a
    demand forecast for such area. The Market Operator may further adjust this
    forecast to ensure that the Reliability Unit Commitment produces adequate local
    capacity procurement.
    @created 28-Dec-2023 12:20:54 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.loss_clearing_results: LossClearingResults = LossClearingResults()
