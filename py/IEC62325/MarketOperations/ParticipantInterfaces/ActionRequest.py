# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from typing import Optional

from IEC62325.MarketOperations.MktDomain.ActionType import ActionType
from IEC62325.MarketOperations.ParticipantInterfaces.Bid import Bid
from IEC62325.MarketOperations.ParticipantInterfaces.Trade import Trade


class ActionRequest:
    """
    Action request against an existing Trade.
    @created 28-Dec-2023 5:17:29 PM
    """

    def __init__(self) -> None:
        self.action_name: ActionType = ActionType.CANCEL
        self.bid: Optional[Bid] = Bid()
        self.trade: Optional[Trade] = Trade()
