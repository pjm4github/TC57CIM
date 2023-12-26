import IEC61968.Common.Status;
import IEC61968.InfIEC61968.InfWork.Design;

/**
 * Of an ErpQuote, the item or product quoted along with quantity, price and other
 * descriptive information.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class ErpQuoteLineItem extends ErpIdentifiedObject {

	public Status status;
	public ErpReqLineItem ErpReqLineItem;
	/**
	 * Some utilities provide quotes to customer for services, where the customer
	 * accepts the quote by making a payment. An invoice is required for this to occur.
	 */
	public ErpInvoiceLineItem ErpInvoiceLineItem;
	public ErpQuote ErpQuote;
	public Design Design;

	public ErpQuoteLineItem(){

	}
}//end ErpQuoteLineItem