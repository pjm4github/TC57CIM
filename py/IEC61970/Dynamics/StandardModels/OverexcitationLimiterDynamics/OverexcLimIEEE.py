# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:00:52 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Dynamics.StandardModels.OverexcitationLimiterDynamics.OverexcitationLimiterDynamics import \
    OverexcitationLimiterDynamics


class OverexcLimIeee(OverexcitationLimiterDynamics):
    """
    The over excitation limiter model is intended to represent the significant
    features of OELs necessary for some large-scale system studies. It is the
    result of a pragmatic approach to obtain a model that can be widely applied
    with attainable data from generator owners. An attempt to include all
    variations in the functionality of OELs and duplicate how they interact with
    the rest of the excitation systems would likely result in a level of
    application insufficient for the studies for which they are intended.
    
    Reference: IEEE OEL 421.5-2005 Section 9.
    """
    
    def __init__(self) -> None:
        super().__init__()
        # OEL pickup/drop-out hysteresis (HYST). Typical Value = 0.03.
        self.hyst: PU = PU(0.03)
        
        # OEL timed field current limit (IFDLIM). Typical Value = 1.05.
        self.ifdlim: PU = PU(1.05)
        
        # OEL instantaneous field current limit (IFDMAX). Typical Value = 1.5.
        self.ifdmax: PU = PU(1.5)
        
        # OEL timed field current limiter pickup level (ITFPU). Typical Value = 1.05.
        self.itfpu: PU = PU(1.05)
        
        # OEL cooldown gain (KCD). Typical Value = 1.
        self.kcd: PU = PU(1.0)
        
        # OEL ramped limit rate (KRAMP). Unit = PU/sec. Typical Value = 10.
        self.kramp: float = 10.0
