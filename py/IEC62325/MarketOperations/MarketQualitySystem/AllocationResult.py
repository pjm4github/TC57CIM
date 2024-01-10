from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MarketQualitySystem.AllocationResultValues import AllocationResultValues


class AllocationResult:
    """
    Models Market clearing results. Indicates market horizon, interval based. Used
    by a market quality system for billing and settlement purposes.
    """
    def __init__(self):
        self.interval_start_time = DateTime()  # Start time of the interval
        self.update_time_stamp = DateTime()  # Timestamp of the last update
        self.update_user = str()  # User who last updated the record
        self.allocation_result_values = AllocationResultValues()  # Associated AllocationResultValues
