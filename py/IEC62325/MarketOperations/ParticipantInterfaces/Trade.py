# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023

from typing import Optional

from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MktDomain.MarketType import MarketType
from IEC62325.MarketOperations.ParticipantInterfaces.TradeError import TradeError


class Trade:
    """
    Inter Scheduling Coordinator Trades to model financial trades which may impact
    settlement.
    """
    def __init__(self) -> None:
        self.adjusted_trade_quantityOptional[float] = 0.0

        # The validated and current market accepted trade amount of a physical energy
        # trade.
        self.counter_trade_quantityOptional[float] = 0.0

        # MW quantity submitted by counter SC for the same trade.
        self.depend_on_trade_nameOptional[str] = ""

        # The Depend On IST Name points to the unique IST Name in the chain of physical
        # energy trades
        self.last_modifiedOptional[DateTime] = DateTime()

        # Time and date the trade was last modified.
        self.market_typeOptional[MarketType] = MarketType.DAM

        self.start_timeOptional[DateTime] = DateTime()

        # Start time and date for which trade applies.
        self.stop_timeOptional[DateTime] = DateTime()

        # Stop time and date for which trade is applicable.
        self.submit_from_time_stampOptional[DateTime] = DateTime()

        # Timestamp of submittal of submit From Scheduling Coordinator Trade to Market
        # Participant Bid Submittal.
        self.submit_from_userOptional[str] = ""
        # Userid of the submit From Scheduling Coordinator trade
        self.submit_to_time_stampOptional[DateTime] = DateTime()

        # Timestamp of submittal of submit To Scheduling Coordinator Trade to Market
        # Participant Bid Submittal.
        self.submit_to_userOptional[str] = ""

        # Userid of the submit To Scheduling Coordinator trade
        self.trade_quantityOptional[float] = 0.0

        # tradeQuantity:
        # If tradeType = IST, The amount of an Energy Trade.
        # If tradeType = AST, The amount of an Ancillary Service Obligation Trade.
        # If tradeType = UCT, The amount of a Unit Commitment Obligation Trade.

        self.trade_statusOptional[str] = ""
        # Resulting status of the trade following the rule engine processing.

        self.update_time_stampOptional[DateTime] = DateTime()

        self.update_userOptional[str] = ""

        self.trade_errorOptional[TradeError] = TradeError()
