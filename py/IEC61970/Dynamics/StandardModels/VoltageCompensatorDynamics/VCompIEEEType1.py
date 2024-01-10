# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:28:11 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.VoltageCompensatorDynamics.VoltageCompensatorDynamics import \
    VoltageCompensatorDynamics


class VCompIeeeType1(VoltageCompensatorDynamics):
    """
    The class represents the terminal voltage transducer and
    the load compensator as defined in the IEEE Std 421.5-2005,
    Section 4. This model is common to all excitation system models
    described in the IEEE Standard.

    Reference: IEEE Standard 421.5-2005 Section 4.
    """
    
    def __init__(self):
        super().__init__()
        self.rc = PU()  # Resistive component of compensation of a generator (Rc).
        self.tr = Seconds()  # Time constant which is used for the combined voltage sensing and compensation signal (Tr).
        self.xc = PU()  # Reactive component of compensation of a generator (Xc).
