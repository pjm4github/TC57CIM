# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.WindDynamics.WindGenTurbineType2IEC import WindGenTurbineType2IEC


class WindContRotorRIEC(IdentifiedObject):
    """Rotor resistance control model.

    Reference: IEC Standard 61400-27-1 Section 5.6.5.3.
    """
    def __init__(self) -> None:
        """Constructor method"""
        super().__init__()
        self.kirr: PU = PU()  # Integral gain in rotor resistance PI controller (K_Irr). It is type dependent parameter.
        self.komegafilt: float = 1.0  # Filter gain for generator speed measurement (K_omegafilt). It is type dependent parameter.
        self.kpfilt: float = 1.0  # Filter gain for power measurement (K_pfilt). It is type dependent parameter.
        self.kprr: PU = PU()  # Proportional gain in rotor resistance PI controller (K_Prr). It is type dependent parameter.
        self.rmax: PU = PU()  # Maximum rotor resistance (r_max). It is type dependent parameter.
        self.rmin: PU = PU()  # Minimum rotor resistance (r_min). It is type dependent parameter.
        self.tomegafiltrr: Seconds = Seconds()  # Filter time constant for generator speed measurement (T_omegafiltrr). It is type dependent parameter.
        self.tpfiltrr: Seconds = Seconds()  # Filter time constant for power measurement (T_pfilt_rr). It is type dependent parameter.
        self.wind_gen_turbine_type2_iec: Optional[WindGenTurbineType2IEC] = WindGenTurbineType2IEC()  # Wind turbine type 2 model with which this wind control rotor resistance model is associated.
