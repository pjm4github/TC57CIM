import IEC61968.Common.Status;

/**
 * Individual entry of an ErpReceivable, it is a particular transaction
 * representing an invoice, credit memo or debit memo to a customer.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class ErpRecLineItem extends ErpIdentifiedObject {

	public Status status;
	public ErpJournalEntry ErpJournalEntries;
	public ErpReceivable ErpReceivable;
	public ErpPayment ErpPayments;

	public ErpRecLineItem(){

	}
}//end ErpRecLineItem