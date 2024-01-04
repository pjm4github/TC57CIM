# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 22:25:18 2024
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.OperationalLimits.OperationalLimitType import OperationalLimitType


class OperatonalLimitTypeScaling:
    """
    One operational limit type scales values of another operational limit type when under the same operational limit set.
    This applies to any operational limit assigned to the target operational limit type and without other limit dependency models.
    """
    def __init__(self):
        self.scaling_percent = PerCent()  # The percentage scaling of the source limit to compute the target limit. Applies to operational limits within an operational limit set when both source and target operational limit types exist.
        self.source_operational_limit_type = OperationalLimitType()
        self.target_operational_limit = OperationalLimitType()

# end OperatonalLimitTypeScaling
