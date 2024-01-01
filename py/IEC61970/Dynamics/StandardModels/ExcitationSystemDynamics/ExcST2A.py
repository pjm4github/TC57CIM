# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional, Union

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
        self.ka: Optional[float] = 120.0

        """
        Rectifier loading factor proportional to commutating reactance (Kc).  Typical
        Value = 1.82.
        """
        self.kc: Optional[float] = 1.82

        """
        Exciter constant related to self-excited field (Ke).  Typical Value = 1.
        """
        self.ke: Optional[float] = 1.0

        """
        Excitation control system stabilizer gains (Kf).  Typical Value = 0.05.
        """
        self.kf: Optional[float] = 0.05

        """
        Potential circuit gain coefficient (Ki).  Typical Value = 8.
        """
        self.ki: Optional[float] = 8.0

        """
        Potential circuit gain coefficient (Kp).  Typical Value = 4.88.
        """
        self.kp: Optional[float] = 4.88

        """
        Voltage regulator time constant (Ta).  Typical Value = 0.15.
        """
        self.ta: Optional[float] = 0.15

        """
        Voltage regulator time constant (Tb).  Typical Value = 0.
        """
        self.tb: Optional[float] = 0.0

        """
        Voltage regulator time constant (Tc).  Typical Value = 0.
        """
        self.tc: Optional[float] = 0.0

        """
        Exciter time constant, integration rate associated with exciter control (Te).
        Typical Value = 0.5.
        """
        self.te: Optional[float] = 0.5

        """
        Excitation control system stabilizer time constant (Tf).  Typical Value = 0.7.
        """
        self.tf: Optional[float] = 0.7

        """
        UEL input (UELin).
        true = HV gate
        false = add to error signal.
        Typical Value = false.
        """
        self.uelin: Optional[bool] = False

        """
        Maximum voltage regulator outputs (Vrmax).  Typical Value = 1.
        """
        self.vrmax: Optional[float] = 1.0

        """
        Minimum voltage regulator outputs (Vrmin).  Typical Value = -1.
        """
        self.vrmin: Optional[float] = -1.0
