package IEC61968.PaymentMetering;


/**
 * Kind of tender.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public enum TenderKind {
	/**
	 * Payment method by means of a cheque.
	 */
	cheque,
	/**
	 * Payment method by means of a credit or debit card.
	 */
	card,
	/**
	 * Payment method by means of cash.
	 */
	cash,
	/**
	 * Payment method is not known.
	 */
	unspecified,
	/**
	 * Other payment method such as electronic finds transfer.
	 */
	other
}