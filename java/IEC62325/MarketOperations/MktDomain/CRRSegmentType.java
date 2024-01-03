package IEC62325.MarketOperations.MktDomain;


/**
 * Type of the CRR, from the possible type definitions in the CRR System (e.g.
 * 'LSE', 'ETC').
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum CRRSegmentType {
	AUC,
	CAP,
	CF,
	/**
	 * Converted rights.
	 */
	CVR,
	/**
	 * Existing Transmission Contract.
	 */
	ETC,
	/**
	 * Load Serving Entity.
	 */
	LSE,
	/**
	 * Merchant transmission.
	 */
	MT,
	/**
	 * Transmission Ownership Rights.
	 */
	TOR
}