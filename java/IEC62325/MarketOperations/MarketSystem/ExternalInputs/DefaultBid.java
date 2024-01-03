package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC62325.MarketOperations.MktDomain.BidType;
import IEC61970.Base.Domain.CostRate;
import IEC62325.MarketOperations.MktDomain.OnOff;
import IEC62325.MarketOperations.ParticipantInterfaces.Bid;
import IEC62325.MarketCommon.RegisteredResource;

/**
 * DefaultBid is a generic class to hold Default Energy Bid, Default Startup Bid,
 * and Default Minimum Load Bid:
 * 
 * Default Energy Bid
 * A Default Energy Bid is a monotonically increasing staircase function
 * consisting at maximum 10 economic bid segments, or 10 ($/MW, MW) pairs. There
 * are three methods for determining the Default Energy Bid:
 * <ul>
 * 	<li>Cost Based: derived from the Heat Rate or Average Cost multiplied by the
 * Gas Price Index plus 10%.</li>
 * 	<li>LMP Based: a weighted average of LMPs in the preceding 90 days.</li>
 * 	<li>Negotiated: an amount negotiated with the designated Independent Entity.
 * </li>
 * </ul>
 * 
 * Default Startup Bid
 * A Default Startup Bid (DSUB) shall be calculated for each RMR unit based on the
 * Startup Cost stored in the Master File and the applicable GPI and EPI.
 * 
 * Default Minimum Load Bid
 * A Default Minimum Load Bid (DMLB) shall be calculated for each RMR unit based
 * on the Minimum Load Cost stored in the Master File and the applicable GPI.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class DefaultBid extends Bid {

	/**
	 * Default bid type such as Default Energy Bid, Default Minimum Load Bid, and
	 * Default Startup Bid
	 */
	public BidType bidType;
	/**
	 * Minimum load cost in $/hr
	 */
	public CostRate minLoadCost;
	/**
	 * on-peak, off-peak, or all
	 */
	public OnOff peakFlag;
	public DefaultBidCurve DefaultBidCurve;
	public RegisteredResource RegisteredResource;

	public DefaultBid(){

	}
}//end DefaultBid