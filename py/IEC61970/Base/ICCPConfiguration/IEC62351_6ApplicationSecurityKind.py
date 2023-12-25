# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
from enum import Enum

class IEC62351_6ApplicationSecurityKind(Enum):
    """
    Specifies the expected security mechanism, per IEC 62351-6, to be utilized.
    @author herb
    @version 1.0
    @created 15-Dec-2023 4:38:27 PM
    """

    # Indicates that the link does not require security.
    NO_SECURITY = 0

    # Indicates that authentication based upon ACSE is required.
    APPLICATION_LEVEL = 1

    # Indicates that the Edition 3, end-to-end security is needed. (this would not be
    # utilized for ICCP, but for IEC 61850).
    END_TO_END = 2
