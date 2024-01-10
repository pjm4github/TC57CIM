#######################################################
# 
# ConfigurationEvent.py
# Python implementation of the Class ConfigurationEvent
# Generated by Enterprise Architect
# Created on:      17-Dec-2023 7:26:42 PM
# Original author: T. Kostic
# 
#######################################################
from IEC61970.Base.Domain.DateTime import DateTime
# from IEC61970.Base.Domain.String import String
from IEC61970.Base.Faults.FaultCauseType import FaultCauseType
from IEC61968.Common.ActivityRecord import ActivityRecord


class ConfigurationEvent(ActivityRecord):
    """Used to report details on creation, change or deletion of an entity or its
    configuration.
    """

    def __init__(self):
        super().__init__()
        self.effective_DateTime = DateTime()  # Date and time this event has or will become effective.
        self.modified_by = ""  # Source/initiator of modification.
        self.remark = ""  # Free text remarks.
        self.fault_cause_type = FaultCauseType()
