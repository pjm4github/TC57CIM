#######################################################
# 
# RegularIntervalSchedule.py
# Python implementation of the Class RegularIntervalSchedule
# Generated by Enterprise Architect
# Created on:      17-Dec-2023 10:03:16 PM
# 
#######################################################
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Base.Core.RegularTimePoint import RegularTimePoint
from IEC61970.Base.Core.BasicIntervalSchedule import BasicIntervalSchedule

class RegularIntervalSchedule(BasicIntervalSchedule):
    """
    The schedule has time points where the time between them is constant.
    """

    def __init__(self):
        super().__init__()
        self.time_step = Seconds()
        self.end_time = DateTime()
        # The regular interval time point data values that define this schedule.
        self.time_points = [RegularTimePoint()]
