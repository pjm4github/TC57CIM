package IEC62325.MarketOperations.MktDomain;


/**
 * Market product self schedule bid types.
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum MarketProductSelfSchedType {
	/**
	 * Existing Transmission Contract.
	 */
	ETC,
	/**
	 * Transmission Ownership Right.
	 */
	TOR,
	/**
	 * Reliability Must Run.
	 */
	RMR,
	/**
	 * Regulatory must run.
	 */
	RGMR,
	/**
	 * Reliability must take.
	 */
	RMT,
	/**
	 * Price taker.
	 */
	PT,
	/**
	 * Low price taker.
	 */
	LPT,
	/**
	 * Self provision.
	 */
	SP,
	/**
	 * Resource adequacy.
	 */
	RA
}