# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

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
        self.efd1: Optional[float] = 1.0
        self.efd2: Optional[float] = 1.0
        self.ka: Optional[float] = 1.0
        self.ke: Optional[float] = 1.0
        self.kf: Optional[float] = 1.0
        self.seefd1: Optional[float] = 1.0
        self.seefd2: Optional[float] = 1.0
        self.ta: Optional[float] = 1.0
        self.te: Optional[float] = 1.0
        self.tf1: Optional[float] = 1.0
        self.tf2: Optional[float] = 1.0
        self.tf3: Optional[float] = 1.0
        self.vrmax: Optional[float] = 1.0
        self.vrmin: Optional[float] = 1.0
