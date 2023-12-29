# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.ReferenceData.FlowgateValue import FlowgateValue


class FlowgatePartner(IdentifiedObject):

    def __init__(self) -> None:
        super().__init__()

        self.flowgate_value: FlowgateValue = FlowgateValue()

