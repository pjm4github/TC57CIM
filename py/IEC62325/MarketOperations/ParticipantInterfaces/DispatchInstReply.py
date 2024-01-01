# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from datetime import datetime
from typing import Optional

from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MktDomain.DispatcpyResponseType import DispatchResponseType
from IEC62325.MarketOperations.MktDomain.PassIndicatorType import PassIndicatorType


class DispatchInstReply:

    def __init__(self) -> None:
        self.accept_mwOptional[ActivePower] = ActivePower()  # The accepted mw amount by the responder. aka response mw.
        self.accept_statusOptional[DispatchResponseType] = DispatchResponseType.ACCEPT  # The accept status submitted by the responder. enumeration type needs to be defined
        self.certification_nameOptional[str] = ""  # The Subject DN is the X509 Certificate Subject DN. This is the essentially the certificate name presented by the client. In the case of ADS Certificates, this will be the user name. It may be from an API Client or the MP Client (GUI).
        self.cleared_mwOptional[ActivePower] = ActivePower()  # MW amount associated with instruction. For 5 minute binding dispatches, this is the Goto MW or DOT
        self.instruction_timeOptional[DateTime] = DateTime()   # The target date/time for the received instruction
        self.instruction_typeOptional[str] = ""  # instruction type: commitment, out of sequence, dispatch
        self.pass_indicatorOptional[PassIndicatorType] = PassIndicatorType.DA  # The type of run for the market clearing
        self.received_timeOptional[DateTime] = DateTime()   # Timestamp indicating the time at which the instruction was received
        self.start_timeOptional[DateTime] = DateTime()   # start time
