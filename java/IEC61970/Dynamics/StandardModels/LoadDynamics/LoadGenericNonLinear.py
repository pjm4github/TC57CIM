# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 16:32:51 2023
from typing import Union


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

    bs: Union[float, None]
    bt: Union[float, None]
    generic_non_linear_load_model_type: Union[GenericNonLinearLoadModelKind, None]
    ls: Union[float, None]
    lt: Union[float, None]
    pt: Union[float, None]
    qt: Union[float, None]
    tp: Union[Seconds, None]
    tq: Union[Seconds, None]

    def __init__(self) -> None:
        pass
