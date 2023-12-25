
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class FloatQuantity:
	def __init__(self):
		self.multiplier = UnitMultiplier.none
		self.unit = UnitSymbol.none
		self.value = 0.0
