# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:03:17 2023
from typing import Optional

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import \
    PowerSystemStabilizerDynamics


class Pss5(PowerSystemStabilizerDynamics):

    def __init__(self) -> None:
        super().__init__()
        self.ctw2: Optional[bool] = True  # Selector for Second washout enabling (C_TW2). True = second washout filter is bypassed, False = second washout filter in use. Typical Value = True.
        self.deadband: PU = PU(0.0)  # Stabilizer output dead band (DeadBand). Typical Value = 0.
        self.isfreq: Optional[bool] = True  # Selector for Frequency/shaft speed input (IsFreq). True = speed, False = frequency. Typical Value = True.
        self.kf: Optional[float] = 5.0  # Frequency/shaft speed input gain (K_F). Typical Value = 5.
        self.kpe: Optional[float] = 0.3  # Electric power input gain (K_PE). Typical Value = 0.3.
        self.kpss: Optional[float] = 1.0  # PSS gain (K_PSS). Typical Value = 1.
        self.pmm: PU = PU(1.0)  # Minimum power PSS enabling (P_mn). Typical Value = 0.25.
        self.tl1: Seconds = Seconds(0) # Lead/lag time constant (T_L1). Typical Value = 0.
        self.tl2: Seconds = Seconds(0) # Lead/lag time constant (T_L2). Typical Value = 0.
        self.tl3: Seconds = Seconds(0) # Lead/lag time constant (T_L3). Typical Value = 0.
        self.tl4: Seconds = Seconds(0) # Lead/lag time constant (T_L4). Typical Value = 0.
        self.tpe: Seconds = Seconds(0.05) # Electric power filter time constant (T_PE). Typical Value = 0.05.
        self.tw1: Seconds = Seconds(3.5) # First WashOut (T_W1). Typical Value = 3.5.
        self.tw2: Seconds = Seconds(0) # Second WashOut (T_W2). Typical Value = 0.
        self.vadat: Optional[bool] = False  # Signal selector (V_adAtt). True = closed (Generator Power is greater than P_min), False = open (Pe is smaller than P_min). Typical Value = True.
        self.vsmn: PU = PU(-.1)  # Stabilizer output max limit (V_SMN). Typical Value = -0.1.
        self.vsmx: PU = PU(.10)  # Stabilizer output min limit (V_SMX). Typical Value = 0.1.
