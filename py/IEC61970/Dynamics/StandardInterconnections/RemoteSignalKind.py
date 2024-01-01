# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:50:27 2023
from enum import Enum
from typing import Any


class RemoteSignalKind(Enum):
    """
    Type of input signal coming from remote bus.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 10:56:03 PM
    """

    # Input is voltage frequency from remote terminal bus.
    REMOTE_BUS_VOLTAGE_FREQUENCY: Any = 1

    # Input is voltage frequency deviation from remote terminal bus.
    REMOTE_BUS_VOLTAGE_FREQUENCY_DEVIATION: Any = 2

    # Input is frequency from remote terminal bus.
    REMOTE_BUS_FREQUENCY: Any = 3

    # Input is frequency deviation from remote terminal bus.
    REMOTE_BUS_FREQUENCY_DEVIATION: Any = 4

    # Input is voltage amplitude from remote terminal bus.
    REMOTE_BUS_VOLTAGE_AMPLITUDE: Any = 5

    # Input is voltage from remote terminal bus.
    REMOTE_BUS_VOLTAGE: Any = 6

    # Input is branch current amplitude from remote terminal bus.
    REMOTE_BRANCH_CURRENT_AMPLITUDE: Any = 7

    # Input is branch current amplitude derivative from remote terminal bus.
    REMOTE_BUS_VOLTAGE_AMPLITUDE_DERIVATIVE: Any = 8

    # Input is PU voltage derivative from remote terminal bus.
    REMOTE_PU_BUS_VOLTAGE_DERIVATIVE: Any = 9
