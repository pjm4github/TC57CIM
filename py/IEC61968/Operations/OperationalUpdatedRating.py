# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.OperationalRestriction import OperationalRestriction
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.PlannedOutage import PlannedOutage


class OperationalUpdatedRating(OperationalRestriction):

    def __init__(self):
        self.change_type = ""
        self.planned_outage = PlannedOutage()
