from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MarketQualitySystem.AuxiliaryValues import AuxiliaryValues


class FiveMinAuxiliaryData:
    """
    Models 5-Minutes Auxiliary Data.
    """
    def __init__(self):
        self.interval_start_time = DateTime()  # Start time of the interval
        self.update_time_stamp = DateTime()  # Timestamp of the last update
        self.update_user = str()  # User who last updated the record
        self.auxiliary_values = AuxiliaryValues()  # Associated AuxiliaryValues
