import IEC61970.Base.Domain.DateTimeInterval;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Float;
import IEC61968.Common.UserAttribute;

/**
 * An individual line item on an invoice.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class ErpInvoiceLineItem extends ErpDocument {

	/**
	 * Bill period for the line item.
	 */
	public DateTimeInterval billPeriod;
	/**
	 * General Ledger account code, must be a valid combination.
	 */
	public String glAccount;
	/**
	 * Date and time line item will be posted to the General Ledger. 
	 */
	public DateTime glDateTime;
	/**
	 * Kind of line item.
	 */
	public ErpInvoiceLineItemKind kind;
	/**
	 * Amount due for this line item.
	 */
	public Float lineAmount;
	/**
	 * Line item number on invoice statement.
	 */
	public String lineNumber;
	/**
	 * Version number of the bill run.
	 */
	public String lineVersion;
	/**
	 * Net line item charge amount.
	 */
	public Float netAmount;
	/**
	 * Previous line item charge amount. 
	 */
	public Float previousAmount;
	public ErpJournalEntry ErpJournalEntries;
	public ErpInvoiceLineItem ContainerErpInvoiceLineItem;
	public ErpRecLineItem ErpRecLineItem;
	public ErpPayment ErpPayments;
	public ErpInvoice ErpInvoice;
	public ErpPayableLineItem ErpPayableLineItem;
	public UserAttribute UserAttributes;

	public ErpInvoiceLineItem(){

	}
}//end ErpInvoiceLineItem