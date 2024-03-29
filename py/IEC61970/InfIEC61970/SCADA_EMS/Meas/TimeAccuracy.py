from enum import Enum


class TimeAccuracy(Enum):
    T10SEC = 1
    T1SEC = 2
    T100MILLISEC = 3
    T10MILLISEC = 4
    T1MILLISEC = 5
    T100MICROSEC = 6
    T25MICROSEC = 7
    T4MICROSEC = 8
    T1MICROSEC = 9
