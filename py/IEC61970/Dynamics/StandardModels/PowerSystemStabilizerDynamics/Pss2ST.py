# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:03:17 2023
from typing import Union

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.InputSignalKind import InputSignalKind
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import \
    PowerSystemStabilizerDynamics


class Pss2ST(PowerSystemStabilizerDynamics):
    """
    PTI Microprocessor-Based Stabilizer type 1.
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.input_signal1_type: InputSignalKind  # Type of input signal #1.  Typical Value = rotorAngularFrequencyDeviation.
        self.input_signal2_type: InputSignalKind  # Type of input signal #2.  Typical Value = generatorElectricalPower.                      
        self.k1: PU = PU()  # Gain (K1). 
        self.k2: PU = PU()  # Gain (K2). 
        self.lsmax: PU = PU()  # Limiter (Lsmax).    
        self.lsmin: PU = PU()  # Limiter (Lsmin).    
        self.t1: Seconds = Seconds()  # Time constant (T1).           
        self.t10: Seconds = Seconds()  # Time constant (T10).            
        self.t2: Seconds = Seconds()  # Time constant (T2).          
        self.t3: Seconds = Seconds()  # Time constant (T3).           
        self.t4: Seconds = Seconds()  # Time constant (T4).          
        self.t5: Seconds = Seconds()  # Time constant (T5).           
        self.t6: Seconds = Seconds()  # Time constant (T6).           
        self.t7: Seconds = Seconds()  # Time constant (T7).           
        self.t8: Seconds = Seconds()  # Time constant (T8).           
        self.t9: Seconds = Seconds()  # Time constant (T9).           
        self.vcl: PU = PU()  # Cutoff limiter (Vcl).  
        self.vcu: PU = PU()  # Cutoff limiter (Vcu).  





















