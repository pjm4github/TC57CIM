import IEC61970.Base.Domain.String;

/**
 * Payment infromation and status for any individual line item of an ErpInvoice (e.
 * g., when payment is from a customer). ErpPayable is also updated when payment
 * is to a supplier and ErpReceivable is updated when payment is from a customer.
 * Multiple payments can be made against a single line item and an individual
 * payment can apply to more that one line item.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class ErpPayment extends ErpDocument {

	/**
	 * Payment terms (e.g., net 30).
	 */
	public String termsPayment;

	public ErpPayment(){

	}
}//end ErpPayment