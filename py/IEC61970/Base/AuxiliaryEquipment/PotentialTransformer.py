from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.AuxiliaryEquipment.PotentialTransformerKind import PotentialTransformerKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.AuxiliaryEquipment.Sensor import Sensor


class PotentialTransformer(Sensor):
	# Instrument transformer (also known as Voltage Transformer) used to measure
	# electrical qualities of the circuit that is being protected and/or monitored.
	# Typically used as voltage transducer for the purpose of metering, protection,
	# or sometimes auxiliary substation supply. A typical secondary voltage rating
	# would be 120V.

	def __init__(self):
		# PT accuracy classification.
		super().__init__()
		self.accuracy_class = ""
		# Nominal ratio between the primary and secondary voltage.
		self.nominal_ratio = 1.0
		# Potential transformer (PT) classification covering burden.
		self.pt_class = ""
		# Potential transformer construction type.
		self.type = PotentialTransformerKind.INDUCTIVE
