from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.UnderexcitationLimiterDynamics.UnderexcitationLimiterDynamics import \
    UnderexcitationLimiterDynamics


class UnderexcLimIEEE2(UnderexcitationLimiterDynamics):
    def __init__(self):
        super().__init__()
        self.k1 = 2.  # UEL terminal voltage exponent applied to real power input to UEL limit look-up table (k1).  Typical Value = 2.
        self.k2 = 2.  # UEL terminal voltage exponent applied to reactive power output from UEL limit look-up table (k2).  Typical Value = 2.
        self.kfb = PU(0)  # Gain associated with optional integrator feedback input signal to UEL (K_FB).  Typical Value = 0.
        self.kuf = PU(0)  # UEL excitation system stabilizer gain (K_UF).  Typical Value = 0.
        self.kui = PU(.5)  # UEL integral gain (K_UI).  Typical Value = 0.5.
        self.kul = PU(.8)  # UEL proportional gain (K_UL).  Typical Value = 0.8.
        self.p0 = PU(0)  # Real power values for endpoints (P_0).  Typical Value = 0.
        self.p1 = PU(.3)  # Real power values for endpoints (P_1).  Typical Value = 0.3.
        self.p10 = PU()  # Real power values for endpoints (P_10).
        self.p2 = PU(.6)  # Real power values for endpoints (P_2).  Typical Value = 0.6.
        self.p3 = PU(.9)  # Real power values for endpoints (P_3).  Typical Value = 0.9.
        self.p4 = PU(1.02)  # Real power values for endpoints (P_4).  Typical Value = 1.02.
        self.p5 = PU()  # Real power values for endpoints (P_5).
        self.p6 = PU()  # Real power values for endpoints (P_6).
        self.p7 = PU()  # Real power values for endpoints (P_7).
        self.p8 = PU()  # Real power values for endpoints (P_8).
        self.p9 = PU()  # Real power values for endpoints (P_9).
        self.q0 = PU(-.31)  # Reactive power values for endpoints (Q_0).  Typical Value = -0.31.
        self.q1 = PU(.31)  # Reactive power values for endpoints (Q_1).  Typical Value = -0.31.
        self.q10 = PU()  # Reactive power values for endpoints (Q_10).
        self.q2 = PU(-.28)  # Reactive power values for endpoints (Q_2).  Typical Value = -0.28.
        self.q3 = PU(-.21)  # Reactive power values for endpoints (Q_3).  Typical Value = -0.21.
        self.q4 = PU(0)  # Reactive power values for endpoints (Q_4).  Typical Value = 0.
        self.q5 = PU()  # Reactive power values for endpoints (Q_5).
        self.q6 = PU()  # Reactive power values for endpoints (Q_6).
        self.q7 = PU()  # Reactive power values for endpoints (Q_7).
        self.q8 = PU()  # Reactive power values for endpoints (Q_8).
        self.q9 = PU()  # Reactive power values for endpoints (Q_9).
        self.tu1 = Seconds(0)  # UEL lead time constant (T_U1).  Typical Value = 0.
        self.tu2 = Seconds(0)  # UEL lag time constant (T_U2).  Typical Value = 0.
        self.tu3 = Seconds(0)  # UEL lead time constant (T_U3).  Typical Value = 0.
        self.tu4 = Seconds(0)  # UEL lag time constant (T_U4).  Typical Value = 0.
        self.tul = Seconds(0)  # Time constant associated with optional integrator feedback input signal to UEL (T_UL).  Typical Value = 0.
        self.tup = Seconds(5)  # Real power filter time constant (T_UP).  Typical Value = 5.
        self.tuq = Seconds(0)  # Reactive power filter time constant (T_UQ).  Typical Value = 0.
        self.tuv = Seconds(5)  # Voltage filter time constant (T_UV).  Typical Value = 5.
        self.vuimax = PU(.25)  # UEL integrator output maximum limit (V_UIMAX).  Typical Value = 0.25.
        self.vuimin = PU(0)  # UEL integrator output minimum limit (V_UIMIN).  Typical Value = 0.
        self.vulmax = PU(.25)  # UEL output maximum limit (V_ULMAX).  Typical Value = 0.25.
        self.vulmin = PU(0)  # UEL output minimum limit (V_ULMIN).  Typical Value = 0.
