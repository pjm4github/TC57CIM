from IEC62325.MarketManagement.TimeSeries import TimeSeries


class BidTimeSeries(TimeSeries):
    """
    The formal specification of specific characteristics related to a bid.
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.block_bid = str()  # Indication that the values in the period are considered as a whole.
        self.direction = str()  # The coded identification of the energy flow.
        self.divisible = str()  # An indication whether each element of the bid may be partially accepted.
        self.exclusive_bids_identification = str()  # Unique identification associated with all linked tenders.
        self.linked_bids_identification = str()  # Unique identification associated with all linked bids.
        self.minimum_activation_quantity = 0  # The minimum quantity of energy that can be activated at a given time interval.
        self.priority = int()  # The numeric local priority given to a bid.
        self.status = str()  # The information about the status of the bid.
        self.step_increment_quantity = 0 # The minimum increment that can be applied for an increase in an activation request.
