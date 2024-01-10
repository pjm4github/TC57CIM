# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import Enum


class AssetHazardKind(Enum):
    AMBIENT_TEMP_BELOW_MINUS12 = 1  # 'AMBIENTTEMPBELOWMINUS12'
    AMBIENT_TEMP_ABOVE_38 = 2  # 'AMBIENTTEMPABOVE38'
    VEGETATION = 3  # 'VEGETATION'
    CHILDREN_AT_PLAY = 4  # 'CHILDRENATPLAY'
    FISHING_AREA = 5  # 'FISHINGAREA'
    OTHER = 6  # 'OTHER'
