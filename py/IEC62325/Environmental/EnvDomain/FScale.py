# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# Local import
from enum import Enum


class FScale(Enum):
    """
    Fujita scale (referred to as EF-scale starting in 2007) for tornado damage.  A
    set of wind estimates (not measurements) based on damage. It uses three-second
    gusts estimated at the point of damage based on a judgment of 8 levels of
    damage to 28 indicators. These estimates vary with height and exposure.
    The 3-second gust is not the same wind as in standard surface observations.
    Enumerations based on NOAA conventions.
    """

    # 65-85 mph 3-second gust.
    ZERO = 0

    # 86-110 mph 3-second gust.
    ONE = 1

    # 111-135 mph 3-second gust.
    TWO = 2

    # 136-165 mph 3-second gust.
    THREE = 3

    # 166-200 mph 3-second gust.
    FOUR = 4

    # Over 200 mph 3-second gust.
    FIVE = 5

    # Unknown.
    MINUS_NINE = -9
