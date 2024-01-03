package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.Boolean;
import IEC62325.MarketOperations.MarketSystem.ExternalInputs.EnergyProfile;

/**
 * Bilateral or scheduled transactions for energy and ancillary services
 * considered by market clearing process.
 * @created 28-Dec-2023 5:24:21 PM
 */
public class TransactionBid extends Bid {

	/**
	 * Set true if this is a demand transaction.
	 */
	public Boolean demandTransaction;
	/**
	 * Set true if this is a dispatchable transaction.
	 */
	public Boolean dispatchable;
	/**
	 * Set true if this is a willing to pay transaction. This flag is used to
	 * determine whether a schedule is willing-to-pay-congestion or not.
	 */
	public Boolean payCongestion;
	public EnergyProfile EnergyProfiles;

	public TransactionBid(){

	}
}//end TransactionBid