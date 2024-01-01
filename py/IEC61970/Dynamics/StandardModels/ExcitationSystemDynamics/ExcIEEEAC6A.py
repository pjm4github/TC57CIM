# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIeeeAc6A(ExcitationSystemDynamics):

    def __init__(self) -> None:
        super().__init__()
        self.ka: Optional[float] = 1.0  # Voltage regulator gain (K_A). Typical Value = 536.
        self.kc: Optional[float] = 1.0  # Rectifier loading factor proportional to commutating reactance (K_C).
                                         # Typical Value = 0.173.
        self.kd: Optional[float] = 1.0  # Demagnetizing factor, a function of exciter alternator reactances (K_D).
                                         # Typical Value = 1.91.
        self.ke: Optional[float] = 1.0  # Exciter constant related to self-excited field (K_E). Typical Value = 1.6.
        self.kh: Optional[float] = 1.0  # Exciter field current limiter gain (K_H). Typical Value = 92.
        self.seve1: Optional[float] = 1.0  # Exciter saturation function value at the corresponding exciter voltage,
                                            # V_E1, back of commutating reactance (S_E[VE1]). Typical Value = 0.214.
        self.seve2: Optional[float] = 1.0  # Exciter saturation function value at the corresponding exciter voltage,
                                            # V_E2, back of commutating reactance (S_E[VE2]). Typical Value = 0.044.
        self.ta: Optional[float] = 1.0  # Voltage regulator time constant (T_A). Typical Value = 0.086.
        self.tb: Optional[float] = 1.0  # Voltage regulator time constant (T_B). Typical Value = 9.
        self.tc: Optional[float] = 1.0  # Voltage regulator time constant (T_C). Typical Value = 3.
        self.te: Optional[float] = 1.0  # Exciter time constant, integration rate associated with exciter control (T_E).
                                         # Typical Value = 1.
        self.th: Optional[float] = 1.0  # Exciter field current limiter time constant (T_H). Typical Value = 0.08.
        self.tj: Optional[float] = 1.0  # Exciter field current limiter time constant (T_J). Typical Value = 0.02.
        self.tk: Optional[float] = 1.0  # Voltage regulator time constant (T_K). Typical Value = 0.18.
        self.vamax: Optional[float] = 1.0  # Maximum voltage regulator output (V_AMAX). Typical Value = 75.
        self.vamin: Optional[float] = 1.0  # Minimum voltage regulator output (V_AMIN). Typical Value = -75.
        self.ve1: Optional[float] = 1.0  # Exciter alternator output voltages back of commutating reactance at which
                                          # saturation is defined (VE1) equals V_EMAX(VE1). Typical Value = 7.4.
        self.ve2: Optional[float] = 1.0  # Exciter alternator output voltages back of commutating reactance at which
                                          # saturation is defined (VE2). Typical Value = 5.55.
        self.vfelim: Optional[float] = 1.0  # Exciter field current limit reference (VFELIM). Typical Value = 19.
        self.vhmax: Optional[float] = 1.0  # Maximum field current limiter signal reference (V_HMAX). Typical Value = 75.
        self.vrmax: Optional[float] = 1.0  # Maximum voltage regulator output (V_RMAX). Typical Value = 44.
        self.vrmin: Optional[float] = 1.0  # Minimum voltage regulator output (V_RMIN). Typical Value = -36.
