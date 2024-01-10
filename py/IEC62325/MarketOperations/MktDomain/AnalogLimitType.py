from enum import Enum


class AnalogLimitType(Enum):
    # Limit type specified for AnalogLimits.

    # Branch Medium Term Limit
    BranchMediumTerm = 1

    # Branch Long Term Limit
    BranchLongTerm = 2

    # Branch Short Term Limit
    BranchShortTerm = 3

    # Voltage High Limit
    VoltageHigh = 4

    # Voltage Low Limit
    VoltageLow = 5
