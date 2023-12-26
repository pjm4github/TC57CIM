package IEC62325.MarketOperations.MktDomain;


/**
 * Area's present control mode.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public enum AreaControlMode {
	/**
	 * CF = Constant Frequency
	 */
	CF,
	/**
	 * Constant Tie-Line
	 */
	CTL,
	/**
	 * Tie-Line Bias
	 */
	TLB,
	/**
	 * Off control
	 */
	OFF
}