# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from enum import StrEnum


class HydroPlantStorageKind(StrEnum):
    """
    The type of hydro power plant.
    @created 02-Jan-2024 11:01:16 PM
    """
    
    # Run of river.
    RUN_OF_RIVER = 1
    
    # Pumped storage.
    PUMPED_STORAGE = 2
    
    # Storage.
    STORAGE = 3
