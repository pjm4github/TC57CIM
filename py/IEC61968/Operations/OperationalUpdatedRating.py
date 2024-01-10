# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Operations.OperationalRestriction import OperationalRestriction
from IEC61968.Operations.PlannedOutage import PlannedOutage


class OperationalUpdatedRating(OperationalRestriction):

    def __init__(self):
        super().__init__()
        self.change_type = ""
        self.planned_outage = PlannedOutage()
