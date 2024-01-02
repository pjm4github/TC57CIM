# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:03:17 2023
from typing import Optional

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.InputSignalKind import InputSignalKind
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import \
    PowerSystemStabilizerDynamics


class Pss1A(PowerSystemStabilizerDynamics):
    """
    Single input power system stabilizer. It is a modified version in order to
    allow representation of various vendors' implementations on PSS type 1A.
    """
    
    def __init__(self) -> None:
        super().__init__()
        self.a1: PU = PU()  # Notch filter parameter (A1)
        self.a2: PU = PU()  # Notch filter parameter (A2)
        self.a3: PU = PU()  # Notch filter parameter (A3)
        self.a4: PU = PU()  # Notch filter parameter (A4)
        self.a5: PU = PU()  # Notch filter parameter (A5)
        self.a6: PU = PU()  # Notch filter parameter (A6)
        self.a7: PU = PU()  # Notch filter parameter (A7)
        self.a8: PU = PU()  # Notch filter parameter (A8)
        self.input_signal_type: Optional[InputSignalKind] = InputSignalKind.BUS_VOLTAGE  # Type of input signal
        self.kd: bool = False  # Selector (Kd)
        self.ks: PU = PU()  # Stabilizer gain (Ks)
        self.t1: Seconds = Seconds()  # Lead/lag time constant (T1)
        self.t2: Seconds = Seconds()  # Lead/lag time constant (T2)
        self.t3: Seconds = Seconds()  # Lead/lag time constant (T3)
        self.t4: Seconds = Seconds()  # Lead/lag time constant (T4)
        self.t5: Seconds = Seconds()  # Washout time constant (T5)
        self.t6: Seconds = Seconds()  # Transducer time constant (T6)
        self.tdelay: Seconds = Seconds()  # Time constant (Tdelay)
        self.vcl: PU = PU()  # Stabilizer input cutoff threshold (Vcl)
        self.vcu: PU = PU()  # Stabilizer input cutoff threshold (Vcu)
        self.vrmax: PU = PU()  # Maximum stabilizer output (Vrmax)
        self.vrmin: PU = PU()  # Minimum stabilizer output (Vrmin)
