from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.MonthDay import MonthDay


class Season(IdentifiedObject):
    """
    Represents a specified time period of the year.
    @created 03-Jan-2024 10:44:40 PM
    """
    def __init__(self):
        super().__init__()
        self.end_date = MonthDay()  # Date season ends.
        self.start_date = MonthDay()  # Date season starts.
        self.season_day_type_schedules = SeasonDayTypeSchedule()  # Schedules that use this Season.

# end Season
