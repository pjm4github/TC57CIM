# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.Pressure import Pressure
from IEC61970.Base.Domain.Speed import Speed
from IEC62325.Environmental.AtmosphericPhenomenon import AtmosphericPhenomenon


class Cyclone(AtmosphericPhenomenon):
    """
    A cyclone (or tropical cyclone), a rapidly-rotating storm system characterized
    by a low-pressure center, strong winds, and a spiral arrangement of
    thunderstorms that produce heavy rain.
    @author mcmorran
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        super().__init__()
        self.central_pressure = Pressure()  # The central pressure of the cyclone during the time interval.
        self.max_surface_wind_speed = Speed()  # The maximum surface wind speed of the cyclone during the time interval.
        self.wind_force = 0  # Wind Force as classified on the Beaufort Scale (0-12) during the time interval.
