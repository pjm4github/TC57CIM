package IEC61968.Operations;


/**
 * Type of clearance action.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public enum ClearanceActionKind {
	/**
	 * Issue clearance.
	 */
	issue,
	/**
	 * Update clearance.
	 */
	update,
	/**
	 * Release clearance.
	 */
	release
}