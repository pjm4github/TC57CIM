# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from typing import Optional

from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketCommon.MarketParticipant import MarketParticipant
from IEC62325.MarketOperations.ReferenceData.ContractRight import ContractRight
from IEC62325.MarketOperations.ReferenceData.SchedulingCoordinatorUser import SchedulingCoordinatorUser
from IEC62325.MarketOperations.ParticipantInterfaces.Trade import Trade


class SchedulingCoordinator(MarketParticipant):

    def __init__(self) -> None:
        super().__init__()
        self.credit_flag: Optional[str] = ""  # Flag to indicate creditworthiness (Y, N)
        self.credit_start_effective_date: Optional[DateTime] = DateTime()  # Date that the scheduling coordinator becomes creditworthy
        self.last_modified: Optional[DateTime] = DateTime()  # Indication of the last time this scheduling coordinator information was modified
        self.qualification_status: Optional[str] = ""  # Scheduling coordinator qualification status, Qualified, Not Qualified, or Disqualified
        self.scid: Optional[str] = ""  # This is the short name or Scheduling Coordinator ID field
        self.transmission_contract_right: Optional[ContractRight] = ContractRight()
        self.submit_to_sc_trade: Optional[Trade] = Trade()
        self.to_sc_trade: Optional[Trade] = Trade()
        self.from_sc_trade: Optional[Trade] = Trade()
        self.submit_from_sc_trade: Optional[Trade] = Trade()
        self.market_participant: Optional[MarketParticipant] = MarketParticipant()
        self.scheduling_coordinator_user: Optional[SchedulingCoordinatorUser] = SchedulingCoordinatorUser()
