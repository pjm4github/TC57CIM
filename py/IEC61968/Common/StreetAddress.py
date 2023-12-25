from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Status import Status
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.StreetDetail import StreetDetail
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.TownDetail import TownDetail


class StreetAddress:
    """
    General purpose street and postal address information.
    """

    def __init__(self):
        """
        Constructor for StreetAddress.
        """
        self.po_box = ""
        """
        Post office box.
        """

        self.postal_code = ""
        """
        Postal code for the address.
        """

        self.status = Status()
        """
        Status of this address.
        """

        self.street_detail = StreetDetail()
        """
        Street detail.
        """

        self.town_detail = TownDetail()
        """
        Town detail.
        """
