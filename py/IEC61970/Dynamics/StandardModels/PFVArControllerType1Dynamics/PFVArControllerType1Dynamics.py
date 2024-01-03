# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:02:02 2023
from IEC61970.Dynamics.StandardInterconnections.RemoteInputSignal import RemoteInputSignal
from IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class PFVArControllerType1Dynamics(DynamicsFunctionBlock):
    """
    Power Factor or VAr controller Type I function block whose behaviour is
    described by reference to a standard model or by definition of a user-defined model.
    """

    def __init__(self) -> None:
        """
        Constructor for PFVarControllerType1Dynamics
        """

        # Excitation system model with which this Power Factor or VAr controller Type I model is associated.
        super().__init__()
        self.excitation_system_dynamics: ExcitationSystemDynamics = ExcitationSystemDynamics()

        # Remote input signal used by this Power Factor or VAr controller Type I model.
        self.remote_input_signal: RemoteInputSignal = RemoteInputSignal()
