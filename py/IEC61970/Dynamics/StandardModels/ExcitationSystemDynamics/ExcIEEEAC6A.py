# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIeeeAc6A(ExcitationSystemDynamics):

    def __init__(self) -> None:
        super().__init__()
        self.ka: float = 1.0  # Voltage regulator gain (K_A). Typical Value = 536.
        self.kc: float = 1.0  # Rectifier loading factor proportional to commutating reactance (K_C).
                                         # Typical Value = 0.173.
        self.kd: float = 1.0  # Demagnetizing factor, a function of exciter alternator reactances (K_D).
                                         # Typical Value = 1.91.
        self.ke: float = 1.0  # Exciter constant related to self-excited field (K_E). Typical Value = 1.6.
        self.kh: float = 1.0  # Exciter field current limiter gain (K_H). Typical Value = 92.
        self.seve1: float = 1.0  # Exciter saturation function value at the corresponding exciter voltage,
                                            # V_E1, back of commutating reactance (S_E[VE1]). Typical Value = 0.214.
        self.seve2: float = 1.0  # Exciter saturation function value at the corresponding exciter voltage,
                                            # V_E2, back of commutating reactance (S_E[VE2]). Typical Value = 0.044.
        self.ta: Seconds = Seconds() # Voltage regulator time constant (T_A). Typical Value = 0.086.
        self.tb: Seconds = Seconds() # Voltage regulator time constant (T_B). Typical Value = 9.
        self.tc: Seconds = Seconds() # Voltage regulator time constant (T_C). Typical Value = 3.
        self.te: Seconds = Seconds() # Exciter time constant, integration rate associated with exciter control (T_E).
                                         # Typical Value = 1.
        self.th: Seconds = Seconds() # Exciter field current limiter time constant (T_H). Typical Value = 0.08.
        self.tj: Seconds = Seconds() # Exciter field current limiter time constant (T_J). Typical Value = 0.02.
        self.tk: Seconds = Seconds() # Voltage regulator time constant (T_K). Typical Value = 0.18.
        self.vamax: float = 1.0  # Maximum voltage regulator output (V_AMAX). Typical Value = 75.
        self.vamin: float = 1.0  # Minimum voltage regulator output (V_AMIN). Typical Value = -75.
        self.ve1: float = 1.0  # Exciter alternator output voltages back of commutating reactance at which
                                          # saturation is defined (VE1) equals V_EMAX(VE1). Typical Value = 7.4.
        self.ve2: float = 1.0  # Exciter alternator output voltages back of commutating reactance at which
                                          # saturation is defined (VE2). Typical Value = 5.55.
        self.vfelim: float = 1.0  # Exciter field current limit reference (VFELIM). Typical Value = 19.
        self.vhmax: float = 1.0  # Maximum field current limiter signal reference (V_HMAX). Typical Value = 75.
        self.vrmax: float = 1.0  # Maximum voltage regulator output (V_RMAX). Typical Value = 44.
        self.vrmin: float = 1.0  # Minimum voltage regulator output (V_RMIN). Typical Value = -36.
