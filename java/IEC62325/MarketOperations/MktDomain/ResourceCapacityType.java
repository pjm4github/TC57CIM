package IEC62325.MarketOperations.MktDomain;


/**
 * Resource capacity type.
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum ResourceCapacityType {
	/**
	 * Regulation Up.
	 */
	RU,
	/**
	 * Regulation Down.
	 */
	RD,
	/**
	 * Spinning reserve.
	 */
	SR,
	/**
	 * Non spinning reserve.
	 */
	NR,
	/**
	 * Must Offer.
	 */
	MO,
	/**
	 * Flexible Offer.
	 */
	FO,
	/**
	 * Resource Adequacy.
	 */
	RA,
	/**
	 * Reliability Must Run.
	 */
	RMR
}