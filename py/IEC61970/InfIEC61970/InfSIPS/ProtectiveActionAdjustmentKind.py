from enum import Enum


class ProtectiveActionAdjustmentKind(Enum):
    """
    Categorisation of different protective action adjustments that can be performed on equipment.
    Author: sveinols
    Version: 1.0
    Created: 02-Jan-2024 9:36:55 PM
    """
    BY_PERCENTAGE = 1  # "byPercentage"  # The adjustment is in percentage of the active value.
    BY_VALUE = 2  # "byValue"  # The adjustment is given by a value that defines the changes to the active value.
    SET_VALUE = 3  # "setValue"  # The equipment will operate on the new value.
    MEASUREMENT = 4  # "measurement"  # The equipment will operate on a value given by a measurement.
