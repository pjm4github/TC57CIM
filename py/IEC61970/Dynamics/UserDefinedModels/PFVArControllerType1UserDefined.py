# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:51:45 2023
from IEC61970.Dynamics.StandardModels.PFVArControllerType1Dynamics.PFVArControllerType1Dynamics import \
    PFVArControllerType1Dynamics


class PFVArControllerType1UserDefined(PFVArControllerType1Dynamics):
    """ 
    Power Factor or VAr controller Type I function block 
    whose dynamic behaviour is described by a user-defined model.
    """

    def __init__(self) -> None:
        super().__init__()
        self.proprietary: bool
