from enum import Enum


class TurbineType(Enum):
    """
    Type of turbine.
    Created: 02-Jan-2024 11:07:35 PM
    """
    FRANCIS = 1  # Francis turbine
    PELTON = 2   # Pelton turbine
    KAPLAN = 3   # Kaplan turbine
