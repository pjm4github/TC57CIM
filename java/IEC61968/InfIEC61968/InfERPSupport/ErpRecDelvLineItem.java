import IEC61968.Common.Status;

/**
 * Of an ErpReceiveDelivery, this is an individually received good or service by
 * the Organisation receiving goods or services. It may be used to indicate
 * receipt of goods in conjunction with a purchase order line item.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class ErpRecDelvLineItem extends ErpIdentifiedObject {

	public Status status;
	public ErpReceiveDelivery ErpReceiveDelivery;
	public ErpPOLineItem ErpPOLineItem;
	public ErpInvoiceLineItem ErpInvoiceLineItem;

	public ErpRecDelvLineItem(){

	}
}//end ErpRecDelvLineItem