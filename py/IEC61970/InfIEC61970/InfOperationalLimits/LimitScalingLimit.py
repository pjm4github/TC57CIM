# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 22:25:18 2024
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.OperationalLimits.OperationalLimit import OperationalLimit
from IEC61970.InfIEC61970.InfOperationalLimits.LimitDependency import LimitDependency


class LimitScalingLimit(LimitDependency):
    """
    Specifies that an operational limit is calculated by scaling another operational limit.
    """
    def __init__(self):
        super().__init__()
        self.limit_scaling_percent = PerCent()  # The associated source limit is scaled by this value to compute the limit of the dependency model.
        self.source_operational_limit = OperationalLimit()

# end LimitScalingLimit
