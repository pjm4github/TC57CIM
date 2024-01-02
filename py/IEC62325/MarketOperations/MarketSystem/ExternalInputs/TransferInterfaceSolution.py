# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from typing import Optional

from IEC62325.MarketOperations.ReferenceData.MktContingency import MktContingency

from IEC62325.MarketOperations.MarketSystem.ExternalInputs.TransferInterface import TransferInterface


class TransferInterfaceSolution:
    """
    The TNA Interface Definitions from OPF for VSA.
    """

    def __init__(self) -> None:
        self.interface_marginfloat = 0.0  # The margin for the interface
        self.post_transfer_mwfloat = 0.0  # Post Transfer MW for step
        self.transfer_limitfloat = 0.0  # Transfer Interface + Limit

        self.mkt_contingency_aOptional[MktContingency] = MktContingency()
        self.mkt_contingency_bOptional[MktContingency] = MktContingency()
        self.transfer_interfaceOptional[TransferInterface] = TransferInterface()
