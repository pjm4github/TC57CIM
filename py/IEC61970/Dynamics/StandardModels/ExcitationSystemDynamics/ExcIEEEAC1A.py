# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIeeeAc1A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type AC1A model. The model represents
    the field-controlled alternator-rectifier excitation systems designated Type
    AC1A. These excitation systems consist of an alternator main exciter with non-
    controlled rectifiers.
    Reference: IEEE Standard 421.5-2005 Section 6.1.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:17 PM
    """

    def __init__(self) -> None:
        """
        Constructor for initializing AC1A excitation system model
        """
        super().__init__()
        self.ka: PU = PU()  # Voltage regulator gain (K_A), Typical Value = 400
        self.kc: PU = PU()  # Rectifier loading factor proportional to commutating reactance (K_C), Typical Value = 0.2
        self.kd: PU = PU()  # Demagnetizing factor, a function of exciter alternator reactances (K_D), Typical Value = 0.38
        self.ke: PU = PU()  # Exciter constant related to self-excited field (K_E), Typical Value = 1
        self.kf: PU = PU()  # Excitation control system stabilizer gains (K_F), Typical Value = 0.03
        self.seve1: float = 1.0  # Exciter saturation function value at the corresponding exciter voltage, V_E1 (S_E[V_E1]), Typical Value = 0.1
        self.seve2: float = 1.0  # Exciter saturation function value at the corresponding exciter voltage, V_E2 (S_E[V_E2]), Typical Value = 0.03
        self.ta: Seconds = Seconds()  # Voltage regulator time constant (T_A), Typical Value = 0.02
        self.tb: Seconds = Seconds()  # Voltage regulator time constant (T_B), Typical Value = 0
        self.tc: Seconds = Seconds()  # Voltage regulator time constant (T_C), Typical Value = 0
        self.te: Seconds = Seconds()  # Exciter time constant, integration rate associated with exciter control (T_E), Typical Value = 0.8
        self.tf: Seconds = Seconds()  # Excitation control system stabilizer time constant (T_F), Typical Value = 1
        self.vamax: PU = PU()  # Maximum voltage regulator output (V_AMAX), Typical Value = 14.5
        self.vamin: PU = PU()  # Minimum voltage regulator output (V_AMIN), Typical Value = -14.5
        self.ve1: PU = PU()  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (V_E1), Typical Value = 4.18
        self.ve2: PU = PU()  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (V_E2), Typical Value = 3.14
        self.vrmax: PU = PU()  # Maximum voltage regulator outputs (V_RMAX), Typical Value = 6.03
        self.vrmin: PU = PU()  # Minimum voltage regulator outputs (V_RMIN), Typical Value = -5.43
