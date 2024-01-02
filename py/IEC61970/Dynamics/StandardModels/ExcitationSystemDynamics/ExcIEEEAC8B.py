# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIeeeAc8B(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type AC8B model. This model represents
    a PID voltage regulator with either a brushless exciter or dc exciter. The AVR
    in this model consists of PID control, with separate constants for the
    proportional (K_PR), integral (K_IR), and derivative (K_DR) gains. The
    representation of the brushless exciter (T_E, K_E, S_E, K_C, K_D) is similar to the
    model Type AC2A. The Type AC8B model can be used to represent static voltage
    regulators applied to brushless excitation systems. Digitally based voltage
    regulators feeding dc rotating main exciters can be represented with the AC
    Type AC8B model with the parameters K_C and K_D set to 0. For thyristor power
    stages fed from the generator terminals, the limits V_RMAX and V_RMIN should be
    a function of terminal voltage: V_T * V_RMAX and V_T * V_RMIN.
    Reference: IEEE Standard 421.5-2005 Section 6.8.
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:18 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.ka: float = 0.0  # Voltage regulator gain (K_A). Typical Value = 1.
        self.kc: float = 0.0  # Rectifier loading factor proportional to commutating reactance (K_C). Typical Value = 0.55.
        self.kd: float = 0.0  # Demagnetizing factor, a function of exciter alternator reactances (K_D). Typical Value = 1.1.
        self.kdr: float = 0.0  # Voltage regulator derivative gain (K_DR). Typical Value = 10.
        self.ke: float = 0.0  # Exciter constant related to self-excited field (K_E). Typical Value = 1.
        self.kir: float = 0.0  # Voltage regulator integral gain (K_IR). Typical Value = 5.
        self.kpr: float = 0.0  # Voltage regulator proportional gain (K_PR). Typical Value = 80.
        self.seve1: float = 0.0  # Exciter saturation function value at the corresponding exciter voltage, V_E1, back of commutating reactance (S_E[V_E1]). Typical Value = 0.3.
        self.seve2: float = 0.0  # Exciter saturation function value at the corresponding exciter voltage, V_E2, back of commutating reactance (S_E[V_E2]). Typical Value = 3.
        self.ta: Seconds = Seconds() # Voltage regulator time constant (T_A). Typical Value = 0.
        self.tdr: Seconds = Seconds() # Lag time constant (T_DR). Typical Value = 0.1.
        self.te: Seconds = Seconds() # Exciter time constant, integration rate associated with exciter control (T_E). Typical Value = 1.2.
        self.ve1: float = 0.0  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (V_E1) equals V_EMAX (V_E1). Typical Value = 6.5.
        self.ve2: float = 0.0  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (V_E2). Typical Value = 9.
        self.vemin: float = 0.0  # Minimum exciter voltage output (V_EMIN). Typical Value = 0.
        self.vfemax: float = 0.0  # Exciter field current limit reference (V_FEMAX). Typical Value = 6.
        self.vrmax: float = 0.0  # Maximum voltage regulator output (V_RMAX). Typical Value = 35.
        self.vrmin: float = 0.0  # Minimum voltage regulator output (V_RMIN). Typical Value = 0.

