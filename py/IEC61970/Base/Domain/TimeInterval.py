# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:33:10 2023

from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Time import Time


class TimeInterval:
    """Interval between two times.
    """

    def __init__(self):
        """
        Start time of this interval.
        """
        self.start: Time = Time()

        """
        End time of this interval.
        """
        self.end: Time = Time()
