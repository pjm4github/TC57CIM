#######################################################
# 
# Curve.py
# Python implementation of the Class Curve
# Generated by Enterprise Architect
# Created on:      16-Dec-2023 5:21:03 PM
# 
#######################################################
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.CurveStyle import CurveStyle
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.CurveData import CurveData

class Curve(IdentifiedObject):
    """A multi-purpose curve or functional relationship between an independent
    variable (X-axis) and dependent (Y-axis) variables.
    """

    def __init__(self):
        super().__init__()
        self.curve_style = CurveStyle.STRAIGHT_LINE_Y_VALUES
        self.x_multiplier = UnitMultiplier()
        self.x_unit = UnitSymbol()
        self.y1_multiplier = UnitMultiplier()
        self.y1_unit = UnitSymbol()
        self.y2_multiplier = UnitMultiplier()
        self.y2_unit = UnitSymbol()
        self.y3_mutiplier = UnitMultiplier()
        self.y3_unit = UnitSymbol()
        self.curve_datas = CurveData() # The point data values that define this curve.
