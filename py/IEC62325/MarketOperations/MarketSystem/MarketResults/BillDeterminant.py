from IEC61968.Common.Document import Document
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MarketSystem.MarketResults.ChargeProfileData import ChargeProfileData


class BillDeterminant(Document):
    """
    Models various charges to support billing and settlement.
    @created 28-Dec-2023 8:18:27 PM
    """

    def __init__(self):
        # Level in charge calculation order.
        super().__init__()
        self.calculation_level = ""

        # The version of configuration of calculation logic in the settlement.
        self.config_version = ""

        self.delete_status = ""
        self.effective_date = DateTime()
        self.exception = ""
        self.factor = ""
        self.frequency = ""

        # Number of intervals of bill determinant in trade day, e.g. 300 for five minute intervals.
        self.number_interval = 0

        self.offset = ""

        # The level of precision in the current value.
        self.precision_level = ""

        self.primary_yn = ""
        self.reference_flag = ""
        self.reportable = ""
        self.round_off = ""
        self.source = ""
        self.termination_date = DateTime()

        # The UOM for the current value of the Bill Determinant.
        self.unit_of_measure = ""

        self.charge_profile_data = ChargeProfileData()
        self.mkt_user_attribute = ()
