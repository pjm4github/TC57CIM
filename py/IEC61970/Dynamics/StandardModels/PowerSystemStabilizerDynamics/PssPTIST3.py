# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:03:17 2023
from typing import Optional, Any

from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import \
    PowerSystemStabilizerDynamics


class PssPtist3(PowerSystemStabilizerDynamics):

    def __init__(self) -> None:
        # Filter coefficient (A0).
        super().__init__()
        self.a0: Optional[float] = 1.0

        # Limiter (Al).
        self.a1: Optional[float] = 1.0

        # Filter coefficient (A2).
        self.a2: Optional[float] = 1.0

        # Filter coefficient (A3).
        self.a3: Optional[float] = 1.0

        # Filter coefficient (A4).
        self.a4: Optional[float] = 1.0

        # Filter coefficient (A5).
        self.a5: Optional[float] = 1.0

        # Limiter (Al).
        self.al: Optional[float] = 1.0

        # Threshold value above which output averaging will be bypassed (Athres).
        self.athres: Optional[float] = 1.0

        # Filter coefficient (B0).
        self.b0: Optional[float] = 1.0

        # Filter coefficient (B1).
        self.b1: Optional[float] = 1.0

        # Filter coefficient (B2).
        self.b2: Optional[float] = 1.0

        # Filter coefficient (B3).
        self.b3: Optional[float] = 1.0

        # Filter coefficient (B4).
        self.b4: Optional[float] = 1.0

        # Filter coefficient (B5).
        self.b5: Optional[float] = 1.0

        # Limiter (Dl).
        self.dl: Optional[float] = 1.0

        # Time step related to activation of controls (0.03 for 50 Hz) (Dtc).  Typical Value = 0.025.
        self.dtc: Optional[float] = 1.0

        # Time step frequency calculation (0.03 for 50 Hz) (Dtf).  Typical Value = 0.025.
        self.dtf: Optional[float] = 1.0

        # Time step active power calculation (0.015 for 50 Hz) (Dtp).  Typical Value = 0.0125.
        self.dtp: Optional[float] = 1.0

        # Digital/analog output switch (Isw).  true = produce analog output false = convert to digital output, using tap selection table.
        self.isw: Optional[bool] = False

        # Gain (K).  Typical Value = 9.
        self.k: Optional[float] = 1.0

        # Threshold value (Lthres).
        self.lthres: Optional[float] = 1.0

        # (M).  M=2*H.  Typical Value = 5.
        self.m: Optional[float] = 1.0

        # Number of control outputs to average (Nav) (1 <= Nav <= 16).  Typical Value = 4.
        self.nav: Optional[float] = 1.0

        # Number of counts at limit to active limit function (Ncl) (>0).
        self.ncl: Optional[float] = 1.0

        # Number of counts until reset after limit function is triggered (Ncr).
        self.ncr: Optional[float] = 1.0

        # (Pmin).
        self.pmin: Optional[float] = 1.0

        # Time constant (T1).  Typical Value = 0.3.
        self.t1: Optional[float] = 1.0

        # Time constant (T2).  Typical Value = 1.
        self.t2: Optional[float] = 1.0

        # Time constant (T3).  Typical Value = 0.2.
        self.t3: Optional[float] = 1.0

        # Time constant (T4).  Typical Value = 0.05.
        self.t4: Optional[float] = 1.0

        # Time constant (T5).
        self.t5: Optional[float] = 1.0

        # Time constant (T6).
        self.t6: Optional[float] = 1.0

        # Time constant (Tf).  Typical Value = 0.2.
        self.tf: Optional[float] = 1.0
