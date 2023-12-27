# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Common.Location import Location
from IEC62325.Environmental.EnvDomain.LocationKind import LocationKind


class EnvironmentalLocationType:
    """
    Type of environmental location. Used when an environmental alert or phenomenon
    has multiple locations associated with it.
    @author ppbr003
    @version 1.0
    @created 25-dec-2023 9:21:22 PM
    """

    def __init__(self):
        # The kind of location. Typical values might be center, extent, primary,
        # secondary, etc.
        self.kind = LocationKind.CENTER

        # Location of this instance of this kind of environmental location.
        self.location = Location()
