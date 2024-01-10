# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:07:00 2023
from enum import Enum


class SynchronousMachineModelKind(Enum):
    """
    Type of synchronous machine model used in Dynamic simulation applications.
    """
    SUBTRANSIENT = 1  # Subtransient synchronous machine model.

    SUBTRANSIENT_TYPE_F = 2  # WECC Type F variant of subtransient synchronous machine model.

    SUBTRANSIENT_TYPE_J = 3  # WECC Type J variant of subtransient synchronous machine model.

    SUBTRANSIENT_SIMPLIFIED = 4  # Simplified version of subtransient synchronous machine model where magnetic
    # coupling between the direct and quadrature axes is ignored.

    SUBTRANSIENT_SIMPLIFIED_DIRECT_AXIS = 5  # Simplified version of a subtransient synchronous machine model
    # with no damper circuit on d-axis.
