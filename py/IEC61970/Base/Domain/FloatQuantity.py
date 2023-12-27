
from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class FloatQuantity:
	def __init__(self):
		self.multiplier = UnitMultiplier.none
		self.unit = UnitSymbol.none
		self.value = 0.0
