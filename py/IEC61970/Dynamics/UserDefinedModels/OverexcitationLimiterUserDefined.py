# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:51:45 2023
from IEC61970.Dynamics.StandardModels.OverexcitationLimiterDynamics.OverexcitationLimiterDynamics import \
    OverexcitationLimiterDynamics


class OverexcitationLimiterUserDefined(OverexcitationLimiterDynamics):
    """
    Overexcitation limiter system function block whose dynamic behaviour is described by a user-defined model.
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()
        self.proprietary = False
