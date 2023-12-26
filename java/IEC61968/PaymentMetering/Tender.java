package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.Money;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Tender is what is "offered" by the customer towards making a payment and is
 * often more than the required payment (hence the need for 'change'). The payment
 * is thus that part of the Tender that goes towards settlement of a particular
 * transaction.
 * Tender is modelled as an aggregation of Cheque and Card. Both these tender
 * types can exist in a single tender bid thus 'accountHolderName' has to exist
 * separately in each of Cheque and Card as each could have a different account
 * holder name.
 * @created 25-Dec-2023 8:45:25 PM
 */
public class Tender extends IdentifiedObject {

	/**
	 * Amount tendered by customer.
	 */
	public Money amount;
	/**
	 * Difference between amount tendered by customer and the amount charged by point
	 * of sale.
	 */
	public Money change;
	/**
	 * Kind of tender from customer.
	 */
	public TenderKind kind;
	/**
	 * Receipt that recorded this receiving of a payment in the form of tenders.
	 */
	public Receipt Receipt;

	public Tender(){

	}
}//end Tender