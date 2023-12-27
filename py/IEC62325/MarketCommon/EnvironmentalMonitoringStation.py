# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject

from IEC61970.Base.Domain.Minutes import Minutes
from IEC61968.Common.Location import Location
from IEC61968.Metering.UsagePoint import UsagePoint

class EnvironmentalMonitoringStation(IdentifiedObject):

    """
    An environmental monitoring station, examples of which could be a weather
    station or a seismic monitoring station.
    @author mcmorran
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        """
        Whether this station is currently reporting using daylight saving time.
        Intended to aid a utility Weather Service in interpreting information coming
        from a station and has no direct relationship to the manner in which time is
        expressed in EnvironmentalValueSet.
        """
        super().__init__()
        self.dst_observed = False

        """
        Indication that station is part of a network of stations used to monitor
        weather phenomena covering a large geographical area.
        """
        self.is_networked = False

        """
        The time offset from UTC (a.k.a. GMT) configured in the station "clock", not
        (necessarily) the time zone in which the station is physically located.
        This attribute exists to support management of utility monitoring stations and
        has no direct relationship to the manner in which time is expressed in
        EnvironmentalValueSet.
        """
        self.time_zone_offset = Minutes()

        """Location of this monitoring station."""
        self.location = Location()

        self.usage_point = UsagePoint()
