# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAc6A(ExcitationSystemDynamics):
    """
    Modified IEEE AC6A alternator-supplied rectifier excitation system with speed input.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:17 PM
    """

    def __init__(self) -> None:        
         super().__init__()
         self.ka: PU = PU(536)  # Voltage regulator gain (Ka).  Typical Value = 536.
         self.kc: PU = PU(.173)  # Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 0.173.
         self.kd: PU = PU(1.91)  # Demagnetizing factor, a function of exciter alternator reactances (Kd).  Typical Value = 1.91.
         self.ke: PU = PU(1.6)  # Exciter constant related to self-excited field (Ke).  Typical Value = 1.6.
         self.kh: PU = PU(92)  # Exciter field current limiter gain (Kh).  Typical Value = 92.
         self.ks: PU = PU(0)  # Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0.
         self.seve1: float = 0.214  # Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance (Se[Ve1]).  Typical Value = 0.214.
         self.seve2: float = 0.044  # Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance (Se[Ve2]).  Typical Value = 0.044.
         self.ta: Seconds = Seconds(0.086)  # Voltage regulator time constant (Ta).  Typical Value = 0.086.
         self.tb: Seconds = Seconds(9)  # Voltage regulator time constant (Tb).  Typical Value = 9.
         self.tc: Seconds = Seconds(3)  # Voltage regulator time constant (Tc).  Typical Value = 3.
         self.te: Seconds = Seconds(1)  # Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1.
         self.th: Seconds = Seconds(0.08)  # Exciter field current limiter time constant (Th).  Typical Value = 0.08.
         self.tj: Seconds = Seconds(0.02)  # Exciter field current limiter time constant (Tj).  Typical Value = 0.02.
         self.tk: Seconds = Seconds(0.18)  # Voltage regulator time constant (Tk).  Typical Value = 0.18.
         self.vamax: PU = PU(75)  # Maximum voltage regulator output (Vamax).  Typical Value = 75.
         self.vamin: PU = PU(-75)  # Minimum voltage regulator output (Vamin).  Typical Value = -75.
         self.ve1: PU = PU(7.4)  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1).  Typical Value = 7.4.
         self.ve2: PU = PU(5.55)  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2).  Typical Value = 5.55.
         self.vfelim: PU = PU(19)  # Exciter field current limit reference (Vfelim).  Typical Value = 19.
         self.vhmax: PU = PU(75)  # Maximum field current limiter signal reference (Vhmax).  Typical Value = 75.
         self.vrmax: PU = PU(44)  # Maximum voltage regulator output (Vrmax).  Typical Value = 44.
         self.vrmin: PU = PU(-36)  # Minimum voltage regulator output (Vrmin).  Typical Value = -36.
