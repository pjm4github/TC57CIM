from IEC62325.MarketOperations.MarketQualitySystem.AuxiliaryObject import AuxiliaryObject
from IEC62325.MarketOperations.MktDomain.YesNo import YesNo


class AuxiliaryValues(AuxiliaryObject):
    """
    Models Auxiliary Values.
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.avail_undispatched_q = 0.0  # Available undispatched quantity
        self.incremental_or_avail = 0.0  # Incremental operating reserve available
        self.max_expost_capacity = 0.0  # Maximum expost capacity
        self.min_expost_capacity = 0.0  # Minimum expost capacity
        self.no_load_cost = 0.0  # No load cost
        self.no_load_cost_eligibility_flag = YesNo.NO  # No load cost eligibility flag
        self.start_up_cost = 0.0  # Start up cost
        self.start_up_cost_eligibility_flag = YesNo.NO  # Start up cost eligibility flag
