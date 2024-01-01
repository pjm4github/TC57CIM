# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIeeeAc7B(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type AC7B model. The model represents
    excitation systems which consist of an ac alternator with either stationary or
    rotating rectifiers to produce the dc field requirements. It is an upgrade to
    earlier ac excitation systems, which replace only the controls but retain the
    ac alternator and diode rectifier bridge.

    Reference: IEEE Standard 421.5-2005 Section 6.7.

    Note: In the IEEE Standard 421.5 - 2005, the [1 / sT<sub>E</sub>] block
    is shown as [1 / (1 + sT<sub>E</sub>)], which is incorrect.
    """

    def __init__(self) -> None:
        super().__init__()
        self.kc: Optional[float] = 0.0  # Rectifier loading factor proportional to commutating reactance (Kc). Typical Value = 0.18
        self.kd: Optional[float] = 0.0  # Demagnetizing factor, a function of exciter alternator reactances (Kd). Typical Value = 0.02
        self.kdr: Optional[float] = 0.0  # Voltage regulator derivative gain (Kdr). Typical Value = 0
        self.ke: Optional[float] = 0.0  # Exciter constant related to self-excited field (Ke). Typical Value = 1
        self.kf1: Optional[float] = 0.0  # Excitation control system stabilizer gain (Kf1). Typical Value = 0.212
        self.kf2: Optional[float] = 0.0  # Excitation control system stabilizer gain (Kf2). Typical Value = 0
        self.kf3: Optional[float] = 0.0  # Excitation control system stabilizer gain (Kf3). Typical Value = 0
        self.kia: Optional[float] = 0.0  # Voltage regulator integral gain (Kia). Typical Value = 59.69
        self.kir: Optional[float] = 0.0  # Voltage regulator integral gain (Kir). Typical Value = 4.24
        self.kl: Optional[float] = 0.0  # Exciter field voltage lower limit parameter (Kl). Typical Value = 10
        self.kp: Optional[float] = 0.0  # Potential circuit gain coefficient (Kp). Typical Value = 4.96
        self.kpa: Optional[float] = 0.0  # Voltage regulator proportional gain (Kpa). Typical Value = 65.36
        self.kpr: Optional[float] = 0.0  # Voltage regulator proportional gain (Kpr). Typical Value = 4.24
        self.seve1: Optional[float] = 0.0  # Exciter saturation function value at the corresponding exciter voltage (Seve1). Typical Value = 0.44
        self.seve2: Optional[float] = 0.0  # Exciter saturation function value at the corresponding exciter voltage (Seve2). Typical Value = 0.075
        self.tdr: Optional[float] = 0.0  # Lag time constant (Tdr). Typical Value = 0
        self.te: Optional[float] = 0.0  # Exciter time constant, integration rate associated with exciter control (Te). Typical Value = 1.1
        self.tf: Optional[float] = 0.0  # Excitation control system stabilizer time constant (Tf). Typical Value = 1
        self.vamax: Optional[float] = 0.0  # Maximum voltage regulator output (Vamax). Typical Value = 1
        self.vamin: Optional[float] = 0.0  # Minimum voltage regulator output (Vamin). Typical Value = -0.95
        self.ve1: Optional[float] = 0.0  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1). Typical Value = 6.3
        self.ve2: Optional[float] = 0.0  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2). Typical Value = 3.02
        self.vemin: Optional[float] = 0.0  # Minimum exciter voltage output (Vemin). Typical Value = 0
        self.vfemax: Optional[float] = 0.0  # Exciter field current limit reference (Vfemax). Typical Value = 6.9
        self.vrmax: Optional[float] = 0.0  # Maximum voltage regulator output (Vrmax). Typical Value = 5.79
        self.vrmin: Optional[float] = 0.0  # Minimum voltage regulator output (Vrmin). Typical Value = -5.79
