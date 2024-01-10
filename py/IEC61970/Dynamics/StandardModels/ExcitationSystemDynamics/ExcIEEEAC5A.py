# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIeeeAc5A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type AC5A model. The model represents
    a simplified model for brushless excitation systems. The regulator is supplied
    from a source, such as a permanent magnet generator, which is not affected by
    system disturbances. Unlike other ac models, this model uses loaded rather
    than open circuit exciter saturation data in the same way as it is used for the
    dc models. Because the model has been widely implemented by the industry, it
    is sometimes used to represent other types of systems when either detailed data
    for them are not available or simplified models are required.

    Reference: IEEE Standard 421.5-2005 Section 6.5.
    """

    def __init__(self) -> None:
        super().__init__()
        self.efd1: float = 1.0
        self.efd2: float = 1.0
        self.ka: float = 1.0
        self.ke: float = 1.0
        self.kf: float = 1.0
        self.seefd1: float = 1.0
        self.seefd2: float = 1.0
        self.ta: Seconds = Seconds(1.0)
        self.te: Seconds = Seconds(1.0)
        self.tf1: Seconds = Seconds(1.0)
        self.tf2: Seconds = Seconds(1.0)
        self.tf3: Seconds = Seconds(1.0)
        self.vrmax: float = 1.0
        self.vrmin: float = 1.0
