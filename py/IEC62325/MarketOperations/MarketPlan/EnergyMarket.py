# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local imports
from IEC62325.MarketOperations.ReferenceData.RTO import RTO
from IEC62325.MarketOperations.MarketSystem.MarketResults.Settlement import Settlement
from IEC62325.MarketOperations.MarketSystem.MarketResults.MarketResults import MarketResults
from IEC62325.MarketCommon.RegisteredResource import RegisteredResource


class EnergyMarket:
    # Energy and Ancillary Market (e.g. Energy, Spinning Reserve, Non-Spinning
    # Reserve) with a description of the Market operation control parameters.
    # @author mspivbe2
    # @version 1.0
    # @created 25-Dec-2023 9:21:22 PM
    def __init__(self):
        self.rto = RTO()
        self.settlements = Settlement()
        self.market_results = MarketResults()
        self.registered_resources = RegisteredResource()
