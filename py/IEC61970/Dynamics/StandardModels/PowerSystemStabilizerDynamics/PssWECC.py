# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:03:17 2023
from typing import Union

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.InputSignalKind import InputSignalKind
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import \
    PowerSystemStabilizerDynamics


class PssWecc(PowerSystemStabilizerDynamics):
    """
    Dual input Power System Stabilizer, based on IEEE type 2, with modified output limiter defined by WECC (Western Electricity Coordinating Council, USA).
    """
    
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.input_signal1_type: InputSignalKind = InputSignalKind.BUS_VOLTAGE # Type of input signal #1.
        self.input_signal2_type: InputSignalKind = InputSignalKind.BUS_FREQUENCY # Type of input signal #2.
        self.k1: PU = PU()  # Input signal 1 gain  (K<sub>1</sub>).
        self.k2: PU = PU()  # Input signal 2 gain (K<sub>2</sub>).
        self.t1: Seconds = Seconds()  # Input signal 1 transducer time constant (T<sub>1</sub>).
        self.t10: Seconds = Seconds()  # Lag time constant (T<sub>10</sub>).
        self.t2: Seconds = Seconds()  # Input signal 2 transducer time constant (T<sub>2</sub>).
        self.t3: Seconds = Seconds()  # Stabilizer washout time constant (T<sub>3</sub>).
        self.t4: Seconds = Seconds()  # Stabilizer washout time lag constant (T<sub>4</sub>) (>0).
        self.t5: Seconds = Seconds()  # Lead time constant (T<sub>5</sub>).
        self.t6: Seconds = Seconds()  # Lag time constant (T<sub>6</sub>).
        self.t7: Seconds = Seconds()  # Lead time constant (T<sub>7</sub>).
        self.t8: Seconds = Seconds()  # Lag time constant (T<sub>8</sub>).
        self.t9: Seconds = Seconds()  # Lead time constant (T<sub>9</sub>).
        self.vcl: PU = PU()  # Minimum value for voltage compensator output (V<sub>CL</sub>).
        self.vcu: PU = PU()  # Maximum value for voltage compensator output (V<sub>CU</sub>).
        self.vsmax: PU = PU()  # Maximum output signal (Vsmax).
        self.vsmin: PU = PU()  # Minimum output signal (Vsmin).




















