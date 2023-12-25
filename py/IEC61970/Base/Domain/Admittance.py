from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class Admittance:
	"""
	Ratio of current to voltage.
	"""

	def __init__(self):
		self.multiplier = UnitMultiplier.none
		self.value = 0.0
		self.unit = UnitSymbol.S