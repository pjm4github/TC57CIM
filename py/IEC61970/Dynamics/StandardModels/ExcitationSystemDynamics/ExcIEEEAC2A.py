# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIeeeAc2A(ExcitationSystemDynamics):

    def __init__(self) -> None:
        super().__init__()
        self.ka: PU = PU()  # Voltage regulator gain (K_A). Typical Value = 400.
        self.kb: PU = PU()  # Second stage regulator gain (K_B). Typical Value = 25.
        self.kc: PU = PU()  # Rectifier loading factor proportional to commutating reactance (K_C). Typical Value = 0.28.
        self.kd: PU = PU()  # Demagnetizing factor, a function of exciter alternator reactances (K_D). Typical Value = 0.35.
        self.ke: PU = PU()  # Exciter constant related to self-excited field (K_E). Typical Value = 1.
        self.kf: PU = PU()  # Excitation control system stabilizer gains (K_F). Typical Value = 0.03.
        self.kh: PU = PU()  # Exciter field current feedback gain (K_H). Typical Value = 1.
        self.seve1: float = 1.0  # Exciter saturation function value at the corresponding exciter voltage, V_E1, back of commutating reactance (S_E{V_E1}). Typical Value = 0.037.
        self.seve2: float = 1.0  # Exciter saturation function value at the corresponding exciter voltage, V_E2, back of commutating reactance (S_E{V_E2}). Typical Value = 0.012.
        self.ta: Seconds = Seconds()  # Voltage regulator time constant (T_A). Typical Value = 0.02.
        self.tb: Seconds = Seconds()  # Voltage regulator time constant (T_B). Typical Value = 0.
        self.tc: Seconds = Seconds()  # Voltage regulator time constant (T_C). Typical Value = 0.
        self.te: Seconds = Seconds()  # Exciter time constant, integration rate associated with exciter control (T_E). Typical Value = 0.6.
        self.tf: Seconds = Seconds()  # Excitation control system stabilizer time constant (T_F). Typical Value = 1.
        self.vamax: PU = PU()  # Maximum voltage regulator output (V_AMAX). Typical Value = 8.
        self.vamin: PU = PU()  # Minimum voltage regulator output (V_AMIN). Typical Value = -8.
        self.ve1: PU = PU()  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (V_E1). Typical Value = 4.4.
        self.ve2: PU = PU()  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (V_E2). Typical Value = 3.3.
        self.vfemax: PU = PU()  # Exciter field current limit reference (V_FEMAX). Typical Value = 4.4.
        self.vrmax: PU = PU()  # Maximum voltage regulator outputs (V_RMAX). Typical Value = 105.
        self.vrmin: PU = PU()  # Minimum voltage regulator outputs (V_RMIN). Typical Value = -95.
