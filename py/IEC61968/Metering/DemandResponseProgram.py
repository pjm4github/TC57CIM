# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Customers.CustomerAgreement import CustomerAgreement
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval


class DemandResponseProgram(IdentifiedObject):
    
    def __init__(self):
        super().__init__()
        self.type = ""
        self.validity_interval = DateTimeInterval()
        self.usage_point_groups = None  # Type UsagePointGroup not defined
        self.end_device_groups = None    # Type EndDeviceGroup not defined
        self.customer_agreements = CustomerAgreement()
