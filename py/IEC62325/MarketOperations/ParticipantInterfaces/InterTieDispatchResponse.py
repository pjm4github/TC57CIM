# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from typing import Optional

from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MktDomain.DispatcpyResponseType import DispatchResponseType
from IEC62325.MarketOperations.MktDomain.PassIndicatorType import PassIndicatorType


class InterTieDispatchResponse:
    """
    Response from an intertie resource acknowledging receipt of dispatch instructions.
    @created 28-Dec-2023 5:21:39 PM
    """

    def __init__(self) -> None:
        """
        Constructor for InterTieDispatchResponse
        """
        self.accept_mwOptional[float] = 0.0  # The accepted mw amount by the responder. aka response mw.
        self.accept_statusOptional[DispatchResponseType] = DispatchResponseType()  # The accept status submitted by the responder.
        self.cleared_mwOptional[float] = 0.0  # MW amount associated with instruction.
        self.pass_indicatorOptional[PassIndicatorType] = PassIndicatorType()
        self.start_timeOptional[DateTime] = DateTime()   # Part of the Composite key that downstream app uses to match the instruction
