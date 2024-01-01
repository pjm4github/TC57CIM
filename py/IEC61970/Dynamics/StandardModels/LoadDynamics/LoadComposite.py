# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 16:32:51 2023
from datetime import datetime
from typing import Optional

from IEC61970.Dynamics.StandardModels.LoadDynamics.LoadDynamics import LoadDynamics


class LoadComposite(LoadDynamics):
    """
    This model combines static load and induction motor load effects.
    The dynamics of the motor are simplified by linearizing the induction machine
    equations.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """

    def __init__(self) -> None:
        # Active load-frequency dependence index (dynamic) (Epfd).  Typical Value = 1.5.
        super().__init__()
        self.epfd: Optional[float] = 1.5

        # Active load-frequency dependence index (static) (Epfs).  Typical Value = 1.5.
        self.epfs: Optional[float] = 1.5

        # Active load-voltage dependence index (dynamic) (Epvd).  Typical Value = 0.7.
        self.epvd: Optional[float] = 0.7

        # Active load-voltage dependence index (static) (Epvs).  Typical Value = 0.7.
        self.epvs: Optional[float] = 0.7

        # Reactive load-frequency dependence index (dynamic) (Eqfd).  Typical Value = 0.
        self.eqfd: Optional[float] = 0.0

        # Reactive load-frequency dependence index (static) (Eqfs).  Typical Value = 0.
        self.eqfs: Optional[float] = 0.0

        # Reactive load-voltage dependence index (dynamic) (Eqvd).  Typical Value = 2.
        self.eqvd: Optional[float] = 2.0

        # Reactive load-voltage dependence index (static) (Eqvs).  Typical Value = 2.
        self.eqvs: Optional[float] = 2.0

        # Inertia constant (H).  Typical Value = 2.5.
        self.h: Optional[float] = 2.5

        # Loading factor - ratio of initial P to motor MVA base (Lfrac).  Typical Value = 0.8.
        self.l_frac: Optional[float] = 0.8

        # Fraction of constant-power load to be represented by this motor model (Pfrac)
        # (>=0.0 and <=1.0).  Typical Value = 0.5.
        self.p_frac: Optional[float] = 0.5
