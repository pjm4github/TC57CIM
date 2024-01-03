package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Core.IdentifiedObject;
import IEC62325.MarketOperations.ParticipantInterfaces.TransactionBid;

/**
 * Contains the cleared results for each TransactionBid submitted to and accepted
 * by the market.
 * @created 28-Dec-2023 8:26:45 PM
 */
public class TransactionBidResults extends IdentifiedObject {

	/**
	 * The market transaction megawatt
	 */
	public Float clearedMW;
	/**
	 * The price of the market transaction
	 */
	public Float clearedPrice;
	public TransactionBid TransactionBid;
	public TransactionBidClearing TransactionBidClearing;

	public TransactionBidResults(){

	}
}//end TransactionBidResults