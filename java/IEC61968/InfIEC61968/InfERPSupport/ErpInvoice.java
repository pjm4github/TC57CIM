import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.Date;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;

/**
 * A roll up of invoice line items. The whole invoice has a due date and amount to
 * be paid, with information such as customer, banks etc. being obtained through
 * associations. The invoice roll up is based on individual line items that each
 * contain amounts and descriptions for specific services or products.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class ErpInvoice extends ErpDocument {

	/**
	 * Total amount due on this invoice based on line items and applicable adjustments.
	 */
	public Money amount;
	/**
	 * Kind of media by which the CustomerBillingInfo was delivered.
	 */
	public BillMediaKind billMediaKind;
	/**
	 * Calculated date upon which the Invoice amount is due.
	 */
	public Date dueDate;
	/**
	 * Kind of invoice (default is 'sales').
	 */
	public ErpInvoiceKind kind;
	/**
	 * Date on which the customer billing statement/invoice was printed/mailed.
	 */
	public Date mailedDate;
	/**
	 * True if payment is to be paid by a Customer to accept a particular ErpQuote
	 * (with associated Design) and have work initiated, at which time an associated
	 * ErpInvoice should automatically be generated. EprPayment.subjectStatus
	 * satisfies terms specificed in the ErpQuote.
	 */
	public Boolean proForma;
	/**
	 * Number of an invoice to be reference by this invoice.
	 */
	public String referenceNumber;
	/**
	 * Date and time when the invoice is issued.
	 */
	public DateTime transactionDateTime;
	/**
	 * Type of invoice transfer.
	 */
	public String transferType;

	public ErpInvoice(){

	}
}//end ErpInvoice