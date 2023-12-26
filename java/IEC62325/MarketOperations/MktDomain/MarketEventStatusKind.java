package IEC62325.MarketOperations.MktDomain;


/**
 * Market event status types.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public enum MarketEventStatusKind {
	/**
	 * The status of the event is currently in a active state.
	 * Active (when sysdate is equal or greater than to planned start time)
	 */
	active,
	/**
	 * The status of the event is currently in a cancelled state.
	 * Cancelled (stopped before planned start time or planned end time)
	 */
	cancelled,
	/**
	 * The status of the event is currently in a completed state.
	 * Complete (when sysdate is equal to the release time)
	 */
	completed,
	/**
	 * The status of the event is currently in a planned state.
	 * Planned (sysdate is less than planned start time)
	 */
	planned
}