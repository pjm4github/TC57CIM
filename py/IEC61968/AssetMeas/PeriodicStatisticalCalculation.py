# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.AssetMeas.CalculationIntervalUnitKind import CalculationIntervalUnitKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.AssetMeas.StatisticalCalculation import StatisticalCalculation


class PeriodicStatisticalCalculation(StatisticalCalculation):
    
    def __init__(self):
        super().__init__()
        self.calculation_interval_magnitude = 0
        self.calculation_interval_unit = CalculationIntervalUnitKind.DAY
