
from IEC61970.Base.Core.Curve import Curve


class HydroGeneratingEfficiencyCurve(Curve):
    # Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
    # Relationship between unit efficiency in percent and unit output active power
    # for a given net head in meters. The relationship between efficiency, discharge,
    # head, and power output is expressed as follows:  E = K*P/H*Q
    # Where:  (E=percentage)  (P=active power)  (H=height)  (Q=volume/time unit)
    # (K=constant)
    # For example, a curve instance for a given net head could relate efficiency
    # (Y-axis) versus active power output (X-axis) or versus discharge on the X-axis.
    # @created 02-Jan-2024 10:55:02 PM
    def __init__(self):
        super().__init__()
        # constructor
