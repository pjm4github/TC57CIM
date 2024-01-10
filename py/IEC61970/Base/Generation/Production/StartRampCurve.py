# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024

from IEC61970.Base.Core.Curve import Curve
from IEC61970.Base.Domain.ActivePowerChangeRate import ActivePowerChangeRate


class StartRampCurve(Curve):
    # Rate in gross active power/minute (Y-axis) at which a unit can be loaded versus
    # the number of hours (X-axis) the unit was off line.
    #
    # @created 02-Jan-2024 10:58:31 PM

    def __init__(self):
        super().__init__()
        #    The startup ramp rate in gross for a unit that is on hot standby.
        self.hot_standby_ramp = ActivePowerChangeRate()  # initialize with typical value
