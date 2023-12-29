# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.ReferenceData.RegisteredDistributedResource import RegisteredDistributedResource


class ResourcePerformanceRating(IdentifiedObject):
    """
    Rating of a resource for its demand response performance. e.g. given a set on
    monthly resource demand response performance evaluations, the resource may be
    rated with excellent, average, or poor performance for the sample set.
    @author mwald
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """

    def __init__(self):
        super().__init__()
        # starting date time that the rating is valid for
        self.effective_end_time = DateTime()
        
        # ending date time that the rating is valid for
        self.effective_start_time = DateTime()
        
        # the resource's demand response rating description
        self.rating_description = ""
        
        # the type of performance rating, e.g. which market or product the rating is for
        self.rating_type = ""
        
        # the resource's demand response rating
        self.rating_value = ""
        
        self.registered_resource = RegisteredDistributedResource()
