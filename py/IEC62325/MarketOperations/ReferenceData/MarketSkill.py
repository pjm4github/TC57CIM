# ///////////////////////////////////////////////////////////
# //  MarketSkill.h
# //  Implementation of the Class MarketSkill
# //  Created on:      26-Dec-2023 7:59:55 PM
# ///////////////////////////////////////////////////////////
from IEC61968.Common.Document import Document
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval
from IEC62325.MarketOperations.ReferenceData.MarketQualificationRequirement import MarketQualificationRequirement


class MarketSkill(Document) :
	# /**
	#  * Proficiency level of a craft, which is required to operate or maintain a
	#  * particular type of asset and/or perform certain types of work.
	#  */
	def __init__(self):
		# Interval between the certification and its expiry.
		super().__init__()
		self.certification_period = DateTimeInterval()
		#Date and time the skill became effective.
		self.effective_date_time = DateTime()
		#Level of skill for a Craft.
		self.level = ""
		self.market_qualification_requirements = [MarketQualificationRequirement()]