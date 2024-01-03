from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.VoltageAdjusterDynamics.VoltageAdjusterDynamics import VoltageAdjusterDynamics


class VAdjIEEE(VoltageAdjusterDynamics):
    def __init__(self):
        super().__init__()
        self.adjslew = 300  # Rate at which output of adjuster changes (ADJ_SLEW).  Unit = sec./PU. Typical Value = 300.
        self.taoff = Seconds(0.5)  # Time that adjuster pulses are off (T_AOFF).  Typical Value = 0.5.
        self.taon = Seconds(0.1)  # Time that adjuster pulses are on (T_AON).  Typical Value = 0.1.
        self.vadjf = 0.0  # Set high to provide a continuous raise or lower (V_ADJF).
        self.vadjmax = PU(1.1)  # Maximum output of the adjuster (V_ADJMAX).  Typical Value = 1.1.
        self.vadjmin = PU(0.9)  # Minimum output of the adjuster (V_ADJMIN).  Typical Value = 0.9.
