# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:39:47 2023
from IEC61970.Base.Core.Curve import Curve


class SubscribePowerCurve(Curve):
    """
    Price curve for specifying the cost of energy (X) at points in time (y1)
    according to a prcing structure, which is based on a tariff.
    @created 29-Dec-2023 9:26:13 PM
    """
    def __init__(self) -> None:
        super().__init__()
