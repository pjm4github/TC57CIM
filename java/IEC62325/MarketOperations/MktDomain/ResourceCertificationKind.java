package IEC62325.MarketOperations.MktDomain;


/**
 * Types used for resource certification.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public enum ResourceCertificationKind {
	/**
	 * Regulation Up (RU, REGUP)
	 */
	RegulationUp,
	/**
	 * Regulation Down (RD, REGDN)
	 */
	RegulationDown,
	/**
	 * Spinning Reserve (SR, RRSPIN)
	 */
	SpinningReserve,
	/**
	 * Non Spinning Reserve (NR, NONSPIN)
	 */
	NonSpinningReserve,
	/**
	 * Reliability Must Run (RMR)
	 */
	ReliabilityMustRun,
	/**
	 * Black start
	 */
	BLACKSTART,
	/**
	 * Demand Side Reponse (DSR)
	 */
	DemandSideResponse,
	/**
	 * Synchronous Condenser (SYNCCOND)
	 */
	SynchronousCondenser,
	/**
	 * Intermittent resource
	 */
	IntermittentResource,
	/**
	 * Reliability unit commitment (RUC)
	 */
	ReliabilityUnitCommitment,
	Energy,
	Capacity
}