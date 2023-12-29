# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from datetime import datetime
from enum import Enum

from IEC61970.Base.Domain.DateTime import DateTime


class FlowDirectionType(Enum):
    UPSTREAM = 1
    DOWNSTREAM = 2
    BI_DIRECTIONAL = 3


class FlowgateValue:

    def __init__(self) -> None:
        self.economic_dispatch_limit: int = 0  # Limit for Economic Dispatch priority 6 energy flow on the specified flowgate
        self.effective_date: DateTime = DateTime()  # Date/Time when record becomes effective
        self.firm_network_limit: int  # Limit for firm flow on the specified flowgate for the specified time period
        self.flow_direction_flag: FlowDirectionType = FlowDirectionType.BI_DIRECTIONAL  # Specifies the direction of energy flow in the flowgate
        self.mkt_flow: int = 0  # The amount of energy flow over a specified flowgate due to generation in the market
        self.net_firm_network_limit: int = 0  # Net Energy flow in flowgate for the associated FlowgatePartner

