from enum import Enum


class CalculationKind(Enum):
    """
    Created on:      17-Dec-2023 6:48:20 PM
    Original author: sveinols
    Categorisation of calculation operation that can be done to Measurement.
    """
    SUM = 1  # Summation operation over the input values (operands).
    MUL = 2  # Multiplication operation the input values (operands).
    DIV = 3  # Division operation the input values (operands).
    SQRT = 4  # Square root operator - only one input value (operands).
