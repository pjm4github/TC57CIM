# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local import
from enum import Enum

class TransmissionModeKind(Enum):
    
    # Message transmission mode whereby messages or commands are sent to specific devices.
    NORMAL = 1
    
    # Message transmission mode whereby messages or commands are broadcast to unspecified devices 
    # listening for such communications.
    ANONYMOUS = 2
    
    # Message transmission mode whereby messages or commands are sent by both 'normal' and 'anonymous' methods.
    BOTH = 3
