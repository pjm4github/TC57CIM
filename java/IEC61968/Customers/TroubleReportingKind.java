package IEC61968.Customers;


/**
 * Kind of trouble reporting.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public enum TroubleReportingKind {
	/**
	 * Trouble call received by customer service representative.
	 */
	call,
	/**
	 * Trouble reported by email.
	 */
	email,
	/**
	 * Trouble reported by letter.
	 */
	letter,
	/**
	 * Trouble reported by other means.
	 */
	other,
	/**
	 * Trouble reported through interactive voice response system.
	 */
	ivr
}