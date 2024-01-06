from IEC61968.Common.Agreement import Agreement
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC62325.MarketOperations.ReferenceData.Pnode import Pnode

class FTR(Agreement):
    """
    Financial Transmission Rights (FTR) regarding transmission capacity at a
    flowgate.
    @created 28-Dec-2023 7:42:18 PM
    """

    def __init__(self):
        super().__init__()  # Calling the __init__() method of the superclass
        # 	 * Buy, Sell
        self.action = ""

        # 	 * Quantity, typically MWs - Seller owns all rights being offered, MWs over time
        # 	 * on same Point of Receipt, Point of Delivery, or Resource.
        self.base_energy = ActivePower()

        # 	 * Peak, Off-peak, 24-hour
        self.class_ = ""

        # 	 * Type of rights being offered (product) allowed to be auctioned (option,
        # 	 * obligation).
        self.ftr_type = ""  # Creating an instance of String class and assigning it to the 'ftr_type' attribute

        # 	 * Fixed (covers re-configuration, grandfathering) or Optimized (up for
        # 	 * sale/purchase
        self.optimized = ""  # Creating an instance of String class and assigning it to the 'optimized' attribute
        self.pnodes = Pnode()  # Creating an instance of Pnode class and assigning it to the 'pnodes' attribute
