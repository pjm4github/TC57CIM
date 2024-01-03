package IEC62325.MarketOperations.MarketOpCommon;

import IEC61970.Base.Domain.Money;
import IEC62325.MarketOperations.MktDomain.MktBillMediaKind;
import IEC61970.Base.Domain.Date;
import IEC62325.MarketOperations.MktDomain.MktAccountKind;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC62325.MarketOperations.ParticipantInterfaces.MajorChargeGroup;

/**
 * A roll up of invoice line items. The whole invoice has a due date and amount to
 * be paid, with information such as customer, banks etc. being obtained through
 * associations. The invoice roll up is based on individual line items that each
 * contain amounts and descriptions for specific services or products.
 * @created 03-Jan-2024 2:03:20 PM
 */
public class MarketInvoice {

	/**
	 * Total amount due on this invoice based on line items and applicable adjustments.
	 */
	public Money amount;
	/**
	 * Kind of media by which the CustomerBillingInfo was delivered.
	 */
	public MktBillMediaKind billMediaKind;
	/**
	 * Calculated date upon which the Invoice amount is due.
	 */
	public Date dueDate;
	/**
	 * Kind of invoice (default is 'sales').
	 */
	public MktAccountKind kind;
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
	public MajorChargeGroup MajorChargeGroup;

	public MarketInvoice(){

	}
}//end MarketInvoice