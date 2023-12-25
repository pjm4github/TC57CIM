# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.AssetMeas.CalculationMethodOrder import CalculationMethodOrder
from CIM_STD_PYTHON.TC57CIM.IEC61968.AssetMeas.CalculationModeKind import CalculationModeKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.AssetMeas.CalculationTechniqueKind import CalculationTechniqueKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class StatisticalCalculation(IdentifiedObject):

    def __init__(self):
        super().__init__()
        self.calculation_mode = CalculationModeKind.total  # * Calculation mode.
        # Kind of statistical calculation, specifying how the measurement value is
        # calculated.
        self.calculation_technique = CalculationTechniqueKind.AVERAGE
        self.calculation_method_order = CalculationMethodOrder()
