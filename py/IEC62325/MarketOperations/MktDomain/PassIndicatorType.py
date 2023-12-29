# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum

class PassIndicatorType(Enum):
    """
    Defines the individual passes that produce results per execution type/market
    type.
    """
    MPM_1 = 1  # Market Power Mitigation Pass 1
    MPM_2 = 2  # Market Power Mitigation Pass 2
    MPM_3 = 3  # Market Power Mitigation Pass 3
    MPM_4 = 4  # Market Power Mitigation Pass 4
    RUC = 5  # Residual Unit Commitment
    RTPD = 6  # Real Time Pre Dispatch
    RTED = 7  # Real Time Economic Dispatch
    HA_SCUC = 8  # Hour Ahead Security Constrained Unit Commitment
    DA = 9  # Day Ahead
