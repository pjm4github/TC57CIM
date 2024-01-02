# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:07:00 2023
from enum import Enum

class RotorKind(Enum):
    """
    Type of rotor on physical machine.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """
    # Round rotor type of synchronous machine.
    ROUND_ROTOR = 1
    
    # Salient pole type of synchronous machine.
    SALIENT_POLE = 2
