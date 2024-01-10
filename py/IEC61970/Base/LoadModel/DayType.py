# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 16:20:57 2024
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule

class DayType(IdentifiedObject):
    """
    Group of similar days. For example, it could be used to represent weekdays,
    weekend, or holidays.
    @created 03-Jan-2024 10:44:40 PM
    """

    season_day_type_schedules: SeasonDayTypeSchedule

    def __init__(self) -> None:
        super().__init__()
        self.season_day_type_schedules = SeasonDayTypeSchedule()  # Schedules that use this DayType.
