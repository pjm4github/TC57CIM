# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 16:32:51 2023
from typing import Union

from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.LoadDynamics.GenericNonLinearLoadModelKind import GenericNonLinearLoadModelKind
from IEC61970.Dynamics.StandardModels.LoadDynamics.LoadDynamics import LoadDynamics


class LoadGenericNonLinear(LoadDynamics):
    """
    These load models (known also as generic non-linear dynamic (GNLD) load models)
    can be used in mid-term and long-term voltage stability simulations (i.e., to
    study voltage collapse), as they can replace a more detailed representation of
    aggregate load, including induction motors, thermostatically controlled and
    static loads.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """

    def __init__(self) -> None:
        super().__init__()

        # Steady state voltage index for reactive power (BS).
        self.bs: Union[float, None] = 1.0

        # Transient voltage index for reactive power (BT).
        self.bt: Union[float, None] = 1.0

        # Type of generic non-linear load model.
        self.generic_non_linear_load_model_type: Union[
            GenericNonLinearLoadModelKind, None] = GenericNonLinearLoadModelKind.LOAD_ADAPTIVE

        # Steady state voltage index for active power (LS).
        self.ls: Union[float, None] = 1.0

        # Transient voltage index for active power (LT).
        self.lt: Union[float, None] = 1.0

        # Dynamic portion of active load (P<sub>T</sub>).
        self.pt: Union[float, None] = 1.0

        # Dynamic portion of reactive load (Q<sub>T</sub>).
        self.qt: Union[float, None] = 1.0

        # Time constant of lag function of active power (T<sub>P</sub>).
        self.tp: Union[Seconds, None] = Seconds()

        # Time constant of lag function of reactive power (T<sub>Q</sub>).
        self.tq: Union[Seconds, None] = Seconds()
