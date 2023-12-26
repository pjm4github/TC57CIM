package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Record of total receipted payment from customer.
 * @created 25-Dec-2023 8:45:24 PM
 */
public class Receipt extends IdentifiedObject {

	/**
	 * True if this receipted payment is manually bankable, otherwise it is an
	 * electronic funds transfer.
	 */
	public Boolean isBankable;
	/**
	 * Receipted amount with rounding, date and note.
	 */
	public LineDetail line;
	/**
	 * All transactions recorded for this receipted payment.
	 */
	public Transaction Transactions;

	public Receipt(){

	}
}//end Receipt