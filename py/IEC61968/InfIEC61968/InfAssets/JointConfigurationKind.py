# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 14:41:22 2024
from enum import Enum

class JointConfigurationKind(Enum):
    """
    Kind of configuration for joints.
    @author T. Kostic
    @version 1.0
    @created 29-Dec-2023 6:13:59 PM
    """
    WIRES3TO1 = 1
    WIRES2TO1 = 2
    WIRES1TO1 = 3
    OTHER = 4
