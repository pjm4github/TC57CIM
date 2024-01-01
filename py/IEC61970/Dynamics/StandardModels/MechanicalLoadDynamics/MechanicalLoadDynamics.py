# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 16:59:22 2023
from typing import Any

from IEC61970.Dynamics.StandardModels.AsynchronousMachineDynamics.AsynchronousMachineDynamics import \
    AsynchronousMachineDynamics
from IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock
from IEC61970.Dynamics.StandardModels.SynchronousMachineDynamics.SynchronousMachineDynamics import \
    SynchronousMachineDynamics


class MechanicalLoadDynamics(DynamicsFunctionBlock):
    """
    Mechanical load function block whose behavior is described by reference to a
    standard model <font color="#0f0f0f">or by definition of a user-defined model.
    </font>
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()
        self.asynchronous_machine_dynamics: AsynchronousMachineDynamics = AsynchronousMachineDynamics()  # Asynchronous machine model with which this mechanical load model is associated.
        self.synchronous_machine_dynamics: SynchronousMachineDynamics = SynchronousMachineDynamics()  # Synchronous machine model with which this mechanical load model is associated
