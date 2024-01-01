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
        self.a1: Optional[PU] = PU()  # Notch filter parameter (A1)
        self.a2: Optional[PU] = PU()  # Notch filter parameter (A2)
        self.a3: Optional[PU] = PU()  # Notch filter parameter (A3)
        self.a4: Optional[PU] = PU()  # Notch filter parameter (A4)
        self.a5: Optional[PU] = PU()  # Notch filter parameter (A5)
        self.a6: Optional[PU] = PU()  # Notch filter parameter (A6)
        self.a7: Optional[PU] = PU()  # Notch filter parameter (A7)
        self.a8: Optional[PU] = PU()  # Notch filter parameter (A8)
        self.input_signal_type: Optional[InputSignalKind] = InputSignalKind.BUS_VOLTAGE  # Type of input signal
        self.kd: Optional[bool] = False  # Selector (Kd)
        self.ks: Optional[PU] = PU()  # Stabilizer gain (Ks)
        self.t1: Optional[Seconds] = Seconds()  # Lead/lag time constant (T1)
        self.t2: Optional[Seconds] = Seconds()  # Lead/lag time constant (T2)
        self.t3: Optional[Seconds] = Seconds()  # Lead/lag time constant (T3)
        self.t4: Optional[Seconds] = Seconds()  # Lead/lag time constant (T4)
        self.t5: Optional[Seconds] = Seconds()  # Washout time constant (T5)
        self.t6: Optional[Seconds] = Seconds()  # Transducer time constant (T6)
        self.tdelay: Optional[Seconds] = Seconds()  # Time constant (Tdelay)
        self.vcl: Optional[PU] = PU()  # Stabilizer input cutoff threshold (Vcl)
        self.vcu: Optional[PU] = PU()  # Stabilizer input cutoff threshold (Vcu)
        self.vrmax: Optional[PU] = PU()  # Maximum stabilizer output (Vrmax)
        self.vrmin: Optional[PU] = PU()  # Minimum stabilizer output (Vrmin)
