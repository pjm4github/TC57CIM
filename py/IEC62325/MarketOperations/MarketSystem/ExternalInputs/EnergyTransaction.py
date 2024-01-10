# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from typing import Optional

from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.Money import Money
from IEC62325.InfIEC62325.InfEnergyScheduling.CurtailmentProfile import CurtailmentProfile
from IEC62325.InfIEC62325.InfEnergyScheduling.EnergyProduct import EnergyProduct
from IEC62325.InfIEC62325.InfEnergyScheduling.LossProfile import LossProfile
from IEC62325.InfIEC62325.InfEnergyScheduling.TieLine import TieLine
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.EnergyProfile import EnergyProfile
from IEC62325.MarketOperations.MktDomain.EnergyTransactionType import EnergyTransactionType
from IEC62325.MarketOperations.ParticipantInterfaces.EnergyPriceCurve import EnergyPriceCurve


class EnergyTransaction:
    """
    Specifies the schedule for energy transfers between interchange areas that are
    necessary to satisfy the associated interchange transaction.
    """

    def __init__(self) -> None:
        self.capacity_backed: bool = False  # Interchange capacity flag
        self.congest_charge_max: Optional[Money] = Money()  # Maximum congestion charges in monetary units
        self.delivery_point_p: Optional[ActivePower] = ActivePower()  # Delivery point active power
        self.energy_min: Optional[ActivePower] = ActivePower()  # Transaction minimum active power if dispatchable
        self.firm_interchange_flag: bool = False  # Firm interchange flag indicates whether this energy transaction
        # can be changed without potential financial consequences
        self.pay_congestion: bool = False  # Willing to Pay congestion flag
        self.reason: Optional[str] = ""  # Reason for energy transaction
        self.receipt_point_p: Optional[ActivePower] = ActivePower()  # Receipt point active power
        self.state: Optional[EnergyTransactionType] = EnergyTransactionType.APPROVE  # { Approve | Deny | Study }
        self.tie_lines: Optional[TieLine] = TieLine()  # A dynamic energy transaction can act as a pseudo tie line
        self.energy_price_curves: Optional[EnergyPriceCurve] = EnergyPriceCurve()
        self.energy_product: Optional[
            EnergyProduct] = EnergyProduct()  # The "Source" for an EnergyTransaction is an EnergyProduct which is
        # injected into a ControlArea. Typically this is a ServicePoint
        self.energy_profiles: Optional[
            EnergyProfile] = EnergyProfile()  # An EnergyTransaction shall have at least one EnergyProfile
        self.curtailment_profiles: Optional[
            CurtailmentProfile] = CurtailmentProfile()  # An EnergyTransaction may be curtailed by any of the
        # participating entities
        self.loss_profiles: Optional[LossProfile] = LossProfile()  # An EnergyTransaction may have a LossProfile
