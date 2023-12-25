# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# from iec61968.der_parameter_kind import DERParameterKind
# from iec61968.metering.flow_direction_kind import FlowDirectionKind
# from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.unit_multiplier import UnitMultiplier
# from iec61968.der_unit_symbol import DERUnitSymbol
# from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.float import Float
from CIM_STD_PYTHON.TC57CIM.IEC61968.DER.DERParameterKind import DERParameterKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.DER.DERUnitSymbol import DERUnitSymbol
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.FlowDirectionKind import FlowDirectionKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier


class DERMonitorableParameter:

    def __init__(self):
        self.der_parameter = DERParameterKind.VOLTAGE
        self.flow_direction = FlowDirectionKind.forward
        self.y_multiplier = UnitMultiplier()
        self.y_unit = DERUnitSymbol.V
        self.y_unit_installed_max = 1.0
        self.y_unit_installed_min = 0.0
