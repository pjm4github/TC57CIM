# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.AngleDegrees import AngleDegrees
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.PowerTransformerEnd import PowerTransformerEnd


class PowerTransformer:
    
    def __init__(self) -> None:
        self.before_sh_circuit_highest_operating_current: Optional[CurrentFlow] = CurrentFlow()
        self.before_sh_circuit_highest_operating_voltage: Optional[Voltage] = Voltage()
        self.before_short_circuit_angle_pf: Optional[AngleDegrees] = AngleDegrees()
        self.high_side_min_operating_u: Optional[Voltage] = Voltage()
        self.is_part_of_generator_unit: bool = False
        self.operational_values_considered: bool = True
        self.vector_group: Optional[str] = ""
        self.power_transformer_end: Optional[PowerTransformerEnd] = PowerTransformerEnd()
    
    def get_before_sh_circuit_highest_operating_current(self) -> Optional[CurrentFlow]:
        return self.before_sh_circuit_highest_operating_current

    def get_before_sh_circuit_highest_operating_voltage(self) -> Optional[Voltage]:
        return self.before_sh_circuit_highest_operating_voltage

    def get_before_short_circuit_angle_pf(self) -> Optional[AngleDegrees]:
        return self.before_short_circuit_angle_pf

    def get_high_side_min_operating_u(self) -> Optional[Voltage]:
        return self.high_side_min_operating_u

    def get_is_part_of_generator_unit(self) -> bool:
        return self.is_part_of_generator_unit

    def get_operational_values_considered(self) -> bool:
        return self.operational_values_considered

    def get_power_transformer_end(self) -> Optional[PowerTransformerEnd]:
        return self.power_transformer_end

    def get_vector_group(self) -> Optional[str]:
        return self.vector_group

    def set_before_sh_circuit_highest_operating_current(self, new_val: CurrentFlow) -> None:
        self.before_sh_circuit_highest_operating_current = new_val

    def set_before_sh_circuit_highest_operating_voltage(self, new_val: Voltage) -> None:
        self.before_sh_circuit_highest_operating_voltage = new_val

    def set_before_short_circuit_angle_pf(self, new_val: AngleDegrees) -> None:
        self.before_short_circuit_angle_pf = new_val

    def set_high_side_min_operating_u(self, new_val: Voltage) -> None:
        self.high_side_min_operating_u = new_val

    def set_is_part_of_generator_unit(self, new_val: bool) -> None:
        self.is_part_of_generator_unit = new_val

    def set_operational_values_considered(self, new_val: bool) -> None:
        self.operational_values_considered = new_val
    
    def set_power_transformer_end(self, new_val: PowerTransformerEnd) -> None:
        self.power_transformer_end = new_val

    def set_vector_group(self, new_val: str) -> None:
        self.vector_group = new_val
