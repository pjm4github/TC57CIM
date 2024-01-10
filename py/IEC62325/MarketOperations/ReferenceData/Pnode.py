# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketCommon.RegisteredResource import RegisteredResource
from IEC62325.MarketOperations.CongestionRevenueRights.CRRSegment import CRRSegment
from IEC62325.MarketOperations.MarketOpCommon.MktMeasurement import MktMeasurement
from IEC62325.MarketOperations.MarketSystem.MarketResults.ExPostPricingResults import ExPostPricingResults
from IEC62325.MarketOperations.MarketSystem.MarketResults.PnodeResults import PnodeResults
from IEC62325.MarketOperations.ParticipantInterfaces.Trade import Trade
from IEC62325.MarketOperations.ParticipantInterfaces.TransactionBid import TransactionBid
from IEC62325.MarketOperations.ReferenceData.AdjacentCASet import SubControlArea


class Pnode(IdentifiedObject):
    """
    A pricing node is directly associated with a connectivity node. 
    It is a pricing location for which market participants submit their bids, offers, 
    buy/sell CRRs, and settle.
    @created 28-Dec-2023 12:19:18 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        super().__init__()
        # 	 * If true, this Pnode is public (prices are published for DA/RT and FTR markets),
        # 	 * otherwise it is private (location is not usable by market for
        # 	 * bidding/FTRs/transactions).
        self.is_public: bool = False
        self.sub_control_area: SubControlArea = SubControlArea()
        self.receipt_transaction_bids: TransactionBid = TransactionBid()
        self.delivery_transaction_bids: TransactionBid = TransactionBid()
        self.trade: Trade = Trade()
        self.ex_post_results: ExPostPricingResults = ExPostPricingResults()
        self.pnode_results: PnodeResults = PnodeResults()
        # 	 * Allows Measurements to be associated to Pnodes.
        self.mkt_measurement: MktMeasurement = MktMeasurement()
        self.source_crr_segment: CRRSegment = CRRSegment()
        self.sink_crr_segment: CRRSegment = CRRSegment()
        # 	 * A registered resource injects power at one or more connectivity nodes related
        # 	 * to a pnode
        self.registered_resources: RegisteredResource = RegisteredResource()
