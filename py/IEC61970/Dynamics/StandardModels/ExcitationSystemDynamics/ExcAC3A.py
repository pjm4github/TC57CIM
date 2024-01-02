# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Any, Union

from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAc3A(ExcitationSystemDynamics):
    """
    Modified IEEE AC3A alternator-supplied rectifier excitation system with 
    different field current limit.
    """
    
    def __init__(self) -> None:
        super().__init__()
        self.efdn = 2.36  # Value of EFD at which feedback gain changes (Efdn). Typical Value = 2.36
        self.ka = 45.62  # Voltage regulator gain (Ka). Typical Value = 45.62
        self.kc = 0.104  # Rectifier loading factor proportional to commutating reactance (Kc). Typical Value = 0.104
        self.kd = 0.499  # Demagnetizing factor, a function of exciter alternator reactances (Kd). Typical Value = 0.499
        self.ke = 1.0  # Exciter constant related to self-excited field (Ke). Typical Value = 1
        self.kf = 0.143  # Excitation control system stabilizer gains (Kf). Typical Value = 0.143
        self.kf1 = 1  # Coefficient to allow different usage of the model (Kf1). Typical Value = 1
        self.kf2 = 0.0  # Coefficient to allow different usage of the model (Kf2). Typical Value = 0
        self.klv = 194  # Gain used in the minimum field voltage limiter loop (Klv). Typical Value = 194
        self.kn = 0.05  # Excitation control system stabilizer gain (Kn). Typical Value = 0.05
        self.kr = 3.77  # Constant associated with regulator and alternator field power supply (Kr). Typical Value = 3.77
        self.ks = 0.0  # Coefficient to allow different usage of the model-speed coefficient (Ks). Typical Value = 0
        self.seve1 = 1.143  # Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance (Se[Ve1]). Typical Value = 1.143
        self.seve2 = 0.1  # Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance (Se[Ve2]). Typical Value = 0.1
        self.ta: Seconds = Seconds(.013)  #Voltage regulator time constant (Ta). Typical Value = 0.013
        self.tb: Seconds = Seconds(0)  #Voltage regulator time constant (Tb). Typical Value = 0
        self.tc: Seconds = Seconds(0)  #Voltage regulator time constant (Tc). Typical Value = 0
        self.te: Seconds = Seconds(1.17)  #Exciter time constant, integration rate associated with exciter control (Te). Typical Value = 1.17
        self.tf: Seconds = Seconds(1.0)  #Excitation control system stabilizer time constant (Tf). Typical Value = 1
        self.vamax = 1.0  # Maximum voltage regulator output (Vamax). Typical Value = 1
        self.vamin = -0.95  # Minimum voltage regulator output (Vamin). Typical Value = -0.95
        self.ve1 = 6.24  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1) equals Vemax (Ve1). Typical Value = 6.24
        self.ve2 = 4.68  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2). Typical Value = 4.68
        self.vemin = 0.1  # Minimum exciter voltage output (Vemin). Typical Value = 0.1
        self.vfemax = 16.0  # Exciter field current limit reference (Vfemax). Typical Value = 16
        self.vlv = 0.79  # Field voltage used in the minimum field voltage limiter loop (Vlv). Typical Value = 0.79
