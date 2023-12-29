from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource
from IEC62325.InfIEC62325.InfEnergyScheduling.InadvertentAccount import InadvertentAccount
from IEC62325.MarketOperations.ParticipantInterfaces.BidSelfSched import BidSelfSched
from IEC62325.MarketOperations.MarketSystem.MarketResults.GeneralClearingResults import GeneralClearingResults
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.EnergyTransaction import EnergyTransaction


class SubControlArea(PowerSystemResource):
    """
    An area defined for the purpose of tracking interchange with surrounding areas
    via tie points; may or may not serve as a control area.
    @created 27-Dec-2023 12:55:42 PM
    """
    def __init__(self):
        super().__init__()
        self.area_short_name = ""  # Market area short name, which is the regulation zone. It references AGC regulation zone name.
        self.constant_coefficient = 0.0  # Loss estimate constant coefficient
        self.embedded_control_area = True  # Used in conjunction with the InternalCA flag. If the InternalCA flag is YES, this flag does not apply. If the InternaCA flag is NO, this flag provides an indication of AdjacentCA (NO) or Embedded CA (YES).
        self.internal_ca = True  # A Yes/No indication that this control area is contained internal to the system.
        self.linear_coefficient = 0.0  # Loss estimate linear coefficient
        self.local_ca = True  # Indication that this control area is the local control area.
        self.max_self_sched_mw = 1.0  # Maximum amount of self schedule MWs allowed for an embedded control area.
        self.min_self_sched_mw = 1.0  # Minimum amount of self schedule MW allowed for an embedded control area.
        self.quadratic_coefficient = 1.0  # Loss estimate quadratic coefficient
        self.bid_self_sched = BidSelfSched()
        self.general_clearing_results = GeneralClearingResults()
        self.export_energy_transactions = EnergyTransaction()  # Energy is transferred between interchange areas
        self.import_energy_transactions = EnergyTransaction()  # Energy is transferred between interchange areas
        self.inadvertent_account = InadvertentAccount()  # A control area can have one or more net inadvertent interchange accounts
