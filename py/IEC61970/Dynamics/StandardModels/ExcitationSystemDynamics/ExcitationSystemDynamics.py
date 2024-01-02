# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock
from IEC61970.Dynamics.StandardModels.SynchronousMachineDynamics.SynchronousMachineDynamics import \
    SynchronousMachineDynamics


class ExcitationSystemDynamics(DynamicsFunctionBlock):
    """
    Excitation system function block whose behavior is described by reference to a
    standard model <font color="#0f0f0f">or by definition of a user-defined model.
    </font>
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:18 PM
    """
    def __init__(self) -> None:
        super().__init__()
        self.synchronous_machine_dynamics: SynchronousMachineDynamics = SynchronousMachineDynamics()
