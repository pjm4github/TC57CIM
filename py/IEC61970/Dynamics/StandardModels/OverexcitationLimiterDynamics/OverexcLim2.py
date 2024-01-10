# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:00:52 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Dynamics.StandardModels.OverexcitationLimiterDynamics.OverexcitationLimiterDynamics import \
    OverexcitationLimiterDynamics


class OverexcLim2(OverexcitationLimiterDynamics):
    """
    Different from LimIEEEOEL, LimOEL2 has a fixed pickup threshold and reduces the
    excitation set-point by mean of non-windup integral regulator.
    Irated is the rated machine excitation current (calculated from nameplate
    conditions: V_nom, P_nom, CosPhi_nom).
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """

    def __init__(self) -> None:
        # Limit value of rated field current (IFDLIM).  Typical Value = 1.05.
        super().__init__()
        self.ifd_lim: PU = PU(1.05)
        # Gain Over excitation limiter (KOI).  Typical Value = 0.1.
        self.koi: PU = PU(0.1)

        # Maximum error signal (VOIMAX).  Typical Value = 0.
        self.voi_max: PU = PU(0.0)

        # Minimum error signal (VOIMIN).  Typical Value = -9999.
        self.voi_min: PU = PU(-9999)
