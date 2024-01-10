# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:25:38 2023
from IEC61970.Dynamics.StandardInterconnections.RemoteInputSignal import RemoteInputSignal
from IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class UnderexcitationLimiterDynamics(DynamicsFunctionBlock):
    """
    Underexcitation limiter function block whose behaviour is described by
    reference to a standard model <font color="#0f0f0f">or by definition of a
    user-defined model.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()
        self.excitation_system_dynamics: ExcitationSystemDynamics = ExcitationSystemDynamics()  # Excitation system
        # model with which this underexcitation limiter model is associated
        self.remote_input_signal: RemoteInputSignal = RemoteInputSignal()  # Remote input signal used by this
        # underexcitation limiter model
