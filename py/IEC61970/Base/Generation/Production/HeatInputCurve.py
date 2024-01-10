# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from IEC61970.Base.Core.Curve import Curve
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Generation.Production.HeatRate import HeatRate


class HeatInputCurve(Curve):
    """
    Relationship between unit heat input in energy per time for main fuel (Y1-axis)
    and supplemental fuel (Y2-axis) versus unit output in active power (X-axis).
    The quantity of main fuel used to sustain generation at this output level is
    prorated for throttling between definition points. The quantity of supplemental
    fuel used at this output level is fixed and not prorated.
    @created 02-Jan-2024 10:54:29 PM
    """

    def __init__(self):
        super().__init__()
        # Power output - auxiliary power multiplier adjustment factor.
        self.aux_power_mult = PU(0)  # 0 as typical value
        # Power output - auxiliary power offset adjustment factor.
        self.aux_power_offset = ActivePower(0)  # 0 as typical value
        # Heat input - efficiency multiplier adjustment factor.
        self.heat_input_eff = PU(0)  # 0 as typical value
        # Heat input - offset adjustment factor.
        self.heat_input_offset = HeatRate(0)  # 0 as typical value
        # Flag is set to true when output is expressed in net active power.
        self.is_net_gross_p = False  # False as typical value
