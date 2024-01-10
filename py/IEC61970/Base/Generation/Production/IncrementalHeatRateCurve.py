# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from IEC61970.Base.Core.Curve import Curve


class IncrementalHeatRateCurve(Curve):
    """
    Relationship between unit incremental heat rate in (delta energy/time) per
    (delta active power) and unit output in active power. The IHR curve represents
    the slope of the HeatInputCurve. Note that the "incremental heat rate" and the
    "heat rate" have the same engineering units.
    @created 02-Jan-2024 10:56:15 PM
    """

    def __init__(self):
        super().__init__()
        # No extra parameters
        # Flag is set to true when output is expressed in net active power.
        self.is_net_gross_p = False
