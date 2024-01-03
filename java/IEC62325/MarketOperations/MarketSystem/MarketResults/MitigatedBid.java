package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Core.IdentifiedObject;
import IEC62325.MarketOperations.ParticipantInterfaces.Bid;

/**
 * Mitigated bid results posted for a given settlement period.
 * @created 28-Dec-2023 8:23:39 PM
 */
public class MitigatedBid extends IdentifiedObject {

	public Bid Bid;
	public MitigatedBidClearing MitigatedBidClearing;

	public MitigatedBid(){

	}
}//end MitigatedBid