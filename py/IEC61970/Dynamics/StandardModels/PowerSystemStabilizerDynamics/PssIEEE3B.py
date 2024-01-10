# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:03:17 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.InputSignalKind import InputSignalKind
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import \
    PowerSystemStabilizerDynamics


class PssIeee3B(PowerSystemStabilizerDynamics):

    def __init__(self) -> None:
        super().__init__()
        self.a1: PU = PU(.359)  # Notch filter parameter (A1).  Typical Value = 0.359.
        self.a2: PU = PU(.586)  # Notch filter parameter (A2).  Typical Value = 0.586.
        self.a3: PU = PU(.429)  # Notch filter parameter (A3).  Typical Value = 0.429.
        self.a4: PU = PU(.564)  # Notch filter parameter (A4).  Typical Value = 0.564.
        self.a5: PU = PU(.001)  # Notch filter parameter (A5).  Typical Value = 0.001.
        self.a6: PU = PU(0.0)  # Notch filter parameter (A6).  Typical Value = 0.
        self.a7: PU = PU(.031)  # Notch filter parameter (A7).  Typical Value = 0.031.
        self.a8: PU = PU(0.0)  # Notch filter parameter (A8).  Typical Value = 0.
        self.input_signal1_type: InputSignalKind = InputSignalKind.GENERATOR_ELECTRICAL_POWER  # Type of input signal #1.  Typical Value = generatorElectricalPower.
        self.input_signal2_type: InputSignalKind = InputSignalKind.ROTOR_SPEED  # Type of input signal #2.  Typical Value = rotorSpeed.
        self.ks1: PU = PU(-.602)  # Gain on signal #1 (Ks1).  Typical Value = -0.602.
        self.ks2: PU = PU(30.12)  # Gain on signal #2 (Ks2).  Typical Value = 30.12.
        self.t1: Seconds = Seconds(0.012)  # Transducer time constant (T1).  Typical Value = 0.012.
        self.t2: Seconds = Seconds(0.012)  # Transducer time constant (T2).  Typical Value = 0.012.
        self.tw1: Seconds = Seconds(.3)  # Washout time constant (Tw1).  Typical Value = 0.3.
        self.tw2: Seconds = Seconds(.3)  # Washout time constant (Tw2).  Typical Value = 0.3.
        self.tw3: Seconds = Seconds(.6)  # Washout time constant (Tw3).  Typical Value = 0.6.
        self.vstmax: PU = PU(.1)  # Stabilizer output max limit (Vstmax).  Typical Value = 0.1.
        self.vstmin: PU = PU(.1)  # Stabilizer output min limit (Vstmin).  Typical Value = -0.1.
