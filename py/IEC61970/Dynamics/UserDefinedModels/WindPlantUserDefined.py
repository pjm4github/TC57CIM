# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:51:45 2023
from IEC61970.Dynamics.StandardModels.WindDynamics.WindPlantDynamics import WindPlantDynamics
from IEC61970.Dynamics.UserDefinedModels.ProprietaryParameterDynamics import ProprietaryParameterDynamics


class WindPlantUserDefined(WindPlantDynamics):
    """Wind plant function block whose dynamic behaviour is described by a user-defined model."""
    
    def __init__(self) -> None:
        super().__init__()
        self.proprietarybool = False  # Behaviour is based on proprietary model as opposed to detailed model.
        self.proprietary_parameter_dynamics = ProprietaryParameterDynamics()
