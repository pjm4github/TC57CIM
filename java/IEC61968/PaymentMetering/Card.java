package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Date;

/**
 * Documentation of the tender when it is a type of card (credit, debit, etc).
 * @created 25-Dec-2023 8:45:19 PM
 */
public class Card {

	/**
	 * Name of account holder.
	 */
	public String accountHolderName;
	/**
	 * The card verification number.
	 */
	public String cvNumber;
	/**
	 * The date when this card expires.
	 */
	public Date expiryDate;
	/**
	 * The primary account number.
	 */
	public String pan;
	/**
	 * Payment tender this card is being used for.
	 */
	public Tender Tender;

	public Card(){

	}
}//end Card