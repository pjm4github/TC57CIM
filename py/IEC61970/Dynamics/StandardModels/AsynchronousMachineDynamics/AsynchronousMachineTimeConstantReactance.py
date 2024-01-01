# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:57:45 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from typing import Optional

from IEC61970.Dynamics.StandardModels.AsynchronousMachineDynamics.AsynchronousMachineDynamics import \
    AsynchronousMachineDynamics


class AsynchronousMachineTimeConstantReactance(AsynchronousMachineDynamics):
    """Parameter Notes:
    - If X'' = X', a single cage (one equivalent rotor winding per
      axis) is modelled.
    - The "p" in the attribute names is a substitution for a "prime" in the
      usual parameter notation, e.g. tpo refers to T'o.
    
    The parameters used for models expressed in time constant reactance form
    include:
    - RotatingMachine.ratedS (MVAbase)
    - RotatingMachineDynamics.damping (D)
    - RotatingMachineDynamics.inertia (H)
    - RotatingMachineDynamics.saturationFactor (S1)
    - RotatingMachineDynamics.saturationFactor120 (S12)
    - RotatingMachineDynamics.statorLeakageReactance (Xl)
    - RotatingMachineDynamics.statorResistance (Rs)
    - .xs (Xs)
    - .xp (X')
    - .xpp (X'')
    - .tpo (T'o)
    - .tppo (T''o).
    """

    def __init__(self) -> None:
        super().__init__()

        self.tpo: Optional[Seconds] = Seconds(5)  # Transient rotor time constant (T'o) (> T''o). Typical Value = 5.
        self.tppo: Optional[Seconds] = Seconds(0.03)  # Subtransient rotor time constant (T''o) (> 0). Typical Value = 0.03.
        self.xp: Optional[PU] = PU(0.5)  # Transient reactance (unsaturated) (X') (>=X''). Typical Value = 0.5.
        self.xpp: Optional[PU] = PU(0.2)  # Subtransient reactance (unsaturated) (X'') (> Xl). Typical Value = 0.2.
        self.xs: Optional[PU] = PU(1.8)  # Synchronous reactance (Xs) (>= X'). Typical Value = 1.8.
