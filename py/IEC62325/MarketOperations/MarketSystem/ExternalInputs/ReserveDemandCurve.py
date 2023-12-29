# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from typing import Optional

from IEC61970.Base.Core.Curve import Curve
from IEC62325.MarketOperations.MktDomain.ReserveRequirementType import ReserveRequirementType


class ReserveDemandCurve(Curve):
    """
    Reserve demand curve.  Models maximum quantities of reserve required per Market
    Region and models a reserve demand curve for the minimum quantities of reserve.
    The ReserveDemandCurve is a relationship between unit operating reserve price
    in $/MWhr (Y-axis) and unit reserves in MW (X-axis).
    @created 27-Dec-2023 3:31:29 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()
        self.req_max_mw: Optional[float] = 0.0

        """
        Region requirement maximum limit
        """

        self.reserve_requirement_type: Optional[ReserveRequirementType] = ReserveRequirementType()
        """
        Reserve requirement type that the max and curve apply to. 
        For example, operating reserve, regulation and contingency.
        """

