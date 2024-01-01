# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

class ExcAc6A(ExcitationSystemDynamics):
    """
    Modified IEEE AC6A alternator-supplied rectifier excitation system with speed input.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:17 PM
    """

    def __init__(self) -> None:
        """
        Voltage regulator gain (Ka).  Typical Value = 536.
        """
        self.ka: Optional[float] = 1.0
        
        """
        Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 0.173.
        """
        self.kc: Optional[float] = 1.0

        """
        Demagnetizing factor, a function of exciter alternator reactances (Kd).  Typical Value = 1.91.
        """
        self.kd: Optional[float] = 1.0

        """
        Exciter constant related to self-excited field (Ke).  Typical Value = 1.6.
        """
        self.ke: Optional[float] = 1.0

        """
        Exciter field current limiter gain (Kh).  Typical Value = 92.
        """
        self.kh: Optional[float] = 1.0

        """
        Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0.
        """
        self.ks: Optional[float] = 1.0

        """
        Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance (Se[Ve1]).  Typical Value = 0.214.
        """
        self.seve1: Optional[float] = 1.0

        """
        Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance (Se[Ve2]).  Typical Value = 0.044.
        """
        self.seve2: Optional[float] = 1.0

        """
        Voltage regulator time constant (Ta).  Typical Value = 0.086.
        """
        self.ta: Optional[float] = 1.0

        """
        Voltage regulator time constant (Tb).  Typical Value = 9.
        """
        self.tb: Optional[float] = 1.0

        """
        Voltage regulator time constant (Tc).  Typical Value = 3.
        """
        self.tc: Optional[float] = 1.0

        """
        Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1.
        """
        self.te: Optional[float] = 1.0

        """
        Exciter field current limiter time constant (Th).  Typical Value = 0.08.
        """
        self.th: Optional[float] = 1.0

        """
        Exciter field current limiter time constant (Tj).  Typical Value = 0.02.
        """
        self.tj: Optional[float] = 1.0

        """
        Voltage regulator time constant (Tk).  Typical Value = 0.18.
        """
        self.tk: Optional[float] = 1.0

        """
        Maximum voltage regulator output (Vamax).  Typical Value = 75.
        """
        self.vamax: Optional[float] = 1.0

        """
        Minimum voltage regulator output (Vamin).  Typical Value = -75.
        """
        self.vamin: Optional[float] = 1.0

        """
        Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1).  Typical Value = 7.4.
        """
        self.ve1: Optional[float] = 1.0

        """
        Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2).  Typical Value = 5.55.
        """
        self.ve2: Optional[float] = 1.0

        """
        Exciter field current limit reference (Vfelim).  Typical Value = 19.
        """
        self.vfelim: Optional[float] = 1.0

        """
        Maximum field current limiter signal reference (Vhmax).  Typical Value = 75.
        """
        self.vhmax: Optional[float] = 1.0

        """
        Maximum voltage regulator output (Vrmax).  Typical Value = 44.
        """
        self.vrmax: Optional[float] = 1.0

        """
        Minimum voltage regulator output (Vrmin).  Typical Value = -36.
        """
        self.vrmin: Optional[float] = 1.0
