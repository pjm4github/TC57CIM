# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 16:32:51 2023
from datetime import datetime
from typing import Optional


class LoadComposite:
    """
    This model combines static load and induction motor load effects.
    The dynamics of the motor are simplified by linearizing the induction machine
    equations.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """

    def __init__(self) -> None:
        """
        Active load-frequency dependence index (dynamic) (Epfd).  Typical Value = 1.5.
        """
        self.epfd: Optional[float] = None
        """
        Active load-frequency dependence index (static) (Epfs).  Typical Value = 1.5.
        """
        self.epfs: Optional[float] = None
        """
        Active load-voltage dependence index (dynamic) (Epvd).  Typical Value = 0.7.
        """
        self.epvd: Optional[float] = None
        """
        Active load-voltage dependence index (static) (Epvs).  Typical Value = 0.7.
        """
        self.epvs: Optional[float] = None
        """
        Reactive load-frequency dependence index (dynamic) (Eqfd).  Typical Value = 0.
        """
        self.eqfd: Optional[float] = None
        """
        Reactive load-frequency dependence index (static) (Eqfs).  Typical Value = 0.
        """
        self.eqfs: Optional[float] = None
        """
        Reactive load-voltage dependence index (dynamic) (Eqvd).  Typical Value = 2.
        """
        self.eqvd: Optional[float] = None
        """
        Reactive load-voltage dependence index (static) (Eqvs).  Typical Value = 2.
        """
        self.eqvs: Optional[float] = None
        """
        Inertia constant (H).  Typical Value = 2.5.
        """
        self.h: Optional[float] = None
        """
        Loading factor - ratio of initial P to motor MVA base (Lfrac).  Typical Value = 0.8.
        """
        self.l_frac: Optional[float] = None
        """
        Fraction of constant-power load to be represented by this motor model (Pfrac)
        (>=0.0 and <=1.0).  Typical Value = 0.5.
        """
        self.p_frac: Optional[float] = None
