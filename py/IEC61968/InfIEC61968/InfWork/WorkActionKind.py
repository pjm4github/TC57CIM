# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from enum import Enum

class WorkActionKind(Enum):
    """
    Kinds of activities to be performed on a Compatible Unit.
    @created 29-Dec-2023 9:21:05 PM
    """
    # Install.
    INSTALL = 1

    # Remove.
    REMOVE = 2

    # Leave it in place but not use it.
    ABANDON = 3

    # Remove from one and install at another location.
    TRANSFER = 4
