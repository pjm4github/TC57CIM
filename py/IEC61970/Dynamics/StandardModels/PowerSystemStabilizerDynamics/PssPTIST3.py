  # Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:03:17 2023
from typing import Optional, Any

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import \
    PowerSystemStabilizerDynamics


class PssPtist3(PowerSystemStabilizerDynamics):

    def __init__(self) -> None:
        
        super().__init__()
        self.a0: PU = PU(0.0)  # Filter coefficient (A0).
        self.a1: PU = PU(0.0)  # Limiter (Al).
        self.a2: PU = PU(0.0)  # Filter coefficient (A2).
        self.a3: PU = PU(0.0)  # Filter coefficient (A3).
        self.a4: PU = PU(0.0)  # Filter coefficient (A4).
        self.a5: PU = PU(0.0)  # Filter coefficient (A5).
        self.al: PU = PU(0.0)  # Limiter (Al).
        self.athres: PU = PU(0.005)  # Threshold value above which output averaging will be bypassed (Athres).  Typical Value = 0.005.
        self.b0: PU = PU(0.0)  # Filter coefficient (B0).
        self.b1: PU = PU(0.0)  # Filter coefficient (B1).
        self.b2: PU = PU(0.0)  # Filter coefficient (B2).
        self.b3: PU = PU(0.0)  # Filter coefficient (B3).
        self.b4: PU = PU(0.0)  # Filter coefficient (B4).
        self.b5: PU = PU(0.0)  # Filter coefficient (B5).
        self.dl: PU = PU(0.0)  # Limiter (Dl).
        self.dtc: PU = PU(0.025)  # Time step related to activation of controls (0.03 for 50 Hz) (Dtc).  Typical Value = 0.025.
        self.dtf: PU = PU(0.025)  # Time step frequency calculation (0.03 for 50 Hz) (Dtf).  Typical Value = 0.025.
        self.dtp: PU = PU(0.0125)  # Time step active power calculation (0.015 for 50 Hz) (Dtp).  Typical Value = 0.0125.
        self.isw: bool = False  # Digital/analog output switch (Isw).  true = produce analog output false = convert to digital output, using tap selection table.
        self.k: PU = PU(9)  # Gain (K).  Typical Value = 9.
        self.lthres: PU = PU(0.0)  # Threshold value (Lthres).
        self.m: PU = PU(5)  # (M).  M=2*H.  Typical Value = 5.
        self.nav: PU = PU(4.0)  # Number of control outputs to average (Nav) (1 <= Nav <= 16).  Typical Value = 4.
        self.ncl: PU = PU(0.1)  # Number of counts at limit to active limit function (Ncl) (>0).
        self.ncr: PU = PU(0.0)  # Number of counts until reset after limit function is triggered (Ncr).
        self.pmin: PU = PU(0.0)  # (Pmin).
        self.t1: Seconds = Seconds(0.3)  # Time constant (T1).  Typical Value = 0.3.
        self.t2: Seconds = Seconds(1.0)  # Time constant (T2).  Typical Value = 1.
        self.t3: Seconds = Seconds(0.2)  # Time constant (T3).  Typical Value = 0.2.
        self.t4: Seconds = Seconds(0.05)  # Time constant (T4).  Typical Value = 0.05.
        self.t5: Seconds = Seconds(0.0)  # Time constant (T5)
        self.t6: Seconds = Seconds(0.0)  # Time constant (T6).
        self.tf: Seconds = Seconds(0.2)  # Time constant (Tf).  Typical Value = 0.2.
