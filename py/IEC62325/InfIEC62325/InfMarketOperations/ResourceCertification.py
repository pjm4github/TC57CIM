from IEC62325.MarketOperations.MktDomain.YesNo import YesNo  # Importing YesNo class from IEC62325.MarketOperations.MktDomain module

class ResourceCertification:
    """
    This class represents the resource certification for a specific product type.
    For example, a resource is certified for Non-Spinning reserve for RTM.
    @created 28-Dec-2023 8:00:02 PM
    """

    def __init__(self):
        self.certified_dam = YesNo.NO  # Creating an instance of YesNo class and assigning it to the 'certified_dam' attribute
        self.certified_nonspin_dam = YesNo.NO  # Creating an instance of YesNo class and assigning it to the 'certified_nonspin_dam' attribute
        self.certified_nonspin_dam_mw = 1.0  # Creating an instance of Float class and assigning it to the 'certified_nonspin_dam_mw' attribute
        self.certified_nonspin_rtm = YesNo.NO  # Creating an instance of YesNo class and assigning it to the 'certified_nonspin_rtm' attribute
        self.certified_nonspin_rtm_mw = 1.0  # Creating an instance of Float class and assigning it to the 'certified_nonspin_rtm_mw' attribute
        self.certified_pirp = YesNo.NO  # Creating an instance of YesNo class and assigning it to the 'certified_pirp' attribute
        self.certified_regulation = YesNo.NO  # Creating an instance of YesNo class and assigning it to the 'certified_regulation' attribute
        self.certified_regulation_mw = 1.0  # Creating an instance of Float class and assigning it to the 'certified_regulation_mw' attribute
        self.certified_replace_as = YesNo.NO  # Creating an instance of YesNo class and assigning it to the 'certified_replace_as' attribute
        self.certified_rtm = YesNo.NO  # Creating an instance of YesNo class and assigning it to the 'certified_rtm' attribute
        self.certified_ruc = YesNo.NO  # Creating an instance of YesNo class and assigning it to the 'certified_ruc' attribute
        self.certified_spin = YesNo.NO  # Creating an instance of YesNo class and assigning it to the 'certified_spin' attribute
        self.certified_spin_mw = 1.0  # Creating an instance of Float class and assigning it to the 'certified_spin_mw' attribute