package IEC61968.Work;


/**
 * Possible types of breaker maintenance work.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public enum BreakerMaintenanceKind {
	/**
	 * External out-of-service inspection and maintenance.
	 */
	externalOutOfService,
	/**
	 * Internal (interrupter) inspection and maintenance (breaker out of service).
	 */
	internalOutOfService,
	/**
	 * Overhaul of breaker interrupter unit. 
	 */
	interrupterOverhaul
}