package IEC61968.PaymentMetering;


/**
 * Kind of cheque.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public enum ChequeKind {
	/**
	 * Payment order used by institutions other than banks.
	 */
	postalOrder,
	/**
	 * Payment order used by a bank.
	 */
	bankOrder,
	/**
	 * Other kind of cheque.
	 */
	other
}