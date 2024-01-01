# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional


class ExcBbc:
    """Transformer fed static excitation system (static with ABB regulator). This
    model represents a static excitation system in which a gated thyristor bridge
    fed by a transformer at the main generator terminals feeds the main generator
    directly.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:17 PM
    """

    def __init__(self) -> None:
        """Constructor"""

        # Maximum open circuit exciter voltage (Efdmax).  Typical Value = 5.
        self.efd_max: Optional[float] = 1.0

        # Minimum open circuit exciter voltage (Efdmin).  Typical Value = -5.
        self.efd_min: Optional[float] = 1.0

        # Steady state gain (K).  Typical Value = 300.
        self.k: Optional[float] = 1.0

        # Supplementary signal routing selector (switch).
        # True = Vs connected to 3rd summing point
        # False = Vs connected to 1st summing point (see diagram).
        # Typical Value = True.
        self.switch: Optional[bool] = False

        # Controller time constant (T1).  Typical Value = 6.
        self.t1: Optional[float] = 1.0

        # Controller time constant (T2).  Typical Value = 1.
        self.t2: Optional[float] = 1.0

        # Lead/lag time constant (T3).  Typical Value = 0.05.
        self.t3: Optional[float] = 1.0

        # Lead/lag time constant (T4).  Typical Value = 0.01.
        self.t4: Optional[float] = 1.0

        # Maximum control element output (Vrmax).  Typical Value = 5.
        self.vr_max: Optional[float] = 1.0

        # Minimum control element output (Vrmin).  Typical Value = -5.
        self.vr_min: Optional[float] = 1.0

        # Effective excitation transformer reactance (Xe).  Typical Value = 0.05.
        self.xe: Optional[float] = 1.0
