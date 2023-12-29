from IEC61970.Base.Core.Curve import Curve
from IEC61970.Base.Domain.PerCent import PerCent
from IEC62325.MarketOperations.ReferenceData.ResourceVerifiableCosts import ResourceVerifiableCosts


class ResourceOperationMaintenanceCost(Curve):
    """
    To model the Operation and Maintenance (O and M)
    costs of a generation resource.

    author: USRAKHA
    version: 1.0
    created: 25-Dec-2023 9:21:23 PM
    """

    def __init__(self):
        super().__init__()
        """
        Constructor
        """
        self.gas_percent_above_low_sustained_limit = PerCent()
        self.oil_percent_above_low_sustained_limit = PerCent()
        self.om_cost_cold_startup = 0.0
        self.om_cost_hot_startup = 0.0
        self.om_cost_intermediate_startup = 0.0
        self.om_cost_low_sustained_limit = 0.0
        self.solidfuel_percent_above_low_sustained_limit = PerCent()
        self.resource_verifiable_costs = ResourceVerifiableCosts()
