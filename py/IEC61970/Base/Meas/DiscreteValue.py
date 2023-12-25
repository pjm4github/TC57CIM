from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Meas.Command import Command
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Meas.MeasurementValue import MeasurementValue


class DiscreteValue(MeasurementValue):
	#  * DiscreteValue represents a discrete MeasurementValue.
	# /**
	#  * The value to supervise.
	#  */
	def __init__(self):
		super().__init__()
		self.value = 0
		# The Control variable associated with the MeasurementValue.
		self.command = Command()
