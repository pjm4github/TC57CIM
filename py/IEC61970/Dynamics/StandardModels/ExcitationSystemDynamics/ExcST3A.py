# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from IEC61970.Base.Domain.AngleDegrees import AngleDegrees
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcSt3A(ExcitationSystemDynamics):
    """
    Modified IEEE ST3A static excitation system with added speed multiplier.
    """

    def __init__(self) -> None:
        super().__init__()
        self.efdmax: PU = PU(6.9)  # Maximum AVR output (Efdmax).  Typical Value = 6.9.
        self.kc: PU = PU(1.1) # Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 1.1.
        self.kg: PU = PU(1)   # Feedback gain constant of the inner loop field regulator (Kg).  Typical Value = 1.
        self.ki: PU = PU(4.83)  # Potential circuit gain coefficient (Ki).  Typical Value = 4.83.
        self.kj: PU = PU(200)  # AVR gain (Kj).  Typical Value = 200.
        self.km: PU = PU(7.04)  # Forward gain constant of the inner loop field regulator (Km).  Typical Value = 7.04.
        self.kp: PU = PU(4.37)  # Potential source gain (Kp) (>0).  Typical Value = 4.37.
        self.ks: PU = PU(0)   # Coefficient to allow different usage of the model-speed coefficient (Ks). Typical Value = 0.
        self.ks1: PU = PU(0)   # Coefficient to allow different usage of the model-speed coefficient (Ks1). Typical Value = 0.
        self.tb: Seconds = Seconds(6.67)  # Voltage regulator time constant (Tb).  Typical Value = 6.67.
        self.tc: Seconds = Seconds(1.0)  # Voltage regulator time constant (Tc).  Typical Value = 1.
        self.thetap: AngleDegrees = AngleDegrees(20) # Potential circuit phase angle (thetap).  Typical Value = 20.
        self.tm: Seconds = Seconds(1)  # Forward time constant of inner loop field regulator (Tm).  Typical Value = 1.
        self.vbmax: PU = PU(8.63)  # Maximum excitation voltage (Vbmax).  Typical Value = 8.63.
        self.vgmax: PU = PU(6.53)  # Maximum inner loop feedback voltage (Vgmax).  Typical Value = 6.53.
        self.vimax: PU = PU(0.2)  # Maximum voltage regulator input limit (Vimax).  Typical Value = 0.2.
        self.vimin: PU = PU(-0.2)  # Minimum voltage regulator input limit (Vimin).  Typical Value = -0.2.
        self.vrmax: PU = PU(1.0)  # Maximum voltage regulator output (Vrmax).  Typical Value = 1.
        self.vrmin: PU = PU(0.0)  # Minimum voltage regulator output (Vrmin).  Typical Value = 0.
        self.xl: PU = PU(0.09)  # Reactance associated with potential source (Xl).  Typical Value = 0.09.
