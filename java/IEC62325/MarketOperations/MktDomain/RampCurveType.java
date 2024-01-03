package IEC62325.MarketOperations.MktDomain;


/**
 * For example:
 * 0 - Fixed ramp rate independent of rate function unit MW output
 * 1 - Static ramp rates as a function of unit MW output only
 * 2 - Dynamic ramp rates as a function of unit MW output and ramping time
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum RampCurveType {
	/**
	 * Fixed ramp rate independent of rate function unit MW output
	 */
	0,
	/**
	 * Static ramp rates as a function of unit MW output only
	 */
	1,
	/**
	 * Dynamic ramp rates as a function of unit MW output and ramping time
	 */
	2
}