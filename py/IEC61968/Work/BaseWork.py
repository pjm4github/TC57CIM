#######################################################
# 
# BaseWork.py
# Python implementation of the Class BaseWork
# Generated by Enterprise Architect
# Created on:      19-Dec-2023 6:02:49 PM
# Original author: T. Kostic
# 
#######################################################
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Document import Document
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Priority import Priority
from CIM_STD_PYTHON.TC57CIM.IEC61968.Work.WorkActivityRecord import WorkActivityRecord
from CIM_STD_PYTHON.TC57CIM.IEC61968.Work.WorkKind import WorkKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Work.WorkLocation import WorkLocation
from CIM_STD_PYTHON.TC57CIM.IEC61968.Work.WorkStatusKind import WorkStatusKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Work.WorkTimeSchedule import WorkTimeSchedule


class BaseWork(Document):
    """Common representation for work and work tasks.
    """

    def __init__(self):
        super().__init__()
        self.kind = WorkKind
        self.priority = Priority()
        self.status_kind = WorkStatusKind
        self.work_activity = WorkActivityRecord()  # All activity records for this work or work task.
        self.location = WorkLocation()   # Location for this work/task.
        self.time_schedule = WorkTimeSchedule()    # All time schedules for this work or work task.