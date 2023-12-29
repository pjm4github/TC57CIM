# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import StrEnum


class ResourceRegistrationStatus(StrEnum):
    """
    Types of resource registration status, for example:
    
    - Active
    - Mothballed
    - Planned
    - Decommissioned
    
    @author mspivbe2
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """

    # Resource registration is active
    ACTIVE = "Active"

    # Registration status is in the planning stage
    PLANNED = "Planned"

    # Resource registration has been suspended
    MOTHBALLED = "Mothballed"

    # Resource registration status is decommissioned
    DECOMMISSIONED = "Decommissioned"
