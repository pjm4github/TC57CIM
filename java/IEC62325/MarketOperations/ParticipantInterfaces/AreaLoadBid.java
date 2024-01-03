package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.Float;

/**
 * AreaLoadBid is not submitted by a market participant into the Markets. Instead,
 * it is simply an aggregation of all LoadBids contained wtihin a specific
 * SubControlArea. This entity should inherit from Bid for representation of the
 * timeframe (startTime, stopTime) and the market type.
 * @created 28-Dec-2023 5:17:54 PM
 */
public class AreaLoadBid extends Bid {

	/**
	 * The Demand Bid Megawatt for the area case.
	 * Attribute Usage: This is Scheduled demand MW in Day Ahead
	 */
	public Float demandBidMW;
	public LoadBid LoadBid;

	public AreaLoadBid(){

	}
}//end AreaLoadBid