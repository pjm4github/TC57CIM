from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.UnderexcitationLimiterDynamics.UnderexcitationLimiterDynamics import \
    UnderexcitationLimiterDynamics


class UnderexcLimX1(UnderexcitationLimiterDynamics):
    def __init__(self):
        super().__init__()
        self.k = PU()  # Minimum excitation limit slope (K) (>0).
        self.kf2 = PU()  # Differential gain (Kf2).
        self.km = PU()  # Minimum excitation limit gain (Km).
        self.melmax = PU()  # Minimum excitation limit value (MELMAX).
        self.tf2 = Seconds()  # Differential time constant (Tf2) (>0).
        self.tm = Seconds()  # Minimum excitation limit time constant (Tm).
