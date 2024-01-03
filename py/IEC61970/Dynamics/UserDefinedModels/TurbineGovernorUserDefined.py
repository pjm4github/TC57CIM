# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:51:45 2023
from IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics import TurbineGovernorDynamics


class TurbineGovernorUserDefined(TurbineGovernorDynamics):
    """Turbine-governor function block whose dynamic behaviour is described by a user-defined model."""
    
    def __init__(self) -> None:
        super().__init__()
        """
        Behaviour is based on a proprietary model as opposed to a detailed model.
        True = user-defined model is proprietary with behaviour mutually understood by
        sending and receiving applications and parameters passed as general attributes.
        False = user-defined model is explicitly defined in terms of control blocks and
        their input and output signals.
        """
        self.proprietary = False
