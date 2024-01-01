# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from typing import Optional, Any

from IEC61970.Base.Core.Curve import Curve
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.SecurityConstraintSum import SecurityConstraintSum


class DefaultConstraintLimit(Curve):
    """
    Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit
    (Y1 and Y2, respectively) applied as a default value if no specific constraint
    limits are specified for a contingency analysis. Use CurveSchedule XAxisUnits
    to specify MW or MVA.
    @created 27-Dec-2023 3:27:15 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.security_constraint_sumOptional[SecurityConstraintSum] = SecurityConstraintSum()
