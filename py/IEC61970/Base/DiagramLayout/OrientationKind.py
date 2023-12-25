# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:25:23 2023
from enum import Enum

class OrientationKind(Enum):
    """
    The orientation of the coordinate system with respect to top, left, and the coordinate number system.
    @author mcmorran
    @version 1.0
    @created 15-Dec-2023 4:38:28 PM
    """

    POSITIVE = 0  # "positive"  # For 2D diagrams, a positive orientation will result in X values increasing from left
                  # to right and Y values increasing from bottom to top.  This is also known as a right hand orientation.

    NEGATIVE = 1  # "negative"  # For 2D diagrams, a negative orientation gives the left-hand orientation
                  # (favoured by computer graphics displays) with X values increasing from left to right and Y values
                  # increasing from top to bottom.  This is also known as a left hand orientation.
