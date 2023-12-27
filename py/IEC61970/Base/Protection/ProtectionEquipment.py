# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Core.ConductingEquipment import ConductingEquipment
from IEC61970.Base.Core.Equipment import Equipment
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol
from IEC61970.Base.Wires.ProtectedSwitch import ProtectedSwitch
from IEC61970.InfIEC61970.InfSIPS.ProtectiveAction import ProtectiveAction


class ProtectionEquipment(Equipment):
    
    def __init__(self):
        super().__init__()
        self.high_limit = 0.0
        self.low_limit = 0.0
        self.power_direction_flag = False
        self.relay_delay_time = Seconds()
        self.unit_multiplier = UnitMultiplier.none
        self.unit_symbol = UnitSymbol.none
        self.protected_switches = ProtectedSwitch()
        self.conducting_equipments = ConductingEquipment()
        self.protective_action = ProtectiveAction()

