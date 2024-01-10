# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from IEC61970.Base.Domain.Seconds import Seconds


class ExcScrx:
    """
    Simple excitation system model representing generic characteristics of many
    excitation systems; intended for use where negative field current may be a
    problem.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:18 PM
    """
    
    def __init__(self) -> None:
        """
        Power source switch (Cswitch).
        True = fixed voltage of 1.0 PU
        False = generator terminal voltage.
        """
        self.c_switch: bool = False

        # Maximum field voltage output (Emax).  Typical Value = 5.
        self.emax: float = 5.0

        # Minimum field voltage output (Emin).  Typical Value = 0.
        self.emin: float = 0.0

        # Gain (K) (>0).  Typical Value = 200.
        self.k: float = 200.0

        # Rc/Rfd - ratio of field discharge resistance to field winding resistance        (RcRfd).  Typical Value = 0.
        self.rcrfd: float = 0.0

        # Ta/Tb - gain reduction ratio of lag-lead element (TaTb). The parameter Ta         is not defined explicitly.  Typical Value = 0.1.
        self.tatb: Seconds = Seconds(0.1)

        # Denominator time constant of lag-lead block (Tb).  Typical Value = 10.
        self.tb: Seconds = Seconds(10.0)

        # Time constant of gain block (Te) (>0).  Typical Value = 0.02.
        self.te: Seconds = Seconds(0.02)
