# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# env_domain.py
from enum import Enum


class UncertaintyKind(Enum):
    """
    The type of uncertainty for a reading.
    @author mcmorran
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """
    
    # The value has standard uncertainty consistent with National Weather Service
    # practises given the instrument and manner of observation.
    STANDARD = 1
    
    # The value is interpolated.
    INTERPOLATED = 2
    
    # The value is estimated.
    ESTIMATED = 3
    
    # The process of value calculation or measurement is unknown.
    UNKNOWN = 4
