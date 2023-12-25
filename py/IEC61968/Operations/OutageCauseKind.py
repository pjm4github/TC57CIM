# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# outage_cause_kind.py
from enum import Enum


class OutageCauseKind(Enum):
    LIGHTING_STRIKE = 1  # "LIGHTING_STRIKE"
    ANIMAL = 2  # "ANIMAL"
    LINE_DOWN = 3  # "LINE_DOWN"
    POLE_DOWN = 4  # "POLE_DOWN"
    TREE_DOWN = 5  #"TREE_DOWN"
