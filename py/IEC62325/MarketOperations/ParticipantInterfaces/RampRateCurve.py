# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from typing import Union

from IEC61970.Base.Core.Curve import Curve
from IEC62325.MarketOperations.MktDomain.ConstraintRampType import ConstraintRampType
from IEC62325.MarketOperations.MktDomain.RampRateCondition import RampRateCondition
from IEC62325.MarketOperations.MktDomain.RampRateType import RampRateType


class RampRateCurve(Curve):
    """
    Ramp rate as a function of resource MW output.
    @created 28-Dec-2023 5:23:12 PM
    """
    def __init__(self) -> None:
        super().__init__()
        # condition for the ramp rate
        self.condition: RampRateCondition = RampRateCondition.BEST

        # The condition that identifies whether a Generating Resource should be
        # constrained from Ancillary Service provision if its Schedule or Dispatch change
        # across Trading Hours or Trading Intervals requires more than a specified
        # fraction of the duration of the Trading Hour or Trading Interval.
        # Valid values are Fast/Slow
        self.constraint_ramp_type: ConstraintRampType = ConstraintRampType.FAST

        # How ramp rate is applied (e.g. raise or lower, as when applied to a generation
        # resource)
        self.ramp_rate_type: RampRateType = RampRateType.REG
