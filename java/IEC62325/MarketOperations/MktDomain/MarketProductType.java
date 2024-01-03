package IEC62325.MarketOperations.MktDomain;


/**
 * For example:
 * Energy, Reg Up, Reg Down, Spin Reserve, Nonspin Reserve, RUC, Load Folloing Up,
 * and Load Following Down.
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum MarketProductType {
	/**
	 * energy type
	 */
	EN,
	/**
	 * regulation up
	 */
	RU,
	/**
	 * regulation down
	 */
	RD,
	/**
	 * spinning reserve
	 */
	SR,
	/**
	 * non spinning reserve
	 */
	NR,
	/**
	 * Residual Unit Commitment
	 */
	RC,
	/**
	 * Load following up
	 */
	LFU,
	/**
	 * Load following down
	 */
	LFD,
	/**
	 * Regulation
	 */
	REG
}