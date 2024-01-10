#######################################################
# 
# Work.py
# Python implementation of the Class Work
# Generated by Enterprise Architect
# Created on:      19-Dec-2023 6:01:06 PM
# 
#######################################################
from IEC61968.InfIEC61968.InfERPSupport.ErpProjectAccounting import ErpProjectAccounting
from IEC61968.InfIEC61968.InfWork.Project import Project
from IEC61968.Work.BaseWork import BaseWork
from IEC61968.Work.WorkTask import WorkTask


class Work(BaseWork):
    """Document used to request, initiate, track and record work.
    """

    def __init__(self):
        super().__init__()
        self.project = Project()
        self.work_tasks = WorkTask()  # All tasks in this work.
        self.erp_project_accounting = ErpProjectAccounting()
