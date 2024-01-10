# Created on:      17-Dec-2023 6:50:17 PM
# Original author: sveinols
from enum import Enum


class PinEquipmentKind(Enum):
    """
    Categorisation of type of compare done on Equipment.
    """
    INSERVICE = 1  # Check if equipment is in service, True if in service otherwise false.
    RATEDCURRENT = 2  # Compare load flow result against rated current on the equipment (switch).
    VOLTAGELIMIT = 3  # Compare load flow result against the active voltage limit for the equipment.
    CURRENTLIMIT = 4  # Compare load flow result against the active current limit for the equipment.
    ACTIVEPOWERLIMIT = 5  # Compare load flow result against the active limit for active power for the
    # given equipment.
    APPARENTPOWERLIMIT = 6  # Compare load flow result against the active limit for apparent power for the
    # given equipment.
    CONNECTED = 7  # Check if all terminal on the equipment is connected.
