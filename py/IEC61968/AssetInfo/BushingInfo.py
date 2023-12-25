# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.AssetInfo.BushingInsulationKind import BushingInsulationKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Capacitance import Capacitance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.PerCent import PerCent
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.AssetInfo import AssetInfo

class BushingInfo(AssetInfo):
    
    def __init__(self):
        super().__init__()
        self.c1_capacitance = Capacitance()
        self.c1_power_factor = PerCent()
        self.c2_capacitance = Capacitance()
        self.c2_power_factor = PerCent()
        self.insulation_kind = BushingInsulationKind.COMPOUND
        self.rated_current = CurrentFlow()
        self.rated_impulse_withstand_voltage = Voltage()
        self.rated_line_to_ground_voltage = Voltage()
        self.rated_voltage = Voltage()
