# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from IEC61970.Base.Domain.PU import PU

from IEC61970.Base.Domain.Seconds import Seconds
from typing import Optional

from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAc4A(ExcitationSystemDynamics):
    """
    Modified IEEE AC4A alternator-supplied rectifier excitation system with
    different minimum controller output.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:17 PM
    """


    def __init__(self) -> None:
        super().__init__()
        self.ka: Optional[PU] = PU()  # Voltage regulator gain (Ka).  Typical Value = 200.
        self.kc: Optional[PU] = PU()  # Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 0.
        self.ta: Optional[Seconds] = Seconds()  # Voltage regulator time constant (Ta).  Typical Value = 0.015.
        self.tb: Optional[Seconds] = Seconds()  # Voltage regulator time constant (Tb).  Typical Value = 10.
        self.tc: Optional[Seconds] = Seconds()  # Voltage regulator time constant (Tc).  Typical Value = 1.
        self.vimax: Optional[PU] = PU()  # Maximum voltage regulator input limit (Vimax).  Typical Value = 10.
        self.vimin: Optional[PU] = PU()  # Minimum voltage regulator input limit (Vimin).  Typical Value = -10.
        self.vrmax: Optional[PU] = PU()  # Maximum voltage regulator output (Vrmax).  Typical Value = 5.64.
        self.vrmin: Optional[PU] = PU()  # Minimum voltage regulator output (Vrmin).  Typical Value = -4.53.
