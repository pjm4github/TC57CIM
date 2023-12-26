package IEC61968.InfIEC61968.InfLocations;


/**
 * Kind of (land) property.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public enum LandPropertyKind {
	/**
	 * Site enclosed within a building.
	 */
	building,
	/**
	 * Site with a customer.
	 */
	customerPremise,
	/**
	 * Storehouse for supplies that also serves as a station for supporting crews.
	 */
	depot,
	/**
	 * Place of storage (e.g., a warehouse) to put aside, or accumulate, material and
	 * equipment for use when needed.
	 */
	store,
	/**
	 * Transmission network switchyard.
	 */
	substation,
	/**
	 * Substation where the distribution and transmission networks meet and hence have
	 * mixed ownership and mixed operational control.
	 */
	gridSupplyPoint,
	/**
	 * Property owned or used by an external party that is not a customer.
	 */
	external
}