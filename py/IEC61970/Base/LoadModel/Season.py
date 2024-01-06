# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 16:30:57 2024
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.MonthDay import MonthDay
from IEC61970.Base.LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule


class Season(IdentifiedObject):
    """A specified time period of the year."""

    def __init__(self):
        super().__init__()
        self.end_date = MonthDay()  # Date season ends
        self.start_date = MonthDay()  # Date season starts
        self.season_day_type_schedules = SeasonDayTypeSchedule()  # Schedules that use this Season

