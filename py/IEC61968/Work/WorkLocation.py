#######################################################
# 
# WorkLocation.py
# Python implementation of the Class WorkLocation
# Generated by Enterprise Architect
# Created on:      19-Dec-2023 8:38:06 PM
# 
#######################################################
from IEC61968.Common.Location import Location
from IEC61968.InfIEC61968.InfWork.OneCallRequest import OneCallRequest


class WorkLocation(Location):
    """Information about a particular location for various forms of work.
    """

    def __init__(self):
        super().__init__()
        self.one_call_request = OneCallRequest()
