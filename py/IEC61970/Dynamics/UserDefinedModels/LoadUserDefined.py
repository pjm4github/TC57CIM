# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:51:45 2023
from IEC61970.Dynamics.StandardModels.LoadDynamics.LoadDynamics import LoadDynamics


class LoadUserDefined(LoadDynamics):
    """
    Load whose dynamic behaviour is described by a user-defined model.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:21:46 PM
    """

    def __init__(self) -> None:
        """
        Constructor for LoadUserDefined
        """
        super().__init__()
        self.proprietary = False
