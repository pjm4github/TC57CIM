from IEC61970.Base.Core.CurveData import CurveData
from IEC62325.MarketOperations.MktDomain.BidCalculationBasis import BidCalculationBasis


class DefaultBidCurveData(CurveData):
    #  * Curve data for default bid curve and startup cost curve.
    #  * @created 27-Dec-2023 3:27:05 PM

    def __init__(self) -> None:
        super().__init__()
        # 	 * Type of calculation basis used to define the default bid segment curve.
        self.bid_segment_calc_type: BidCalculationBasis = BidCalculationBasis()
