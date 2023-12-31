#######################################################
# 
# Project.py
# Python implementation of the Class Project
# Generated by Enterprise Architect
# Created on:      19-Dec-2023 8:45:01 PM
# 
#######################################################
from IEC61968.InfIEC61968.InfWork.WorkDocument import WorkDocument


class Project(WorkDocument):
    """A collection of related work. For construction projects and maintenance
    projects, multiple phases may be performed.
    """

    def __init__(self):
        super().__init__()
        self.sub_projects = [Project()]