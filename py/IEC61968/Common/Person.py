# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.TelephoneNumber import TelephoneNumber
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.ElectronicAddress import ElectronicAddress
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject

class Person(IdentifiedObject):
    
    def __init__(self):
        super().__init__()
        self.electronic_address = ElectronicAddress()
        self.first_name = ""
        self.landline_phone = TelephoneNumber()
        self.last_name = ""
        self.middle_name = ""
        self.mobile_phone = TelephoneNumber()
        self.prefix = ""
        self.special_need = ""
        self.suffix = ""
        self.roles = ""
