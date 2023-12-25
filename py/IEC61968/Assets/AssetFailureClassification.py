# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# asset_failure_classification.py

from enum import Enum

class AssetFailureClassification(Enum):
    MAJOR = 1
    MINOR = 2
    DEFECT = 3
    MAJOR_NEEDS_REPLACEMENT = 4
