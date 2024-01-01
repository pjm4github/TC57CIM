# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from datetime import datetime
from typing import Optional, Union

class ExcSExs:
    """
    Simplified Excitation System Model.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:18 PM
    """

    def __init__(self) -> None:
        """
        Constructor for ExcSExs
        """

        # Field voltage clipping maximum limit (Efdmax).  Typical Value = 5.
        self.efdmax: Optional[float] = 5.0

        # Field voltage clipping minimum limit (Efdmin).  Typical Value = -5.
        self.efdmin: Optional[float] = -5.0

        # Maximum field voltage output (Emax).  Typical Value = 5.
        self.emax: Optional[float] = 5.0

        # Minimum field voltage output (Emin).  Typical Value = -5.
        self.emin: Optional[float] = -5.0

        # Gain (K) (>0).  Typical Value = 100.
        self.k: Optional[float] = 100.0

        # PI controller gain (Kc).  Typical Value = 0.08.
        self.kc: Optional[float] = 0.08

        # Ta/Tb - gain reduction ratio of lag-lead element (TaTb).  Typical Value = 0.1.
        self.tatb: Optional[float] = 0.1

        # Denominator time constant of lag-lead block (Tb).  Typical Value = 10.
        self.tb: Optional[float] = 10.0

        # PI controller phase lead time constant (Tc).  Typical Value = 0.
        self.tc: Optional[float] = 0.0

        # Time constant of gain block (Te).  Typical Value = 0.05.
        self.te: Optional[float] = 0.05
