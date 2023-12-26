import IEC61968.Common.Status;

/**
 * Of an ErpPayable, a line item references an ErpInvoiceLineitem or other source
 * such as credit memos.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class ErpPayableLineItem extends ErpIdentifiedObject {

	public Status status;
	public ErpJournalEntry ErpJournalEntries;
	public ErpPayable ErpPayable;
	public ErpPayment ErpPayments;

	public ErpPayableLineItem(){

	}
}//end ErpPayableLineItem