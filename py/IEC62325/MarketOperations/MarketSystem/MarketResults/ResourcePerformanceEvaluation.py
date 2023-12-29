# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MarketSystem.MarketResults.ResourcePerformanceTimeSeriesFactor import \
    ResourcePerformanceTimeSeriesFactor


class ResourcePerformanceEvaluation(IdentifiedObject):
    """
    Represents an the performance evaluation of a resource deployment. Every
    resource deployment may have many performance evaluations, using different
    evaluation metrics or algorithms, or produced by different evaluation
    authorities.
    @author mwald
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """
    def __init__(self):
        super().__init__()
        self.effective_end_time = DateTime()
        self.effective_start_time = DateTime()
        # 	 * Description of the performance evaluation, e.g. the rating classification used
        # 	 * (any is allowed), why the evaluation was performed, anything that describes the
        # 	 * demand response performance evaluation.
        self.evaluation_description = ""
        # 	 * The value of the performance. as a String, any rating scheme is supported (e.g.
        # 	 * "1","2","3" or "low", "medium", "high"). The rating scheme is described in the
        # 	 * performanceValueDescription attribute.
        self.evaluation_value = ""
        self.resource_performance_time_series_factors = ResourcePerformanceTimeSeriesFactor()
