# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
from enum import Enum

class IccpAccessPrivilegeKind(Enum):
    """Provides access privilege information regarding an ICCP point."""
    
    # Indicates that the remote is not allowed to change the value of the ICCPPoint.
    READ_ONLY = 0  # "readOnly"
    
    # Indicates that the remote can not only get the value, but may also change the value of the ICCP Point.
    READ_WRITE = 1  # "readWrite"
