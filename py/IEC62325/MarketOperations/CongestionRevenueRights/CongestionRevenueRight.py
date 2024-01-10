from IEC61968.Common import Document
from IEC62325.MarketOperations.ReferenceData.Flowgate import Flowgate
from IEC62325.MarketOperations.MarketPlan.CRRMarket import CRRMarket
from IEC62325.MarketOperations.CongestionRevenueRights.CRRSegment import CRRSegment
from IEC62325.MarketOperations.MktDomain.CRRCategoryType import CRRCategoryType

from IEC62325.MarketOperations.MktDomain.CRRHedgeType import CRRHedgeType
from IEC62325.MarketOperations.MktDomain.CRRSegmentType import CRRSegmentType
from IEC62325.MarketOperations.MktDomain.TimeOfUse import TimeOfUse


class CongestionRevenueRight(Document):
    """
    Congestion Revenue Rights (CRR) class that is inherited from a Document class.

    A CRR is a financial concept that is used to hedge congestion charges.

    The CRR is usually settled based on the Locational Marginal Prices (LMPs) that
    are calculated in the day-ahead market. These LMPs are determined by the day-ahead
    resource schedules/bids. CRRs will not hedge against marginal losses. If
    the congestion component of LMP at the sink is greater than at the source, then
    the CRR owner is entitled to receive a portion of congestion revenues. If the
    congestion component at the sink is less than at the source, then an obligation-type
    CRR owner will be charged, but an option-type CRR owner will not.
    """

    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.crr_category = CRRCategoryType.POINT_TO_POINT  # CRR category represents 'PTP' for a point-to-point CRR,
        # or 'NSR' for a Network Service Right.
        self.crr_type = CRRSegmentType.AUC  # Type of the CRR, from the possible type definitions in the CRR System.
        self.hedge_type = CRRHedgeType.OPTION  # Hedge type Obligation or Option.
        self.time_of_use = TimeOfUse.ON  # Time of Use flag of the CRR - Peak (ON), Offpeak (OFF) or all 24 hours (
        # 24HR).
        self.trade_slice_id = str()  # Segment of the CRR described in the current record.
        self.flowgate = Flowgate()  # Associated Flowgate
        self.crr_market = CRRMarket()  # Associated CRRMarket
        self.crr_segment = CRRSegment()  # Associated CRRSegment
