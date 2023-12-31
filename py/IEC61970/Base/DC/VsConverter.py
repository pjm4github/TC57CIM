# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:22:57 2023
from IEC61970.Base.DC.ACDCConverter import ACDCConverter

from IEC61970.Base.DC.VsCapabilityCurve import VsCapabilityCurve
from IEC61970.Base.DC.VsPpccControlKind import VsPpccControlKind
from IEC61970.Base.DC.VsQpccControlKind import VsQpccControlKind
from IEC61970.Base.Domain.AngleDegrees import AngleDegrees
from IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.Domain.ReactivePower import ReactivePower
from IEC61970.Base.Domain.Resistance import Resistance
from IEC61970.Base.Domain.Voltage import Voltage


class VsConverter(ACDCConverter):
    def __init__(self) -> None:
        super().__init__()
        self.delta: AngleDegrees = AngleDegrees()
        self.droop: float = 0.0
        self.droop_compensation: Resistance = Resistance()
        self.max_modulation_index: float = 0.0
        self.max_valve_current: CurrentFlow = CurrentFlow()
        self.p_pcc_control: VsPpccControlKind = VsPpccControlKind.PPCC_AND_UDC_DROOP
        self.q_pcc_control: VsQpccControlKind = VsQpccControlKind.VOLTAGE_PCC
        self.q_share: PerCent = PerCent()
        self.target_q_pcc: ReactivePower = ReactivePower()
        self.target_upcc: Voltage = Voltage()
        self.uv: Voltage = Voltage()
        self.capability_curve: VsCapabilityCurve = VsCapabilityCurve()
