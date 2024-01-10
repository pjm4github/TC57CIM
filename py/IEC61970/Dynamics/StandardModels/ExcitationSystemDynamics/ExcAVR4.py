# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAvr4(ExcitationSystemDynamics):
    """Italian excitation system. It represents static exciter and electric voltage regulator."""
    
    def __init__(self) -> None:
        """Constructor"""
        super().__init__()
        self.imul: bool = False  #: AVR output voltage dependency selector (Imul).
        self.ka: float = 1.0  #: AVR gain (K_A). Typical Value = 300.
        self.ke: float = 1.0  #: Exciter gain (K_E). Typical Value = 1.
        self.kif: float = 1.0  #: Exciter internal reactance (K_IF). Typical Value = 0.
        self.t1: Seconds = Seconds()  #: AVR time constant (T_1). Typical Value = 4.8.
        self.t1if: Seconds = Seconds()  #: Exciter current feedback time constant (T_1IF). Typical Value = 60.
        self.t2: Seconds = Seconds()  #: AVR time constant (T_2). Typical Value = 1.5.
        self.t3: Seconds = Seconds()  #: AVR time constant (T_3). Typical Value = 0.
        self.t4: Seconds = Seconds()  #: AVR time constant (T_4). Typical Value = 0.
        self.tif: Seconds = Seconds()  #: Exciter current feedback time constant (T_IF). Typical Value = 0.
        self.vfmn: PU = PU()  #: Minimum exciter output (V_FMN). Typical Value = 0.
        self.vfmx: PU = PU()  #: Maximum exciter output (V_FMX). Typical Value = 5.
        self.vrmn: PU = PU()  #: Minimum AVR output (V_RMN). Typical Value = 0.
        self.vrmx: PU = PU()  #: Maximum AVR output (V_RMX). Typical Value = 5.


# Note: ExcitationSystemDynamics is assumed to be a superclass with appropriate typings
