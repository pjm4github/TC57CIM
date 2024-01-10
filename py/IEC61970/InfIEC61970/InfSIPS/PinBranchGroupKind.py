from enum import Enum


class PinBranchGroupKind(Enum):
    """
    Created on:      17-Dec-2023 6:49:07 PM
    Original author: sveinols
    Categorisation of type of compare done on a branch group.
    """
    ACTIVEPOWER = 1  # Active power in the branch group.
    REACTIVEPOWER = 2  # reactive power in the branch group.
