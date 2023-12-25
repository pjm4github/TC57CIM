# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:22:57 2023
from enum import Enum

class VsPpccControlKind(Enum):
    """
    Types applicable to the control of real power and/or DC voltage
    by voltage source converter.
    """
    PPCC = 1  # Control variable (target) is real power at PCC bus.

    UDC = 2   # Control variable (target) is DC voltage and real power at PCC bus is derived.

    PPCC_AND_UDC_DROOP = 3  # Control variables (targets) are both active power at point of common coupling
    # and local DC voltage, with the droop.

    PPCC_AND_UDC_DROOP_WITH_COMPENSATION = 4  # Control variables (targets) are both active power at point of
    # common coupling
    # and compensated DC voltage, with the droop; compensation factor is the
    # resistance, as an approximation of the DC voltage of a common (real or virtual)
    # node in the DC network.

    PPCC_AND_UDC_DROOP_PILOT = 5   # Control variables (targets) are both active power at point of
    # common coupling and the pilot DC voltage, with the droop.