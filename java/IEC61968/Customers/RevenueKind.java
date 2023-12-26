package IEC61968.Customers;


/**
 * Accounting classification of the type of revenue collected for the customer
 * agreement, typically used to break down accounts for revenue accounting.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public enum RevenueKind {
	/**
	 * Residential revenue.
	 */
	residential,
	/**
	 * Non-residential revenue.
	 */
	nonResidential,
	/**
	 * Commercial revenue.
	 */
	commercial,
	/**
	 * Industrial revenue.
	 */
	industrial,
	/**
	 * Irrigation revenue.
	 */
	irrigation,
	/**
	 * Streetlight revenue.
	 */
	streetLight,
	/**
	 * Other revenue kind.
	 */
	other
}