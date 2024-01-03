# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from enum import Enum

class WindPlantQControlModeKind(Enum):
    """ Reactivate power/voltage controller mode.
    @author civanov
    @version 1.0
    @created 29-Dec-2023 11:24:21 PM
    """

    # Reactive power reference.
    REACTIVE_POWER: int = 1

    # Power factor reference.
    POWER_FACTOR: int = 2

    # UQ static.
    UQ_STATIC: int = 3

    # Voltage control.
    VOLTAGE_CONTROL: int = 4
