# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
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
        self.ka: PU = PU()  # Voltage regulator gain (Ka).  Typical Value = 200.
        self.kc: PU = PU()  # Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 0.
        self.ta: Seconds = Seconds()  # Voltage regulator time constant (Ta).  Typical Value = 0.015.
        self.tb: Seconds = Seconds()  # Voltage regulator time constant (Tb).  Typical Value = 10.
        self.tc: Seconds = Seconds()  # Voltage regulator time constant (Tc).  Typical Value = 1.
        self.vimax: PU = PU()  # Maximum voltage regulator input limit (Vimax).  Typical Value = 10.
        self.vimin: PU = PU()  # Minimum voltage regulator input limit (Vimin).  Typical Value = -10.
        self.vrmax: PU = PU()  # Maximum voltage regulator output (Vrmax).  Typical Value = 5.64.
        self.vrmin: PU = PU()  # Minimum voltage regulator output (Vrmin).  Typical Value = -4.53.
