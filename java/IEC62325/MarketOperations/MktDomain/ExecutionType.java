package IEC62325.MarketOperations.MktDomain;


/**
 * Execution types of Market Runs.
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum ExecutionType {
	/**
	 * Day Ahead
	 */
	DA,
	/**
	 * Real TIme Hour Ahead Execution
	 */
	HASP,
	/**
	 * Real Time Pre-dispatch
	 */
	RTPD,
	/**
	 * Real Time Dispatch
	 */
	RTD
}