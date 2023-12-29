# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from typing import List

from IEC61970.Base.Core.Curve import Curve


class LoadReductionPriceCurve(Curve):
    """
    This is the price sensitivity that bidder expresses for allowing market load 
    interruption. Relationship between price (Y1-axis) vs. MW (X-axis).
    @created 28-Dec-2023 5:22:11 PM
    """

    def __init__(self) -> None:
        super().__init__()
