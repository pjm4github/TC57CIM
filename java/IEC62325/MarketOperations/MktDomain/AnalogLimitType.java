package IEC62325.MarketOperations.MktDomain;


/**
 * Limit type specified for AnalogLimits.
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum AnalogLimitType {
	/**
	 * Branch Medium Term Limit
	 */
	BranchMediumTerm,
	/**
	 * Branch Long Term Limit
	 */
	BranchLongTerm,
	/**
	 * Branch Short Term Limit
	 */
	BranchShortTerm,
	/**
	 * Voltage High Limit
	 */
	VoltageHigh,
	/**
	 * Voltage Low Limit
	 */
	VoltageLow
}