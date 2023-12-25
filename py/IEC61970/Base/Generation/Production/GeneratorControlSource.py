from enum import Enum

class GeneratorControlSource(Enum):
    """
    The source of controls for a generating unit.
    """
    UNAVAILABLE = 0  # Not available.
    OFFAGC = 1  # Off of automatic generation control (AGC).
    ONAGC = 2  # On automatic generation control (AGC).
    PLANTCONTROL = 3  # Plant is controlling.
