# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.CostPerEnergyUnit import CostPerEnergyUnit


class RegisteredControllableLoad:
    """
    Temporary holding for load reduction attributes removed from RegisteredLoad.
    Use for future use case when developing the RegisteredDistributedResource specialized classes.
    @author mspivbe2
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """

    def __init__(self):
        super().__init__()
        """
        Default constructor
        """
        # Maximum Base Load (MW), per Participating Load Resource
        self.max_base_load = ActivePower()
        # Maximum Deployment time (seconds)
        self.max_deployment_time = 0.0
        # Maximum Number of Daily Load Curtailments
        self.max_load_red_times_per_day = 0
        # maximum load reduction
        self.max_load_reduction = ActivePower()
        # Maxiimum Load Reduction Time (min), per Participating Load Resource
        self.max_reduction_time = 0.0
        # Maximum weekly deployments
        self.max_weekly_deployment = 0
        # Minimum MW for a load reduction (e.g., MW rating of a discrete pump.
        #
        # This attribute may be used also in the LoadBid class. The reason that the
        # attribute is also modeled in this class is that it is resource attribute and
        # needs to be persistently stored.
        self.min_load_reduction = ActivePower()
        # minimum load reduction cost. Single number for the load
        self.min_load_reduction_cost = CostPerEnergyUnit()
        # Shortest period load reduction shall be maintained before load can be restored
        # to normal levels.
        #
        # This attribute may be used also in the LoadBid class. The reason that the
        # attribute is also modeled in this class is that it is resource attribute and
        # needs to be persistently stored.
        self.min_load_reduction_interval = 0.0
        # Minimum Load Reduction Time (min), per Participating Load Resource
        self.min_reduction_time = 0.0
        # Shortest time that load shall be left at normal levels before a new load
        # reduction.
        #
        # This attribute may be used also in the LoadBid class. The reason that the
        # attribute is also modeled in this class is that it is resource attribute and
        # needs to be persistently stored.
        self.min_time_bet_load_red = 0.0
        # Time period that is required from an order to reduce a load to the time that it
        # takes to get to the minimum load reduction.
        #
        # This attribute may be used also in the LoadBid class. The reason that the
        # attribute is also modeled in this class is that it is resource attribute and
        # needs to be persistently stored.
        self.req_notice_time = 0.0
