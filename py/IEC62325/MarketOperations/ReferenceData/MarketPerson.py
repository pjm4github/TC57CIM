from IEC61968.Common.ElectronicAddress import ElectronicAddress
from IEC61968.Common.Status import Status
from IEC61968.Common.TelephoneNumber import TelephoneNumber
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.ReferenceData.MarketSkill import MarketSkill


class MarketPerson(IdentifiedObject):
    def __init__(self):
        super().__init__()
        self.category = ""  # Category of this person relative to utility operations
        self.electronic_address_alternate = ElectronicAddress()  # Alternate Electronic address
        self.electronic_address_primary = ElectronicAddress()  # Primary Electronic address
        self.first_name = ""  # Person's first name
        self.government_id = ""  # Unique identifier for person relative to its governing authority
        self.landline_phone = TelephoneNumber()  # Landline phone number
        self.last_name = ""  # Person's last (family, sir) name
        self.middle_name = ""  # Middle name(s) or initial(s)
        self.mobile_phone = TelephoneNumber()  # Mobile phone number
        self.prefix = ""  # A prefix or title for the person's name
        self.special_need = ""  # Special service needs for the person (contact) are described
        self.status = Status()  # Status
        self.suffix = ""  # A suffix for the person's name
        self.user_id = ""  # The user name for the person
        self.market_skills = [MarketSkill()]  # Market skills