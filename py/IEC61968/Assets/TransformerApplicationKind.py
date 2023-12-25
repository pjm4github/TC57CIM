# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# transformer_application_kind.py
from enum import Enum


class TransformerApplicationKind(Enum):
    TRANSMISSION_BUS_TO_BUS = 1
    TRANSMISSION_BUS_TO_DISTRIBUTION = 2
    GENERATOR_STEP_UP = 3
    DISTRIBUTION = 4
