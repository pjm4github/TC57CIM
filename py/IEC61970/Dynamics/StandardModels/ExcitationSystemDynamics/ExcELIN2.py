# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcElin2(ExcitationSystemDynamics):
    """
    Detailed Excitation System Model - ELIN (VATECH).  This model represents an all-
    static excitation system. A PI voltage controller establishes a desired field
    current set point for a proportional current controller. The integrator of the
    PI controller has a follow-up input to match its signal to the present field
    current. Power system stabilizer models used in conjunction with this
    excitation system model: PssELIN2, PssIEEE2B, Pss2B.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:17 PM
    """

    def __init__(self) -> None:
        """
        Constructor for ExcELIN2
        """
        super().__init__()
        self.efdbasOptional[float] = 1.0  # Gain (Efdbas).  Typical Value = 0.1.
        self.iefmaxOptional[float] = 1.0  # Limiter (Iefmax).  Typical Value = 1.
        self.iefmax2: Optional[float] = 1.0  # Minimum open circuit excitation voltage (Iefmax2).  Typical Value = -5.
        self.iefmin: Optional[float] = 1.0  # Limiter (Iefmin).  Typical Value = 1.
        self.k1: Optional[float] = 1.0  # Voltage regulator input gain (K1).  Typical Value = 0.
        self.k1ec: Optional[float] = 1.0  # Voltage regulator input limit (K1ec).  Typical Value = 2.
        self.k2: Optional[float] = 1.0  # Gain (K2).  Typical Value = 5.
        self.k3: Optional[float] = 1.0  # Gain (K3).  Typical Value = 0.1.
        self.k4: Optional[float] = 1.0  # Gain (K4).  Typical Value = 0.
        self.kd1: Optional[float] = 1.0  # Voltage controller derivative gain (Kd1).  Typical Value = 34.5.
        self.ke2: Optional[float] = 1.0  # Gain (Ke2).  Typical Value = 0.1.
        self.ketb: Optional[float] = 1.0  # Gain (Ketb).  Typical Value = 0.06.
        self.pid1max: Optional[float] = 1.0  # Controller follow up gain (PID1max).  Typical Value = 2.
        self.seve1: Optional[float] = 1.0  # Exciter saturation function value at the corresponding exciter voltage, Ve1, back of commutating reactance (Se[Ve1]).  Typical Value = 0.
        self.seve2: Optional[float] = 1.0  # Exciter saturation function value at the corresponding exciter voltage, Ve2, back of commutating reactance (Se[Ve2]).  Typical Value = 1.
        self.tb1: Optional[float] = 1.0  # Voltage controller derivative washout time constant (Tb1).  Typical Value = 12.45.
        self.te: Optional[float] = 1.0  # Time constant (Te).  Typical Value = 0.
        self.te2: Optional[float] = 1.0  # Time Constant (Te2).  Typical Value = 1.
        self.ti1: Optional[float] = 1.0  # Controller follow up dead band (Ti1).  Typical Value = 0.
        self.ti3: Optional[float] = 1.0  # Time constant (Ti3).  Typical Value = 3.
        self.ti4: Optional[float] = 1.0  # Time constant (Ti4).  Typical Value = 0.
        self.tr4: Optional[float] = 1.0  # Time constant (Tr4).  Typical Value = 1.
        self.upmax: Optional[float] = 1.0  # Limiter (Upmax).  Typical Value = 3.
        self.upmin: Optional[float] = 1.0  # Limiter (Upmin).  Typical Value = 0.
        self.ve1: Optional[float] = 1.0  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1).  Typical Value = 3.
        self.ve2: Optional[float] = 1.0  # Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve2).  Typical Value = 0.
        self.xp: Optional[float] = 1.0  # Excitation transformer effective reactance (Xp).  Typical Value = 1.
