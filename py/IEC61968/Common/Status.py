#######################################################
# 
# Status.py
# Python implementation of the Class Status
# Generated by Enterprise Architect
# Created on:      17-Dec-2023 7:28:20 PM
# 
#######################################################
from IEC61970.Base.Domain.DateTime import DateTime
# from IEC61970.Base.Domain.String import String

class Status:
    """Current status information relevant to an entity.
    """
    def __init__(self):
        self.DateTime = DateTime()  # Date and time for which status 'value' applies.
        self.reason = ""  # Reason code1 or explanation for why an object went to the current status 'value'.
        self.remark = ""  # Pertinent information regarding the current 'value', as free form text.
        self.value = ""  # Status value at 'dateTime'; prior status changes may have been kept in instances of activity
        # records associated with the object to which this status applies.