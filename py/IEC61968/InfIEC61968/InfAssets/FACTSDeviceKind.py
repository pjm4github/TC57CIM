# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 14:41:22 2024
from enum import Enum

class FACTSDeviceKind(Enum):
    SVC = 1  # "svc"  # Static VAr compensator
    STATCOM = 2  # "statcom"  # Static synchronous compensator
    TCPAR = 3  # "tcpar"  # Thyristor-controlled phase-angle regulator
    TCSC = 4  # "tcsc"  # Thyristor-controlled series capacitor
    TCVL = 5  # "tcvl"  # Thyristor-controlled voltage limiter
    TSBR = 6  # "tsbr"  # Thyristor-switched braking resistor
    TSSC = 7  # "tssc"  # Thyristor-switched series capacitor
    UPFC = 8  # "upfc"  # Unified power flow controller
