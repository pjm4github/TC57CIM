# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:51:45 2023
from typing import Optional

from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType3or4Dynamics import WindTurbineType3or4Dynamics
from IEC61970.Dynamics.UserDefinedModels.ProprietaryParameterDynamics import ProprietaryParameterDynamics


class WindType3Or4UserDefined(WindTurbineType3or4Dynamics):
    """
    Wind Type 3 or Type 4 function block whose dynamic behaviour is described by a user-defined model.
    @author civanov
    @version 1.0
    @created 29-Dec-2023 11:21:46 PM
    """

    def __init__(self) -> None:
        super().__init__()
        """
        Behaviour is based on proprietary model as opposed to detailed model.
        true = user-defined model is proprietary with behaviour mutually understood by 
        sending and receiving applications and parameters passed as general attributes.
        false = user-defined model is explicitly defined in terms of control blocks and 
        their input and output signals.
        """
        self.proprietarybool = False
        """
        Parameter of this proprietary user-defined model.
        """
        self.proprietary_parameter_dynamics = ProprietaryParameterDynamics()
