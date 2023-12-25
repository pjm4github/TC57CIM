from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.ElectronicAddress import ElectronicAddress
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.ParentOrganization import ParentOrganization
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.StreetAddress import StreetAddress
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.TelephoneNumber import TelephoneNumber
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class Organisation(IdentifiedObject):
    """
    Organisation that might have roles as utility, contractor, supplier,
    manufacturer, customer, etc.
    """

    def __init__(self):
        """
        Constructor for Organisation.
        """
        super().__init__()
        self.electronic_address = ElectronicAddress()
        """
        Electronic address.
        """

        self.phone1 = TelephoneNumber()
        """
        Phone number.
        """

        self.phone2 = TelephoneNumber()
        """
        Additional phone number.
        """

        self.postal_address = StreetAddress()
        """
        Postal address, potentially different than 'street_address' (e.g., another city).
        """

        self.street_address = StreetAddress()
        """
        Street address.
        """

        self.parent_organisation = ParentOrganization()
        """
        Parent organisation of this organisation.
        """
