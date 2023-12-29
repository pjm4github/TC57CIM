from IEC62325.MarketOperations.MarketSystem.ExternalInputs.Profile import Profile
from IEC62325.MarketOperations.MarketSystem.MarketResults.BillDeterminant import BillDeterminant
from IEC62325.MarketOperations.MarketSystem.MarketResults.ChargeProfileData import ChargeProfileData
from IEC62325.MarketOperations.MarketSystem.MarketResults.PassThroughBill import PassThroughBill


class ChargeProfile(Profile):
    """
    A type of profile for financial charges.
    @created 28-Dec-2023 8:18:35 PM
    """

    def __init__(self):
        # The calculation frequency, daily or monthly.
        super().__init__()
        self.frequency = ""

        # The number of intervals in the profile data.
        self.number_interval = 0

        # The type of profile. It could be an amount, price, or quantity.
        self.type = ""

        # The unit of measure applied to the value attribute of the profile data.
        self.unit_of_measure = ""

        self.bill_determinant = BillDeterminant()
        self.charge_profile_data = ChargeProfileData()
        self.pass_through_bill = PassThroughBill()

