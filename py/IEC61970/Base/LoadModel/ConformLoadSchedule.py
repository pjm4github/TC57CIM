# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 16:20:57 2024
from IEC61970.Base.LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule


class ConformLoadSchedule(SeasonDayTypeSchedule):
    """A curve of load versus time (X-axis) showing the active power values (Y1-axis)
    and reactive power (Y2-axis) for each unit of the period covered. This curve
    represents a typical pattern of load over the time period for a given day type
    and season.
    @created 03-Jan-2024 10:44:40 PM
    """

    def __init__(self) -> None:
        super().__init__()
