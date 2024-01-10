# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from IEC61970.Base.Core.RegularIntervalSchedule import RegularIntervalSchedule


class SteamSendoutSchedule(RegularIntervalSchedule):
    """
    The cogeneration plant's steam sendout schedule in volume per time unit.
    @created 02-Jan-2024 10:58:54 PM
    """

    def __init__(self):
        super().__init__()
