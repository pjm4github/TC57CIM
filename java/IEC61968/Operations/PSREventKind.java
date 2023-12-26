package IEC61968.Operations;


/**
 * Kind of power system resource event.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public enum PSREventKind {
	/**
	 * Power system resource state change to in service.
	 */
	inService,
	/**
	 * Power system resource state change to out of service.
	 */
	outOfService,
	/**
	 * Power system resource state change to pending add.
	 */
	pendingAdd,
	/**
	 * Power system resource state change to pending remove.
	 */
	pendingRemove,
	/**
	 * Power system resource state change to pending replace.
	 */
	pendingReplace,
	/**
	 * Other power system resource state change.
	 */
	other,
	/**
	 * Unknown power system resource state change.
	 */
	unknown
}