package IEC61968.Customers;


/**
 * Kind of trigger to notify customer.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public enum NotificationTriggerKind {
	/**
	 * Notify customer for the first time that estimated restoration time is available.
	 */
	initialEtr,
	/**
	 * Notify customer if estimated restoration time changes.
	 */
	etrChange,
	/**
	 * Notify customer when power has been restored.
	 */
	powerRestored,
	/**
	 * Notify customer of planned outage.
	 */
	powerOut,
	/**
	 * Notify customer that a crew has been dispatched to investigate the problem.
	 */
	informDispatched
}