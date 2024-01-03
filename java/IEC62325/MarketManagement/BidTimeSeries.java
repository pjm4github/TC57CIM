package IEC62325.MarketManagement;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Decimal;
import IEC61970.Base.Domain.Integer;

/**
 * The formal specification of specific characteristics related to a bid.
 * @created 03-Jan-2024 1:58:51 PM
 */
public class BidTimeSeries extends TimeSeries {

	/**
	 * Indication that  the values in the period are considered as a whole. They
	 * cannot be changed or subdivided.
	 */
	public String blockBid;
	/**
	 * The coded identification of the energy flow.
	 */
	public String direction;
	/**
	 * An indication whether or not each element of the bid may be partially accepted
	 * or not.
	 */
	public String divisible;
	/**
	 * Unique identification associated with all linked tenders.
	 * The identification of a set of tenders that are linked together signifying that
	 * only one can be accepted.
	 * This identification is defined by the tenderer and must be unique for a given
	 * auction.
	 */
	public String exclusiveBidsIdentification;
	/**
	 * Unique identification associated with all linked bids.
	 */
	public String linkedBidsIdentification;
	/**
	 * The minimum quantity of energy that can be activated at a given time interval.
	 */
	public Decimal minimumActivationQuantity;
	/**
	 * The numeric local priority given to a bid. Lower numeric values will have
	 * higher priority.
	 */
	public Integer priority;
	/**
	 * The information about the status of the bid, such as "shared", "restricted", ...
	 */
	public String status;
	/**
	 * The minimum increment that can be applied for an increase in an activation
	 * request.
	 */
	public Decimal stepIncrementQuantity;

	public BidTimeSeries(){

	}
}//end BidTimeSeries