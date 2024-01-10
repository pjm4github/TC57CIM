# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# No need for package declaration in Python
from enum import Enum


# Convert enum class to Python class
class UnitRegulationKind(Enum):
    # Unit regulation kind.
    # @author mspivbe2
    # @version 1.0
    # @created 25-Dec-2023 9:21:23 PM

    # Unit is not on regulation.
    ZERO = 0

    # Unit is on AGC and regulating.
    ONE = 1

    # Unit is supposed to be on regulation, but it is not under regulation now.
    TWO = 2
