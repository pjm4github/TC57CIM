# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.InfIEC61970.EnergyArea.EnergyComponent import EnergyComponent


class EnergyConnection:
    def __init__(self) -> None:
        self.energy_component = EnergyComponent()

    def get_energy_component(self) -> Optional[EnergyComponent]:
        return self.energy_component
    
    def set_energy_component(self, new_val: EnergyComponent) -> None:
        self.energy_component = new_val
