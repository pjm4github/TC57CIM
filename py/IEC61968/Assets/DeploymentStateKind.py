# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# deployment_state_kind.py

from enum import Enum

class DeploymentStateKind(Enum):
    NOT_YET_INSTALLED = 1
    INSTALLED = 2
    IN_SERVICE = 3
    OUT_OF_SERVICE = 4
    REMOVED = 5
