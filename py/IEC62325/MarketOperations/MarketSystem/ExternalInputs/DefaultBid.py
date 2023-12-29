# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from IEC62325.MarketOperations.MktDomain.BidType import BidType
from IEC61970.Base.Domain.CostRate import CostRate
from IEC62325.MarketOperations.MktDomain.OnOff import OnOff
from IEC62325.MarketOperations.ParticipantInterfaces.Bid import Bid
from IEC62325.MarketCommon.RegisteredResource import RegisteredResource
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.DefaultBidCurve import DefaultBidCurve


class DefaultBid(Bid):
    """
    DefaultBid is a generic class to hold Default Energy Bid, Default Startup Bid,
    and Default Minimum Load Bid:
    
    Default Energy Bid
    A Default Energy Bid is a monotonically increasing staircase function
    consisting at maximum 10 economic bid segments, or 10 ($/MW, MW) pairs. There
    are three methods for determining the Default Energy Bid:
    <ul>
    	<li>Cost Based: derived from the Heat Rate or Average Cost multiplied by the
    Gas Price Index plus 10%.</li>
    	<li>LMP Based: a weighted average of LMPs in the preceding 90 days.</li>
    	<li>Negotiated: an amount negotiated with the designated Independent Entity.
    </li>
    </ul>
    
    Default Startup Bid
    A Default Startup Bid (DSUB) shall be calculated for each RMR unit based on the
    Startup Cost stored in the Master File and the applicable GPI and EPI.
    
    Default Minimum Load Bid
    A Default Minimum Load Bid (DMLB) shall be calculated for each RMR unit based
    on the Minimum Load Cost stored in the Master File and the applicable GPI.
    @created 27-Dec-2023 3:26:47 PM
    """
    def __init__(self) -> None:
        pass
        # 	 * Default bid type such as Default Energy Bid, Default Minimum Load Bid, and
        # 	 * Default Startup Bid
        self.bid_type: BidType = BidType()
        #  * Minimum load cost in $/hr
        self.min_load_cost: CostRate = CostRate()
        #  * on-peak, off-peak, or all
        self.peak_flag: OnOff = OnOff()
        self.default_bid_curve: DefaultBidCurve = DefaultBidCurve()
        self.registered_resource: RegisteredResource = RegisteredResource()
