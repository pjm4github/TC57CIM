#######################################################
# 
# ActivityRecord.py
# Python implementation of the Class ActivityRecord
# Generated by Enterprise Architect
# Created on:      17-Dec-2023 7:27:25 PM
# 
#######################################################
from IEC61970.Base.Domain.DateTime import DateTime
# from IEC61970.Base.Domain.String import String
from IEC61968.Common.Status import Status
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject

class ActivityRecord(IdentifiedObject):
    """
    Records activity for an entity at a point in time; activity may be for an event
    that has already occurred or for a planned activity.
    """
    def __init__(self):
        super().__init__()
        self.created_datetime = DateTime()  # Date and time this activity record has been created (different from the
        # 'status.dateTime', which is the time of a status change of the associated object, if applicable).
        self.reason = ""  # Reason for event resulting in this activity record, typically supplied when user initiated.
        self.severity = ""  # Severity level of event resulting in this activity record.
        self.status = Status() # Information on consequence of event resulting in this activity record.
        self.type = ""  # Type of event resulting in this activity record.



