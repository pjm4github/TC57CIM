package IEC61968.InfIEC61968.InfCustomers;


/**
 * Kind of customer billing.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public enum CustomerBillingKind {
	/**
	 * Consolidated bill from energy service supplier (ESS).
	 */
	consolidatedEss,
	/**
	 * Consolidated bill from utility distribution company (UDC).
	 */
	consolidatedUdc,
	/**
	 * Separate bills from ESS and UDC.
	 */
	separateEssUdc,
	other
}