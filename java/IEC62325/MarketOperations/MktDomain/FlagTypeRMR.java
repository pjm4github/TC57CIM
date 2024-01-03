package IEC62325.MarketOperations.MktDomain;


/**
 * Indicates whether the unit is RMR and it's condition type, for example:
 * N' - not an RMR unit
 * '1' - RMR Condition 1 unit
 * '2' - RMR Condition 2 unit
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum FlagTypeRMR {
	/**
	 * 'N' - not an RMR unit
	 */
	N,
	/**
	 * '1' - RMR Condition 1 unit
	 */
	1,
	/**
	 * '2' - RMR Condition 2 unit
	 */
	2
}