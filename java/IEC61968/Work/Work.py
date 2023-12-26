#######################################################
# 
# Work.py
# Python implementation of the Class Work
# Generated by Enterprise Architect
# Created on:      25-Dec-2023 8:45:26 PM
# 
#######################################################
from IEC61968 import Project
from java.IEC61968.Work import WorkTask
import ErpProjectAccounting
from IEC61968 import BaseWork

class Work(BaseWork):
    """Document used to request, initiate, track and record work.
    """
    Project= Project()

    # All tasks in this work.
    WorkTasks= WorkTask()

    ErpProjectAccounting= ErpProjectAccounting()