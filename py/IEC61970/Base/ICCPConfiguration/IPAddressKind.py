# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
from enum import Enum

class IPAddressKind(Enum):
    """
    Indicates if the addressing of the IPAccessPoint, gateway, and subnet are per
    IPv4 or IPv6
    @author herb
    @version 1.0
    @created 15-Dec-2023 4:38:27 PM
    """
    IPv4 = 0  # Indicates that IPv4 dotted decimal notation is in use.
    IPv6 = 1  # Indicates that an IPv6 dotted decimal is in use.
