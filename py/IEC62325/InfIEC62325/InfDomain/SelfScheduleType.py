# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 19:52:13 2023
from enum import Enum

class SelfScheduleType(Enum):
    PT = 1  # PT
    ETC = 2  # ETC
    TOR = 3  # TOR
    RMR = 4  # RMR
    RMT = 5  # RMT
    RGMR = 6  # RGMR
    ORFC = 7  # ORFC
    
    # Self-Provision
    SP = 8  # SP
    IFM = 9  # IFM
    RUC = 10  # RUC
    
    # RA Obligations
    RA = 11  # RA
    
    PUMP_ETC = 12  # PUMP_ETC
    PUMP_TOR = 13  # PUMP_TOR
    
    # Base Schedule
    BAS = 14  # BAS
    
    # Lay-off schedule
    LOF = 15  # LOF
    WHL = 16  # WHL
