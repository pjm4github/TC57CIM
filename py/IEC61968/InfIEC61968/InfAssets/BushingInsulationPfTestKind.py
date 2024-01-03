# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 14:41:22 2024
from enum import Enum


class BushingInsulationPfTestKind(Enum):
    """
    Kind of PF test for bushing insulation.
    @author T. Kostic
    @version 1.0
    @created 29-Dec-2023 6:12:55 PM
    """
    
    # Power factor tap-to-ground.
    C1 = 1
    
    # Power factor tap-to-conductor.
    C2 = 2
