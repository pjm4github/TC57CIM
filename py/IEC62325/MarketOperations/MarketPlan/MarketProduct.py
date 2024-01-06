from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.MarketPlan.Market import Market
from IEC62325.MarketOperations.MarketSystem.MarketResults.MarketRegionResults import MarketRegionResults
from IEC62325.MarketOperations.MarketSystem.MarketResults.ResourceAwardInstruction import ResourceAwardInstruction
from IEC62325.MarketOperations.MktDomain.MarketProductType import MarketProductType
from IEC62325.MarketOperations.ParticipantInterfaces.BidError import BidError
from IEC62325.MarketOperations.ParticipantInterfaces.ProductBid import ProductBid
from IEC62325.MarketOperations.ReferenceData.BidPriceCap import BidPriceCap


class MarketProduct(IdentifiedObject):
    """
    A product traded by an RTO (e.g. energy, 10 minute spinning reserve).
    Ancillary service product examples include: Regulation, Regulation Up,
    Regulation Down, Spinning Reserve, Non-Spinning Reserve, etc.
    @created 27-Dec-2023 5:34:36 PM
    """

    #
    # Market product type examples:
    #
    # EN (Energy)
    # RU (Regulation Up)
    # RD (Regulation Dn)
    # SR (Spinning Reserve)
    # NR (Non-Spinning Reserve)
    # RC (RUC)
    #
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.market_product_type = MarketProductType.LFD  # Market product type examples: EN, RU, RD, SR, NR, RC.
        self.ramp_interval = 0.0  # Ramping time interval for the specific market product type.
        self.product_bids = [ProductBid()]  # Associated ProductBids
        self.resource_award_instruction = ResourceAwardInstruction()  # Associated ResourceAwardInstruction
        self.bid_error = BidError()  # Associated BidError
        self.bid_price_cap = BidPriceCap()  # Associated BidPriceCap
        self.market_region_results = MarketRegionResults()  # Associated MarketRegionResults
        self.market = Market()  # Associated Market