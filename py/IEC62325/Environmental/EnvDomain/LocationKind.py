# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# No imports needed
from enum import Enum


# The nature of the location being defined for an environmental entity. Possible
# values are center, perimeter, primary, secondary.
# @author ppbr003
# @version 1.0
# @created 25-Dec-2023 9:21:22 PM
class LocationKind(Enum):
    # The center of a phenomenon. Will typically be used with a Location with a
    # single PositionPoint instance.
    CENTER = 0

    # The area or line of a phenomenon, not the center. Will typically be used with a
    # Location with multiple PositionPoint instances.
    EXTENT = 1

    # Primary area to which an environmental alert applies.
    PRIMARY = 2

    # Secondary area to which an environmental alert applies.
    SECONDARY = 3
