from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MarketQualitySystem.AuxiliaryValues import AuxiliaryValues
from IEC62325.MarketOperations.MktDomain.MarketType import MarketType


class AuxiliaryCost:
    """
    Models Market clearing results for Auxiliary costs.
    """
    def __init__(self):
        self.interval_start_time = DateTime()  # Start time of the interval
        self.market_type = MarketType.DAM  # Type of market
        self.update_time_stamp = DateTime()  # Timestamp of the last update
        self.update_user = str()  # User who last updated the record
        self.auxiliary_values = AuxiliaryValues()  # Associated AuxiliaryValues
