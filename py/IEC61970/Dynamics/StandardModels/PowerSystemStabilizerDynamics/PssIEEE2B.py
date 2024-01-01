# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:03:17 2023
from typing import Optional

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.InputSignalKind import InputSignalKind
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import \
    PowerSystemStabilizerDynamics


class PssIeee2b(PowerSystemStabilizerDynamics):
    """
    The class represents IEEE Std 421.5-2005 type PSS2B power system stabilizer
    model. This stabilizer model is designed to represent a variety of dual-input
    stabilizers, which normally use combinations of power and speed or frequency to
    derive the stabilizing signal.
    
    Reference: IEEE 2B 421.5-2005 Section 8.2.
    """
    def __init__(self) -> None:
        """
        Initializes a new instance of PssIEEE2B
        """
        super().__init__()
        self.input_signal1_type: Optional[InputSignalKind] = InputSignalKind.ROTOR_SPEED  # Type of input signal #1.  Typical Value = rotorSpeed.
        self.input_signal2_type: Optional[InputSignalKind] = InputSignalKind.GENERATOR_ELECTRICAL_POWER  # Type of input signal #2.  Typical Value = generatorElectricalPower.
        self.ks1: Optional[PU] = PU(12)  # Stabilizer gain (Ks1).  Typical Value = 12.
        self.ks2: Optional[PU] = PU(.2)  # Gain on signal #2 (Ks2).  Typical Value = 0.2.
        self.ks3: Optional[PU] = PU(1)  # Gain on signal #2 input before ramp-tracking filter (Ks3).  Typical Value = 1.
        self.m: Optional[int] = 5 # Denominator order of ramp tracking filter (M).  Typical Value = 5.
        self.n: Optional[int] = 1 # Order of ramp tracking filter (N).  Typical Value = 1.
        self.t1: Optional[Seconds] = Seconds(.12)  # Lead/lag time constant (T1).  Typical Value = 0.12.
        self.t10: Optional[Seconds] = Seconds(0)  # Lead/lag time constant (T10).  Typical Value = 0.
        self.t11: Optional[Seconds] = Seconds(0)  # Lead/lag time constant (T11).  Typical Value = 0.
        self.t2: Optional[Seconds] = Seconds(.02)  # Lead/lag time constant (T2).  Typical Value = 0.02.
        self.t3: Optional[Seconds] = Seconds(.3)  # Lead/lag time constant (T3).  Typical Value = 0.3.
        self.t4: Optional[Seconds] = Seconds(.02)  # Lead/lag time constant (T4).  Typical Value = 0.02.
        self.t6: Optional[Seconds] = Seconds(0)  # Time constant on signal #1 (T6).  Typical Value = 0.
        self.t7: Optional[Seconds] = Seconds(2)  # Time constant on signal #2 (T7).  Typical Value = 2.
        self.t8: Optional[Seconds] = Seconds(.2)  # Lead of ramp tracking filter (T8).  Typical Value = 0.2.
        self.t9: Optional[Seconds] = Seconds(.1)  # Lag of ramp tracking filter (T9).  Typical Value = 0.1.
        self.tw1: Optional[Seconds] = Seconds(2)  # First washout on signal #1 (Tw1).  Typical Value = 2.
        self.tw2: Optional[Seconds] = Seconds(2)  # Second washout on signal #1 (Tw2).  Typical Value = 2.
        self.tw3: Optional[Seconds] = Seconds(2)  # First washout on signal #2 (Tw3).  Typical Value = 2.
        self.tw4: Optional[Seconds] = Seconds(0)  # Second washout on signal #2 (Tw4).  Typical Value = 0.
        self.vsi1max: Optional[PU] = PU(2)  # Input signal #1 max limit (Vsi1max).  Typical Value = 2.
        self.vsi1min: Optional[PU] = PU(-2)  # Input signal #1 min limit (Vsi1min).  Typical Value = -2.
        self.vsi2max: Optional[PU] = PU(2)  # Input signal #2 max limit (Vsi2max).  Typical Value = 2.
        self.vsi2min: Optional[PU] = PU(-2)  # Input signal #2 min limit (Vsi2min).  Typical Value = -2.
        self.vstmax: Optional[PU] = PU(.1)  # Stabilizer output max limit (Vstmax).  Typical Value = 0.1.
        self.vstmin: Optional[PU] = PU(-.1)  # Stabilizer output min limit (Vstmin).  Typical Value = -0.1.
