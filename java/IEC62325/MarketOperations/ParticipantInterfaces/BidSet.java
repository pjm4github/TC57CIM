package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * As set of mutually exclusive bids for which a maximum of one may be scheduled.
 * Of these generating bids, only one generating bid can be scheduled at a time.
 * @created 28-Dec-2023 5:20:00 PM
 */
public class BidSet extends IdentifiedObject {

	public GeneratingBid GeneratingBids;

	public BidSet(){

	}
}//end BidSet