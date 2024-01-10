from IEC61968.Common.Document import Document
from IEC61968.Customers.RevenueKind import RevenueKind
from IEC61968.Customers.Tariff import Tariff
from IEC61968.Metering.UsagePoint import UsagePoint
from IEC61968.PaymentMetering.Transaction import Transaction


###########################################################
#  pricing_structure.py
#  Implementation of the Class PricingStructure
#  Created on:      19-Dec-2023 3:28:34 PM
###########################################################


class PricingStructure(Document):
    """
    Grouping of pricing components and prices used in the creation of customer
    charges and the eligibility criteria under which these terms may be offered to
    a customer. The reasons for grouping include state, customer classification,
    site characteristics, classification (i.e. fee price structure, deposit price
    structure, electric service price structure, etc.) and accounting requirements.
    """

    def __init__(self):
        """
        Constructor for PricingStructure class.
        """
        super().__init__()
        self.code = ""
        self.daily_ceiling_usage = 0
        self.daily_estimated_usage = 0
        self.daily_floor_usage = 0
        self.revenue_kind = RevenueKind.RESIDENTIAL
        self.tax_exemption = False
        self.usage_points = UsagePoint()
        self.transactions = Transaction()
        self.tariffs = Tariff()
