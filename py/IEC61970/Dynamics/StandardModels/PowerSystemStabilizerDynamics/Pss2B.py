# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:03:17 2023
from typing import Optional

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.InputSignalKind import InputSignalKind
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import \
    PowerSystemStabilizerDynamics


class Pss2B(PowerSystemStabilizerDynamics):
    """
    Modified IEEE PSS2B Model.  Extra lead/lag (or rate) block added at end (up to 4 lead/lags total).
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()
        self.a: float = 1.0  # Numerator constant (a).  Typical Value = 1.
        self.input_signal_1_type: Optional[
            InputSignalKind] = InputSignalKind.ROTOR_SPEED  # Type of input signal #1.  Typical Value = rotorSpeed.
        self.input_signal_2_type: Optional[
            InputSignalKind] = InputSignalKind.GENERATOR_ELECTRICAL_POWER  # Type of input signal #2.  Typical Value
        # = generatorElectricalPower.
        self.ks1: PU = PU(12)  # Stabilizer gain (Ks1).  Typical Value = 12.
        self.ks2: PU = PU(.2)  # Gain on signal #2 (Ks2).  Typical Value = 0.2.
        self.ks3: PU = PU(1)  # Gain on signal #2 input before ramp-tracking filter (Ks3).  Typical Value = 1.
        self.ks4: PU = PU(1)  # Gain on signal #2 input after ramp-tracking filter (Ks4).  Typical Value = 1.
        self.m: Optional[int] = 5  # Denominator order of ramp tracking filter (M).  Typical Value = 5.
        self.n: Optional[int] = 1  # Order of ramp tracking filter (N).  Typical Value = 1.
        self.t1: Seconds = Seconds(.12)  # Lead/lag time constant (T1).  Typical Value = 0.12.
        self.t10: Seconds = Seconds(0)  # Lead/lag time constant (T10).  Typical Value = 0.
        self.t11: Seconds = Seconds(0)  # Lead/lag time constant (T11).  Typical Value = 0.
        self.t2: Seconds = Seconds(.02)  # Lead/lag time constant (T2).  Typical Value = 0.02.
        self.t3: Seconds = Seconds(.3)  # Lead/lag time constant (T3).  Typical Value = 0.3.
        self.t4: Seconds = Seconds(.02)  # Lead/lag time constant (T4).  Typical Value = 0.02.
        self.t6: Seconds = Seconds(0)  # Time constant on signal #1 (T6).  Typical Value = 0.
        self.t7: Seconds = Seconds(2)  # Time constant on signal #2 (T7).  Typical Value = 2.
        self.t8: Seconds = Seconds(.2)  # Lead of ramp tracking filter (T8).  Typical Value = 0.2.
        self.t9: Seconds = Seconds(.1)  # Lag of ramp tracking filter (T9).  Typical Value = 0.1.
        self.ta: Seconds = Seconds(0)  # Lead constant (Ta).  Typical Value = 0.
        self.tb: Seconds = Seconds(0)  # Lag time constant (Tb).  Typical Value = 0.
        self.tw1: Seconds = Seconds(2)  # First washout on signal #1 (Tw1).  Typical Value = 2.
        self.tw2: Seconds = Seconds(2)  # Second washout on signal #1 (Tw2).  Typical Value = 2.
        self.tw3: Seconds = Seconds(2)  # First washout on signal #2 (Tw3).  Typical Value = 2.
        self.tw4: Seconds = Seconds(0)  # Second washout on signal #2 (Tw4).  Typical Value = 0.
        self.vsi1max: PU = PU(2.)  # Input signal #1 max limit (Vsi1max).  Typical Value = 2.
        self.vsi1min: PU = PU(-2.)  # Input signal #1 min limit (Vsi1min).  Typical Value = -2.
        self.vsi2max: PU = PU(2.)  # Input signal #2 max limit (Vsi2max).  Typical Value = 2.
        self.vsi2min: PU = PU(-2.)  # Input signal #2 min limit (Vsi2min).  Typical Value = -2.
        self.vstmax: PU = PU(.1)  # Stabilizer output max limit (Vstmax).  Typical Value = 0.1.
        self.vstmin: PU = PU(-.1)  # Stabilizer output min limit (Vstmin).  Typical Value = -0.1
