# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# Types used for resource certification.
# @author mspivbe2
# @version 1.0
# @created 25-Dec-2023 9:21:23 PM
from enum import Enum


class ResourceCertificationKind(Enum):
    # Regulation Up (RU, REGUP)
    REGULATION_UP = 1
    # Regulation Down (RD, REGDN)
    REGULATION_DOWN = 2
    # Spinning Reserve (SR, RRSPIN)
    SPINNING_RESERVE = 3
    # Non Spinning Reserve (NR, NONSPIN)
    NON_SPINNING_RESERVE = 4
    # Reliability Must Run (RMR)
    RELIABILITY_MUST_RUN = 5
    # Black start
    BLACK_START = 6
    # Demand Side Reponse (DSR)
    DEMAND_SIDE_RESPONSE = 7
    # Synchronous Condenser (SYNCCOND)
    SYNCHRONOUS_CONDENSER = 8
    # Intermittent resource
    INTERMITTENT_RESOURCE = 9
    # Reliability unit commitment (RUC)
    RELIABILITY_UNIT_COMMITMENT = 10
    ENERGY = 11
    CAPACITY = 12
