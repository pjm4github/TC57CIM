# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from typing import List

from IEC61970.Base.Core.Curve import Curve


class MaxStartUpCostCurve(Curve):
    """
    The maximum Startup costs and time as a function of down time.  Relationship
    between unit startup cost (Y1-axis) vs. unit elapsed down time (X-axis). This
    is used to validate the information provided in the Bid.
    @created 28-Dec-2023 12:17:58 PM
    """
    def __init__(self) -> None:
        super().__init__()
