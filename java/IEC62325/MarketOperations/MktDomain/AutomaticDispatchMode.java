package IEC62325.MarketOperations.MktDomain;


/**
 * Automatic Dispatch mode.
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum AutomaticDispatchMode {
	INTERVAL,
	/**
	 * Contingnency occurance, redispatch of contingency reserves
	 */
	CONTINGENCY,
	/**
	 * Operator override
	 */
	MANUAL
}