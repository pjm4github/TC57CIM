# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 19:52:13 2023
from enum import Enum

class EnergyTypeCode(Enum):
    DASE = 1  # Day Ahead Scheduled Energy
    DSSE = 2  # Day Ahead Incremental Self Schedule Energy
    DABE = 3  # Day Ahead Incremental Energy Bid Awarded Energy
    OE = 4    # Optimal Energy
    HASE = 5  # Hour ahead pre-dispatched schedule energy
    SRE = 6   # Standard Ramping Energy
    RED = 7   # Ramping Energy Deviation
    EDE = 8   # Exceptional Dispatch energy
    RMRE = 9  # RMR Energy
    MSSLFE = 10  # MSSLF Energy
    RE = 11   # Residual Energy
    MLE = 12  # Minimum Load Energy
    SE = 13   # SLIC Energy
    RTSSE = 14  # Real time self scheduled energy
    DMLE = 15  # Day ahead minimum load energy
    PE = 16   # Pumping Energy
    TEE = 17  # Total Expected Energy
    DAPE = 18  # Day-Ahead Pumping Energy
