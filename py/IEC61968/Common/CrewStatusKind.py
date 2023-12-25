# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import Enum

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.String import String


class CrewStatusKind(Enum):
    ARRIVED = 1  # STRING("ARRIVED")
    ASSIGNED = 2  # STRING("ASSIGNED")
    AWAITING_CREW_ASSIGNMENT = 3  # STRING("AWAITINGCREWASSIGNMENT")
    ENROUTE = 4  # STRING("ENROUTE")
    FIELD_COMPLETE = 5  # STRING("FIELDCOMPLETE")
