from IEC61970.Base.Domain.Money import Money  # Importing Money class from IEC61970.Base.Domain module


class BilateralTransaction:
    """
    Bilateral transaction
    @created 28-Dec-2023 7:59:42 PM
    """

    def __init__(self):
        self.curtailTimeMax = 0  # Creating an instance of Integer class and assigning it to the 'curtailTimeMax'
        # attribute
        self.curtailTimeMin = 0  # Creating an instance of Integer class and assigning it to the 'curtailTimeMin'
        # attribute
        self.marketType = ""  # Creating an instance of String class and assigning it to the 'marketType' attribute
        self.purchaseTimeMax = 0  # Creating an instance of Integer class and assigning it to the 'purchaseTimeMax'
        # attribute
        self.purchaseTimeMin = 0  # Creating an instance of Integer class and assigning it to the 'purchaseTimeMin'
        # attribute
        self.scope = ""  # Creating an instance of String class and assigning it to the 'scope' attribute
        self.totalTranChargeMax = Money()  # Creating an instance of Money class and assigning it to the
        # 'totalTranChargeMax' attribute
        self.transactionType = ""  # Creating an instance of String class and assigning it to the 'transactionType'
        # attribute
