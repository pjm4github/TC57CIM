package IEC62325.MarketOperations.MktDomain;


/**
 * Types of resource registration status, for example:
 * 
 * Active
 * Mothballed
 * Planned
 * Decommissioned
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public enum ResourceRegistrationStatus {
	/**
	 * Resource registration is active
	 */
	Active,
	/**
	 * Registration status is in the planning stage
	 */
	Planned,
	/**
	 * Resource registration has been suspended
	 */
	Mothballed,
	/**
	 * Resource registration status is decommissioned
	 */
	Decommissioned
}