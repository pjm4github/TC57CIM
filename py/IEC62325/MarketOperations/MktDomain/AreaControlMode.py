# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
"""
Area's present control mode.
@author mspivbe2
@version 1.0
@created 25-Dec-2023 9:21:22 PM
"""

from enum import Enum


class AreaControlMode(Enum):
    """
    CF = Constant Frequency
    """
    CF = 1
    
    """
    Constant Tie-Line
    """
    CTL = 2
    
    """
    Tie-Line Bias
    """
    TLB = 3
    
    """
    Off control
    """
    OFF = 4
