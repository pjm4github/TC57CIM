#######################################################
# 
# TimeSchedule.py
# Python implementation of the Class TimeSchedule
# Generated by Enterprise Architect
# Created on:      25-Dec-2023 8:45:25 PM
# 
#######################################################
from java.IEC61968.Common import Document
from IEC61968 import TimePoint

class TimeSchedule(Document):
    """Description of anything that changes through time. Time schedule is used to
    perform a single-valued function of time. Use inherited 'type' attribute to
    give additional information on this schedule, such as: periodic (hourly, daily,
    weekly, monthly, etc.), day of the month, by date, calendar (specific times and
    dates).
    """
    # Sequence of time points belonging to this time schedule.
    TimePoints= TimePoint()
