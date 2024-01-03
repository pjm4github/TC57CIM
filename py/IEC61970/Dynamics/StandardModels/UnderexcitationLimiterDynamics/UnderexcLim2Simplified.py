from IEC61970.Base.Domain.PU import PU
from IEC61970.Dynamics.StandardModels.UnderexcitationLimiterDynamics.UnderexcitationLimiterDynamics import \
    UnderexcitationLimiterDynamics


class UnderexcLim2Simplified(UnderexcitationLimiterDynamics):
    """
    This model can be derived from UnderexcLimIEEE2.
    The limit characteristic (look-up table) is a single straight-line, the same
    as UnderexcLimIEEE2 (see Figure 10.4 (p 32), IEEE 421.5-2005 Section 10.2).
    """

    def __init__(self, kui=0.1, p0=0, p1=1, q0=-0.31, q1=-0.1, vuimax=1, vuimin=0):
        super().__init__()
        self.kui = PU(kui)  # Gain Under excitation limiter (Kui)
        self.p0 = PU(p0)  # Segment P initial point (P0)
        self.p1 = PU(p1)  # Segment P end point (P1)
        self.q0 = PU(q0)  # Segment Q initial point (Q0)
        self.q1 = PU(q1)  # Segment Q end point (Q1)
        self.vuimax = PU(vuimax)  # Maximum error signal (V_UImax)
        self.vuimin = PU(vuimin)  # Minimum error signal (V_UImin)
