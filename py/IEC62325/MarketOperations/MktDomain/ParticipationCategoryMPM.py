# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum


class ParticipationCategoryMPM(Enum):
    Y = 1  # * 'Y' - Participates in both LMPM and SMPM
    N = 2  # * 'N' - Not included in LMP price measures
    S = 3  # * 'S' - Participates in SMPM price measures
    L = 4  # * 'L' - Participates in LMPM price measures