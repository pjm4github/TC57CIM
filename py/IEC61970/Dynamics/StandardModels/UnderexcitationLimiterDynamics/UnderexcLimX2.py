from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.UnderexcitationLimiterDynamics.UnderexcitationLimiterDynamics import \
    UnderexcitationLimiterDynamics


class UnderexcLimX2(UnderexcitationLimiterDynamics):
    """
    <font color="#0f0f0f">Westinghouse minimum excitation limiter.</font>
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """
    def __init__(self):
        super().__init__()
        self.kf2 = PU()  # Differential gain (Kf2).
        self.km = PU()  # Minimum excitation limit gain (Km).
        self.melmax = PU()  # Minimum excitation limit value (MELMAX).
        self.qo = PU()  # Excitation center setting (Qo).
        self.r = PU()  # Excitation radius (R).
        self.tf2 = Seconds()  # Differential time constant (Tf2) (>0).
        self.tm = Seconds()  # Minimum excitation limit time constant (Tm).
