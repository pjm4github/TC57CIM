# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
# Relationship between tailbay head loss hight (y-axis) and the total discharge
# into the power station's tailbay volume per time unit (x-axis). There could be
# more than one curve depending on the level of the tailbay reservoir or river
# level. 
# @created 02-Jan-2024 10:59:06 PM
from IEC61970.Base.Core.Curve import Curve


class TailbayLossCurve(Curve):
    """
    Relationship between tailbay head loss height (y-axis) and the total discharge
    into the power station's tailbay volume per time unit (x-axis). There could be
    more than one curve depending on the level of the tailbay reservoir or river
    level.
    """

    def __init__(self):
        super().__init__()

