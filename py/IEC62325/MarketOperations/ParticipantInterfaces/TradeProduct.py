# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from IEC62325.MarketOperations.MktDomain.TradeType import TradeType
from IEC62325.MarketOperations.ParticipantInterfaces.Trade import Trade


class TradeProduct:
    """
    TradeType                             TradeProduct
    IST  (InterSC Trade)
    IST                                 PHY  (Physical Energy Trade)
    IST                                 APN  (Energy Trades at
    IST                                 Aggregated Pricing Nodes)
    IST                                 CPT  (Converted Physical
    IST                                 Energy Trade)
    AST  (Ancilliary Services Trade)      RUT  (Regulation Up Trade)
    AST                                     RDT  (Regulation Down
    AST                                     Trade)
    AST                                     SRT  (Spinning Reserve
    AST                                     Trade)
    AST                                     NRT  (Non-Spinning Reserve
    UCT  (Unit Commitment Trade)         null
    @created 28-Dec-2023 5:24:10 PM
    """

    def __init__(self) -> None:
        self.trade_product_type: str = ""
        self.trade_type: TradeType = TradeType.AST
        self.trade: Trade = Trade()
