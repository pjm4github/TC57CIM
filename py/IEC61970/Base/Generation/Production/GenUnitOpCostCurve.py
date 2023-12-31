#######################################################
# 
# GenUnitOpCostCurve.py
# Python implementation of the Class GenUnitOpCostCurve
# Generated by Enterprise Architect
# Created on:      17-Dec-2023 10:15:07 PM
# 
#######################################################
from IEC61970.Base.Core.Curve import Curve


class GenUnitOpCostCurve(Curve):
    """Relationship between unit operating cost (Y-axis) and unit output active power
    (X-axis). The operating cost curve for thermal units is derived from heat input
    and fuel costs. The operating cost curve for hydro units is derived from water
    flow rates and equivalent water costs.
    """
    def __init__(self):
        super().__init__()
        self.is_net_gross_p = True
