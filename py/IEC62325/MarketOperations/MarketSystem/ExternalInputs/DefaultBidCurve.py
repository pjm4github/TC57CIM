# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from typing import Optional

from IEC61970.Base.Core.Curve import Curve


class DefaultBidCurve(Curve):
    """
    Default bid curve for default energy bid curve and default startup curves (cost and time).
    @created 27-Dec-2023 3:26:57 PM
    """
    def __init__(self) -> None:
        """
        Constructor for DefaultBidCurve
        """
        super().__init__()
        self.curve_typeOptional[str] = ""  # To indicate a type used for a default energy bid curve, such as LMP, cost or consultative based.
        self.deb_adder_flagbool = False  # Default energy bid adder flag
