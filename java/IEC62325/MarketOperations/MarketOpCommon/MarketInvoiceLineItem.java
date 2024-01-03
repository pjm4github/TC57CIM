package IEC62325.MarketOperations.MarketOpCommon;

import IEC61970.Base.Domain.DateTimeInterval;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC62325.MarketOperations.MktDomain.MktInvoiceLineItemKind;
import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MarketSystem.MarketResults.Settlement;

/**
 * An individual line item on an invoice.
 * @created 03-Jan-2024 2:03:20 PM
 */
public class MarketInvoiceLineItem {

	/**
	 * Bill period for the line item.
	 */
	public DateTimeInterval billPeriod;
	/**
	 * General Ledger account code, shall be a valid combination.
	 */
	public String glAccount;
	/**
	 * Date and time line item will be posted to the General Ledger. 
	 */
	public DateTime glDateTime;
	/**
	 * Kind of line item.
	 */
	public MktInvoiceLineItemKind kind;
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
	public Settlement Settlement;
	public MarketInvoiceLineItem ContainerMarketInvoiceLineItem;
	public MarketInvoice MarketInvoice;

	public MarketInvoiceLineItem(){

	}
}//end MarketInvoiceLineItem