# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106

from IEC61968.Assets.Asset import Asset
from IEC61968.Metering.ComFunction import ComFunction
from IEC61970.Base.Domain.Minutes import Minutes


class ComModule(Asset):

    def __init__(self):
        super().__init__()
        self.amr_system = ""
        self.supports_autonomous_dst = False
        self.time_zone_offset = Minutes()
        self.com_functions = ComFunction()
