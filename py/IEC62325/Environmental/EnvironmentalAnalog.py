# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Meas.Analog import Analog
from IEC62325.Environmental.ClassificationCondition import ClassificationCondition
from IEC62325.Environmental.EnvironmentalInformation import EnvironmentalInformation
from IEC62325.Environmental.ReportingCapability import ReportingCapability
from IEC62325.MarketCommon.EnvironmentalMonitoringStation import EnvironmentalMonitoringStation


class EnvironmentalAnalog(Analog):

    def __init__(self):
        super().__init__()
        # Classification condition which this analog helps define.
        self.classification_condition = ClassificationCondition()

        # Observation or forecast with which this environmental analog measurement is associated.
        self.environmental_information = EnvironmentalInformation()

        # The reporting capability this environmental value set helps define.
        self.reporting_capability = ReportingCapability()

        # Monitoring station which provides this environmental analog measurement
        self.environmental_monitoring_station = EnvironmentalMonitoringStation()
