from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class ValueToAlias(IdentifiedObject):
	#
	# Describes the translation of one particular value into a name, e.g. 1 as "Open".
	#
	def __init__(self):
		super().__init__()
		self.value = 0  # The value that is mapped.
