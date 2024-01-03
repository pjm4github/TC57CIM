package IEC62325.MarketOperations.MktDomain;


/**
 * Ramp rate curve type.
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum RampRateType {
	/**
	 * Operational ramp rate.
	 */
	OP,
	/**
	 * Regulating ramp rate.
	 */
	REG,
	/**
	 * Operating reserve ramp rate.
	 */
	OP_RES,
	/**
	 * Load drop ramp rate.
	 */
	LD_DROP,
	/**
	 * Load pick up rate.
	 */
	LD_PICKUP,
	/**
	 * Intertie ramp rate.
	 */
	INTERTIE
}