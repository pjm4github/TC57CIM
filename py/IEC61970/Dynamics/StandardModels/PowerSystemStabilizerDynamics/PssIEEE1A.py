# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:03:17 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.InputSignalKind import InputSignalKind
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import \
    PowerSystemStabilizerDynamics


# class InputSignalKind(Enum):
#     speed = 1
#     frequency = 2
#     power = 3
#     rotorAngularFrequencyDeviation = 4

class PssIeee1a(PowerSystemStabilizerDynamics):

    def __init__(self):
        super().__init__()
        self.a1: PU = PU(.061)  # PSS signal conditioning frequency filter constant (A1). Typical Value = 0.061.
        self.a2: PU = PU(.0017)  # PSS signal conditioning frequency filter constant (A2). Typical Value = 0.0017.
        self.input_signal_type: InputSignalKind = InputSignalKind.ROTOR_ANGULAR_FREQUENCY_DEVIATION  # Type of input signal. Typical Value = rotorAngularFrequencyDeviation.
        self.ks: PU = PU(5)  # Stabilizer gain (Ks). Typical Value = 5.
        self.t1: Seconds = Seconds(.3)  # Lead/lag time constant (T1). Typical Value = 0.3.
        self.t2: Seconds = Seconds(.03)  # Lead/lag time constant (T2). Typical Value = 0.03.
        self.t3: Seconds = Seconds(.3)  # Lead/lag time constant (T3). Typical Value = 0.3.
        self.t4: Seconds = Seconds(.03)  # Lead/lag time constant (T4). Typical Value = 0.03.
        self.t5: Seconds = Seconds(10)  # Washout time constant (T5). Typical Value = 10.
        self.t6: Seconds = Seconds(.01)  # Transducer time constant (T6). Typical Value = 0.01.
        self.vrmax: PU = PU(.05)  # Maximum stabilizer output (Vrmax). Typical Value = 0.05.
        self.vrmin: PU = PU(-.05)  # Minimum stabilizer output (Vrmin). Typical Value = -0.05.

