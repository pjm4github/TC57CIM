# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:00:52 2023
from IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class OverexcitationLimiterDynamics(DynamicsFunctionBlock):
    """
    Overexcitation limiter function block whose
    behaviour is described by reference to a standard model
    or by definition of a user-defined model.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """



    def __init__(self) -> None:
        super().__init__()

        # 	 * Excitation system model with which this overexcitation limiter model is
        # 	 * associated.
        self.excitation_system_dynamics: ExcitationSystemDynamics = ExcitationSystemDynamics()