package IEC62325.MarketManagement;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * A class providing the identification and type of an auction.
 * @created 03-Jan-2024 1:58:51 PM
 */
public class Auction extends IdentifiedObject {

	/**
	 * Identification of the method of allocation in an auction.
	 */
	public String allocationMode;
	/**
	 * An indicator that signifies that the auction has been cancelled.
	 */
	public String cancelled;
	/**
	 * The product category of an auction.
	 */
	public String category;
	/**
	 * The terms which dictate the determination of the bid payment price.
	 */
	public String paymentTerms;
	/**
	 * The rights of use the transmission capacity acquired in an auction.
	 */
	public String rights;
	/**
	 * The kind of the Auction (e.g. implicit, explicit ...).
	 */
	public String type;
	public TimeSeries TimeSeries;

	public Auction(){

	}
}//end Auction