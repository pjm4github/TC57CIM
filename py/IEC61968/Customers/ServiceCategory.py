from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.ConfigurationEvent import ConfigurationEvent
from CIM_STD_PYTHON.TC57CIM.IEC61968.Customers.PricingStructure import PricingStructure
from CIM_STD_PYTHON.TC57CIM.IEC61968.Customers.ServiceKind import ServiceKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


###########################################################
#  service_category.py
#  Implementation of the Class ServiceCategory
#  Created on:      19-Dec-2023 3:28:49 PM
###########################################################


class ServiceCategory(IdentifiedObject):

    def __init__(self):
        """
        Constructor for ServiceCategory class.
        """
        super().__init__()
        self.kind = ServiceKind.ELECTRICITY
        self.pricing_structures = PricingStructure()
        self.configuration_events = ConfigurationEvent()
