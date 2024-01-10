
from IEC61970.Base.Core.Curve import Curve


class HeatRateCurve(Curve):
    # Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
    # Relationship between unit heat rate per active power (Y-axis) and unit output (X-axis). The heat input is from all fuels.
    # @created 02-Jan-2024 10:54:51 PM
    def __init__(self):
        super().__init__()

        # Flag is set to true when output is expressed in net active power.
        self.is_net_gross_p = False  # default value is None  # end HeatRateCurve
