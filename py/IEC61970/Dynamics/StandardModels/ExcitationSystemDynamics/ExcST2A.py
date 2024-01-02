# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional, Union

from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcSt2a(ExcitationSystemDynamics):
    """
    Modified IEEE ST2A static excitation system - another lead-lag block added to
    match  the model defined by WECC.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:18 PM
    """

    def __init__(self) -> None:
        """
        Voltage regulator gain (Ka).  Typical Value = 120.
        """
        super().__init__()
        self.ka: float = 120.0

        """
        Rectifier loading factor proportional to commutating reactance (Kc).  Typical
        Value = 1.82.
        """
        self.kc: float = 1.82

        """
        Exciter constant related to self-excited field (Ke).  Typical Value = 1.
        """
        self.ke: float = 1.0

        """
        Excitation control system stabilizer gains (Kf).  Typical Value = 0.05.
        """
        self.kf: float = 0.05

        """
        Potential circuit gain coefficient (Ki).  Typical Value = 8.
        """
        self.ki: float = 8.0

        """
        Potential circuit gain coefficient (Kp).  Typical Value = 4.88.
        """
        self.kp: float = 4.88

        """
        Voltage regulator time constant (Ta).  Typical Value = 0.15.
        """
        self.ta: Seconds = Seconds(0.15)

        """
        Voltage regulator time constant (Tb).  Typical Value = 0.
        """
        self.tb: Seconds = Seconds(0.0)

        """
        Voltage regulator time constant (Tc).  Typical Value = 0.
        """
        self.tc: Seconds = Seconds(0.0)

        """
        Exciter time constant, integration rate associated with exciter control (Te).
        Typical Value = 0.5.
        """
        self.te: Seconds = Seconds(0.5)

        """
        Excitation control system stabilizer time constant (Tf).  Typical Value = 0.7.
        """
        self.tf: Seconds = Seconds(0.7)

        """
        UEL input (UELin).
        true = HV gate
        false = add to error signal.
        Typical Value = false.
        """
        self.uelin: bool = False

        """
        Maximum voltage regulator outputs (Vrmax).  Typical Value = 1.
        """
        self.vrmax: float = 1.0

        """
        Minimum voltage regulator outputs (Vrmin).  Typical Value = -1.
        """
        self.vrmin: float = -1.0
