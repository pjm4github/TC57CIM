# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics import ExcitationSystemDynamics
from typing import Union


class ExcOEX3T(ExcitationSystemDynamics):
    """
    Modified IEEE Type ST1 Excitation System with semi-continuous and acting
    terminal voltage limiter.
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:18 PM
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        super().__init__()
        self.e1: Union[float, int] = 0  # Saturation parameter (E1)
        self.e2: Union[float, int] = 0  # Saturation parameter (E2)
        self.ka: Union[float, int] = 0  # Gain (KA)
        self.kc: Union[float, int] = 0  # Gain (KC)
        self.kd: Union[float, int] = 0  # Gain (KD)
        self.ke: Union[float, int] = 0  # Gain (KE)
        self.kf: Union[float, int] = 0  # Gain (KF)
        self.see1: Union[float, int] = 0  # Saturation parameter (S*E1(E1))
        self.see2: Union[float, int] = 0  # Saturation parameter (S*E1(E1))
        self.t1: Union[float, int] = 0  # Time constant (T1)
        self.t2: Union[float, int] = 0  # Time constant (T2)
        self.t3: Union[float, int] = 0  # Time constant (T3)
        self.t4: Union[float, int] = 0  # Time constant (T4)
        self.t5: Union[float, int] = 0  # Time constant (T5)
        self.t6: Union[float, int] = 0  # Time constant (T6)
        self.te: Union[float, int] = 0  # Time constant (TE)
        self.tf: Union[float, int] = 0  # Time constant (TF)
        self.vrmax: Union[float, int] = 0  # Limiter (VRMAX)
        self.vrmin: Union[float, int] = 0  # Limiter (VRMIN)
