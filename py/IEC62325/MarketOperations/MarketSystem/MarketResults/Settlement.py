from IEC61968.Common.Document import Document
from IEC61970.Base.Domain.DateTime import DateTime


class Settlement(Document):
	"""
	#  * Specifies a settlement run.
	#  * @created 28-Dec-2023 8:26:27 PM
	"""
	def __init__(self):
		super().__init__()
		# # 	 * The trade date on which the settlement is run.
		self.trade_date = DateTime()
