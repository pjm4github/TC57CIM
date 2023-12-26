package IEC61968.PaymentMetering;


/**
 * Kind of supplier.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public enum SupplierKind {
	/**
	 * Entity that delivers the service to the customer.
	 */
	utility,
	/**
	 * Entity that sells the service, but does not deliver to the customer; applies to
	 * the deregulated markets.
	 */
	retailer,
	lse,
	mdma,
	msp,
	/**
	 * Other kind of supplier.
	 */
	other
}