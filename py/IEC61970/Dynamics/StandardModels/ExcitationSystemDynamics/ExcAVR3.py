# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcAvr3(ExcitationSystemDynamics):
    """
    Italian excitation system. It represents exciter dynamo and electric regulator.

    @uthor pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:17 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()
        self.e1: PU = PU()  # Field voltage value 1 (E1). Typical Value = 4.18
        self.e2: PU = PU()  # Field voltage value 2 (E2). Typical Value = 3.14
        self.ka: float = 1.0  # AVR gain (K<A>). Typical Value = 100
        self.se1: float = 1.0  # Saturation factor at E1 (S(E1)). Typical Value = 0.1
        self.se2: float = 1.0  # Saturation factor at E2 (S(E2)). Typical Value = 0.03
        self.t1: Seconds = Seconds()  # AVR time constant (T1). Typical Value = 20
        self.t2: Seconds = Seconds()  # AVR time constant (T2). Typical Value = 1.6
        self.t3: Seconds = Seconds()  # AVR time constant (T3). Typical Value = 0.66
        self.t4: Seconds = Seconds()  # AVR time constant (T4). Typical Value = 0.07
        self.te: Seconds = Seconds()  # Exciter time constant (TEE). Typical Value = 1
        self.vrmn: PU = PU()  # Minimum AVR output (V<RMN>). Typical Value = -7.5
        self.vrmx: PU = PU()  # Maximum AVR output (V<RMX>). Typical Value = 7.5
