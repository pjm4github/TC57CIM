# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from typing import Any, Optional

from IEC61970.Base.Core.Curve import Curve
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.SecurityConstraintSum import SecurityConstraintSum


class BaseCaseConstraintLimit(Curve):
    """
    Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit
    (Y1 and Y2, respectively) assigned to a contingency analysis base case. Use
    CurveSchedule XAxisUnits to specify MW or MVA. To be used only if the
    BaseCaseConstraintLimit differs from the DefaultConstraintLimit.
    @created 27-Dec-2023 3:25:02 PM
    """
    def __init__(self) -> None:
        super().__init__()
        self.security_constraint_sum: Optional[SecurityConstraintSum] = SecurityConstraintSum()
