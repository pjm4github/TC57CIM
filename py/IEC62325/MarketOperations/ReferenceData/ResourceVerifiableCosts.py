# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC62325.MarketOperations.ReferenceData.MktHeatRateCurve import MktHeatRateCurve
from IEC62325.MarketOperations.ReferenceData.ResourceStartupCost import ResourceStartupCost
from IEC62325.MarketCommon.RegisteredResource import RegisteredResource


class ResourceVerifiableCosts:
    # class to describe the verifiable costs associated with a generation resource
    # author: USRAKHA
    # version: 1.0
    # created: 25-Dec-2023 9:21:23 PM

    def __init__(self):
        self.mkt_heat_rate_curve = MktHeatRateCurve()
        self.registered_resource = RegisteredResource()
        self.resource_startup_cost = ResourceStartupCost()
