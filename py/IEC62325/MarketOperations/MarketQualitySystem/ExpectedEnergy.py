from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MarketQualitySystem.ExpectedEnergyValues import ExpectedEnergyValues


class ExpectedEnergy:
    """
    Model Expected Energy from Market Clearing, interval based.
    """
    def __init__(self):
        self.interval_start_time = DateTime()  # Start time of the interval
        self.update_time_stamp = DateTime()  # Timestamp of the last update
        self.update_user = str()  # User who last updated the record
        self.expected_energy_values = ExpectedEnergyValues()  # Associated ExpectedEnergyValues
