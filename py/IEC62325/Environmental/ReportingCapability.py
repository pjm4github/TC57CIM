# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local imports
from IEC61968.AssetMeas.CalculationIntervalUnitKind import CalculationIntervalUnitKind
from IEC62325.Environmental.EnvDomain.ReportingMethodKind import ReportingMethodKind
from IEC62325.MarketCommon.EnvironmentalMonitoringStation import EnvironmentalMonitoringStation


# Class definition
class ReportingCapability:
    """
    Definition of one set of reporting capabilities for this
    monitoring station. The associated EnvironmentalValueSets describe the maximum
    range of possible environmental values the station is capable of returning.
    This attribute is intended primarily to assist a utility in managing its
    stations.
  
    @author ppbr003
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """


    def __init__(self):
        super().__init__()
        pass
        # Number of units of time making up reporting period.
        self.reporting_interval_period = 0

        # Unit of time in which reporting period is expressed.
        self.reporting_interval_type = CalculationIntervalUnitKind.MONTH

        # Indicates how the weather station reports observations.
        self.reporting_method = ReportingMethodKind.MANUAL

        # The environmental monitoring station to which this set of reporting
        # capabilities belong.
        self.environmental_monitoring_station = EnvironmentalMonitoringStation()
