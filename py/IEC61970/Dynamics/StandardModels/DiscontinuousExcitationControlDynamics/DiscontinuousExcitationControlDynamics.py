# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:59:32 2023
from IEC61970.Dynamics.StandardInterconnections.RemoteInputSignal import RemoteInputSignal
from IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class DiscontinuousExcitationControlDynamics(DynamicsFunctionBlock):
    """
    Discontinuous excitation control function block whose behaviour is described by
    reference to a standard model <font color="#0f0f0f">or by definition of a user-
    defined model</font>.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:17 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        # 	 * Excitation system model with which this discontinuous excitation control model
        # 	 * is associated.

        super().__init__()
        self.excitation_system_dynamics: ExcitationSystemDynamics = ExcitationSystemDynamics()
        # 	 * Remote input signal used by this discontinuous excitation control system model.
        self.remote_input_signal: RemoteInputSignal = RemoteInputSignal()

