# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIeeeDc3A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type DC3A model. This model represents older systems,
    in particular those dc commutator exciters with non-continuously acting regulators that were
    commonly used before the development of the continuously acting varieties. These systems respond
    at basically two different rates, depending upon the magnitude of voltage error. For small errors,
    adjustment is made periodically with a signal to a motor-operated rheostat. Larger errors cause
    resistors to be quickly shorted or inserted and a strong forcing signal applied to the exciter.
    Continuous motion of the motor-operated rheostat occurs for these larger error signals, even
    though it is bypassed by contactor action.
    
    Reference: IEEE Standard 421.5-2005 Section 5.3.
    
    @author pcha006
    @version 1.0
    @created 29-Dec-2023 11:24:18 PM
    """
    
    def __init__(self) -> None:
        super().__init__()
        self.efd1: Optional[PU] = PU()
        self.efd2: Optional[PU] = PU()
        self.exclim: Optional[bool] = False
        self.ke: Optional[PU] = PU()
        self.kv: Optional[PU] = PU()
        self.seefd1: Optional[float] = 1.0
        self.seefd2: Optional[float] = 1.0
        self.te: Optional[Seconds] = Seconds()
        self.trh: Optional[Seconds] = Seconds()
        self.vrmax: Optional[PU] = PU()
        self.vrmin: Optional[PU] = PU()
