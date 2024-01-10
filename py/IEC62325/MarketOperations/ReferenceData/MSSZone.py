# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from typing import Optional

from IEC62325.MarketOperations.ReferenceData.AggregateNode import AggregateNode
from IEC62325.MarketOperations.ReferenceData.ResourceCertification import YesNo


class MSSZone(AggregateNode):
    """
    Model to define a zone within a Metered Sub System.
    @created 28-Dec-2023 12:17:00 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.ignore_losses: Optional[YesNo] = YesNo.NO  # Provides an indication if losses are to be ignored for this metered subsystem zone.
        self.loss_factor: float = 0.0  # This is the default loss factor for the Metered Sub-System (MSS) zone. The actual losses are calculated during the RT market.
        self.ruc_gross_settlement: Optional[YesNo] = YesNo.NO  # Metered Sub-System (MSS) Load Following may select Net vs. Gross settlement. Net Settlement requires the net Demand settled at the Metered Sub-Sustem (MSS) Load Aggregation Point (LAP) and Net Supply needs to settle at the equivalent to the weighted average price of the MSS generation. Gross load will be settled at the System LAP and the Gross supply will be settled at the LMP. MSS Aggregation that elects gross settlement shall have to identify if its resources are Load Following or not.
