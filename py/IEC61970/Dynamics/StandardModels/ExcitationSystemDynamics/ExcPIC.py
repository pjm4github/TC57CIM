# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcPic(ExcitationSystemDynamics):
    """
    Proportional/Integral Regulator Excitation System Model. This model can be
    used to represent excitation systems with a proportional-integral (PI) voltage
    regulator controller.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:18 PM
    """

    def __init__(self) -> None:
        """
        Constructor for ExcPic
        """
        super().__init__()
        self.e1: PU = PU()  # Field voltage value 1 (E1). Typical Value = 0.
        self.e2: PU = PU()  # Field voltage value 2 (E2). Typical Value = 0.
        self.efdmax: PU = PU()  # Exciter maximum limit (Efdmax). Typical Value = 8.
        self.efdmin: PU = PU()  # Exciter minimum limit (Efdmin). Typical Value = -0.87.
        self.ka: PU = PU()  # PI controller gain (Ka). Typical Value = 3.15.
        self.kc: PU = PU()  # Exciter regulation factor (Kc). Typical Value = 0.08.
        self.ke: PU = PU()  # Exciter constant (Ke). Typical Value = 0.
        self.kf: PU = PU()  # Rate feedback gain (Kf). Typical Value = 0.
        self.ki: PU = PU()  # Current source gain (Ki). Typical Value = 0.
        self.kp: PU = PU()  # Potential source gain (Kp). Typical Value = 6.5.
        self.se1: PU = PU()  # Saturation factor at E1 (Se1). Typical Value = 0.
        self.se2: PU = PU()  # Saturation factor at E2 (Se2). Typical Value = 0.
        self.ta1: Seconds = Seconds()  # PI controller time constant (Ta1). Typical Value = 1.
        self.ta2: Seconds = Seconds()  # Voltage regulator time constant (Ta2). Typical Value = 0.01.
        self.ta3: Seconds = Seconds()  # Lead time constant (Ta3). Typical Value = 0.
        self.ta4: Seconds = Seconds()  # Lag time constant (Ta4). Typical Value = 0.
        self.te: Seconds = Seconds()  # Exciter time constant (Te). Typical Value = 0.
        self.tf1: Seconds = Seconds()  # Rate feedback time constant (Tf1). Typical Value = 0.
        self.tf2: Seconds = Seconds()  # Rate feedback lag time constant (Tf2). Typical Value = 0.
        self.vr1: PU = PU()  # PI maximum limit (Vr1). Typical Value = 1.
        self.vr2: PU = PU()  # PI minimum limit (Vr2). Typical Value = -0.87.
        self.vrmax: PU = PU()  # Voltage regulator maximum limit (Vrmax). Typical Value = 1.
        self.vrmin: PU = PU()  # Voltage regulator minimum limit (Vrmin). Typical Value = -0.87.
