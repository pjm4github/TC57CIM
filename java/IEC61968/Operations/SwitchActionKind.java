package IEC61968.Operations;


/**
 * Kind of action on switch.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public enum SwitchActionKind {
	/**
	 * Open the switch.
	 */
	open,
	/**
	 * Close the switch.
	 */
	close,
	/**
	 * Disable (automatic) switch reclosing.
	 */
	disableReclosing,
	/**
	 * Enable (automatic) switch reclosing.
	 */
	enableReclosing
}