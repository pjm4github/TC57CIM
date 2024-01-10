# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from typing import Optional

from IEC62325.MarketOperations.ReferenceData.MktContingency import MktContingency

from IEC62325.MarketOperations.MarketSystem.ExternalInputs.TransferInterface import TransferInterface


class TransferInterfaceSolution:
    """
    The TNA Interface Definitions from OPF for VSA.
    """

    def __init__(self) -> None:
        self.interface_margin: float = 0.0  # The margin for the interface
        self.post_transfer_mw: float = 0.0  # Post Transfer MW for step
        self.transfer_limit: float = 0.0  # Transfer Interface + Limit

        self.mkt_contingency_a: Optional[MktContingency] = MktContingency()
        self.mkt_contingency_b: Optional[MktContingency] = MktContingency()
        self.transfer_interface: Optional[TransferInterface] = TransferInterface()
