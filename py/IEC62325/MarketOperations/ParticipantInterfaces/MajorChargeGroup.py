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
        self.effective_dateOptional[DateTime] = DateTime()
        self.frequency_typeOptional[str] = ""
        self.invoice_typeOptional[str] = ""
        self.require_autorunOptional[str] = ""
        self.revision_numberOptional[str] = ""
        self.run_typeOptional[str] = ""
        self.run_versionOptional[str] = ""
        self.termination_dateOptional[DateTime] = DateTime()
        # 	 * A MajorChargeGroup can have 0-n ChargeType. A ChargeType can associate to 0-n
        # 	 * MajorChargeGroup.
        self.charge_typeOptional[ChargeType] = ChargeType()
        self.mkt_scheduled_eventOptional[MarketScheduledEvent] = MarketScheduledEvent()
        self.settlementOptional[Settlement] = Settlement()
