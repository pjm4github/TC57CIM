package IEC62325.MarketOperations.MktDomain;


/**
 * Commitment instruction types.
 * @created 03-Jan-2024 2:12:37 PM
 */
public enum AutomaticDispInstTypeCommitment {
	/**
	 * Start up instruction type
	 */
	START_UP,
	/**
	 * Shut down instruction type
	 */
	SHUT_DOWN,
	/**
	 * Distributed Resource Deployment
	 */
	DR_DEPLOY,
	/**
	 * Distributed Resource Release
	 */
	DR_RELEASE,
	/**
	 * Distributed Resource adjustment for a distributed resource that is already
	 * deployed (committed).
	 */
	DR_ADJUSTMENT
}