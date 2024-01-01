# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:03:17 2023
from typing import Any

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import \
    PowerSystemStabilizerDynamics


class PssSB4(PowerSystemStabilizerDynamics):

    def __init__(self) -> None:
        super().__init__()
        self.kx: Any  # Gain (Kx)
        self.ta: Seconds = Seconds()  # Time constant (Ta)
        self.tb: Seconds = Seconds()  # Time constant (Tb)
        self.tc: Seconds = Seconds()  # Time constant (Tc)
        self.td: Seconds = Seconds()  # Time constant (Td)
        self.te: Seconds = Seconds()  # Time constant (Te)
        self.tt: Seconds = Seconds()  # Time constant (Tt)
        self.tx1: Seconds = Seconds()  # Reset time constant (Tx1)
        self.tx2: Seconds = Seconds()  # Time constant (Tx2)
        self.vsmax: PU = PU()  # Limiter (Vsmax)
        self.vsmin: PU = PU()  # Limiter (Vsmin)
