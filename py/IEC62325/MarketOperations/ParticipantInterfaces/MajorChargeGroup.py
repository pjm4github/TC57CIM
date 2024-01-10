# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.ParticipantInterfaces.ChargeType import ChargeType
from IEC62325.MarketOperations.ParticipantInterfaces.MarketScheduledEvent import MarketScheduledEvent
from IEC62325.MarketOperations.MarketSystem.MarketResults.Settlement import Settlement


class MajorChargeGroup(IdentifiedObject):
    def __init__(self) -> None:
        super().__init__()
        self.effective_date: Optional[DateTime] = DateTime()
        self.frequency_type: Optional[str] = ""
        self.invoice_type: Optional[str] = ""
        self.require_autorun: Optional[str] = ""
        self.revision_number: Optional[str] = ""
        self.run_type: Optional[str] = ""
        self.run_version: Optional[str] = ""
        self.termination_date: Optional[DateTime] = DateTime()
        # 	 * A MajorChargeGroup can have 0-n ChargeType. A ChargeType can associate to 0-n
        # 	 * MajorChargeGroup.
        self.charge_type: Optional[ChargeType] = ChargeType()
        self.mkt_scheduled_event: Optional[MarketScheduledEvent] = MarketScheduledEvent()
        self.settlement: Optional[Settlement] = Settlement()
