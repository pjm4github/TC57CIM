from IEC61968.Common.Agreement import Agreement
from IEC61968.Customers.PricingStructure import PricingStructure
from IEC61968.Customers.ServiceCategory import ServiceCategory
from IEC61968.Customers.ServiceLocation import ServiceLocation
from IEC61968.InfIEC61968.InfCustomers.StandardIndustryCode import StandardIndustryCode
from IEC61968.Metering.UsagePoint import UsagePoint
from IEC61968.PaymentMetering.AuxiliaryAgreement import AuxiliaryAgreement
from IEC61970.Base.Domain.DateTime import DateTime


###########################################################
#  customer_agreement.py
#  Implementation of the Class CustomerAgreement
#  Created on:      19-Dec-2023 3:28:20 PM
###########################################################


class CustomerAgreement(Agreement):

    def __init__(self):
        """
        Constructor for CustomerAgreement class.
        """
        super().__init__()
        self.is_pre_pay = False
        self.load_mgmt = ""
        self.shut_off_date_time = DateTime()
        self.service_locations = ServiceLocation()
        self.standard_industry_code = StandardIndustryCode()
        self.auxiliary_agreements = AuxiliaryAgreement()
        self.pricing_structures = PricingStructure()
        self.usage_points = UsagePoint()
        self.service_category = ServiceCategory()
