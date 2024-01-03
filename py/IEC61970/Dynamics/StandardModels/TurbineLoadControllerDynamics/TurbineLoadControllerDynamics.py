# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:25:13 2023
from IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock import DynamicsFunctionBlock
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class TurbineLoadControllerDynamics(DynamicsFunctionBlock):
    """
    Turbine load controller function block whose behavior is described by reference
    to a standard model or by definition of a user-defined model.
    """

    def __init__(self):
        super().__init__()
        self.turbine_governor_dynamics = TurbineGovernorDynamics()  # Turbine-governor controlled by this turbine load controller
