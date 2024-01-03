package IEC61968.InfIEC61968.InfCustomers;

import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.DateTime;
import IEC61968.Work.Work;
import IEC61968.Common.Document;

/**
 * Billing information for work performed for the customer. The history of Work
 * Billing Info, Invoices, and Payments is to be maintained in associated
 * ActivityRecords.
 * @created 29-Dec-2023 9:26:25 PM
 */
public class WorkBillingInfo extends Document {

	/**
	 * Estimated cost for work. 
	 */
	public Money costEstimate;
	/**
	 * Amount of price on deposit.
	 */
	public Money deposit;
	/**
	 * Discount from standard price.
	 */
	public Float discount;
	/**
	 * Date and time by which payment for bill is expected from client.
	 */
	public DateTime dueDateTime;
	/**
	 * Date and time bill was issued to client.
	 */
	public DateTime issueDateTime;
	/**
	 * Date payment was received from client.
	 */
	public DateTime receivedDateTime;
	/**
	 * Amount of bill.
	 */
	public Money workPrice;
	public ErpInvoiceLineItem ErpLineItems;
	public Work Works;

	public WorkBillingInfo(){

	}
}//end WorkBillingInfo