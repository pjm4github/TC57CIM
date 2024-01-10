# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.ReferenceData.MeteredSubSystem import MeteredSubSystem
from IEC62325.MarketOperations.ReferenceData.RTO import RTO
from IEC62325.MarketOperations.ReferenceData.ResourceCertification import YesNo


class MssAggregation(IdentifiedObject):
    def __init__(self) -> None:
        super().__init__()
        self.cost_recovery: Optional[
            YesNo] = YesNo.NO  # Charge for Emission Costs, Start Up Costs, or Minimum Load Costs.
        self.gross_settlement: Optional[YesNo] = YesNo.NO  # MSS Load Following may select Net vs. Gross settlement.
        # Net Settlement requires the net Demand settled at the MSS LAP and Net Supply needs to settle
        # at the equivalent to the weighted average price of the MSS generation.
        # Gross load will be settled at the System LAP and the Gross supply will be settled at the LMP.
        # MSS Aggregation that elects gross settlement shall have to identify if its resources are
        # Load Following or not.
        self.ignore_losses: Optional[
            YesNo] = YesNo.NO  # Provides an indication if losses are to be ignored for this zone.
        # Also referred to as Exclude Marginal Losses.
        self.ignore_marginal_losses: Optional[
            YesNo] = YesNo.NO  # Provides an indication if marginal losses are to be ignored for this zone.
        self.load_following: Optional[
            YesNo] = YesNo.NO  # Indication that this particular MSSA participates in the Load Following function.
        self.ruc_procurement: Optional[
            YesNo] = YesNo.NO  # Indicates that RUC will be procured by the ISO or self provided.
        self.metered_sub_system: Optional[MeteredSubSystem] = MeteredSubSystem()
        self.rto: Optional[RTO] = RTO()
