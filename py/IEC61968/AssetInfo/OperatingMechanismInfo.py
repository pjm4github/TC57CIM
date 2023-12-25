# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.AssetInfo.OperatingMechanismKind import OperatingMechanismKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.AssetInfo import AssetInfo
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage

class OperatingMechanismInfo(AssetInfo):

    def __init__(self):
        super().__init__()
        self.close_amps = CurrentFlow()
        self.close_voltage = Voltage()
        self.mechanism_kind = OperatingMechanismKind.SPRING
        self.motor_run_current = CurrentFlow()
        self.motor_start_current = CurrentFlow()
        self.motor_voltage = Voltage()
        self.trip_amps = CurrentFlow()
        self.trip_voltage = Voltage()
