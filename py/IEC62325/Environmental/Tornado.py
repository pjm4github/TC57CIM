# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.Length import Length
from IEC62325.Environmental.AtmosphericPhenomenon import AtmosphericPhenomenon
from IEC62325.Environmental.EnvDomain.FScale import FScale


class Tornado(AtmosphericPhenomenon):
    """
    A tornado, a violent destructive whirling wind accompanied by a funnel-shaped
    cloud that progresses in a narrow path over the land.
    @author ppbr003
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """

    def __init__(self):
        super().__init__()
        self.f_scale = FScale.ONE  # Fujita scale (referred to as EF-scale starting in 2007) for the tornado.
        self.width = Length()  # Width of the tornado during the time interval.
