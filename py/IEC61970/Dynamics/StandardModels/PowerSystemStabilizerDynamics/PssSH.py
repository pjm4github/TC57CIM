# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:03:17 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import \
    PowerSystemStabilizerDynamics


class PssSH(PowerSystemStabilizerDynamics):
    """
    Model for Siemens "H infinity" power system stabilizer with generator
    electrical power input.
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        super().__init__()
        self.k: PU = PU(1)   # Main gain (K).  Typical Value = 1.
        self.k0: PU = PU(0.012)    # Gain 0 (K0).  Typical Value = 0.012
        self.k1: PU = PU(0.488)    # Gain 1 (K1).  Typical Value = 0.488
        self.k2: PU = PU(0.064)    # Gain 2 (K2).  Typical Value = 0.064
        self.k3: PU = PU(0.224)    # Gain 3 (K3).  Typical Value = 0.224
        self.k4: PU = PU(0.1)    # Gain 4 (K4).  Typical Value = 0.1.
        self.t1: Seconds = Seconds(0.076)  # Time constant 1 (T1).  Typical Value = 0.076.
        self.t2: Seconds = Seconds(0.086)  # Time constant 2 (T2).  Typical Value = 0.086.
        self.t3: Seconds = Seconds(1.068)  # Time constant 3 (T3).   Typical Value = 1.068.
        self.t4: Seconds = Seconds(1.913)  # Time constant 4 (T4).  Typical Value = 1.913.
        self.td: Seconds = Seconds(10)  # Input time constant (Td).  Typical Value = 10.
        self.vsmax: PU = PU(0.1)  # Output maximum limit (Vsmax).  Typical Value = 0.1.
        self.vsmin: PU = PU(-0.1)   # Output minimum limit (Vsmin).  Typical Value = -0.1
