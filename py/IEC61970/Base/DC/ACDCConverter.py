# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:22:57 2023
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.ConductingEquipment import ConductingEquipment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Terminal import Terminal
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePowerPerCurrentFlow import ActivePowerPerCurrentFlow
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ApparentPower import ApparentPower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ReactivePower import ReactivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Resistance import Resistance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage


class ACDCConverter(ConductingEquipment):
    def __init__(self) -> None:
        super().__init__()
        self.base_s: Optional[ApparentPower] = ApparentPower()  # Base apparent power of the converter pole.
        self.idc: Optional[CurrentFlow] = CurrentFlow()  # Converter DC current, also called Id. Converter state variable, result from power flow.
        self.idle_loss: Optional[ActivePower] = ActivePower()  # Active power loss in pole at no power transfer. Converter configuration data used in power flow.
        self.max_udc: Optional[Voltage] = Voltage()  # The maximum voltage on the DC side at which the converter should operate. Converter configuration data used in power flow.
        self.min_udc: Optional[Voltage] = Voltage()  # Min allowed converter DC voltage. Converter configuration data used in power flow.
        self.number_of_valves: Optional[int] = 0  # Number of valves in the converter. Used in loss calculations.
        self.p: Optional[ActivePower] = ActivePower()  # Active power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution in the case a simplified power flow model is used.
        self.pole_loss_p: Optional[ActivePower] = ActivePower()  # The active power loss at a DC Pole = idleLoss + switchingLoss*|Idc| + resitiveLoss*Idc^2. For lossless operation Pdc=Pac. For rectifier operation with losses Pdc=Pac-lossP. For inverter operation with losses Pdc=Pac+lossP. Converter state variable used in power flow.
        self.q: Optional[ReactivePower] = ReactivePower()  # Reactive power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution in the case a simplified power flow model is used.
        self.rated_udc: Optional[Voltage] = Voltage()  # Rated converter DC voltage, also called UdN. Converter configuration data used in power flow.
        self.resistive_loss: Optional[Resistance] = Resistance()  # Converter configuration data used in power flow. Refer to poleLossP.
        self.switching_loss: Optional[ActivePowerPerCurrentFlow] = ActivePowerPerCurrentFlow()  # Switching losses, relative to the base apparent power 'baseS'. Refer to poleLossP.
        self.target_ppcc: Optional[ActivePower] = ActivePower()  # Real power injection target in AC grid, at point of common coupling.
        self.target_udc: Optional[Voltage] = Voltage()  # Target value for DC voltage magnitude.
        self.uc: Optional[Voltage] = Voltage()  # Line-to-line converter voltage, the voltage at the AC side of the valve. Converter state variable, result from power flow.
        self.udc: Optional[Voltage] = Voltage()  # Converter voltage at the DC side, also called Ud. Converter state variable, result from power flow.
        self.valve_u0: Optional[Voltage] = Voltage()  # Valve threshold voltage, also called Uvalve. Forward voltage drop when the valve is conducting. Used in loss calculations, i.e. the switchLoss depend on numberOfValves * valveU0.
        self.pcc_terminal: Optional[Terminal] = Terminal()  # Point of common coupling terminal for this converter DC side. It is typically the terminal on the power transformer (or switch) closest to the AC network. The power flow measurement must be the sum of all flows into the transformer.
