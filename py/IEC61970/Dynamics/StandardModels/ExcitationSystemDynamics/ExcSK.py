# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Base.Domain.Seconds import Seconds


class ExcSk:
    """
    Slovakian Excitation System Model.  UEL and secondary voltage control are
    included in this model. When this model is used, there cannot be a separate
    underexcitation limiter or VAr controller model.
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        # Field voltage clipping limit (Efdmax)
        self.efd_max: float = 1.0

        # Field voltage clipping limit (Efdmin)
        self.efd_min: float = 1.0

        # Maximum field voltage output (Emax). Typical Value = 20.
        self.emax: float = 20.0

        # Minimum field voltage output (Emin). Typical Value = -20.
        self.emin: float = -20.0

        # Gain (K). Typical Value = 1.
        self.k: float = 1.0

        # Parameter of underexcitation limit (K1). Typical Value = 0.1364.
        self.k1: float = 0.1364

        # Parameter of underexcitation limit (K2). Typical Value = -0.3861.
        self.k2: float = -0.3861

        # PI controller gain (Kc). Typical Value = 70.
        self.kc: float = 70.0

        # Rectifier regulation factor (Kce). Typical Value = 0.
        self.kce: float = 0.0

        # Exciter internal reactance (Kd). Typical Value = 0.
        self.kd: float = 0.0

        # P controller gain (Kgob). Typical Value = 10.
        self.kgob: float = 10.0

        # PI controller gain (Kp). Typical Value = 1.
        self.kp: float = 1.0

        # PI controller gain of integral component (Kqi).
        # Typical Value = 0.
        self.kqi: float = 0.0

        # Rate of rise of the reactive power (Kqob).
        self.kqob: float = 0.0

        # PI controller gain (Kqp). Typical Value = 0.
        self.kqp: float = 0.0

        # Dead band of reactive power (nq). Determines the range of sensitivity.
        # Typical Value = 0.001.
        self.nq: float = 0.001

        # Secondary voltage control state (Qc_on_off).
        # True = secondary voltage control is ON
        # False = secondary voltage control is OFF. Typical Value = False.
        self.qc_on_off: bool = False

        # Desired value (setpoint) of reactive power, manual setting (Qz).
        self.qz: float = 1.0

        # Selector to apply automatic calculation in secondary controller model.
        # True = automatic calculation is activated
        # False = manual set is active; the use of desired value of reactive power (Qz) is required.
        # Typical Value = True.
        self.remote: bool = True

        # Apparent power of the unit (Sbase). Unit = MVA. Typical Value = 259.
        self.sbase: float = 259.0

        # PI controller phase lead time constant (Tc). Typical Value = 8.
        self.tc: Seconds = Seconds(8.0)

        # Time constant of gain block (Te). Typical Value = 0.1.
        self.te: Seconds = Seconds(0.1)

        # PI controller phase lead time constant (Ti). Typical Value = 2.
        self.ti: Seconds = Seconds(2.0)

        # Time constant (Tp). Typical Value = 0.1.
        self.tp: Seconds = Seconds(0.1)

        # Voltage transducer time constant (Tr). Typical Value = 0.01.
        self.tr: Seconds = Seconds(0.01)

        # Maximum error (Uimax). Typical Value = 10.
        self.uimax: float = 10.0

        # Minimum error (UImin). Typical Value = -10.
        self.uimin: float = -10.0

        # Maximum controller output (URmax). Typical Value = 10.
        self.urmax: float = 10.0

        # Minimum controller output (URmin). Typical Value = -10.
        self.urmin: float = -10.0

        # Maximum terminal voltage input (Vtmax). Determines the range of voltage dead
        # band. Typical Value = 1.05.
        self.vtmax: float = 1.05

        # Minimum terminal voltage input (Vtmin). Determines the range of voltage dead
        # band. Typical Value = 0.95.
        self.vtmin: float = 0.95

        # Maximum output (Yp). Minimum output = 0. Typical Value = 1.
        self.yp: float = 1.0
