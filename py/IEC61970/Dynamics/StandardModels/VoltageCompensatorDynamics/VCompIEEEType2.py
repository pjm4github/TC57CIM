# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:28:11 2023
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.VoltageCompensatorDynamics.VoltageCompensatorDynamics import \
    VoltageCompensatorDynamics


class VCompIEEEType2(VoltageCompensatorDynamics):
    """
    The class represents the terminal voltage transducer and 
    the load compensator as defined in the IEEE Std 421.5-2005, Section 4. 
    This model is designed to cover the following types of compensation:
    
    - reactive droop
    - transformer-drop or line-drop compensation
    - reactive differential compensation known also as cross-current compensation.
    
    Reference: IEEE Standard 421.5-2005, Section 4.
    """
    
    def __init__(self) -> None:
        super().__init__()
        self.tr: Seconds = Seconds()  # Time constant which is used for the combined voltage sensing and compensation signal (Tr).
