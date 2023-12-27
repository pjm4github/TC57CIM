

from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.Currency import Currency
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class CostRate:
	#  * Cost, in units of currency, per elapsed time.
	def __init__(self):
		self.denominator_multiplier = UnitMultiplier.none  # Cost rate denominator multiplier
		self.denominator_unit = UnitSymbol.s  # Cost rate denominator unit
		self.multiplier = UnitMultiplier.none  # Cost rate multiplier
		self.unit = Currency()  # Cost rate currency
		self.value = 0.0  # Cost rate value
