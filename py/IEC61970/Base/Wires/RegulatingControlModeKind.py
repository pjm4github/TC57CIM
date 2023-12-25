# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import Enum

class RegulatingControlModeKind(Enum):
    """
    The kind of regulation model. For example regulating voltage, reactive power,
    active power, etc.
    """
    # Voltage is specified.
    VOLTAGE = 1

    # Active power is specified.
    ACTIVE_POWER = 2

    # Reactive power is specified.
    REACTIVE_POWER = 3

    # Current flow is specified.
    CURRENT_FLOW = 4

    # Admittance is specified.
    ADMITTANCE = 5

    # Control switches on/off by time of day. The times may change on the weekend, or
    # in different seasons.
    TIME_SCHEDULED = 6

    # Control switches on/off based on the local temperature (i.e., a thermostat).
    TEMPERATURE = 7

    # Power factor is specified.
    POWER_FACTOR = 8
