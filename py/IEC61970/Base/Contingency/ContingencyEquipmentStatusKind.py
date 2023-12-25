# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:02:27 2023
from enum import Enum

class ContingencyEquipmentStatusKind(Enum):
    """
    Indicates the state which the contingency equipment is to be in when the
    contingency is applied.
    """
    # The equipment is to be put into service.
    IN_SERVICE = 0
    OUT_OF_SERVICE = 1

