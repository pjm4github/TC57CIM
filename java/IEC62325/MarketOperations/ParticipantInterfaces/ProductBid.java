package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * Component of a bid that pertains to one market product.
 * @created 28-Dec-2023 5:22:55 PM
 */
public class ProductBid extends IdentifiedObject {

	public BidPriceSchedule BidSchedule;
	/**
	 * A bid comprises one or more product bids of market products
	 */
	public Bid Bid;
	public BidDistributionFactor BidDistributionFactor;
	public BidSelfSched BidSelfSched;

	public ProductBid(){

	}
}//end ProductBid