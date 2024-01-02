# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Union

class ExcElin1:
    """
    Static PI transformer fed excitation system: ELIN (VATECH) - simplified model.
    This model represents an all-static excitation system. A PI voltage controller
    establishes a desired field current set point for a proportional current
    controller. The integrator of the PI controller has a follow-up input to match
    its signal to the present field current.  A power system stabilizer with power
    input is included in the model.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:17 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        self.dpnf: Union[float, int]  = 0  # Controller follow up dead band (Dpnf).  Typical Value = 0.
        self.efmax: Union[float, int]  = 0  # Maximum open circuit excitation voltage (Efmax).  Typical Value = 5.
        self.efmin: Union[float, int]  = 0  # Minimum open circuit excitation voltage (Efmin).  Typical Value = -5.
        self.ks1: Union[float, int]  = 0  # Stabilizer Gain 1 (Ks1).  Typical Value = 0.
        self.ks2: Union[float, int]  = 0  # Stabilizer Gain 2 (Ks2).  Typical Value = 0.
        self.smax: Union[float, int]  = 0  # Stabilizer Limit Output (smax).  Typical Value = 0.1.
        self.tfi: Seconds = Seconds(0)  # Current transducer time constant (Tfi).  Typical Value = 0.
        self.tnu: Seconds = Seconds(0)  # Controller reset time constant (Tnu).  Typical Value = 2.
        self.ts1: Seconds = Seconds(0)  # Stabilizer Phase Lag Time Constant (Ts1).  Typical Value = 1.
        self.ts2: Seconds = Seconds(0)  # Stabilizer Filter Time Constant (Ts2).  Typical Value = 1.
        self.tsw: Seconds = Seconds(0)  # Stabilizer parameters (Tsw).  Typical Value = 3.
        self.vpi: Union[float, int]  = 0  # Current controller gain (Vpi).  Typical Value = 12.45.
        self.vpnf: Union[float, int]  = 0  # Controller follow up gain (Vpnf).  Typical Value = 2.
        self.vpu: Union[float, int]  = 0  # Voltage controller proportional gain (Vpu).  Typical Value = 34.5.
        self.xe: Union[float, int]  = 0  # Excitation transformer effective reactance (Xe) (>=0).  Xe represents the 
        # regulation of the transformer/rectifier unit.  Typical Value = 0.06.
