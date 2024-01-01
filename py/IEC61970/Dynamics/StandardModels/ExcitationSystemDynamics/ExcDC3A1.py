# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional, Type

class ExcDc3A1(ExcitationSystemDynamics):
    """
    This is modified old IEEE type 3 excitation system.
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:17 PM
    """

    def __init__(self) -> None:
        """
        Constructor for ExcDC3A1
        """

        self.exclim: Optional[bool] = False
        """
        (exclim).
        true = lower limit of zero is applied to integrator output
        false = lower limit of zero not applied to integrator output.
        Typical Value = True.
        """

        self.ka: Optional[float] = 1.0
        """
        Voltage regulator gain (Ka).  Typical Value = 300.
        """

        self.ke: Optional[float] = 1.0
        """
        Exciter constant related to self-excited field (Ke).  Typical Value = 1.
        """

        self.kf: Optional[float] = 1.0
        """
        Excitation control system stabilizer gain (Kf).  Typical Value = 0.1.
        """

        self.ki: Optional[float] = 1.0
        """
        Potential circuit gain coefficient (Ki).  Typical Value = 4.83.
        """

        self.kp: Optional[float] = 1.0
        """
        Potential circuit gain coefficient (Kp).  Typical Value = 4.37.
        """

        self.ta: Optional[float] = 1.0
        """
        Voltage regulator time constant (Ta).  Typical Value = 0.01.
        """

        self.te: Optional[float] = 1.0
        """
        Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1.83.
        """

        self.tf: Optional[float] = 1.0
        """
        Excitation control system stabilizer time constant (Tf).  Typical Value = 0.675.
        """

        self.vb1max: Optional[float] = 1.0
        """
        Available exciter voltage limiter (Vb1max).  Typical Value = 11.63.
        """

        self.vblim: Optional[bool] = False
        """
        Vb limiter indicator.
        true = exciter Vbmax limiter is active
        false = Vb1max is active.
        Typical Value = True.
        """

        self.vbmax: Optional[float] = 1.0
        """
        Available exciter voltage limiter (Vbmax).  Typical Value = 11.63.
        """

        self.vrmax: Optional[float] = 1.0
        """
        Maximum voltage regulator output (Vrmax).  Typical Value = 5.
        """

        self.vrmin: Optional[float] = 1.0
        """
        Minimum voltage regulator output (Vrmin).  Typical Value = 0.
        """
