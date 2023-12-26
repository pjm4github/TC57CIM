package IEC61968.Customers;


/**
 * Kind of customer.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public enum CustomerKind {
	/**
	 * Residential customer.
	 */
	residential,
	/**
	 * Residential and commercial customer.
	 */
	residentialAndCommercial,
	/**
	 * Residential and streetlight customer.
	 */
	residentialAndStreetlight,
	/**
	 * Residential streetlight or other related customer.
	 */
	residentialStreetlightOthers,
	/**
	 * Residential farm service customer.
	 */
	residentialFarmService,
	/**
	 * Commercial industrial customer.
	 */
	commercialIndustrial,
	/**
	 * Pumping load customer.
	 */
	pumpingLoad,
	/**
	 * Wind machine customer.
	 */
	windMachine,
	/**
	 * Customer as energy service supplier.
	 */
	energyServiceSupplier,
	/**
	 * Customer as energy service scheduler.
	 */
	energyServiceScheduler,
	/**
	 * Internal use customer.
	 */
	internalUse,
	enterprise,
	regionalOperator,
	subsidiary,
	/**
	 * Other kind of customer.
	 */
	other
}