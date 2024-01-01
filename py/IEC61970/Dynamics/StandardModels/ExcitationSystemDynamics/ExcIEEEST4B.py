# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIeeeSt4B(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type ST4B model. This model is a
    variation of the Type ST3A model, with a proportional plus integral (PI)
    regulator block replacing the lag-lead regulator characteristic that is in the
    ST3A model. Both potential and compound source rectifier excitation systems are
    modeled. The PI regulator blocks have non-windup limits that are represented.
    The voltage regulator of this model is typically implemented digitally.

    Reference: IEEE Standard 421.5-2005 Section 7.4.
    """

    def __init__(self) -> None:
        """
        Constructor for ExcIEEEST4B
        """
        super().__init__()
        self.kc: Optional[float] = 0.113
        # Rectifier loading factor proportional to commutating reactance (K_C).
        # Typical Value = 0.113.

        self.kg: Optional[float] = 0.0
        # Feedback gain constant of the inner loop field regulator (K_G).
        # Typical Value = 0.

        self.ki: Optional[float] = 0.0
        # Potential circuit gain coefficient (K_I).  Typical Value = 0.

        self.kim: Optional[float] = 0.0
        # Voltage regulator integral gain output (K_IM).  Typical Value = 0.

        self.kir: Optional[float] = 1.0
        # Voltage regulator integral gain (K_IR).  Typical Value = 10.75.

        self.kp: Optional[float] = 9.3
        # Potential circuit gain coefficient (K_P).  Typical Value = 9.3.

        self.kpm: Optional[float] = 1.0
        # Voltage regulator proportional gain output (K_PM).  Typical Value = 1.

        self.kpr: Optional[float] = 10.75
        # Voltage regulator proportional gain (K_PR).  Typical Value = 10.75.

        self.ta: Optional[float] = 0.02
        # Voltage regulator time constant (T_A). Typical Value = 0.02.

        self.thetap: Optional[float] = 0.0
        # Potential circuit phase angle (theta_p).  Typical Value = 0.

        self.vb_max: Optional[float] = 1.0
        # Maximum excitation voltage (V_Bmax).  Typical Value = 11.63.

        self.vm_max: Optional[float] = 11.63
        # Maximum inner loop output (V_Mmax).  Typical Value = 99.

        self.vm_min: Optional[float] = -99.
        # Minimum inner loop output (V_Mmin).  Typical Value = -99.

        self.vr_max: Optional[float] = 1.0
        # Maximum voltage regulator output (V_Rmax).  Typical Value = 1.

        self.vr_min: Optional[float] = -0.87
        # Minimum voltage regulator output (V_Rmin).  Typical Value = -0.87.

        self.xl: Optional[float] = 0.124
        # Reactance associated with potential source (X_L).  Typical Value = 0.124.
