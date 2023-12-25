# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# corporate_standard_kind.py

from enum import Enum

class CorporateStandardKind(Enum):
    # Asset model is used as corporate standard.
    STANDARD = 1
    
    # Asset model is used experimentally.
    EXPERIMENTAL = 2
    
    # Asset model usage is under evaluation.
    UNDER_EVALUATION = 3
    
    # Other kind of corporate standard for the asset model.
    OTHER = 4
