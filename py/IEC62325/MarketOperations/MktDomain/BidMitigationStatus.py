# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum


class BidMitigationStatus(Enum):
    """
    For example:
        'S' - Mitigated by SMPM because of "misconduct"
        'L; - Mitigated by LMPM because of "misconduct"
        'R' - Modified by LMPM because of RMR rules
        'M' - Mitigated because of "misconduct" both by SMPM and LMPM
        'B' - Mitigated because of "misconduct" both by SMPM and modified by LMLM because of RMR rules
        'O' - original
    """
    S = 1
    L = 2
    R = 3
    M = 4
    B = 5
    O = 6
