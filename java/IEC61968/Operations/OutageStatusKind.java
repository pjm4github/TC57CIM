package IEC61968.Operations;


/**
 * This defines if the outage have been predicted or confirmed
 * @author Margaret
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public enum OutageStatusKind {
	/**
	 * the outage has been verified
	 */
	confirmed,
	/**
	 * the outage may not be real since it has not been verified - it is only thought
	 * to be an outage.
	 */
	predicted,
	/**
	 * Some of the usage points affected by the outage have been restored but other
	 * usage points are still out of power.
	 */
	partiallyRestored,
	/**
	 * All usage points associated with the outage have been restored
	 */
	restored,
	/**
	 * The outage has been fully restored, the crews have been released and the outage
	 * is shown as closed
	 */
	closed
}