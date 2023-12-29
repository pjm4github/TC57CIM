from IEC61970.Base.Core.Curve import Curve


class LoadReductionTimeCurve(Curve):

	#  * This is the cureve that describes the load reduction time. Relationship between
	#  * time (Y1-axis) vs. MW (X-axis).
	#  * @created 28-Dec-2023 7:37:35 PM

	def __init__(self):
		super().__init__()
		# 	 * type of the curve: Possible values are but not limited to:
		# 	 *
		# 	 * Max, Min,
		self.load_reduction_time_curve_type = "Min"
