package IEC62325.MarketOperations.MktDomain;


/**
 * Defines the individual passes that produce results per execution type/market
 * type.
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum PassIndicatorType {
	/**
	 * Market Power Mitigation Pass 1
	 */
	MPM-1,
	/**
	 * Market Power Mitigation Pass 2
	 */
	MPM-2,
	/**
	 * Market Power Mitigation Pass 3
	 */
	MPM-3,
	/**
	 * Market Power Mitigation Pass 4
	 */
	MPM-4,
	/**
	 * Residual Unit Commitment
	 */
	RUC,
	/**
	 * Real Time Pre Dispatch
	 */
	RTPD,
	/**
	 * Real Time Economic Dispatch
	 */
	RTED,
	/**
	 * Hour Ahead Security Constrained Unit Commitment
	 */
	HA-SCUC,
	/**
	 * Day Ahead
	 */
	DA
}