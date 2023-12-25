# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
from enum import Enum

class SecurityRequirementKind(Enum):
    """
    Defines the expected level of security to be negotiated.
    """
    # Indicates that the actor does not support any security options
    NOT_SUPPORTED = 0
    # Indicates that the transport level security, per IEC 62351-6, is required.
    TRANSPORT_SECURITY_REQUIRED = 1
    APPLICATION_SECURITY_REQUIRED = 2
