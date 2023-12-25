# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:39:55 2023
from datetime import timedelta

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.OperationalLimits.OperationalLimitDirectionKind import \
    OperationalLimitDirectionKind


class OperationalLimitType(IdentifiedObject):
    """
    The operational meaning of a category of limits.
    @author kdd
    @version 1.0
    @created 15-Dec-2023 4:38:28 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """

        super().__init__()
        self.acceptable_duration: timedelta = timedelta()
        """The nominal acceptable duration of the limit.  Limits are commonly expressed in
        terms of the a time limit for which the limit is normally acceptable.  The
        actual acceptable duration of a specific limit may depend on other local
        factors such as temperature or wind speed."""

        self.direction: OperationalLimitDirectionKind = OperationalLimitDirectionKind.LOW
        """The direction of the limit."""

