package IEC62325.MarketOperations.MktDomain;


/**
 * Transmission Contract Type, For example:
 * O - Other
 * TE - Transmission Export
 * TI - Transmission Import
 * ETC - Existing Transmission Contract
 * RMT - RMT Contract
 * TOR - Transmission Ownership Right
 * RMR - Reliability Must Run Contract
 * CVR - Converted contract
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum ContractType {
	/**
	 * ETC - Existing Transmission Contract
	 */
	ETC,
	/**
	 * TOR - Transmission Ownership Right
	 */
	TOR,
	/**
	 * RMR - Reliability Must Run Contract
	 */
	RMR,
	/**
	 * RMT - RMT Contract
	 */
	RMT,
	/**
	 * O - Other
	 */
	O,
	/**
	 * TE - Transmission Export
	 */
	TE,
	/**
	 * TI - Transmission Import
	 */
	TI,
	/**
	 * CVR - Converted contract.
	 */
	CVR
}