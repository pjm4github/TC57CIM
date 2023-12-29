# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.MarketSystem.MarketResults.ResourcePerformanceEvaluation import \
    ResourcePerformanceEvaluation


class ResourcePerformanceGlobalFactor(IdentifiedObject):
    #  * Global factors are property/value pairs that are used to adjust resource
    #  * performance values. Example include scale factors (e.g. scale a baseline up or
    #  * down), adders (positive or negative), etc.
    #  * @author mwald
    #  * @version 1.0
    #  * @created 25-Dec-2023 9:21:23 PM
    def __init__(self):
        super().__init__()
        # * Description (name) of the property (factor).
        self.factor_description = ""
        # * Value of the property (factor).
        self.factor_value = ""
        self.resource_performance_evaluation = ResourcePerformanceEvaluation()
