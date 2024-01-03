# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from IEC61970.Dynamics.StandardModels.AsynchronousMachineDynamics.AsynchronousMachineDynamics import \
    AsynchronousMachineDynamics
from IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock

class TurbineGovernorDynamics(DynamicsFunctionBlock):
    """
    Turbine-governor function block whose behavior is described by reference to a
    standard model or by definition of a user-defined model.
    """

    def __init__(self) -> None:
        """
        Constructor method
        """
        super().__init__()
        self.asynchronous_machine_dynamics: AsynchronousMachineDynamics = AsynchronousMachineDynamics()
