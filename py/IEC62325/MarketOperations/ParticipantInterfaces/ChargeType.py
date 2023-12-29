# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from IEC61968.Common.Document import Document
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MarketOpCommon.MktUserAttribute import MktUserAttribute
from IEC62325.MarketOperations.ParticipantInterfaces.ChargeComponent import ChargeComponent
from IEC62325.MarketOperations.ParticipantInterfaces.ChargeGroup import ChargeGroup


class ChargeType(Document):
    """
    Charge Type is the basic level configuration for settlement to process specific
    charges for invoicing purpose. Examples such as: Day Ahead Spinning Reserve
    Default Invoice Interest Charge, etc.
    @created 28-Dec-2023 5:20:37 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.charge_order: str = ""
        self.charge_version: str = ""
        self.effective_date: DateTime = DateTime()
        self.factor: str = ""
        self.frequency_type: str = ""
        self.termination_date: DateTime = DateTime()
        self.total_interval: str = ""

        # A ChargeGroup can have 0-n ChargeType. A ChargeType can associate to 0-n
        # ChargeGroup.
        self.charge_group: ChargeGroup = ChargeGroup()

        # A ChargeType can have 0-n ChargeComponent and a ChargeComponent can associate
        # to 0-n ChargeType
        self.charge_components: ChargeComponent = ChargeComponent()
        self.mkt_user_attribute: MktUserAttribute = MktUserAttribute()
