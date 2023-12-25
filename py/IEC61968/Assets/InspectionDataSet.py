from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.ProcedureDataSet import ProcedureDataSet


class InspectionDataSet(ProcedureDataSet):
	def __init__(self):
		super().__init__()
		self.location_condition = ""  # Description of the conditions of the location where the asset resides.