# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Any

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Pressure import Pressure
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Temperature import Temperature
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Equivalents.EquivalentInjection import EquivalentInjection
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.SynchronousMachine import SynchronousMachine


class ReactiveCapabilityCurve:
    """
    Reactive power rating envelope versus the synchronous machine's active power,
    in both the generating and motoring modes. For each active power value there is
    a corresponding high and low reactive power limit value. Typically there will
    be a separate curve for each coolant condition, such as hydrogen pressure.
    The Y1 axis values represent reactive minimum and the Y2 axis values represent
    reactive maximum.
    @author pmora
    @updated 15-Dec-2023 1:39:42 PM
    """

    def __init__(self) -> None:
        """
        Constructor method to initialize the class
        """
        self.coolant_temperature: Any = Temperature()
        self.hydrogen_pressure: Any = Pressure()
        self.initially_used_by_synchronous_machines: Any = SynchronousMachine()
        self.synchronous_machines: Any = SynchronousMachine()
        self.equivalent_injection = EquivalentInjection()

    def get_coolant_temperature(self) -> Any:
        """
        Getter method for coolant temperature
        """
        return self.coolant_temperature

    def get_equivalent_injection(self) -> Any:
        """
        Getter method for equivalent injection
        """
        return self.equivalent_injection

    def get_hydrogen_pressure(self) -> Any:
        """
        Getter method for hydrogen pressure
        """
        return self.hydrogen_pressure

    def get_initially_used_by_synchronous_machines(self) -> Any:
        """
        Getter method for initially used by synchronous machines
        """
        return self.initially_used_by_synchronous_machines

    def get_synchronous_machines(self) -> Any:
        """
        Getter method for synchronous machines
        """
        return self.synchronous_machines

    def set_coolant_temperature(self, new_val: Any) -> None:
        """
        Setter method for coolant temperature
        """
        self.coolant_temperature = new_val

    def set_equivalent_injection(self, new_val: Any) -> None:
        """
        Setter method for equivalent injection
        """
        self.equivalent_injection = new_val

    def set_hydrogen_pressure(self, new_val: Any) -> None:
        """
        Setter method for hydrogen pressure
        """
        self.hydrogen_pressure = new_val

    def set_initially_used_by_synchronous_machines(self, new_val: Any) -> None:
        """
        Setter method for initially used by synchronous machines
        """
        self.initially_used_by_synchronous_machines = new_val

    def set_synchronous_machines(self, new_val: Any) -> None:
        """
        Setter method for synchronous machines
        """
        self.synchronous_machines = new_val
