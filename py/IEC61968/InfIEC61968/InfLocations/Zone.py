# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:37:42 2023
from IEC61968.Common.Location import Location
from IEC61968.InfIEC61968.InfLocations.ZoneKind import ZoneKind


class Zone(Location):
    """
    Area divided off from other areas. It may be part of the electrical network, a
    land area where special restrictions apply, weather areas, etc. For weather, it
    is an area where a set of relatively homogeneous weather measurements apply.
    @created 29-Dec-2023 6:07:34 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.kind = ZoneKind.WEATHER_ZONE

